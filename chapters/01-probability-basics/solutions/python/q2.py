from random import choice
from tqdm import tqdm

trials_num = 10000000     # Choose it close to infinity
target_sum = 7            # Event

def main():
  n_events = 0
  for i in tqdm(range(trials_num)):
    dice_total = run_experiment()
    if dice_total == target_sum:
      n_events += 1
  probability_e = n_events / trials_num
  print(f'After {i} trials, the probability of two dices shown-numbers equals 7 is {probability_e}.')

def run_experiment():
  d_1 = roll_dice()
  d_2 = roll_dice()
  return d_1 + d_2

def roll_dice():
  # This simulates rolling a dice
  return choice([1, 2, 3, 4, 5, 6])

if __name__ == '__main__':
  # This starts the program
  main()
