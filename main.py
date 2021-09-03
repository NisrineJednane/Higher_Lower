# import art and data
from art import logo, vs
from data_list import data
import random
from replit import clear

# function to format accs into printable data
def format_data(target_account):
  account_name = target_account["name"]
  account_description = target_account["description"]
  account_country = target_account["country"]
  account_followers = target_account["follower_count"]
  return f"{account_name} is a {account_description} from {account_country}"

def check_answer(guess, a_followers, b_followers):
  if a_followers > b_followers:
    # simpler way to return True/False
    return guess == "a"
  else:
    return guess == "b"

# logo
total = 0

# var to activate while loop
game_continue = True
account_b = random.choice(data)
# GAME LOOP STARTS HERE

# generate a random accounts from data
while game_continue == True:
  print(logo)
  account_a = account_b
  account_b = random.choice(data)
  while account_a == account_b:
    account_b = random.choice(data)

  # gameplay
  print(f"Option A: {format_data(account_a)}")
  print(vs)
  print(f"Option B: {format_data(account_b)}")

  user_guess = input("Who do you think has most followerS? A or B? \n").lower()

  # check user guess

  # get first followers count
  a_follower_count = account_a["follower_count"]
  # get second followers count
  b_follower_count = account_b["follower_count"]

  # set variable to check user answer
  is_correct = check_answer(user_guess, a_follower_count, b_follower_count)

  # give user feedback on guess
  if is_correct:
    total += 1
    print(f"That's correct!\nYour score is {total}")
    clear()
  else:
    game_continue = False
    print(f"You lose. \nYour final score is {total}")


