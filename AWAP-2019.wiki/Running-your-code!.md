Running your code is simple! The two main files we have provided for you to run your code are `main.py` and `visualizer.py`. The command line arguments for each are listed below.

## `main.py`
`main.py` is the main file for running your code. Its command line arguments are

### `--num_moves`
Has a default value of 300. This is the upper limit on the number of turns in a game.

### `--score_threshold`
The score threshold has a base threshold of 200.

### `--board_directory`
This is the directory that holds each of the board files. The default value is `board/`; unless you plan on moving the board directory, this should not have to be specified.

### `--log_directory`
Similarly, this is the directory for the log files. The default value is `log/`.

### `--companies`
This reads from the specified file for a list of companies. The default value is `companies.txt`.

### `--board_file`
This specifies which file to use as the board. The default is `tiny`. Do not attach the `.txt` extension! This argument only takes the name of the file.

### `--log_file`
Similarly, this is the suffix to which the board will write the log file. So, if the argument `--board_file` is `tiny`, and the value of `--log_file` is `out`, the script will write to `tiny-out.txt` in the `--board_directory` folder.

### `--debug`
The `--debug` flag indicates whether or not this script prints debug messages at each turn. 

Thus, an example call to `main.py` would be
```
python main.py --board_file gates4 --log_file test
python main.py --board_file sample --debug
```

## `visualizer.py`

The visualizer file is for visualizing your log file. It reads from the log file that `main.py` generates while running. It uses a similar file format scheme as `main.py`. It has `--board_directory`, `--board_file`, `--log_directory`, and `log_file`, all of which act in the same manner that `main.py` does. The only different command line argument here is

### `--speed`
which is how fast the game moves.
