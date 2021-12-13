import pygame

pygame.init()
import classes
import random

white = (255, 255, 255)
green = (71, 120, 62)
bright_green = (0, 255, 0)
maroon = (128, 0, 0)
navy = (65, 67, 118)
orange = (255, 165, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
purple = (128, 0, 128)
grey = (128, 128, 128)
black = (0, 0, 0)
sky_blue = (0, 193, 247)
teal = (55, 103, 123)
pink = (255, 145, 164)
clock = pygame.time.Clock()
WIDTH = 1280
HEIGHT = 720
large_font = "Impact"
small_font = "arial"
sortButton = classes.Button(WIDTH / 2, 50, large_font, 70, black, white, "Sort!", 200, 75)
number_slider = classes.Slider(400, 10, 200, 4, random.randint(4, 75), white, 500, 20)
esc = classes.Text(10,10,small_font,100,100,black,"Press ESC to go back",30)
clock = pygame.time.Clock()


def main_screen():
    window = classes.Window(WIDTH, HEIGHT, "Sorting Algorithm Visualiser", None, None, teal)
    display = window.create_window()
    num_bars = int(number_slider.get_value())
    array = generate_array(num_bars)
    run_main = True
    BubbleSort = classes.Button(175, HEIGHT / 8, large_font, 60, black, sky_blue, "Bubble Sort", 300, 100)
    CocktailSort = classes.Button(500, HEIGHT / 8, large_font, 57, black, pink, "Cocktail Sort", 300, 100)
    InsertionSort = classes.Button(825, HEIGHT / 8, large_font, 53, black, red, "Insertion Sort", 300, 100)
    SelectionSort = classes.Button(175, HEIGHT / 3, large_font, 50, black, green, "Selection Sort", 300, 100)
    MergeSort = classes.Button(500, HEIGHT / 3, large_font, 65, black, yellow, "Merge Sort", 300, 100)
    QuickSort = classes.Button(825, HEIGHT / 3, large_font, 65, black, orange, "Quick Sort", 300, 100)
    buttons = {BubbleSort: "bubble_sort", CocktailSort: "cocktail_sort", InsertionSort: "insertion_sort",
               SelectionSort: "selection_sort", MergeSort: "merge_sort", QuickSort: "quick_sort"}
    number_text = classes.Text(1050,HEIGHT/7,large_font,100,100,white,str(int(number_slider.get_value())),90)
    while run_main:
        window.update_window(teal)
        number_text.draw(display)
        number_slider.draw(display)
        for button in buttons:
            button.draw(display)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if number_slider.isClicked(pygame.mouse.get_pos()):
                number_slider.update(pygame.mouse.get_pos()[0])
                num_bars = int(number_slider.get_value())
                if num_bars == 0:
                    num_bars = 2
                array = generate_array(num_bars)
                number_text.update_text(str(int(number_slider.get_value())))
                number_slider.deactivate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in list(buttons.keys()):
                    if button.isClicked(pygame.mouse.get_pos()):
                        eval(buttons.get(button) + "({})".format(array))
        create_bars(array, display, red)
        pygame.time.delay(  10 )
        pygame.display.update()


def bubble_sort(array):
    window = classes.Window(WIDTH, HEIGHT, "Bubble Sort", None, None, teal)
    display = window.create_window()
    swapped = True
    sorting = False
    run = True
    num_bars = len(array)
    while run:
        window.update_window(teal)
        esc.draw(display)
        if not sorting:
            sortButton.draw(display)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and sorting:
                    random.shuffle(array)
                    bubble_sort(array)
                elif event.key == pygame.K_ESCAPE:
                    main_screen()
        if sortButton.isClicked(pygame.mouse.get_pos()) and swapped:
            sorting = True
            for i in range(0, num_bars - 1):
                if array[i] > array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
                    create_bars(array, display, red)
                    pygame.display.update()
                    window.update_window()
                    swapped = True
                    clock.tick(60)
        if sorted(array) == array and sorting:
            colour = green
            sortButton.deactivate()
        else:
            colour = red
        create_bars(array, display, colour)
        pygame.display.update()


def cocktail_sort(array):
    window = classes.Window(WIDTH, HEIGHT, "Cocktail Sort", None, None, teal)
    display = window.create_window()
    sorting = False
    swapped = True
    run = True
    while run:
        window.update_window(teal)
        if not sorting:
            sortButton.draw(display)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and sorting:
                    random.shuffle(array)
                    sortButton.deactivate()
                    cocktail_sort(array)
                elif event.key == pygame.K_ESCAPE:
                    main_screen()
        if sortButton.isClicked(pygame.mouse.get_pos()):
            sorting = True
            swapped = False
            for n in range(len(array) - 1):
                if array[n] > array[n + 1]:
                    array[n], array[n + 1] = array[n + 1], array[n]
                    swapped = True
            swapped = False
            for i in range(len(array) - 1, 0, -1):
                if array[i] < array[i - 1]:
                    array[i], array[i - 1] = array[i - 1], array[i]
                    swapped = True
        if sorted(array) == array and sorting:
            colour = green
            sortButton.deactivate()
        else:
            colour = red
        create_bars(array, display, colour)
        pygame.time.delay(  10 )
        esc.draw(display)
        pygame.display.update()


def insertion_sort(array):
    window = classes.Window(WIDTH, HEIGHT, "Insertion Sort", None, None, teal)
    display = window.create_window()
    run = True
    sorting = False
    while run:
        window.update_window(teal)
        if not sorting:
            sortButton.draw(display)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and sorting:
                    random.shuffle(array)
                    sortButton.deactivate()
                    insertion_sort(array)
                elif event.key == pygame.K_ESCAPE:
                    main_screen()
        if sortButton.isClicked(pygame.mouse.get_pos()):
            sorting = True
            for n in range(1, len(array)):
                for i in range(n, 0, -1):
                    while array[i - 1] > array[i]:
                        array[i], array[i - 1] = array[i - 1], array[i]
                        window.update_window(teal)
                        pygame.time.delay(10 // len(array))
                        create_bars(array, display, red)
                        pygame.display.update()
        colour = green if sorting else red
        create_bars(array, display, colour)
        esc.draw(display)
        pygame.display.update()


def selection_sort(array):
    window = classes.Window(WIDTH, HEIGHT, "Selection Sort", None, None, teal)
    display = window.create_window()
    run = True
    sorting = False
    while run:
        esc.draw(display)
        window.update_window(teal)
        if not sorting:
            sortButton.draw(display)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and sorting:
                    random.shuffle(array)
                    sortButton.deactivate()
                    selection_sort(array)
                elif event.key == pygame.K_ESCAPE:
                    main_screen()
        if sortButton.isClicked(pygame.mouse.get_pos()) and not sorting:
            sorting = True
            for index in range(len(array) - 1):
                min_index = index
                for j in range(index + 1, len(array)):
                    if array[j] < array[min_index]:
                        min_index = j
                pygame.display.update()
                window.update_window(teal)
                array[index], array[min_index] = array[min_index], array[index]
                create_bars(array, display, red)
                pygame.time.delay(  10 )
        colour = red if not sorting else green
        create_bars(array, display, colour)
        pygame.display.update()


def create_bars(array, display, colour):
    x = 0
    y = 40
    bar_width = (WIDTH) / len(array)
    for number in array:
        bar = pygame.Rect(x, HEIGHT - (number * 2), bar_width, number * 2)
        outline = pygame.Rect(x - 2, (HEIGHT - (number * 2)) - 2, bar_width + 4, (number * 2) + 4)
        pygame.draw.rect(display, black, outline)
        pygame.draw.rect(display, colour, bar, 0, 2)
        x += bar_width


def generate_array(numberOfBars):
    array = []
    for bar in range(numberOfBars):
        array.append(random.randint(30, 200))
    return array


def merge_sort(array):
    window = classes.Window(WIDTH, HEIGHT, "Merge Sort (not working)", None, None, teal)
    display = window.create_window()
    run = True
    sorting = False
    while run:
        window.update_window(teal)
        esc.draw(display)
        if not sorting:
            sortButton.draw(display)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and sorting:
                    random.shuffle(array)
                    sortButton.deactivate()
                    merge_sort(array)
                elif event.key == pygame.K_ESCAPE:
                    main_screen()
            if sortButton.isClicked(pygame.mouse.get_pos()) and not sorting:
                sorting = True

                def merge_sort_alg(array):
                    window.update_window(teal)
                    if len(array) <= 1:
                        return

                    mid = len(array) // 2

                    left = array[:mid]
                    right = array[mid:]

                    merge_sort_alg(left)
                    create_bars(array, display, colour)
                    merge_sort_alg(right)
                    create_bars(array, display, colour)
                    window.update_window(teal)
                    merge(left, right, array)
                    create_bars(array, display, colour)
                    pygame.time.delay(  10 )
                    pygame.display.update()

                def merge(left, right, array):
                    len_left = len(left)
                    len_right = len(right)

                    i = j = k = 0

                    while i < len_left and j < len_right:
                        window.update_window(teal)
                        if left[i] <= right[j]:
                            array[k] = left[i]
                            i += 1
                        else:
                            array[k] = right[j]
                            j += 1
                        k += 1
                        create_bars(array,display,red)

                    while i < len_left:
                        array[k] = left[i]
                        i += 1
                        k += 1

                    while j < len_right:
                        array[k] = right[j]
                        j += 1
                        k += 1
                    create_bars(array,display,red)
                    pygame.display.update()
                merge_sort_alg(array)
        colour = red if not sorting else green
        create_bars(array, display, colour)
        pygame.display.update()


def quick_sort(array):
    window = classes.Window(WIDTH, HEIGHT, "Quick Sort", None, None, teal)
    display = window.create_window()
    run = True
    sorting = False
    while run:
        window.update_window(teal)
        esc.draw(display)
        if not sorting:
            sortButton.draw(display)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and sorting:
                    random.shuffle(array)
                    sortButton.deactivate()
                    quick_sort(array)
                elif event.key == pygame.K_ESCAPE:
                    main_screen()
            if sortButton.isClicked(pygame.mouse.get_pos()) and not sorting:
                sorting = True

                def quick_sort_alg(array, left_idx, right_idx):
                    if left_idx < right_idx:
                        window.update_window(teal)
                        pivot_idx = partition(array, left_idx, right_idx)
                        quick_sort_alg(array, left_idx, pivot_idx - 1)
                        create_bars(array, display, red)
                        quick_sort_alg(array, pivot_idx + 1, right_idx)
                        create_bars(array, display, red)
                        clock.tick(60)
                        pygame.display.update()

                def partition(array, left_idx, right_idx):
                    i = left_idx
                    j = right_idx - 1
                    pivot = array[right_idx]
                    while i < j:
                        while i < right_idx and array[i] < pivot:
                            i += 1
                        while j > left_idx and array[j] >= pivot:
                            j -= 1
                        if i < j:
                            array[i], array[j] = array[j], array[i]
                            create_bars(array, display, red)
                    if array[i] > pivot:
                        array[i], array[right_idx] = array[right_idx], array[i]
                    create_bars(array, display, red)
                    pygame.display.update()
                    return i

                quick_sort_alg(array, 0, len(array) - 1)
        colour = red if not sorting else green
        create_bars(array, display, colour)
        pygame.display.update()


if __name__ == '__main__':
    main_screen()
