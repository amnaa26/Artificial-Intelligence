class FirefightingRobot:
    def __init__(self):
        self.position = 'a'
        self.path = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j']

    def move_to(self, room):
        self.position = room
        print(f"\nRobot moved to Room {room.upper()}")

    def check_fire(self, environment, room):
        if environment.rooms[room] == "fire":
            print(f"Fire detected in Room {room.upper()}! Extinguishing fire...")
            environment.extinguish_fire(room)
        else:
            print(f"Room {room.upper()} is safe.")

class BuildingEnvironment:
    def __init__(self):
        # 3x3 Grid Representation
        self.rooms = {
            'a': " ", 'b': " ", 'c': "fire",
            'd': " ", 'e': "fire", 'f': " ",
            'g': " ", 'h': " ", 'j': "fire"
        }

    def display_environment(self):
        print("\nBuilding Environment:")
        print(f" {self.rooms['a']} | {self.rooms['b']} | {self.rooms['c']} ")
        print("---+---+---")
        print(f" {self.rooms['d']} | {self.rooms['e']} | {self.rooms['f']} ")
        print("---+---+---")
        print(f" {self.rooms['g']} | {self.rooms['h']} | {self.rooms['j']} ")

    def extinguish_fire(self, room):
        self.rooms[room] = " "
        print(f"Fire in Room {room.upper()} has been extinguished!")

def run_firefighting_robot(robot, environment):
    print("\n------ Firefighting Robot Activated ------")
    environment.display_environment()

    for room in robot.path:
        robot.move_to(room)
        robot.check_fire(environment, room)
        environment.display_environment()

    print("\nAll fires have been extinguished. Final building status:")
    environment.display_environment()
    print("\nFirefighting mission completed successfully! ")


fire_robot = FirefightingRobot()
building_environment = BuildingEnvironment()
run_firefighting_robot(fire_robot, building_environment)
