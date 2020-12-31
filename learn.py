from asciimatics.screen import Screen
from asciimatics.screen import ManagedScreen
from environment import Env
import numpy as np
import time
import os
import random

def train():
    with ManagedScreen() as screen:
        TOTAL_WIDTH = 43
        TOTAL_HEIGHT = 21

        epoch_pos_x = random.randint(0, int(screen.dimensions[1]* 0.80))
        epoch_pos_y = random.randint(0, screen.dimensions[0])

        env = Env(random.randint(0, TOTAL_WIDTH - 1), random.randint(0, TOTAL_HEIGHT - 1), random.randint(0, TOTAL_WIDTH), random.randint(0, TOTAL_HEIGHT - 1), TOTAL_WIDTH, TOTAL_HEIGHT)

        qtable = np.random.rand(env.stateCount, env.actionCount).tolist()

        epochs = 50
        gamma = 0.1
        epsilon = 0.08
        decay = 0.1

        for epoch in range(epochs):
            state, reward, done = env.reset()
            steps = 0

            while not done:
                screen.clear_buffer(Screen.COLOUR_RED, Screen.COLOUR_GREEN, Screen.COLOUR_BLACK)
                vals = env.fetch_env()
                for i in range(vals['height']):
                    ev = screen.get_key()
                    if ev == chr(27) or ev in (ord('Q'), ord('q')):
                        return -1

                    for j in range(vals['width']):
                        if vals['original_pos_y'] == i and vals['original_pos_x'] == j:
                            screen.print_at('S', j*3, i*2)
                        elif vals['pos_y'] == i and vals['pos_x'] == j:
                            screen.print_at('O', j*3, i*2)
                        elif vals['end_y'] == i and vals['end_x'] == j:
                            screen.print_at('T', j*3, i*2)
                        else:
                            screen.print_at(' ', j*3, i*2)

                screen.print_at(f"epoch #{epoch+1}/{epochs}", epoch_pos_x, epoch_pos_y, Screen.COLOUR_BLUE, Screen.A_NORMAL)
                screen.refresh()
                time.sleep(0.01)

                steps += 1

                if np.random.uniform() < epsilon:
                    action = env.randomAction()
                else:
                    action = qtable[state].index(max(qtable[state]))

                next_state, reward, done = env.step(action)

                qtable[state][action] = reward + gamma * max(qtable[next_state])

                state = next_state

            epsilon -= decay*epsilon

while True:
    if train() == -1:
        break

print("Exited")
