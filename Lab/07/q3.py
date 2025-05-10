import random

GRID_SIZE = 10
SHIP_SIZES = [3, 2]  #ships: One of size 3, one of size 2

def create_grid():
    return [['~' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

def place_ships():
    grid = create_grid()
    ships = []
    for size in SHIP_SIZES:
        placed = False
        while not placed:
            x = random.randint(0, GRID_SIZE - 1)
            y = random.randint(0, GRID_SIZE - 1)
            direction = random.choice(['H', 'V'])

            if direction == 'H' and y + size <= GRID_SIZE:
                if all(grid[x][y+i] == '~' for i in range(size)):
                    for i in range(size):
                        grid[x][y+i] = 'S'
                    ships.append([(x, y+i) for i in range(size)])
                    placed = True
            elif direction == 'V' and x + size <= GRID_SIZE:
                if all(grid[x+i][y] == '~' for i in range(size)):
                    for i in range(size):
                        grid[x+i][y] = 'S'
                    ships.append([(x+i, y) for i in range(size)])
                    placed = True
    return grid, ships

def parse_input(coord):
    row = ord(coord[0].upper()) - ord('A')
    col = int(coord[1:]) - 1
    return row, col

def is_valid_move(grid, x, y):
    return 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE and grid[x][y] not in ['H', 'M']

def attack(grid, ships, x, y):
    for ship in ships:
        if (x, y) in ship:
            grid[x][y] = 'H'
            ship.remove((x, y))
            if not ship:
                ships.remove(ship)
                return "Sunk"
            return "Hit"
    grid[x][y] = 'M'
    return "Miss"

def display_public(grid):
    print("  " + " ".join([str(i+1).rjust(2) for i in range(GRID_SIZE)]))
    for i, row in enumerate(grid):
        print(chr(ord('A') + i), " ".join(['~' if cell == 'S' else cell for cell in row]))

def ai_guess_strategy(last_hits, tried):
    if last_hits:
        last_x, last_y = last_hits[-1]
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = last_x + dx, last_y + dy
            if (nx, ny) not in tried and 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
                return nx, ny
    # Otherwise random guess
    while True:
        x, y = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
        if (x, y) not in tried:
            return x, y

# Setup
player_grid, player_ships = place_ships()
ai_grid, ai_ships = place_ships()
player_view = create_grid()
ai_view = create_grid()
ai_hits = []
ai_tried = set()

# Game Loop
while player_ships and ai_ships:
    # Player Turn
    display_public(player_view)
    coord = input("Enter your attack (e.g., B4): ")
    try:
        x, y = parse_input(coord)
        if not is_valid_move(ai_view, x, y):
            print("Invalid or already tried. Try again.")
            continue
        result = attack(ai_grid, ai_ships, x, y)
        ai_view[x][y] = 'H' if result != "Miss" else 'M'
        print(f"Player attacks: {coord.upper()} → {result}!")
    except:
        print("Invalid input format.")
        continue

    if not ai_ships:
        print("You win!")
        break

    # AI Turn
    ax, ay = ai_guess_strategy(ai_hits, ai_tried)
    ai_tried.add((ax, ay))
    outcome = attack(player_grid, player_ships, ax, ay)
    if outcome in ['Hit', 'Sunk']:
        ai_hits.append((ax, ay))
        if outcome == 'Sunk':
            ai_hits.clear()
    print(f"AI attacks: {chr(ax + ord('A'))}{ay + 1} → {outcome}!")

    if not player_ships:
        print("AI wins!")
        break
