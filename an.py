import curses
import random

s = curses.initscr()
curses.curs_set(0)
sh, sw = s.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)

snk_x = sw/4
snk_y = sh/2
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
]

food = [sh/2, sw/2]
w.addch(food[0], food[1], curses.ACS_PI)

key = curses.KEY_RIGHT

while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key

    if snake[0][0] in [0, sh] or snake[0][1] in [0, sw] or snake[0] in snake[1:]:
        curses.endwin()
        quit()

    new_head = [snake[0][0], snake[0][1]]

    if key == curses.key_down:
        new_head[0] += 1
    if key == curses.key_up:
        new_head[0] -= 1
    if key == curses.key_left:
        new_head[1] -= 1
    if key == curses.key_right:
        new_head[1] += 1

    snake.insert(0, new_head)

    if snake[0] == food:
        food = none
        while food is none:
            nf = [
                random.randit(1, sh-1),
                random.randit(1, sw-1)
            ]
            food = nf if nf not in snake else none
        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        w.addch(tail[0], fail[1], '  ')

    w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
