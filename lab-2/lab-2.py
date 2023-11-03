import random

class Hotel:
  def __init__(self, name, services=None):
    self.name = name
    self.services = services if services is not None else {}

class Service(Hotel):
  def __init__(self, name, services):
    super().__init__(name, services)
    self.name = name

  def serve(self, client):
    while any(client.needs.values()):
      for need, need_value in client.needs.items():
        if need in self.services and self.services[need] > 0:
          if self.services[need] >= need_value:
            client.needs[need] = 0
          else:
            client.needs[need] -= self.services[need]
      client.needs = {k: round(v, 2) for k, v in client.needs.items()}
      print(vars(client))

class Bar(Service):
  def __init__(self, name, services):
    super().__init__(name, services)

class Client:
  def __init__(self, name):
    self.name = name
    self.needs = self.generate_random_needs()

  def generate_random_needs(self):
    random_needs = ['eat', 'bar', 'child room', 'massage']  
    random_values = {need: round(random.uniform(0.1, 1.0), 1) for need in random.sample(random_needs, 2)}

    return random_values

client = Client("Chivas")
hotel = Hotel("Business Hotel", services={"eat": 0.5, "bar": 0.35, "child room": 0.25, 'massage': 0.5})
service = Service(hotel.name, hotel.services)
service.serve(client)
