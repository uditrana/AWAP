The State class stores information about a single bot. It contains the following information.

### `state.dir`

A State object has a variable `dir` that indicates which direction the bot is moving. This can be checked to see if the bot's previous movement was canceled.

### `state.id`

The State object has a variable `id` that contains the ID of the bot that this State represents.

### `state.x`, `state.y`

`x` and `y` represent the (x, y) position of the bot. The location of the bot is in array format; that is, in a 2D array, the position (x, y) represents `arr[x][y]`.

### `state.progress`

`state.progress` indicates how much progress the bot has made in moving in the direction of `state.dir`. Note that `state.progress` is 0 if the bot is not moving. For more information on progress and threshold, refer to the Direction page.

### `state.threshold`

`state.threshold` indicates the number of turns it takes to move in the direction of `state.dir`. If `state.dir` is not in one of the cardinal direction, `state.threshold` indicates the number of turns it takes to move into the current location.

### `state.line_pos`

`self.line_pos` indicates what position this bot is in the line. If the bot is not in a line, `self.line_pos` has a value of -1.

Although a State object has more variables, only these are relevant to the player.
