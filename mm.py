class Boss:
    def __init__(self, name):
        self.name = name

class EdgeConnection:
    def __init__(self, one, two):
        self.one = one
        self.two = two

metal_man = Boss("Metal Man")
wood_man = Boss("Wood Man")
bubble_man = Boss("Bubble Man")
air_man = Boss("Air Man")
crash_man = Boss("Crash Man")
heat_man = Boss("Heat Man")
flash_man = Boss("Flash Man")
quick_man = Boss("Quick Man")

c1 = EdgeConnection(metal_man, wood_man)
c2 = EdgeConnection(metal_man, bubble_man)
c3 = EdgeConnection(wood_man, air_man)
c4 = EdgeConnection(air_man, crash_man)

edges = [c1, c2, c3, c4]

for connection in edges:
    if connection.one == metal_man:
        print(f"Metal Man can easily beat {connection.two.name}")

