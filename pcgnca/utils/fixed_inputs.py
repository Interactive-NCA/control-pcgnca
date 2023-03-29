"""
Module that includes logic for generating semi-random fixed
tiles for given games. Semi since the generated tiles
must conform to the game rules.
"""

# --------------------- External libaries import
from random import choice, randint
from math import ceil
import json
import os

import numpy as np
from tqdm import tqdm

# --------------------- Internal libaries import
from . import ZeldaLevelViz

# --------------------- Generators
class FixedTilesBase:
    def __init__(self):
        pass

class ZeldaFixedTilesGenerator(FixedTilesBase):

    def __init__(self, difficulty, grid_dim):

        # Initialise the parent
        super().__init__()

        # Grid dimension
        self.grid_dim = grid_dim

        # Save requested difficulty (easy, medium, hard)
        self.difficulty = difficulty

        # Define generator based on difficulty
        self.generator = self._from_difficulty_to_gen()

        # - Set hyper-parameters
        self.configs = dict()

        # -- Number of splits of grid per dimension (0 = full grid, ...)
        self.n_splits = [0, 1]

        # -- Get the configs
        self._get_config() 

    # --------------------- Public functions
    def generate(self, n_seeds):
        return self.generator(n_seeds)

    # --------------------- Private functions
    def _get_config(self):
        for split in self.n_splits:            
            # -- List of bounds of subgrids
            # --- Len of each split
            blocks_avail = self.grid_dim - split - 2 # - 2 for side boundaries
            base = ceil(blocks_avail / (split + 1))
            remainder = blocks_avail % base
            if remainder != 0:
                splits_len = [base]*split + [remainder]
                n_steps = remainder
            else:
                splits_len = [base]*(split + 1)
                n_steps = splits_len[0]

            # --- Generate x and y bounds
            x_min, y_min = 1, 1 # start
            x_bounds, y_bounds = [], []
            for split_len_x in splits_len:
                x_max = x_min + split_len_x - 1

                # ---- Stay within bounds of y
                for split_len_y in splits_len:
                    y_max = y_min + split_len_y - 1
                    x_bounds.append([x_min, x_max])
                    y_bounds.append([y_min, y_max])
                    # ---- For the split and next position
                    y_min += (split_len_y + 1)

                # ---- For the split and next position                    
                x_min += (split_len_x + 1)
                y_min = 1

            # -- Save the config
            self.configs[split] = {
                "x_bounds": x_bounds,
                "y_bounds": y_bounds,
                "n_steps": n_steps
            }

    def _from_difficulty_to_gen(self):

        # Overview of generators 
        generators = {
            "easy": self._easy_generator,
            "medium": self._medium_generator,
            "hard": self._hard_generator
        }

        assert self.difficulty in generators, "The difficulty must be one of easy, medium, hard."

        return generators[self.difficulty]

    def _brick_object_gen(self, x_bound, y_bound, steps, x_off, y_off):

        # Define possible directions
        directions = [
            (1, 0), # up
            (-1, 0), # down
            (0, 1), # right
            (1, 1), # right up diag
            (-1, 1), # right down diag
        ]

        # Extract boundaries
        x_low, x_upper = x_bound
        y_low, y_upper = y_bound

        # Define boundary check
        is_valid = lambda x, y: (x_low <= x <= x_upper) and (y_low <= y <= y_upper)

        # Create the shape
        # - Represent shape as coordinates
        shape_cords = np.zeros((steps, 2), dtype=int)

        # - Start in the upper right corner
        prev = np.array([x_off, y_off])
        shape_cords[0] = prev

        # - Now iterate for N - 1 steps
        for i in range(1, steps):
            
            # -- Next coord
            nxt = prev + np.array(choice(directions))

            # -- While not valid keep generting new possible moves
            while not is_valid(*nxt):
                nxt = prev + np.array(choice(directions))

            # -- Once valid, save and set the prev
            shape_cords[i] = prev = nxt

        return shape_cords[:, 0], shape_cords[:, 1]

    def _easy_generator(self, n_seeds):
        """
        Uses bricks only. Split the given grid
        into different regions. In each of these regions,
        start in the top left corner and keep going for n steps
        generating random shapes.

        TODO
        ----
        Should set numpy seed to control the randomness.

        Notes
        -----
        To prevent creating unreachable regions, the following
        decisions have been made:
        1. There can not be any fixed tiles at the boundaries of the grid
        2. Each region is split with one tile
        """

        # - Generate the seeds with fixe tiles
        result = np.zeros((n_seeds, self.grid_dim, self.grid_dim))
        for i in tqdm(range(n_seeds)):
            # -- Choose configuration
            config = self.configs[choice(self.n_splits)]

            # -- Generate the coordinates of the fixed tiles
            for x_bound, y_bound in zip(config["x_bounds"], config["y_bounds"]):
                rows, cols = self._brick_object_gen(x_bound, y_bound, config["n_steps"], x_bound[0], y_bound[0])
                result[i, rows, cols] = 1

        return result

    def _medium_generator(self):
        pass

    def _hard_generator(self):
        pass


# --------------------- Helper functions
# ------------------------ Public
def generate_fixed_tiles(game, n_seeds, difficulty, path, graphics_path):

    # - Load game's settings
    game_set_path = os.path.join(path, "games", f"{game}.json")
    with open(game_set_path) as f:
        settings = json.load(f)

    # - Get generator for the given game
    generator = _from_name_to_generator(game)(difficulty, settings["grid_dim"])

    # - Generate the batch of seeds
    seeds = generator.generate(n_seeds)

    # - Save these as binary in npy format
    outfile = os.path.join(path, "fixed_tiles", game, f"{difficulty}_{n_seeds}.npy")
    np.save(outfile, seeds)

    # - Visualise some of them
    visualiser = ZeldaLevelViz(graphics_path, dim=seeds[1].shape[0])
    n_frames = int(n_seeds*0.1) # 10 % of the batch
    frames = []
    for _ in range(n_frames):
        pil_img = visualiser.render_level(seeds[randint(0, n_seeds - 1)])
        frames.append(pil_img)
        
    outfile = os.path.join(path, "fixed_tiles", game, f"{difficulty}_{n_seeds}.gif")
    frames[0].save(outfile, format="GIF", append_images=frames, save_all=True, duration=100, loop=0)

# ------------------------ Private
def _from_name_to_generator(name):

    # - Collections of generators
    generators = {
        "zelda": ZeldaFixedTilesGenerator
    }

    # - Make sure the given game has generator
    assert name in generators, "The given game does not have any fixed tiles generator."

    return generators[name]
