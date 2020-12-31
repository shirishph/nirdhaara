from environment import Env
import numpy as np
import time
import os
import random

def train():
        TOTAL_WIDTH = 43
        TOTAL_HEIGHT = 21

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
                os.system('clear')
                env.render()
                time.sleep(0.25)

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
