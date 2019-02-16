"""
The team.py file is where you should write all your code!

Write the __init__ and the step functions. Further explanations
about these functions are detailed in the wiki.

List your Andrew ID's up here!
andrewid1
andrewid2
andrewid3
andrewid4
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

        # for step
        self.current_paths
        self.current_companies

        self.team_name = # Add your team name here!

    def step(self, visible_board, states, score):
        """
        The step function should return a list of four Directions.

        For more information on what visible_board, states, and score
        are, please look on the wiki.
        """
        def get_direction(x, y, dest_x, dest_y):
            if next_x == x - 1:
                state.dir = Direction.LEFT
            elif next_x == x + 1:
                state.dir = Direction.RIGHT
            elif next_y == y - 1:
                state.dir = Direction.DOWN
            elif next_y == y + 1:
                state.dir = Direction.UP

        def defer(i, state, path, company):
            states[i] = state
            self.current_paths[i] = path
            self.current_companies[i] = company

        directions = []

        for i in range(len(states)):
            state = states[i]
            path = self.current_paths[i]
            company = self.current_companies[i]

            # getting onto a tile
            if state.progress != 0:
                directions.append(state.dir)
                defer(i, state, path, company)
                continue
            # have reached a line, in the process of getting to booth
            if len(path) == 0:
                # in line
                if state.line_pos != 1:
                    directions.append(Direction.NONE)
                    defer(i, state, path, company)
                    continue
                # just got out of line
                if state.x == company.front_line[0] && state.y == company.front_line[1]:
                    bfs_result = bfs(state.x, state.y)
                    if bfs_result == None:
                        self.unvisited_companies = self.all_companies
                        bfs_result = bfs(state.x, state.y)
                    (path, company) = bfs_result
                    self.current_paths[i] = path
                    self.current_companies[i] = company
                    self.unvisited_companies.remove(company)
                    (next_x, next_y) = path.pop(0)
                    directions.append(get_direction(state.x, state.y, next_x, next_y))
                    defer(i, state, path, company)
                    continue
                # getting into line
                if Tile.is_end_of_line():
                    directions.append(Direction.ENTER)
                    defer(i, state, path, company)
                    continue
                # moving to end of line
                directions.append(get_direction(state.x, state.y, company.front_line[0], company.front_line[1]))
            # haven't reached destination line
            else:
                (next_x, next_y) = path.pop(0)
                directions.append(get_direction(state.x, state.y, next_x, next_y))

            defer(i, state, path, company)
                

        return directions
                    



            

