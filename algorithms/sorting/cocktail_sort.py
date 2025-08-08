from typing import List, Any

from algorithms.core.base_algorithm import BaseAlgorithm

class CocktailSort(BaseAlgorithm):

    def __init__(self, name, data):
        super().__init__(name, data)
        self.initialize()

    def initialize(self):
        self.start = 0
        self.end = len(self.data) - 1
        self.swapped = True

    def step(self) -> bool:

        print(self.start, self.end)

        if self.swapped:

            self.swapped = False
            if self.start < self.end - 1:
                if self.data[self.start] > self.data[self.start + 1]:
                    self.data[self.start], self.data[self.start + 1] = self.data[self.start + 1], self.data[self.start]
                    self.swapped = True

            print(self.swapped)
            if not self.swapped:
                self.finished = True
                return False

            self.swapped = False
            self.end -= 1

            if self.end - 1 > self.start - 1:
                if self.data[self.end - 1] > self.data[self.end]:
                    self.data[self.end - 1], self.data[self.end] = self.data[self.end - 1], self.data[self.end]
                    self.swapped = True

            self.start += 1
            self.swapped = True
            return True
        else:
            self.finished = True
            return False

    def get_visual_state(self) -> List[Any]:
        return self.data


#    def run_visualization(self):
#
#        start, end = 0, self.n - 1
#        swapped = True
#
#        while swapped:

#            swapped = False

#            for i in range(start, end):

#                if self.firstGreaterThanSecond(i, i + 1):
#                    self.swap(i, i + 1)
#                    swapped = True
#                self.draw_array(self.array, highlight=(i, start, end))
#                pygame.time.delay(DEFAULT_DELAY)

#            if not swapped:
#                break

#            swapped = False
#            end -= 1

#            for i in range(end - 1, start - 1, -1):
#                if self.firstGreaterThanSecond(i, i + 1):
#                    self.swap(i, i + 1)
#                    swapped = True
#                self.draw_array(self.array, highlight=(i, start, end))
#                pygame.time.delay(DEFAULT_DELAY)

#            start += 1

#            for event in pygame.event.get():
#                if event.type == pygame.QUIT:
#                    return