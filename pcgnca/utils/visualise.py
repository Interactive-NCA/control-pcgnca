"""
Module that should help with visualisation of the levels.
"""

import os
from PIL import Image


class ZeldaLevelViz:

    def __init__(self, graphics_path, dim):
        
        # - Load graphics components
        self.tiles = ["empty", "solid", "player", "key", "door", "spider", "bat", "scorpion"]
        self.graphics = dict()
        for tile in self.tiles:
            self.graphics[tile] = Image.open(os.path.join(graphics_path, f"{tile}.png")).convert('RGBA')

        # - Save hyper-parameters
        self.dim = dim
        self.border_size = 1
        self.tile_size = 16

    # --------------------- Public functions
    def render_level(self, grid):

        """
        Args:
            grid (numpy.int[][]): a numpy 2D array of the current map 
        Returns:
            lvl_image: a pillow image on how the map will look like using the binary graphics
        """

        # - Initialise the image
        grid_len = self.dim + 2*self.border_size
        lvl_image = Image.new("RGBA", (grid_len*self.tile_size, grid_len*self.tile_size), (0,0,0,255))

        # - Convert the grid of ints to grid of strings
        grid = self._get_string_map(grid)

        # - Background floor everywhere
        for y in range(grid_len):
            for x in range(grid_len):
                lvl_image.paste(self.graphics['empty'], (x*self.tile_size, y*self.tile_size, (x+1)*self.tile_size, (y+1)*self.tile_size))

        # - Borders
        for y in range(grid_len):
            for x in range(self.border_size):
                lvl_image.paste(self.graphics["solid"], (x*self.tile_size, y*self.tile_size, (x+1)*self.tile_size, (y+1)*self.tile_size))
                lvl_image.paste(self.graphics["solid"], ((grid_len-x-1)*self.tile_size, y*self.tile_size, (grid_len-x)*self.tile_size, (y+1)*self.tile_size))
        for x in range(grid_len):
            for y in range(self.border_size):
                lvl_image.paste(self.graphics["solid"], (x*self.tile_size, y*self.tile_size, (x+1)*self.tile_size, (y+1)*self.tile_size))
                lvl_image.paste(self.graphics["solid"], (x*self.tile_size, (grid_len-y-1)*self.tile_size, (x+1)*self.tile_size, (grid_len-y)*self.tile_size))

        # - Map tiles
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                tile_image = self.graphics[grid[y][x]]
                lvl_image.paste(self.graphics[grid[y][x]], ((x+self.border_size)*self.tile_size, (y+self.border_size)*self.tile_size, (x+self.border_size+1)*self.tile_size, (y+self.border_size+1)*self.tile_size), mask=tile_image)

        return lvl_image

    # --------------------- Private functions
    def _get_string_map(self, map):
        """
        A method to convert the map to use the tile names instead of tile numbers

        Parameters:
            map (numpy.int[][]): a numpy 2D array of the current map
            tiles (string[]): a list of all the tiles in order

        Returns:
            string[][]: a 2D map of tile strings instead of numbers
        """

        int_to_string = dict((i, s) for i, s in enumerate(self.tiles))
        result = []
        for y in range(map.shape[0]):
            result.append([])
            for x in range(map.shape[1]):
                result[y].append(int_to_string[int(map[y][x])])
        return result
