from random import randint
from timeit import default_timer as timer
from numpy import sum, asarray, ndarray, zeros

'''
            HOW THE GAME WORKS

You play the game with an ordered set of dice.

If you roll high on the current die, advance to the next die.
If you do not roll high on the current die, go back to the first die.

You win by rolling high on the last die.
'''

def play_games(dice: list[int], num_games: int) -> ndarray[float]:
    counts: list[int] = [0]*len(dice)

    counts_table: ndarray = zeros((num_games, len(dice)+1), dtype = float)

    for i in range(num_games):
        print(f">> Running trial {i+1}", end="\r", flush=True)
        start: float = timer()
        counts = play_games_helper(dice)
        end: float = timer()

        counts_table[i, -1] = end-start
        counts_table[i, :-1] = asarray(counts)
    
    return counts_table

def play_games_helper(dice: list[int]) -> list[int]:
    counts: list[int] = [0]*len(dice)

    current: int = 0
    finished: bool = False
    while not finished:
        counts[current] += 1
        roll: int = randint(1, dice[current])
        if roll == dice[current]:
            if current == len(dice)-1:
                finished = True
            else:
                current += 1
        else:
            if current > 0:
                current = 0
    
    return counts

def summarize_counts_table(counts_table: ndarray[float], human_time_to_roll: int, dice_str: list[str]) -> str:
    num_games: int = len(counts_table[:, 0])
    num_dice: int = len(counts_table[0,:]) - 1
    total_rolls: int = sum(counts_table[:,:-1])
    human_average: float = human_time_to_roll*total_rolls/num_games

    total_die_rolls: list[int] = [int(sum(counts_table[:,i])) for i in range(num_dice)] + [num_games]

    statistics_summary_arr: list[str] = [] 
    statistics_summary_arr.append(f'{"".join(['<']*15)} Results for {num_games} trials {"".join(['>']*15)}')
    statistics_summary_arr.append(f'Using Dice Setup: {', '.join(dice_str)}')
    statistics_summary_arr.append(f'{''.join(['-']*12)} Average Rolls {''.join(['-']*6)} Average High Rolls {''.join(['-']*5)}')
    statistics_summary_arr.append("\n".join([f'Results for {arr[2]:<4}: {arr[0]//num_games:<15,} | {arr[1]//num_games:<15,}' for arr in zip(total_die_rolls[:-1], total_die_rolls[1:], dice_str)]))
    statistics_summary_arr.append(f'On average, {total_rolls//num_games:,} rolls were made in each game.')
    statistics_summary_arr.append(f'On average, each game took {sum(counts_table[:,-1])/num_games:.5f} seconds to complete.')
    statistics_summary_arr.append(f'Assuming a person rolls once every {human_time_to_roll} seconds, each game takes {human_average:,.2f} seconds on average.')
    statistics_summary_arr.append(f'This equates to {human_average/60:,.2f} minutes, {human_average/(60*60):,.2f} hours, and {human_average/(60*60*24):,.2f} days.')

    return '\n'.join(statistics_summary_arr)


def play_game(dice: list[int]) -> None:
    counts: list[int] = [0] * len(dice)
    current: int = 0
    finished: bool = False

    while not finished:
        counts[current] += 1
        roll: int = randint(1, dice[current])
        if roll == dice[current]:
            if current == len(dice)-1:
                finished = True
            else:
                current += 1
        else:
            if current > 0:
                current = 0
    
    return counts + [1]