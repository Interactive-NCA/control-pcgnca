"""
Module that includes functionality for evaluating generated levels.
"""

# --------------------- External libraries import
import numpy as np

class ZeldaEvaluation:

    def __init__(self, dim, obj_weights):

        # - User defined attributes
        self.dim = dim
        self.obj_weights = obj_weights

        # - Game rules
        self.rules = {
            "n_players": 1,
            "n_keys": 1,
            "n_doors": 1,
            "n_regions": 1,
            "nearest_enemy": (5, 144),
            "n_enemies": (2, 5)
        }

        # - Define reward weights
        self._reward_weights = {
            "n_players": 3,
            "n_keys": 3,
            "n_doors": 3,
            "n_regions": 5,
            "n_enemies": 1,
            "nearest_enemy": 2,
            "path_length": 1
        }

        # - Bounds (TODO: get understanding of this section)
        self._max_nearest_enemy = np.ceil(self.dim / 2 + 1) * (self.dim)
        self._max_path_length = (np.ceil(self.dim / 2) * (self.dim) + np.floor(self.dim / 2)) * 2 - 1
        self._cond_bounds = {
            "nearest_enemy": (0, self._max_nearest_enemy),
            "n_enemies": (0, self.dim * self.dim - 2),
            "n_players": (0, self.dim * self.dim - 2),
            "n_keys": (0, self.dim * self.dim - 2),
            "n_doors": (0, self.dim * self.dim - 2),
            "n_regions": (0, self.dim * self.dim / 2),
            "path_length": (0, self._max_path_length)
        }

        # Normalize reward weights w.r.t. bounds of each metric. (... and also this section)
        self._reward_weights_norm = {
            k: v * 1 / (self._cond_bounds[k][1] - self._cond_bounds[k][0]) \
                for k, v in self._reward_weights.items()
        }
    
    def evaluate_level_batch(self, batch_stats):

        # - Reliability
        # -- Symmetry
        symmetries = self.normalise(np.array([s["symmetry"] for s in batch_stats]))
        symmetries_norm = self.normalise(symmetries)
        symmetry_std = np.array(symmetries_norm).std() # for objective func must be norm
        symmetry_mean = np.array(symmetries).mean() # for archive where to place

        # -- Path length
        path_lengths = np.array([s["path_length"] for s in batch_stats])
        path_lengths_norm = self.normalise(path_lengths)
        path_length_std = np.array(path_lengths_norm).std()
        path_length_mean = np.array(path_lengths).mean()

        # -- Compute reliability penalty
        reliability_penalty = -(symmetry_std + path_length_std)/2

        # - Playbility
        # we want to hit each of our rules exactly, penalize for anything else.
        # for ranges, we take our least distance to any element in the range
        batch_size = len(batch_stats)
        playability_penalties = np.empty(batch_size)
        for i, stats in enumerate(batch_stats):

            playability_penalty = 0

            for k in self.rules:

                # --- Range
                # Example:
                # - n_enemies should be (2, 5) 
                # -- actual number is 0 --> penalty is 2
                # -- actual number is 8 --> penalty is 3
                # -- actual number is 4 --> penalty is 0
                if isinstance(self.rules[k], tuple):
                    low, high = self.rules[k]
                    penalty_k = abs(np.arange(low, high) - stats[k]).min()
                
                # --- Scalar value
                else:
                    penalty_k = abs(self.rules[k] - stats[k])

                # --- Normalise the penalty and add it to the total penalty
                playability_penalty += penalty_k*self._reward_weights_norm[k]

            playability_penalties[i] = playability_penalty
        
        final_playability_penalty = -np.mean(self.normalise(playability_penalties))

        # - Objective function calculation
        objective = self.obj_weights["playability"]*final_playability_penalty + self.obj_weights["reliability"]*reliability_penalty

        return objective, symmetry_mean, path_length_mean

    def get_zelda_level_stats(self, level):
        """
        Args:
            level (2D array): level for which the stats should be computed
        """

        # - Collect the stats into a dictionary
        stats = dict()

        # - Set default values for path length and nearest enemy, if certain conditions are
        # met, these will be overriden to some actual values.
        stats["path_length"] = 0
        stats["nearest_enemy"] = 0

        # - Count the number of occurences of certain entities
        entities = [("n_players", 2), ("n_keys", 3), ("n_doors", 4), ("n_bats", 5), ("n_spiders", 6), ("n_scorpions", 7)]
        for name, i in entities:
            stats[name] = (level == i).sum()

        # - Group the enemies count
        stats["n_enemies"] = stats["n_bats"] + stats["n_spiders"] + stats["n_scorpions"]

        # - Calculate number of the regions
        tiles_loc = get_tile_locations(level, [i for i in range(8)])
        stats["n_regions"] = calc_num_regions(level, tiles_loc, [i for i in range(8) if i != 1])

        # - Calculate distance from nearest enemy and solution path length (if possible)
        if stats["n_players"] == 1 and stats["n_regions"] == 1:

            # -- Distance from the nearest enemy
            # --- Get the position of the zelda
            p_x, p_y = tiles_loc[2][0]

            # --- Collect all the enemies position in the map
            enemies = []
            enemies.extend(tiles_loc[5])
            enemies.extend(tiles_loc[6])
            enemies.extend(tiles_loc[7])


            # --- Compute shortest path from the zelda to each enemy and then find the min distance
            if len(enemies) > 0:
                dijkstra,_ = run_dijkstra(p_x, p_y, level, [i for i in range(8) if i not in [1, 4]])
                min_dist = self.dim*self.dim
                for e_x,e_y in enemies:
                    if dijkstra[e_y][e_x] > 0 and dijkstra[e_y][e_x] < min_dist:
                        min_dist = dijkstra[e_y][e_x]
                stats["nearest_enemy"] = min_dist

            # -- Compute the solution path length
            if stats["n_keys"] == 1 and stats["n_doors"] == 1:
                k_x, k_y = tiles_loc[3][0]
                d_x, d_y = tiles_loc[4][0]

                # start point is people
                dijkstra_k, _ = run_dijkstra(p_x, p_y, level, [i for i in range(8) if i not in [1, 4]])
                stats["path_length"] += dijkstra_k[k_y][k_x]

                # start point is key
                dijkstra_d,_ = run_dijkstra(k_x, k_y, level, [i for i in range(8) if i != 1])
                stats["path_length"] += dijkstra_d[d_y][d_x]

        # - Calculate symmetry
        stats["symmetry"] = get_sym(level, self.dim)

        return stats
    
    def normalise(self, var):
        """Use standard scaler to normalise given variable.
        """

        # - Mean and std
        m = np.mean(var)
        std = np.std(var)
        if std == 0:
            std = 0.0001

        # - z-score
        norm = (var - m)/std

        return norm 

