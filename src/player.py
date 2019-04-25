# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []
    def add_item(self, item):
        self.inventory.append(item)
    def view_inventory(self):
        if len(self.inventory) == 0:
            print('You have no items in you inventory')
            return 0
        else:
            return self.inventory