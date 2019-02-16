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
import math

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

        rows, cols = len(self.board), len(self.board[0])
        frontier = [(row, col, [])]
        visited = set((row, col))
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while True:
            if len(frontier) == 0:
                return None
            new_frontier = []
            for row, col, path in frontier:
                for drow, dcol in dirs:
                    new_row = row + drow
                    new_col = col + dcol
                    if not (0 <= new_row < rows and 0 <= new_col < cols):
                        continue
                    new_tile = self.board[new_row][new_col]
                    is_valid = (new_row, new_col) not in visited
                    is_valid &= new_tile.get_booth() is None
                    if is_valid:
                        new_path = path + [(new_row, new_col)]
                        if (new_row, new_col) in target_locations:
                            return new_path, target_locations[(new_row, new_col)]
                        visited.add((new_row, new_col))
                        new_frontier.append((new_row, new_col, new_path))
            frontier = new_frontier

    # def ClosestCompany(self, row, col):
    #     target_locations = {c.back_line: c for c in self.unvisited_companies}
    #
    #     rows, cols = len(self.board), len(self.board[0])
    #     distances = [[(math.inf, None)] * cols for _ in range(rows)]
    #     distances[row][col] = (0, [])
    #     visited = set()
    #     dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    #
    #     while True:
    #         min_distance = math.inf
    #         min_coordinate = None
    #         min_path = None
    #         for row in range(rows):
    #             for col in range(cols):
    #                 distance, path = distances[row][col]
    #                 if distance < min_distance and (row, col) not in visited:
    #                     min_distance = distance
    #                     min_coordinate = (row, col)
    #                     min_path = path
    #         if min_coordinate is None:
    #             return None
    #         if min_coordinate in target_locations:
    #
    #
    #         visited.add(min_coordinate)
    #
    #         row, col = min_coordinate
    #         for drow, dcol in dirs:
    #             new_row = row + drow
    #             new_col = col + dcol
    #             if not (0 <= new_row < rows and 0 <= new_col < cols):
    #                 continue
    #             new_tile = self.board[new_row][new_col]
    #             if new_tile.get_booth() is None:
    #                 edge_weight = max(new_tile.get_threshold(), 1)
    #                 distances[new_row][new_col] = min(distances[new_row][new_col],
    #                                                   min_distance + edge_weight)


    def step(self, visible_board, states, score):
        """
        The step function should return a list of four Directions.

        For more information on what visible_board, states, and score
        are, please look on the wiki.
        """

        return [Direction.LEFT, Direction.UP, Direction.RIGHT, Direction.DOWN]

