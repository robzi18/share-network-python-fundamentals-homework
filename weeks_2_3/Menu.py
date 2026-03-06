
import datetime
time = datetime.datetime.now()


class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        if time.strftime("%H") >= self.start_time and time.strftime("%H") <= self.end_time:
            return f"the name of the menu is: {self.name} available."
        else:
            return f"the {self.name} is not available now.please check the opening hours!"

    def calculate_bill(self, purchased_items):
        total_bill = 0
        if all(item in self.items for item in purchased_items):
            for item in purchased_items:
                total_bill += self.items[item]
            return f"The total bill in the {self.name} menu is {total_bill}."
        else:
            return f"{purchased_items} are not in the {self.name} menu."


brunch_menu = Menu("brunch", {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50,
                              'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}, "08:00", "16:00")
early_bird = Menu("early_bird", {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00,
                                 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}, "15:00", "18:00")
dinner = Menu("dinner", {'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00,
                         'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}, "17:00", "23:00")
kids = Menu("kids", {'chicken nuggets': 6.50,
                     'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}, "11:00", "21:00")
print(brunch_menu)
print(early_bird)
print(dinner)
print(kids)
print(brunch_menu.calculate_bill(['pancakes', 'home fries', 'coffee']))
print(early_bird.calculate_bill(
    ['salumeria plate', 'mushroom ravioli (vegan)']))


class Franchise(Menu):
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __str__(self):
        return f"{self.name} is located at {self.address}"

    def available_menus(self, time):
        available = []
        for items in self.menus:
            if time >= items.start_time and time <= items.end_time:
                available.append(items.name)
        return f"{available} are available at {time}"


flagship_store = Franchise("1232 West End Road", [
                           brunch_menu, early_bird, dinner, kids])
new_installment = Franchise("12 East Mulberry Street", [
    brunch_menu, early_bird, dinner, kids])
print(flagship_store.available_menus("15:00"))
print(flagship_store.available_menus("12:00"))
print(flagship_store.available_menus("17:00"))


# --- Creating Businesses ---
class Bussiness(Franchise):
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises

    def __str__(self):
        return f"This is {self.name} Business."


first_business = Bussiness("Basta Fazoolin", [flagship_store, new_installment])
arepas_menu = Menu("take_a_arepa", {'arepa pabellon': 7.00, 'pernil arepa': 8.50,
                                    'guayanes arepa': 8.00, 'jamon arepa': 7.50}, "10:00", "08:00")
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])
Arepa = Bussiness("Arepa", [arepas_place])
print(Arepa)
