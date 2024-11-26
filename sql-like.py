class Node:
  def __init__(self, name):
    self.name = name

foundation = Node("Foundation")
framing = Node("Framing")
plumbing = Node("Plumbing")
electrical = Node("Electrical")
hvac = Node("HVAC")
drywall = Node("Drywall")
painting = Node("Painting")

steps = [foundation, framing, plumbing, electrical, hvac, drywall, painting]

connections = [
  (foundation, framing),
  (framing, electrical),
  (framing, plumbing),
  (framing, hvac),
  (electrical, drywall),
  (plumbing, drywall),
  (hvac, drywall),
  (drywall, painting)
]

print([f"{x[0].name}->{x[1].name}" for x in connections])
