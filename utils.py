import random

def play_word(word, letter_to_points):
    point_total = 0
    for item in word:
        point_total += letter_to_points.get(item, 0)
    return point_total

def ins_del_compare(s1, s2, tolerance):
    dif = abs(len(s1) - len(s2))
    if not (dif <= tolerance):
        return False
    shorter, longer = sorted([s1, s2], key=len)
    for letter in shorter:
        for num in range(len(longer)):
            if letter != longer[num] and num == len(longer) - 1:
                return False;
            if letter == longer[num]:
                longer = longer[:num] + longer[num + 1:]
                break;
    return True


def Scrabble():
    while True:
        # immutable
        letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                   "U",
                   "V", "W", "X", "Y", "Z"]
        points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

        letter_to_points = {key: value for key, value in zip(letters, points)}

        # a dictionary that says how many of each letter there is
        letters_to_count = {"A": 9, "B": 2, "C": 2, "D": 4, "E": 12, "F": 2, "G": 3, "H": 2, "I": 9, "J": 1, "K": 1,
                            "L": 4,
                            "M": 2, "N": 6, "O": 8, "P": 2, "Q": 1, "R": 6, "S": 4, "T": 6, "U": 4, "V": 2, "W": 2,
                            "X": 1,
                            "Y": 2, "Z": 1}

        # creates a list of all the letters and stores them in letters1
        letters1 = []
        for key, value in letters_to_count.items():
            for item in range(value):
                letters1.append(key)

        # sets up how many players there are
        number_of_players = 0
        while number_of_players <= 1:
            try:
                number_of_players = int(input("Number of players: "))
            except:
                print("You have to enter a positive number that is greater than 1")
        print()

        # creates a name for each player and appends it to the players list
        players = []
        for item in range(number_of_players):
            players.append(input(f"Player {item + 1} Name: "))
        print()

        # creates a dictionary that stores the player's name as the key and the player's seven letters as the value
        rack = {}
        for item in players:
            rack[item] = []
        for letter in rack.values():
            for item in range(0, 7):
                letter.append(letters1.pop(random.randint(0, len(letters1))))

        # creates a dictionary that stores the player as the key and the player's points as the value
        player_to_points = {}
        for item in players:
            player_to_points[item] = 0

        # actual game
        while len(letters1) != 0:

            # keeps on going through each players turn until there are no more letters
            for item in players:

                # prints each player's reack before they enter their word in
                print(f"{item}: {rack.get(item)}")
                word = input(f"It's {item}'s turn: ").upper()

                # checks to see if the player passes their turns and wants to exchange letters
                if word == "PASS":
                    how_many = int(input("How many to replace? "))
                    for nums in range(how_many):
                        # adds however many letters requested back into the letters1 list and puts new letters into the
                        # value of the player's rack
                        letters1.append(rack.get(item).pop(random.randint(0, 6)))
                        rack.get(item).append(letters1.pop(random.randint(0, len(letters1) - 1)))
                contain = False

                # checks to see if words can be made with the letters in the player's rack
                for h in word:
                    if not (h in rack.get(item)):
                        contain = False
                        break
                    else:
                        contain = True

                # if the player made a legal word points are added and new letters are put in. If not a print line is
                # executed.
                if contain:
                    player_to_points[item] = player_to_points.get(item, 0) + play_word(word, letter_to_points)
                    for num in word:
                        rack.get(item).remove(num)
                    for h in range(len(word)):
                        rack.get(item).append(letters1.pop(random.randint(0, len(letters1) - 1)))
                if (not contain) and word != "PASS":
                    print("Sorry those words are not in your rack or you passed")

                # prints the score of each individual player
                print(player_to_points.get(item))
                print()

            # prints total score of all players
            for player, score in player_to_points.items():
                print(f"{player}: {score}")
            print()
        print("Game Over")
