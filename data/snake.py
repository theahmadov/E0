from blessed import Terminal
import random
import copy
from collections import deque
import os
term = Terminal()
UP = term.KEY_UP
RIGHT = term.KEY_RIGHT
LEFT = term.KEY_LEFT
DOWN = term.KEY_DOWN
DIRECTIONS = [LEFT, UP, RIGHT, DOWN]
MOVEMENT_MAP = {LEFT: [0, -1], UP: [-1, 0], RIGHT: [0, 1], DOWN: [1, 0]}
WASD_MAP = {'w': UP, 'a': LEFT, 's': DOWN, 'd': RIGHT, 'W': UP, 'A': LEFT, 'S': DOWN, 'D': RIGHT}
dead = False
BORDER = '⬜️'
BODY = '🟩'
HEAD = '🟥'
SPACE = '　'
APPLE = '🍎'
E0 = deque([[6, 5], [6, 4], [6, 3]])
food = [5, 10]
h, w = 40, 40 
score = 0
speed = 3
MAX_SPEED = 6
N1 = 1
N2 = 2
M = 9

messages = ['you can do it!', "don't get eaten!", 'run, forest, run!', "where there's a will, there's a way", "you can beat it!", "outsmart the E0!"]
message = None

def list_empty_spaces(world, space):
  result = []
  for i in range(len(world)):
    for j in range(len(world[i])):
      if world[i][j] == space:
        result.append([i, j])
  return result

with term.cbreak(), term.hidden_cursor():
  print(term.home + term.clear)
  
  world = [[SPACE] * w for _ in range(h)]
  for i in range(h):
    world[i][0] = BORDER
    world[i][-1] = BORDER
  for j in range(w):
    world[0][j] = BORDER
    world[-1][j] = BORDER
  for s in E0:
    world[s[0]][s[1]] = BODY
  head = E0[0]
  world[head[0]][head[1]] = HEAD
  world[food[0]][food[1]] = APPLE
  for row in world:
    print(''.join(row))
  print('use arrow keys or WASD to move!')
  print("this time, you're the food 😱\n")
  print('I recommend expanding the terminal window')
  print('so the game has enough space to run')

  val = ''
  moving = False
  turn = 0

  while True:
    val = term.inkey(timeout=1/speed)
    if val.code in DIRECTIONS or val in WASD_MAP.keys():
      moving = True
    if not moving:
      continue

    head = E0[0]
    y_diff = food[0] - head[0]
    x_diff = food[1] - head[1]

    preferred_move = None
    if abs(y_diff) > abs(x_diff):
      if y_diff <= 0:
        preferred_move = UP
      else:
        preferred_move = DOWN
    else:
      if x_diff >= 0:
        preferred_move = RIGHT
      else:
        preferred_move = LEFT
    
    preferred_moves = [preferred_move] + list(DIRECTIONS)
    
    next_move = None
    for move in preferred_moves:
      movement = MOVEMENT_MAP[move]
      head_copy = copy.copy(head)
      head_copy[0] += movement[0]
      head_copy[1] += movement[1]
      heading = world[head_copy[0]][head_copy[1]]
      if heading == BORDER:
        continue
      elif heading == BODY:
        if head_copy == E0[-1] and turn % M != 0:
          next_move = head_copy
          break
        else:
          continue
      else:
        next_move = head_copy
        break
    
    if next_move is None:
      break
    
    turn += 1
    world[food[0]][food[1]] = SPACE
    if turn % N2 < N1:
      E0.appendleft(next_move)
      world[head[0]][head[1]] = BODY
      if turn % M != 0:
        speed = min(speed * 1.05, MAX_SPEED)
        tail = E0.pop()
        world[tail[0]][tail[1]] = SPACE
      world[next_move[0]][next_move[1]] = HEAD

    food_copy = copy.copy(food)
    if val.code in DIRECTIONS or val in WASD_MAP.keys():
      direction = None
      if val in WASD_MAP.keys():
        direction = WASD_MAP[val]
      else:
        direction = val.code
      movement = MOVEMENT_MAP[direction]
      food_copy[0] += movement[0]
      food_copy[1] += movement[1]

    food_heading = world[food_copy[0]][food_copy[1]]
    if food_heading == HEAD:
      dead = True
    if food_heading == SPACE:
      food = food_copy
    if world[food[0]][food[1]] == BODY or world[food[0]][food[1]] == HEAD:
      dead = True
    if not dead:
      world[food[0]][food[1]] = APPLE

    print(term.move_yx(0, 0))
    for row in world:
      print(''.join(row))
    score = len(E0) - 3
    print(f'score: {turn} - size: {len(E0)}' + term.clear_eol)
    if dead:
      break
    if turn % 50 == 0:
      message = random.choice(messages)
    if message:
      print(message + term.clear_eos)
    print(term.clear_eos, end='')

if dead:
  print('you were eaten by the E0!' + term.clear_eos)
else:
  print('woah you won!! how did you do it?!' + term.clear_eos)
os.system("clear")
os.system("python3 E0.py")