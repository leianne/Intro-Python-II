from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
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
def try_direction(direction, current_room):
    attribute = direction + '_to'
    if hasattr(current_room, attribute):
        return getattr(current_room, attribute)
    else:
        print('You can\'t go there')
        return current_room

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
print('Welcome to BonQuiQui\'s Quest!')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
name = input('Please enter your name! ')
current_player = Player(name, room['outside'])
print(f'Welcome {name}!, Your journey has just begun!');
while True: 
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(f'\nYou are currently in the {current_player.current_room.name}')
    print(f'\nThis room is {current_player.current_room.options}')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(f'Ok {name}')
    print('You have a couple of options now!')
    print(f'Would you like to move into another room? Or view the items in {current_player.current_room.name}')
    s = input('Move or View Items? ')
    s = s[0].lower()
    if s == 'm':
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('Where would you like to go?')
        d = input('Enter a direction!')
        d = d[0].lower()
        current_player.current_room = try_direction(d, current_player.current_room)
    elif s == "v" or s == "i":
        print(f'Ok {name}')
        items = current_player.current_room.view_items()
        if items == 0:
            print('Would you like to add an item?')
            i = input('Yes or No? ')
            i = i[0].lower()
            if i == "y":
                item = input('Please enter the name of the item you want to add! ')
                item = item.replace(' ', '')
                current_player.current_room.add_item(item)
        else:
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print(f'Here are the items in {current_player.current_room.name}')
            for x in items:
                print(x)
            i = input('Enter the item that you want to grab!')
            

                
