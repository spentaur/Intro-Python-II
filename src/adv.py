from room import Room
from player import Player
import textwrap

wrapper = textwrap.TextWrapper(width=79)

# Declare all the rooms

room = {
    'outside': Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons"),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player1 = Player("Spencer Adams", room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and descides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

user_input = ''

while user_input != 'q':
    print("Your current room is:")
    print("\n")
    print(f"{player1.current_room.name}:")
    print(wrapper.fill(text=player1.current_room.description))
    print("\n")
    prompt = "Please enter a direction you wish to move (n, s, e, w), or q to exit: \n"
    user_input = input(prompt)

    card_dir = ['n', 's', 'e', 'w']

    if user_input == 'q':
        print("Goodbye!")
        continue

    if user_input not in card_dir:
        print(
            f"\n'{user_input}' is not one of the accpeted directions (n, s, e, w, q). Please try again. \n")
        continue

    if (user_input == 'n') & (hasattr(player1.current_room, 'n_to')):
        player1.current_room = player1.current_room.n_to
    elif (user_input == 's') & (hasattr(player1.current_room, 's_to')):
        player1.current_room = player1.current_room.s_to
    elif (user_input == 'e') & (hasattr(player1.current_room, 'e_to')):
        player1.current_room = player1.current_room.e_to
    elif (user_input == 'w') & (hasattr(player1.current_room, 'w_to')):
        player1.current_room = player1.current_room.w_to
    else:
        print(
            f"\nYou are not able to move '{user_input}' while you are in the room '{player1.current_room.name}'")
        print("Please pick another direction. \n")
