# Created by Gaohan Yu

import random


def move(snake, head):
    if head == 1:

        x, y = snake[0]

        snake[0] = [x + 1, y]

    elif head == 2:

        x, y = snake[0]

        snake[0] = [x - 1, y]

    elif head == 3:

        x, y = snake[0]

        snake[0] = [x, y - 1]

    elif head == 4:

        x, y = snake[0]

        snake[0] = [x, y + 1]

    for i in range(len(snake)):

        if i != 0:
            snake[i] = snake[i - 1]

    return snake


# set up map

X_lim = 8

Y_lim = 8

gmap = [[0] * X_lim] * Y_lim

# 0 for N/A, 1 for food

# first do not consider snake will grow


# score

score = 0

# step

step = 0

# heading direction

# 1:up 2:down 3:left 4:right

hdrc = 1

# Snake position

snake = [[3, 0]]

snake_path = []

# random generate a food and not on snake!!!

food = [3, 7]
# food = [random.randint(0, X_lim - 1), random.randint(0, Y_lim - 1)]

# while food in snake:
    # food = [random.randint(0, X_lim - 1), random.randint(0, Y_lim - 1)]

# food = [3,2]


while score <= 0:

    length = len(snake)

    snake0 = snake.copy()

    snake0 = move(snake0, hdrc)  # fake snake to try if everything ok

    ok = 0

    # meet barriers?

    # print(step,hdrc)

    # print('snake:',snake)

    x0, y0 = snake0[0]

    if 0 <= x0 < X_lim and 0 <= y0 < Y_lim:

        snake = snake0.copy()

        step += 1

        # print(step,hdrc)

        # print('snake:',snake)

        snake_path.append(snake[0])

        # print('food:',food)

    # if next step will out of map, then find a new head direction
    else:

        hdrc0 = hdrc

        while hdrc0 == hdrc:
            hdrc0 = random.randint(1, 4)

        hdrc = hdrc0

    # if snake is run with the wall, we need give it a chance to go back into the map

    if snake[0][0] == 0 or snake[0][1] == 0 or snake[0][0] == X_lim - 1 or snake[0][0] == Y_lim - 1:
        hdrc = random.randint(1, 4)

    # need to think if snake meets death.

    # meet food?

    if snake[0] == food:
        score += 1

        # random generate a food and not on snake!!!

        # food = [random.randint(0,X_lim-1),random.randint(0,Y_lim-1)]

        # while food in snake:

        #    food = [random.randint(0,X_lim-1),random.randint(0,Y_lim-1)]

print('final:', step, score)

# change file name per each scenario for different data sets
f = open('SnakeGameData_Distance7.txt', 'a')
f.write(str(step) + '\n')
f.close()

# print(snake_path)