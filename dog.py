class Dog:
  def __init__(self, data):
    self.name = data["name"]
    self.breed = data["breed"]
    self.age = data["age"]
    self.personality_type = data["p_type"]

    self.energy_level = 100

  def go_for_a_walk(self):
    self.energy_level = self.energy_level - 5
    print(f"My name is {self.name} and my owner took me for a stroll, now my energy level is {self.energy_level}!")


spike_data = {
  "name" : "Spike",
  "breed" : "Golden Doodle",
  "age" : 5,
  "p_type" : "Mellow",
}
spike = Dog(spike_data)

spike.go_for_a_walk()