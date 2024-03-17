place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass
elif place == "cave":
    # Task 2: Based on the corrected code from Task 1, expand the game. If the user chooses "cave", ask them if they want to "light a torch" or "proceed in the dark", and provide outcomes for each decision.
    torch = input("light a torch or proceed in the dark? ")
    if torch == "light a torch":
        print("You're saved! You see the minotaur walking the other direction and are able to sneak  away before he sees you!")
    elif torch == "proceed in the dark":
        print("Bummer. You shoulda lit the torch. You ended up bumping into the minotaur who had you for dinner.")
    else:
        pass
else:
    pass

# Task 3: If the user makes an invalid choice at any point, use the pass statement for now. Later, you can enhance this to provide feedback or a different branch of the story.
