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
import copy

class Company(object):
    def __init__(self, name, points):
        self.name = name
        self.points = points
        self.lineCoords = []
        self.boothCoords = []
        self.front_line = None
        self.back_line = None
        self.cached_line_size = None
    
    def __repr__(self):
        return str(self.name)+",  " + str(self.points)+",  "+str(self.lineCoords)+",  "+str(self.boothCoords)+",  "+str(self.front_line)+",  "+str(self.back_line)
        
def checkFrontOfLine(company, board, row, col):
    if board[row][col].is_end_of_line():
        company.front_line=(row,col)
    # if inBounds(board, row-1, col):
    #     if board[row-1][col].get_booth()==company.name:
    #         company.front_line=(row,col)
    #         return
    # if inBounds(board, row, col-1):
    #     if board[row][col-1].get_booth()==company.name:
    #         company.front_line=(row,col)
    #         return
    # if inBounds(board, row+1, col):
    #     if board[row+1][col].get_booth()==company.name:
    #         company.front_line=(row,col)
    #         return
    # if inBounds(board, row, col+1):
    #     if board[row][col+1].get_booth()==company.name:
    #         company.front_line=(row,col)
    #         return

def checkBackOfLine(company, board, row, col):
    adjLines = 0
    if inBounds(board, row-1, col):
        if board[row-1][col].get_line()==company.name:
            adjLines+=1
    if inBounds(board, row+1, col):
        if board[row+1][col].get_line()==company.name:
            adjLines+=1
    if inBounds(board, row, col-1):
        if board[row][col-1].get_line()==company.name:
            adjLines+=1
    if inBounds(board, row, col+1):
        if board[row][col+1].get_line()==company.name:
            adjLines+=1
    if adjLines<2 and not board[row][col].is_end_of_line():
        company.back_line=(row, col)


def inBounds(board, row, col):
    if row<0 or col<0 or row >= len(board) or col>=len(board[0]):
        return False
    return True


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
        self.cachedThresholds = [[0]*len(initial_board[0]) for _ in range(len(initial_board))]

        self.all_companies = dict()  # compString to compObject

        for comp in company_info:
            self.all_companies[comp] = Company(comp, company_info[comp])
        
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if initial_board[row][col].get_booth(): #this tile is a booth tile
                    company = initial_board[row][col].get_booth()
                    self.all_companies[company].boothCoords.append((row,col))
            
                if initial_board[row][col].get_line(): #this tile is a line Tile
                    company = initial_board[row][col].get_line()
                    checkFrontOfLine(self.all_companies[company], initial_board, row, col)
                    checkBackOfLine(self.all_companies[company], initial_board, row, col)
                    self.all_companies[company].lineCoords.append((row,col))

        # print("OG INFO:", company_info)
        # for comp in self.all_companies:
        #     print("OBJECT COMPANY:", self.all_companies[comp])   

        # for step
        self.current_paths = [[] for team in range(team_size)]
        self.current_companies = [None for team in range(team_size)]
        self.at_starts = [True for team in range(team_size)]

        self.all_companies_list = list(self.all_companies.values())
        self.unvisited_companies = copy.deepcopy(self.all_companies_list)

    def updateCachedLength(self, comp, tile, row, col):
        if self.all_companies[comp].back_line == (row, col):
            lineLength = len(self.all_companies[comp].lineCoords)
            self.all_companies[comp].cached_line_size = tile.get_num_bots() + (lineLength-1)*3
        else:
            (r1, c1) = self.all_companies[comp].front_line
            dist = max(abs(row-r1), abs(col-c1))
            self.all_companies[comp].cached_line_size = min(tile.get_num_bots(), 3) + 3*dist

    def updateCachedThresholds(self, visible_board, states):
        for row in len(visible_board):
            for col in len(visible_board[0]):
                tile = visible_board[row][col]
                if tile.is_visible():
                    self.cachedThresholds[row][col]=tile.get_threshold()
                    
                    if tile.is_end_of_line():
                        comp = tile.get_line()
                        self.updateCachedLength(comp, tile, row, col)

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
        def get_direction(x, y, next_x, next_y):
            if next_x == x - 1:
                return Direction.UP
            elif next_x == x + 1:
                return Direction.DOWN
            elif next_y == y - 1:
                return Direction.LEFT
            elif next_y == y + 1:
                return Direction.RIGHT

        def get_direct_booth(x, y, next_x, next_y):
            if next_x < x:
                return Direction.UP
            elif next_x > x:
                return Direction.DOWN
            elif next_y < y:
                return Direction.LEFT
            elif next_y > y:
                return Direction.RIGHT

        directions = []

        for i in range(len(states)):
            state = states[i]
            path = self.current_paths[i]
            company = self.current_companies[i]

            # getting onto a tile
            if state.progress != 0:
                print("Case 1")
                directions.append(state.dir)
                state = states[i]
                continue
            # have reached a line, in the process of getting to booth OR at starting position
            if len(path) == 0:
                # in line
                if state.line_pos != -1:
                    print("Case 2")
                    directions.append(Direction.NONE)
                    state = states[i]
                    continue
                # just got out of line
                if self.at_starts[i] or (state.x == company.front_line[0] and state.y == company.front_line[1]):
                    print("Case 3")
                    self.at_starts[i] = False
                    print(state.x, state.y)
                    bfs_result = self.BFS(state.x, state.y)
                    if bfs_result == None:
                        self.unvisited_companies = copy.deepcopy(self.all_companies_list)
                        bfs_result = self.BFS(state.x, state.y)
                    # print(self.unvisited_companies)
                    # print(self.all_companies_list)
                    print(self.all_companies_list)
                    path, company = bfs_result
                    print("BFS PATH")
                    print(path)
                    self.current_paths[i] = path
                    self.current_companies[i] = company
                    self.unvisited_companies.remove(company)
                    (next_x, next_y) = path.pop(0)
                    directions.append(get_direction(state.x, state.y, next_x, next_y))
                    state = states[i]
                    continue
                # getting into line
                if visible_board[state.x][state.y].is_end_of_line():
                    print("Case 4")
                    directions.append(Direction.ENTER)
                    state = states[i]
                    continue
                # moving to end of line
                print("Case 5")
                directions.append(get_direct_booth(state.x, state.y, company.front_line[0], company.front_line[1]))
            # haven't reached destination line
            else:
                print("Case 6")
                (next_x, next_y) = path.pop(0)
                directions.append(get_direction(state.x, state.y, next_x, next_y))
            
            state = states[i] 
            # print(state.x)
            # print(state.y) 
            # print(path)
            # print(company)    

        print(directions)
        return directions
                  
