# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, options):
        self.name = name
        self.options = options
        self.contains = []
    def add_item(self, item):
        self.contains.append(item)
    def view_items(self):
        print(f'You have the option of these items: ')
        for x in self.contains:
            print(x)