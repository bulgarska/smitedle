import random
import json


def game_instructions():
    print("Game Instructions:\n"
          "Enter the name of a Smite god.\n"
          "🟩 below a category means the category is correct.\n"
          "🟨 below a category means the category is partially correct.\n"
          "⬛ below a category means the category is incorrect.\n")

def get_gods():
    file_path = "smite.json"
    with open(file_path, "r", encoding="utf-8") as f:
        gods_data = json.load(f)
    gods_list = []
    for god in gods_data["smite"]:
        gods_list.append([god["Name"], god["Roles"], god["Type"].split(",")[0].strip(), god["Type"].split(",")[1].strip(), god["Pros"], god["Pantheon"]])
    return gods_list

def get_god_lists(file_path):
    words_file = open(file_path, "r")
    words_list = words_file.read().splitlines()
    gods_list = []
    for i in words_list:
        gods_list.append(i.split(","))
    return gods_list


def get_guess(gods_list):
    gods_list = gods_list
    guess = ""
    god_names = [god[0] for god in gods_list]
    while not guess.isalpha() or guess not in god_names:
        guess = str(input("Enter a god: \n"))
    for god in gods_list:
        if god[0] == guess:
            return god


def get_hidden_god(gods_list):
    list_hidden_gods = gods_list
    random_num = random.randrange(0, len(list_hidden_gods))
    return list_hidden_gods[random_num]


# game loop
def check_god(gods_list):
    hidden_god = get_hidden_god(gods_list)
    attempts = 6
    guesses_all = []
    while attempts > 0:
        guess = get_guess(gods_list)
        guesses_all.append(guess)
        if guess == hidden_god:
            print(f"You guessed the god correctly! {hidden_god}\n")
            break
        else:
            attempts -= 1
            print(f"You have {attempts} attempts left.\n")
            categories_checked = []
            categories_output = []
            for guess in guesses_all:
                for i in range(0, len(hidden_god)):
                    if guess[i] == hidden_god[i]:
                        categories_checked.append(guess[i])
                        categories_output.append("🟩")
                    elif guess in hidden_god:
                        categories_checked.append(guess[i])
                        categories_output.append("🟨")
                    else:
                        categories_checked.append(guess[i])
                        categories_output.append("⬛")
            # print("God - Gender - Role - Position - Range - Damage - Pros - Pantheon - Release year")
            print("God -------- Role -------- Range -------- Damage -------- Pros -------- Pantheon")
            for start in range(0, len(categories_checked), len(hidden_god)):
                print(' ----- '.join([str(categories_checked[i]) for i in range(start, start + len(hidden_god))]))
                print(' ----------- '.join([str(categories_output[i]) for i in range(start, start + len(hidden_god))]))
            if attempts == 0:
                print(f"Game over !!!! The correct god is: {hidden_god[0]}\n")


if __name__ == '__main__':
    game_instructions()

    gods_list = get_gods()

    check_god(gods_list)