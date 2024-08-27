from dice_game_1 import play_games, summarize_counts_table
import numpy as np

def main() -> None:
    # Alter these three parameters to run games with different metrics.
    dice: list[int] = [4,6,8,10,12,20]
    num_games: int = 20
    human_time_to_roll: int = 1.3

    print(summarize_counts_table(play_games(dice, num_games), human_time_to_roll, [f'D{die}' for die in dice]))
    return

if __name__ == "__main__":
    main()