# --------------------- Helper functions
# ------------------------ Public functions
def get_sym(int_map, dim):
    """
    Code used from Sam Earle's repository control-pcgrl.
    Function to get the vertical symmetry of a level
    int_map (numpy array of ints): representation of level
    returns a symmetry float value normalized to a range of 0.0 to 1.0
    """
    result = (_get_ver_sym(int_map, dim) + _get_hor_sym(int_map, dim)) / 2.0

    return result

def run_dijkstra(x, y, map, passable_values):
    """
    Public function that runs dijkstra algorithm and return the map

    Parameters:
        x (int): the starting x position for dijkstra algorithm
        y (int): the starting y position for dijkstra algorithm
        map (any[][]): the current map being tested
        passable_values (any[]): an array of all the passable tile values

    Returns:
        int[][]: returns the dijkstra map after running the dijkstra algorithm
    """

    dijkstra_map = np.full((len(map), len(map[0])),-1)
    visited_map = np.zeros((len(map), len(map[0])))
    queue = [(x, y, 0)]
    while len(queue) > 0:
        (cx,cy,cd) = queue.pop(0)
        if map[cy][cx] not in passable_values or (dijkstra_map[cy][cx] >= 0 and dijkstra_map[cy][cx] <= cd):
            continue
        visited_map[cy][cx] = 1
        dijkstra_map[cy][cx] = cd
        for (dx,dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx,ny=cx+dx,cy+dy
            if nx < 0 or ny < 0 or nx >= len(map[0]) or ny >= len(map):
                continue
            queue.append((nx, ny, cd + 1))
    return dijkstra_map, visited_map

def calc_num_regions(map, map_locations, passable_values):
    """
    Calculates the number of regions in the current map with passable_values

    Parameters:
        map (any[][]): the current map being tested
        map_locations(Dict(string,(int,int)[])): the histogram of locations of the current map
        passable_values (any[]): an array of all the passable tile values

    Returns:
        int: number of regions in the map
    """
    empty_tiles = _get_certain_tiles(map_locations, passable_values)
    region_index=0
    color_map = np.full((len(map), len(map[0])), -1)
    for (x,y) in empty_tiles:
        num_tiles = _flood_fill(x, y, color_map, map, region_index + 1, passable_values)
        if num_tiles > 0:
            region_index += 1
        else:
            continue
    return region_index


def get_tile_locations(map, tile_values):
    """
    Public function to get a dictionary of all location of all tiles

    Parameters:
        map (any[][]): the current map
        tile_values (any[]): an array of all the tile values that are possible

    Returns:
        Dict(string,(int,int)[]): positions for every certain tile_value
    """
    tiles = {}
    for t in tile_values:
        tiles[t] = []
    for y in range(len(map)):
        for x in range(len(map[y])):
            tiles[map[y][x]].append((x,y))
    return tiles

# ------------------------ Private functions
def _get_certain_tiles(map_locations, tile_values):
    """
    Private function to get a list of all tile locations on the map that have any of
    the tile_values

    Parameters:
        map_locations (Dict(string,(int,int)[])): the histogram of locations of the current map
        tile_values (any[]): an array of all the tile values that the method is searching for

    Returns:
        (int,int)[]: a list of (x,y) position on the map that have a certain value
    """
    tiles=[]
    for v in tile_values:
        tiles.extend(map_locations[v])
    return tiles


def _flood_fill(x, y, color_map, map, color_index, passable_values):
    """
    Private function that runs flood fill algorithm on the current color map

    Parameters:
        x (int): the starting x position of the flood fill algorithm
        y (int): the starting y position of the flood fill algorithm
        color_map (int[][]): the color map that is being colored
        map (any[][]): the current tile map to check
        color_index (int): the color used to color in the color map
        passable_values (any[]): the current values that can be colored over

    Returns:
        int: the number of tiles that has been colored
    """

    num_tiles = 0
    queue = [(x, y)]
    while len(queue) > 0:
        (cx, cy) = queue.pop(0)
        if color_map[cy][cx] != -1 or map[cy][cx] not in passable_values:
            continue
        num_tiles += 1
        color_map[cy][cx] = color_index
        for (dx,dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx,ny=cx+dx,cy+dy
            if nx < 0 or ny < 0 or nx >= len(map[0]) or ny >= len(map):
                continue
            queue.append((nx, ny))
    return num_tiles


def _get_hor_sym(int_map, dim):
    """
    Code used from Sam Earle's repository control-pcgrl.
    Function to get the horizontal symmetry of a level
    int_map (numpy array of ints): representation of level
    returns a symmetry float value normalized to a range of 0.0 to 1.0
    """
    max_val = dim*dim / 2  # for example 14*14/2=98  
    m = 0

    if int(int_map.shape[0]) % 2 == 0:
        m = np.sum(
            (
                int_map[: int(int_map.shape[0] / 2)]
                == np.flip(int_map[int(int_map.shape[0] / 2) :], 0)
            ).astype(int)
        )
        m = m / max_val
    else:
        m = np.sum(
            (
                int_map[: int(int_map.shape[0] / 2)]
                == np.flip(int_map[int(int_map.shape[0] / 2) + 1 :], 0)
            ).astype(int)
        )
        m = m / max_val

    return m


def _get_ver_sym(int_map, dim):
    """
    Code used from Sam Earle's repository control-pcgrl.
    Function to get the vertical symmetry of a level
    int_map (numpy array of ints): representation of level
    returns a symmetry float value normalized to a range of 0.0 to 1.0
    """

    max_val = dim*dim / 2  # for example 14*14/2=98 
    m = 0
    
    if int(int_map.shape[1]) % 2 == 0:
        m = np.sum(
            (
                int_map[:, : int(int_map.shape[1] / 2)]
                == np.flip(int_map[:, int(int_map.shape[1] / 2) :], 1)
            ).astype(int)
        )
        m = m / max_val
    else:
        m = np.sum(
            (
                int_map[:, : int(int_map.shape[1] / 2)]
                == np.flip(int_map[:, int(int_map.shape[1] / 2) + 1 :], 1)
            ).astype(int)
        )
        m = m / max_val

    return m
