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

class Company(object):
    def __init__(self, name, points):
        self.name = name
        self.points = points
        self.lineCoords = []
        self.boothCoords = []
        self.front_line = None
        self.back_line = None
    
    def __repr__(self):
        return str(self.name)+",  " + str(self.points)+",  "+str(self.lineCoords)+",  "+str(self.boothCoords)+",  "+str(self.front_line)+",  "+str(self.back_line)
        
def checkFrontOfLine(company, board, row, col):
    # if board[row][col].is_end_of_line():
    #     print("FUCK")
    #     company.front_line=(row,col)
    # print("RIP")
    if inBounds(board, row-1, col):
        if board[row-1][col].get_booth()==company.name:
            company.front_line=(row,col)
            return
    if inBounds(board, row, col-1):
        if board[row][col-1].get_booth()==company.name:
            company.front_line=(row,col)
            return
    if inBounds(board, row+1, col):
        if board[row+1][col].get_booth()==company.name:
            company.front_line=(row,col)
            return
    if inBounds(board, row, col+1):
        if board[row][col+1].get_booth()==company.name:
            company.front_line=(row,col)
            return

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
        # self.company_info = company_info

        self.team_name = "ThanosDidNothingWrong"

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


        print("OG INFO:", company_info)
        for comp in self.all_companies:
            print("OBJECT COMPANY:", self.all_companies[comp])    



    def step(self, visible_board, states, score):
        """
        The step function should return a list of four Directions.

        For more information on what visible_board, states, and score
        are, please look on the wiki.
        """
        return [Direction.RIGHT, Direction.LEFT, Direction.UP, Direction.DOWN]

        pass
