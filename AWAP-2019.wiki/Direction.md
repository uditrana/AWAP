The Direction class is an Enum type that represents the possible movements in the game. The possible movements are listed below.

### `Direction.LEFT`, `Direction.UP`, `Direction.RIGHT`, `Direction.DOWN`

These four represent the four cardinal directions of movement. 

### `Direction.NONE`

This represents no movement.

### `Direction.ENTER`

This represents the act of entering a line.

### `Direction.REPLACE`

This represents having one player bot replace another player bot. 

## Movement

Movement in this game uses a progress system that depends on how crowded the adjacent destination tile is. Although stated in the flavor text, we will reiterate the movement principles.

* Movement takes one of the listed movements above.
* Movement can take more than one turn, depending on how many people are on the destination tile. If there are no bots on the destination tile, it will only take 1 turn. However, if there are multiple bots on the destination tile, it will now take x number of turns to move to the destination tile, where x is the value returned by `get_threshold()` (as listed in the Tile page). Every turn, the bot will make progress towards `x` if the bot maintains the same movement. 
  * In other words, if we are standing on a tile at (1, 2) and want to move to (1, 3), we need to tell the bot to move in the direction of `Direction.RIGHT`. If the threshold is 5 to move into (1, 3), we must tell the bot to move in the direction `Direction.RIGHT` for all 5 turns until the bot completes the movement. Giving the bot any other movement before the bot completes the movement will reset the progress and perform the new action.
  * This does not apply if the bot performs the action `Direction.ENTER`. If the bot performs the action `Direction.ENTER` on a valid tile (look at the Line page for more information), the bot must perform `Direction.NONE` until the bot is popped off the line by the line itself, after which the score is updated if the bot is part of a team. If any action other than `Direction.REPLACE` is performed while still in the line, the bot leaves the line immediately. 
  * The action `Direction.REPLACE` only works for the player (and more specifically, for the main bot with a helper bot). Note that replacing another bot only effectively works if one player is in a line and the other is not in a tile. Invoking the action `Direction.REPLACE` requires two bots to be on the same location, both of which perform the action `Direction.REPLACE`. If more than two bots or less than two bots are on the same location that use this movement, the action for the bots defaults to `Direction.NONE`. If this action is successful, it switches the states of the main bot and the helper bot. (For example, if the main bot is in line and the helper bot is on the tile, and both perform `Direction.REPLACE`, the helper bot is in the line and the main bot is on the tile in the next turn.) Note that if either bot is moving in one of the directions while performing this movement, the original movement is canceled as if `Direction.NONE` was called.
* If the threshold of the destination tile changes while in movement, the new threshold applies immediately. For example, if a bot has made x progress moving into a tile with threshold y where x < y, and the threshold changes to a value z where x > z, the bot immediately moves into the destination tile.
* A bot cannot move into a booth, nor can it move off the grid. Any invalid movements will not be performed and be reset.

## Helper methods

We provide a few helper methods to help in finding locations and directions.

### `Direction.get_loc(loc)`

Given a movement such as `Direction.RIGHT`, calling `(Direction.RIGHT).get_loc(loc)` will return the location of the tile that is to the right of `loc`. For any of the non-cardinal movements, this returns `loc`.

### `Direction.get_dir(src, dest)`

Note that this is a class method. The specified source and destination must be adjacent; otherwise, this method will return `Direction.NONE`. If source and destination are adjacent, it will return the appropriate cardinal direction that points from source to destination.

Note that this function cannot return `Direction.REPLACE` or `Direction.ENTER`.
