class pokemon:
  def __init__(self, name, level, pokemon_type, max_health, health, is_knocked_out):
    self.name = name
    self.level = level
    self.pokemon_type = pokemon_type
    self.max_health = max_health
    self.health = health
    self.is_knocked_out = is_knocked_out
    
  def lose_health(self, losing_level=1):
    if self.health >=losing_level:
      self.health -= losing_level
    else:
      self.health = 0
      is_knocked_out = True
      print("Your pokemon is knocked out")
    print("{name} now has {health} health".format(name=self.name, health=self.health))
    return self.health
  
  def gain_health(self, healing_level=1):
    self.health = min(self.health + healing_level, self.max_health)
    print("{name} now has {health} health".format(name=self.name, health=self.health))
    return self.health
  
  def attack(self, other_pokemon):
    other_pokemon.lose_health(self.level)
    print("You successfully attacked")
    
    
    