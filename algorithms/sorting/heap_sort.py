from config.constants import *
import pygame
from .base import Base

class HeapSort(Base):

    def __init__(self, win):
        super().__init__(win)

    def draw_array(self):
        pass

    def run_visualization(self):
        
        for i in range(self.n // 2 - 1, - 1, -1):
            self.heapify(i)

        for i in range(self.n - 1, 0, -1):
            self.array[0], self.array[i] = self.array[i], self.array[0]
            self.heapify(i, 0)

    def heapify(self, n: int, i: int):
        
        largest = i
        l, r = 2 * i + 1, 2 * i + 2

        if l < n and self.array[l] > self.array[largest]:
            largest = l

        if r < n and self.array[r] > self.array[largest]:
            largest = r

        if largest != i:
            self.array[i], self.array[largest] = self.array[largest], self.array[i]
            self.heapify(n, largest)