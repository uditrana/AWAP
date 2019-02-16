The Team class is where you will write all of your code. The methods are described below.

## What you should not be doing

You are not allowed to access outside information such as reading from a file. Do not try to access the internal state of the game. Note that we work with our own versions of the runner and not the runner we send out to the players to avoid presenting any extraneous information. We discourage the use of third-party libraries; the problem should be doable without. 

You are, however, allowed to write your own helper functions, initialize your own instance variables, and create your own modules to help you do a good portion of the decision making. For example, you can make a custom module of some commonly used algorithms or decisions you make.

## Initialization

At initialization, you will get a copy of the initial 2D grid of Tile objects (look at the Tile page for more information). Use this time to do any precomputation you need to do, such as finding the positions of the tiles in the Google booth or figuring out where the line for Bloomberg is.

You will also get a dictionary of company informations. This dictionary is a mapping of company names to point values. The point value that is stored is the "major reward"; that is, you will receive these number of points if you talk to the company with your main bot (the first bot). Other bots will receive only half the number of points. 

As mentioned in the writeup, talking to the same company multiple times will result in less rewards, since the recruiters notice you. Note that the updated reward values are not reflected in the dictionary you get at initialization.

## Step

### Description

Step is where you will do a bulk of your work. At each time interval, the game will call the Team class' `step` function and pass it a version of the board, the states of their bots, and a score. 

The board that is passed in represents the board that your team can see - it only presents accurate information in the visible range around each of your bots. In each of these visible tiles, you will get the accurate state of the game at that time step; that is, each visible tile has the information of how many bots are on the tile, whether or not the tile is the end of a line, etc. In non-visible tiles, none of these are present, and the tile is a copy of the original tile stripped of this information. Note that the visibility of a tile is queryable.

The states of each bot is a State object for each bot in the team. Look in the State class for more information.

The score is what score your team has.

### Return type

The `step` function should return a list of 4 Directions. Look at the Direction class for more information. Note that the order of the Directions matter; for example, the first Direction in the list is always for the main bot (aka you), and the second to fourth Directions in the list is for the friend bots. Note that these always stay consistent; the second bot will always perform the action of the second Direction in the list.
