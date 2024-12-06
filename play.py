from pyxel import init, btnp, btn, KEY_0, quit, rect, run, KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT
from sprites.Spaceship import Spaceship


class PlayGame:
    def __init__(self):
        init(600,600)
        self.player = Spaceship()
        run(self.update, self.draw)

    # handles controls - should be in Spaceship class
    def update(self):
        if btn(KEY_DOWN):
            self.player.position[1] += 5
        if btn(KEY_UP):
            self.player.position[1] -= 5
        if btn(KEY_LEFT):
            self.player.position[0] -= 5
        if btn(KEY_RIGHT):
            self.player.position[0] += 5

        if btnp(KEY_0):
            quit()

    def draw(self):
        rect(50, 50, 510, 510, 1) #draws screen


        # convert to triangular box
        # NOTE: Do we use triangular or rectangular hitbox?
        rect(self.player.position[0], self.player.position[1], 10, 10, 3)
    

PlayGame()






