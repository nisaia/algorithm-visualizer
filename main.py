import pygame
import sys
from config.constants import *

from algorithms.sorting.bubble_sort import BubbleSort
from algorithms.sorting.cocktail_sort import CocktailSort
from algorithms.sorting.selection_sort import SelectionSort
from algorithms.sorting.insertion_sort import InsertionSort

ALGORITHMS = {
    "Sorting": {
        "Bubble sort": BubbleSort,
        "Cocktail sort": CocktailSort,
        "Heap sort": 3,
        "Insertion sort": InsertionSort,
        "Merge sort": 5,
        "Quick sort": 6,
        "Selection sort": SelectionSort,
        "Shell sort": 8
    },
    "Searching": {
        "Binary search": 1,
        "Interpolation search": 2,
        "Jump search": 3,
        "Linear search": 4
    }
}

def draw_menu(win, font, options, selected_index, title=""):
    win.fill(DARK_GRAY)
    if title:
        title_text = font.render(title, True, WHITE)
        win.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 50))

    for i, name in enumerate(options):
        color = BLUE if i == selected_index else GRAY
        text = font.render(name, True, color)
        win.blit(text, (WIDTH // 2 - text.get_width() // 2, 150 + i * 60))

    pygame.display.update()

def main():

    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Algorithms visualizer")
    font = pygame.font.SysFont("Arial", FONT_SIZE)

    state = CATEGORY_STATE
    selected_index = 0

    category_names = list(ALGORITHMS.keys())
    current_category = category_names[0]
    
    while True:

        if state == CATEGORY_STATE:
            draw_menu(win, font, category_names, selected_index, "Choose an algorithm category")
        elif state == ALGORITHM_STATE:
            algorithms = list(ALGORITHMS[current_category].keys()) + ["← Indietro"]
            draw_menu(win, font, algorithms, selected_index, f"Current algorithm category: {current_category}")

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_DOWN: selected_index += 1
                elif event.key == pygame.K_UP: selected_index -= 1
                elif event.key == pygame.K_RETURN:

                    if state == CATEGORY_STATE:
                        
                        current_category = category_names[selected_index % len(category_names)]
                        selected_index = 0
                        state = ALGORITHM_STATE
                    
                    elif state == ALGORITHM_STATE:
                        
                        algorithms = list(ALGORITHMS[current_category].keys()) + ["← Indietro"]
                        choice = algorithms[selected_index % len(algorithms)]
                        if choice == "← Indietro":
                            state = CATEGORY_STATE
                            selected_index = 0
                        else:
                            sorting_algorithm = ALGORITHMS[current_category][choice](win)
                            sorting_algorithm.run_visualization()
                            pygame.time.delay(500)

                selected_index %= len(category_names) if state == "category" else len(ALGORITHMS[current_category]) + 1

if __name__ == '__main__':
    main()