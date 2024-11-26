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

connection_matrix = [[0]*len(steps) for i in range(len(steps))]


connection_matrix[steps.index(foundation)][steps.index(framing)] = 1
connection_matrix[steps.index(framing)][steps.index(plumbing)] = 1
connection_matrix[steps.index(framing)][steps.index(electrical)] = 1
connection_matrix[steps.index(framing)][steps.index(hvac)] = 1
connection_matrix[steps.index(electrical)][steps.index(drywall)] = 1
connection_matrix[steps.index(plumbing)][steps.index(drywall)] = 1
connection_matrix[steps.index(hvac)][steps.index(drywall)] = 1
connection_matrix[steps.index(drywall)][steps.index(painting)] = 1

longest_name = max(len(x.name) for x in steps)


# Print header
print("".ljust(longest_name), end=" ")

for step in steps:
  print(step.name[:2], end=" ")
print()

for from_index, step in enumerate(steps):
  print(step.name.ljust(longest_name), end=" ")
  for to_index in range(len(steps)):
    print(connection_matrix[from_index][to_index], end="  ")
  print()
