import sys
import os

sys.path.append('scripts')
import pyglet
import random
from sandpile import sandpile

screen_size = 500, 500
block_size = 10
window = pyglet.window.Window(*screen_size)
rows = screen_size[1] // block_size
cols = screen_size[0] // block_size
a = sandpile(rows, cols, 0)
abs_path = os.getcwd()
pyglet.resource.path = [abs_path + '/resources']
pyglet.resource.reindex()
block0 = pyglet.resource.image('0.png')
block0.height = block_size
block0.width = block_size
block1 = pyglet.resource.image('1.png')
block1.height = block_size
block1.width = block_size
block2 = pyglet.resource.image('2.png')
block2.height = block_size
block2.width = block_size
block3 = pyglet.resource.image('3.png')
block3.height = block_size
block3.width = block_size
block_ls = [block0, block1, block2, block3]
whole_blocks = [[[
    pyglet.sprite.Sprite(each, x=j * block_size, y=i * block_size)
    for each in block_ls
] for j in range(cols)] for i in range(rows)]
batch = pyglet.graphics.Batch()
center = rows // 2 - 1


def sandpile_read():
    for i in range(rows):
        for j in range(cols):
            current = a.mat[i][j]
            whole_blocks[rows - 1 - i][j][current].batch = batch
            for k in range(4):
                if k != current:
                    whole_blocks[rows - 1 - i][j][k].batch = None


@window.event
def on_draw():
    window.clear()
    a.add(center, center)
    #a.add(random.randint(0, rows-1), random.randint(0, cols-1))
    a.transfer()
    sandpile_read()
    batch.draw()


def update(dt):
    pass


pyglet.clock.schedule_interval(update, 0.001)
pyglet.app.run()
