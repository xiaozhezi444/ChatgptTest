import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint


# Initialize the screen
stdscr = curses.initscr()
curses.curs_set(0)  # hide the cursor
height, width = stdscr.getmaxyx()
window = curses.newwin(height, width, 0, 0)
window.keypad(True)
window.timeout(100)

# Initial snake position and food
snake = [
    [height // 2, width // 4],
    [height // 2, width // 4 - 1],
    [height // 2, width // 4 - 2],
]
food = [height // 2, width // 2]
window.addch(food[0], food[1], "*")

key = KEY_RIGHT
score = 0

try:
    while True:
        next_key = window.getch()
        key = key if next_key == -1 else next_key

        if key in [KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN]:
            # Calculate new head position
            head = snake[0].copy()
            if key == KEY_RIGHT:
                head[1] += 1
            elif key == KEY_LEFT:
                head[1] -= 1
            elif key == KEY_UP:
                head[0] -= 1
            elif key == KEY_DOWN:
                head[0] += 1
            snake.insert(0, head)

            # Check for collision with boundaries
            if (
                head[0] in [0, height]
                or head[1] in [0, width]
                or head in snake[1:]
            ):
                break

            if head == food:
                score += 1
                food = None
                while food is None:
                    nf = [randint(1, height - 2), randint(1, width - 2)]
                    if nf not in snake:
                        food = nf
                window.addch(food[0], food[1], "*")
            else:
                tail = snake.pop()
                window.addch(tail[0], tail[1], " ")

            window.addch(head[0], head[1], "#")
        elif key == ord("q"):
            break
finally:
    curses.endwin()
    print("Final score: {}".format(score))
