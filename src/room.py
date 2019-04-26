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
        if len(self.contains) == 0:
            print("\nLooks likes there are no items in this room yet")
            return 0
        else:
            return self.contains