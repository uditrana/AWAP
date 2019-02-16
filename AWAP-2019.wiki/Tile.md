The Tile class contains information about what is on the tile and what it is a part of. A Tile can be either be part of a booth, be part of a line, or neither.

## Methods

### `Tile.get_booth()`

A Tile object can be part of a booth. In other words, this means that the Tile represents the area where a table and the recruiters would be in an actual career fair. Multiple Tile objects make up a single booth, but all the Tile objects must be positioned in a straight line.

Thus, if the specified Tile object is part of a booth, `Tile.get_booth()` returns the name of the company at the booth, and otherwise returns `None`.

### `Tile.get_line()`

Each company has a line associated with the booth. For more information on how the line works, please go to the Line page. In short, however, `Tile.get_line()` returns the name of the company associated with the line if the tile is part of a line, and otherwise returns `None`. 

The Line page explains more on what it means to be "part of a line".

### `Tile.get_num_bots()`

This method returns the number of bots on the tile.

### `Tile.is_end_of_line()`

This method returns `True` if the tile is the end of a line, and otherwise returns `False`. Again, reference the Line page for more on what it means to be the end of a line.

### `Tile.get_threshold()`

This method returns the number of turns it takes to move to a tile. As explained in the problem statement, the more people there are on the destination tile, the longer it takes to move into that tile.

### `Tile.is_visible()`

This method returns `True` if the tile is visible to the player, and `False` if the tile is not visible to the player.

More about movement is explained in the Direction page.
