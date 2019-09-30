import datetime as d

# classes
class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises


class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  def __repr__(self):
    return "The address of the restaurant is " + self.address
  
  def available_menus(self, time):
    result = []
    for menu in self.menus:
      if menu.start_time <= d.time(hour=time) <= menu.end_time:
        result.append(menu)
    return result
	

class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = d.time(hour=start_time)
    self.end_time = d.time(hour=end_time)
    
  def __repr__(self):
    return self.name + " menu available from " + self.start_time.strftime("%I%p") + " to " + self.end_time.strftime("%I%p")
  
  def calculate_bill(self, purchased_items):
    total_price = 0
    for item in purchased_items:
      total_price += self.items[item]
    return total_price

# # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # 
# script
# menus
brunch = Menu("Brunch", 
             {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
},
              11,
              16
)

early_bird = Menu("Early-bird",
                  {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
},
                  15,
                  18
)

dinner = Menu("Dinner",
              {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
},
              17,
              23
)

kids = Menu("Kids",
            {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
},
            11,
            21
)

arepas_menu = ("Arepas menu",
               {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
},
               10,
               20
)


# testing representation
# print(brunch)

# testing .calculate_bill method
our_breakfast = ['pancakes', 'home fries', 'coffee']
# print("Brunch bill:")
# print(brunch.calculate_bill(our_breakfast))
# print()

# testing .calculate_bill method
last_guests_order = ['salumeria plate', 'mushroom ravioli (vegan)']
# print("Early_bird last guests' bill:")
# print(early_bird.calculate_bill(last_guests_order))
# print()

# # # # # # # # # # # # # # # # # # # # # # # # # # # 
# creating franchises
flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])
new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])

arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

# testing franchise representation
# print(flagship_store)

# print(flagship_store.menus)
# print(flagship_store.available_menus(12))
# print()
# print(new_installment.available_menus(12))
# print()
# print()
# print(flagship_store.available_menus(17))
# print()
# print(new_installment.available_menus(17))

# # # # # # # # # # # # # # # # # # # # # # # # # # # 
# testing business class
first_business = Business("Basta Fazoolin' with my Heart", [flagship_store , new_installment])

arepas_business = Business("Take a' Arepa", [arepas_place])
