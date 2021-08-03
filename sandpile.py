from matrix import *
import os, time, random
from txt_to_image import convert as to_image


class sandpile:
    def __init__(self, row, col, value=0, pattern=None):
        if type(value) == matrix:
            self.mat = value
        else:
            self.mat = build(row, col, value)
        self.has_pattern = False
        if pattern is not None:
            self.pattern = pattern
            self.has_pattern = True
            self.pattern_mat = build(row, col)
            self.pattern_mat.fillin([pattern[x] for x in self.mat.element()])

    def add(self, row, col, value=1):
        self.mat[row, col] += value

    def pick(self, row, col, value=1):
        self.mat[row, col] -= value

    def transfer(self, show_each_step=False, time_interval=0.1, interval=1):
        mat = self.mat
        rown, coln = mat.dim()
        while any(x > 3 for x in mat.element()):
            for i in range(rown):
                for j in range(coln):
                    if mat[i, j] > 3:
                        mat[i, j] -= 4
                        if i > 0:
                            mat[i - 1, j] += 1
                        if i < rown - 1:
                            mat[i + 1, j] += 1
                        if j > 0:
                            mat[i, j - 1] += 1
                        if j < coln - 1:
                            mat[i, j + 1] += 1
                        if show_each_step:
                            if self.has_pattern:
                                self.pattern_mat.fillin([
                                    self.pattern[x]
                                    for x in self.mat.element()
                                ])
                            self.show(interval)
                            time.sleep(time_interval)
                            os.system('cls')
        if show_each_step:
            self.show(interval)
            input('finished')
        if self.has_pattern:
            self.pattern_mat.fillin(
                [self.pattern[x] for x in self.mat.element()])

    def __repr__(self):
        if self.has_pattern:
            return self.pattern_mat.__repr__()
        return self.mat.__repr__()

    def show(self, interval=2):
        if self.has_pattern:
            self.pattern_mat.show(interval)
        else:
            self.mat.show(interval)

    def show_get(self, interval=2):
        if self.has_pattern:
            return self.pattern_mat.show(interval=interval, get=True)
        else:
            return self.mat.show(interval=interval, get=True)
