"""
The team.py file is where you should write all your code!

Write the __init__ and the step functions. Further explanations
about these functions are detailed in the wiki.

List your Andrew ID's up here!
eclinch
mpotluri
uar
vnbhatia
"""
from awap2019 import Tile, Direction, State

class Team(object):
    def __init__(self, initial_board, team_size, company_info):
        """
        The initializer is for you to precompute anything from the
        initial board and the company information! Feel free to create any
        new instance variables to help you out.

        Specific information about initial_board and company_info are
        on the wiki. team_size, although passed to you as a parameter, will
        always be 4.
        """
        self.board = initial_board
        self.team_size = team_size
        self.company_info = company_info

        self.team_name = "Thanos Did Nothing Wrong"

    def BFS(self, row, col):
        target_locations = {c.back_line: c for c in self.unvisited_companies}

        frontier = [(self.board[row][col], row, col, [])]
        visited = set((row, col))
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while True:
            if len(frontier) == 0:
                return None
            new_frontier = []
            for tile, row, col, path in frontier:
                for drow, dcol in dirs:
                    new_row = row + drow
                    new_col = col + dcol
                    is_valid = (new_row, new_col) not in visited
                    is_valid &= tile.get_booth() is None
                    if is_valid:
                        new_path = path + [(new_row, new_col)]
                        if (new_row, new_col) in target_locations:
                            return new_path, target_locations[(new_row, new_col)]
                        visited.add((new_row, new_col))
                        new_frontier.append((self.board[new_row][new_col], new_row, new_col, new_path))
            frontier = new_frontier

    def step(self, visible_board, states, score):
        """
        The step function should return a list of four Directions.

        For more information on what visible_board, states, and score
        are, please look on the wiki.
        """

        return [Direction.LEFT, Direction.UP, Direction.RIGHT, Direction.DOWN]

