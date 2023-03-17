"""
Module that includes logic for generating semi-random fixed
tiles for given games. Semi since the generated tiles
must conform to the game rules.
"""

class FixedTilesBase:
    def __init__(self):
        pass

class ZeldaFixedTilesGenerator(FixedTilesBase):

    def __init__(self, evolver, difficulty):

        # Initialise the parent
        super().__init__()

        # Save evolver to access all info about the zelda game
        self.evolver = evolver

        # Save requested difficulty (easy, medium, hard)
        self.difficulty = difficulty

        # Define generator based on difficulty
        self.generator = self._from_difficulty_to_gen()

    # --------------------- Public functions
    def generate(self):
        pass

    # --------------------- Private functions
    def _from_difficulty_to_gen(self):

        # Overview of generators 
        generators = {
            "easy": self._easy_generator,
            "medium": self._medium_generator,
            "hard": self._hard_generator
        }

        assert self.difficulty in generators, "The difficulty must be one of easy, medium, hard."

        return generators[self.difficulty]

    def _easy_generator(self):
        """
        Uses bricks only. From bricks, creates
        various objects and then select a random location
        for these in the grid. All these brick objects, however
        still keep the area connected. In other words,
        flood fill algorithm will return number of regions = 1. 
        """

        # IDEA: split the grid into N regions and to each
        # reg place one of the objects
        # I could vary the number if regs

        # objects ideas
        # vertical rectangle (len, width (x, y) of start, same for end)
        # horizontal rectangle (len, width (x, y) of start, same for end)

        pass

    def _medium_generator(self):
        pass

    def _hard_generator(self):
        pass
