import numpy as np

class Env:
    def __init__(self, pos_x, pos_y, end_x, end_y, total_width, total_height):
        self.original_pos_x = pos_x
        self.original_pos_y = pos_y
        self.height = total_height
        self.width = total_width
        self.posX = self.original_pos_x
        self.posY = self.original_pos_y
        self.endX = end_x
        self.endY = end_y
        self.actions = [0, 1, 2, 3]
        self.stateCount = self.height*self.width
        self.actionCount = len(self.actions)

    def reset(self):
        self.posX = self.original_pos_x
        self.posY = self.original_pos_y
        self.done = False
        return 0, 0, False

    def step(self, action):
        if action == 0: # left
            self.posX = self.posX-1 if self.posX > 0 else self.posX
        if action == 1: # right
            self.posX = self.posX+1 if self.posX < self.width - 1 else self.posX
        if action == 2: # up
            self.posY = self.posY-1 if self.posY > 0 else self.posY
        if action == 3: # down
            self.posY = self.posY+1 if self.posY < self.height - 1 else self.posY

        done = self.posX == self.endX and self.posY == self.endY
        nextState = self.width * self.posY + self.posX
        reward = 1 if done else 0
        return nextState, reward, done

    def randomAction(self):
        return np.random.choice(self.actions)

    def fetch_env(self):
        ret_val = {
            "height": self.height,
            "width": self.width,
            "original_pos_y": self.original_pos_y,
            "original_pos_x": self.original_pos_x,
            "pos_y": self.posY,
            "pos_x": self.posX,
            "end_y": self.endY,
            "end_x": self.endX

        }
        return ret_val

    def render(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.original_pos_y == i and self.original_pos_x == j:
                    print(" S", end='')
                elif self.posY == i and self.posX == j:
                    print(" O", end='')
                elif self.endY == i and self.endX == j:
                    print(" T", end='')
                else:
                    print("  ", end='')
            print("\n")
