from room import Room
from player import Player
from item import Item
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
print(f'\nWelcome {name}!, Your journey has just begun!');

def add_item():
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    item = input('Please enter the name of the item you want to add! ')
    item = item.replace(' ', '')
    description = input('Add a description about the item ')
    new_item = Item(item, description)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(f'\n{new_item.name} was added to {current_player.current_room.name}')
    return current_player.current_room.add_item(new_item)

while True: 
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(f'You are currently in the {current_player.current_room.name}')
    print(f'{current_player.current_room.options}')
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(f'{name}, you have a couple of options now!')
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
        items = current_player.current_room.view_items()
        if items == 0:
            print(f'{name}, would you like to add an item?')
            i = input('Yes or No? ')
            i = i[0].lower()
            if i == "y":
                item = add_item()
        else:
            print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print(f'{name}, here are the items in {current_player.current_room.name}:')
            for x in items:
                print(x)
            print('\nTo grab an item type grab [item_name]!')
            print('To add an item type add [item_name]!')
            d = input('\nWhat would you like to do?').split()
            s = [x.lower() for x in d]
            if len(s) == 2:
                if s[0] == "add":
                    item = add_item()
                elif s[0] == 'grab':
                    item = grab_item()      
    else:
        print('I don\'t understand!')      


                
