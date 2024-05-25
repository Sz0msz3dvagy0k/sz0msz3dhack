with open('./input.txt', 'r') as f:
  input = f.read()

print(input)

def find_path(maze, start, goal):
  """
  Funkció, amely megtalálja a legrövidebb utat a starttól a célig egy 2D útvesztőben.

  Args:
    maze: A 2D útvesztő rácsot ábrázoló karakteres mátrix.
    start: A startpozíciót jelölő tuple (x, y).
    goal: A célpozíciót jelölő tuple (x, y).

  Returns:
    A legrövidebb út listája mozgásirányokban ("U", "D", "L", "R") jelölve,
    beleértve a startot és a célt.
    Vagy None, ha nincs megoldás.
  """

  directions = {
    "U": (0, -1),
    "D": (0, 1),
    "L": (-1, 0),
    "R": (1, 0)
  }

  open_set = {start}
  came_from = {}
  current = None

  while open_set:
    if not open_set:  # Check if open_set is empty
      return None  # No solution found
    current = min(open_set, key=lambda node: len(came_from.get(node, [])))

    for direction, delta in directions.items():
      new_pos = (current[0] + delta[0], current[1] + delta[1])
      if 0 <= new_pos[0] < len(maze[0]) and 0 <= new_pos[1] < len(maze) and maze[new_pos[1]][new_pos[0]] != "#" and new_pos not in came_from:
        open_set.add(new_pos)
        came_from[new_pos] = current

  path = []
  if current:
    while current != start:
      path.append(list(directions.keys())[list(directions.values()).index(came_from[current])])
      current = came_from[current]
  return path

def print_path(path, maze, start):
  """
  Funkció, amely kinyomtatja a legrövidebb utat mozgásirányokban ("U", "D", "L", "R") jelölve,
  és jelöli a rajzon az utat.

  Args:
    path: A legrövidebb út listája mozgásirányokban (vagy None, ha nincs megoldás).
    maze: A 2D útvesztő rácsot ábrázoló karakteres mátrix.
    start: A startpozíciót jelölő tuple (x, y).
  """

  if not path:
    print("Nincs megoldás!")
    return

  for i, direction in enumerate(path):
    x, y = start[0], start[1]
    maze[y][x] = direction  # Jelöli az utat a rajzon

    if direction == "U":
      y -= 1
    elif direction == "D":
      y += 1
    elif direction == "L":
      x -= 1
    elif direction == "R":
      x += 1

    maze[y][x] = "•"  # Jelöli a jelenlegi pozíciót

  for row in maze:
    print("".join(row))

  print("Útvonal:", " ".join(path))

def main():
  """
  Fő funkció, amely beolvassa az útvesztőt, megtalálja a legrövidebb utat, és kinyomtatja.
  """

  with open("input.txt", "r") as f:
    maze = [list(line.strip()) for line in f]

  start = (0, 0)  # Kezdő pozíció megadása
  goal = (len(maze) - 1, len(maze[0]) - 1)  # Cél pozíció megadása

  path = find_path(maze, start, goal)
  print_path(path, maze.copy(), start)

if __name__ == "__main__":
  main()


