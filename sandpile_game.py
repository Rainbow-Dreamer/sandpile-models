from matrix import *
import os, time, random, keyboard
from txt_to_image import convert as to_image
from sandpile import sandpile
size = [35, 35]
init_value = 0
num_pattern = {0: ' ', 1: '.', 2: '+', 3: '@'}
a = sandpile(*size, init_value, pattern=num_pattern)
#counter = 0
ind = [0, 0]
a.pattern_mat[ind] = a.mat[ind]
while True:
    a.show(1)
    print(f'you are currently at row {ind[0]+1}, column {ind[1]+1}')
    if keyboard.is_pressed('a'):
        if ind[1] > 0:
            a.pattern_mat[ind] = a.pattern[a.mat[ind]]
            ind[1] -= 1
            a.pattern_mat[ind] = a.mat[ind]
    if keyboard.is_pressed('d'):
        if ind[1] < size[1] - 1:
            a.pattern_mat[ind] = a.pattern[a.mat[ind]]
            ind[1] += 1
            a.pattern_mat[ind] = a.mat[ind]
    if keyboard.is_pressed('w'):
        if ind[0] > 0:
            a.pattern_mat[ind] = a.pattern[a.mat[ind]]
            ind[0] -= 1
            a.pattern_mat[ind] = a.mat[ind]
    if keyboard.is_pressed('s'):
        if ind[0] < size[0] - 1:
            a.pattern_mat[ind] = a.pattern[a.mat[ind]]
            ind[0] += 1
            a.pattern_mat[ind] = a.mat[ind]
    if keyboard.is_pressed('j'):
        a.add(*ind)
        a.transfer()
        a.pattern_mat[ind] = a.mat[ind]
    if keyboard.is_pressed('k'):
        if a.mat[ind] > 0:
            a.pick(*ind)
        a.transfer()
        a.pattern_mat[ind] = a.mat[ind]
    if keyboard.is_pressed('c'):
        a.mat.clear()
        a.transfer()
        a.pattern_mat[ind] = a.mat[ind]
    #time.sleep(0.02)
    os.system('cls')
    #counter += 1
#a.transfer(show_each_step = True, time_interval = 1)
