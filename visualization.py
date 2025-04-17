import random, time
import sys
import pygame
import pygame_gui

from sorting_algorithm import *
from buttonClass import *

# Initialize pygame
pygame.init()

# Screen dimensions
width, height = 1000, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Algorithm Execution Time Visualization")

# Font
font = pygame.font.SysFont('Arial', 24)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (150, 150, 150)

# Fonts
font = pygame.font.SysFont('Arial', 24)

# Managing
FPS = 60
CLOCK = pygame.time.Clock()
MANAGER = pygame_gui.UIManager((width, height))

# Global and Constants
input_rect = pygame.Rect((100, 285), (800, 40))
capacity = 20000
sys.setrecursionlimit(capacity)
USER_INPUT = []
ALGORITHMS = []

# A Flag designed for Return Button
screen_check = False

# Functions in main
#=========================================================================================

# Functions related to getting user input 
def list_to_str(list):
    text = "" + str(list[0])
    for i in range(1, len(list)):
        text += ", "
        text += str(list[i])
    return text

def show_list(list, x, y):
    text = list_to_str(list)
    lfont = pygame.font.SysFont('Arial', 14)
    show_text = lfont.render(text, True, BLACK)    
    screen.blit(show_text, (x, y))
    
    
    
    
# Functions related to Analysis and Visualization
#==========================================================================
def time_analysis_sort(func, arr):
    start_time = time.time()
    func(arr)
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time

def time_analysis_quick_sort(func, arr, low, high):
    start_time = time.time()
    func(arr, low, high)
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time

def time_analysis_search(func, arr, target):
    start_time = time.time()
    indices = func(arr, target)
    end_time = time.time()
    execution_time = end_time - start_time
    if not indices:
        print ("Element not found")
    else:
        print(f"Element is found at: {indices}")
    return execution_time
#==========================================================================


#+++++++++++++++++++++++
# VISUALIZATION SCREEN +
#+++++++++++++++++++++++

def draw_analysis(times, algorithms):
    growth_rate = 100
    bar_width = 100
    
    # Number of algorithms
    num_algorithms = len(algorithms)
    max_time = max(times)
    
    # Defind buttons
    start_button = Button(850, 40, 100, 50, "Start", GREEN, GRAY)
    stop_button = Button(850, 100, 100, 50, "Stop", RED, GRAY)
    reset_button = Button(850, 160, 100, 50, "Reset", YELLOW, GRAY)
    return_button = Button(850, 220, 100, 50, "Return", BLUE, GRAY)
    
    # Starting time
    start_time = time.time()
    elapsed_time = 0
    started = False  # Timer not started
    paused = True  # Flag to indicate whether the simulation is paused

    # Calculating the max height
    max_heights = []
    for i in range(num_algorithms):
        bar_height = (times[i] / max_time) * (height - 150)
        max_heights.append(bar_height)
        
        
    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # Check if Start button is clicked
            elif start_button.is_clicked(event):
                started = True  # Timer started
                paused = False  # Ensure growth is active
                start_time = time.time() - elapsed_time  # Adjust start_time to resume from current elapsed_time
                
            # Check if the Stop button is clicked
            elif stop_button.is_clicked(event):
                if paused:
                    # Resume growth
                    start_time = time.time() - elapsed_time  # Adjust start_time to resume from the current elapsed_time
                paused = not paused  # Toggle the paused state
            
            # Check if the Reset button is clicked
            elif reset_button.is_clicked(event):
                paused = True  # Stop growth
                started = False  # Reset the start state
                elapsed_time = 0  # Reset elapsed time
                start_time = time.time()  # Reset the start time
                
            # Check if return Button is clicked   
            elif return_button.is_clicked(event):
                if screen_check:
                    getting_algorithms()
                else:
                    generate()            

        # Calculate elapsed time
        if started and not paused:
            elapsed_time = time.time() - start_time
        else:
            elapsed_time = elapsed_time  # Keep time frozen when paused
            
        # Clear the screen
        screen.fill(BLACK)
        
        # Draw the vertical bars for objects
        all_bars_full_height = True  
        for i in range(num_algorithms):
            # Calculate the bar height for each object based on its growth rate and time elapsed
            bar_height = int(elapsed_time * growth_rate)

            # Limit the bar height to its respective maximum height
            bar_height = min(bar_height, max_heights[i])
        
            # Check if the bar has reached its maximum height
            if bar_height < max_heights[i]:
                all_bars_full_height = False  # At least one bar is not full height

            # Draw the bar (from bottom to top)
            pygame.draw.rect(screen, BLUE, 
            (100 + i * 150, height - 50 - bar_height, bar_width, bar_height)
            )

        # Draw the algorithm name
        for i in range(num_algorithms):
            font = pygame.font.SysFont(None, 36)
            text = font.render(algorithms[i], True, WHITE)
            screen.blit(text, (100 + i * 150, height - 40))
            
        # Draw the button:
        start_button.draw(screen)
        stop_button.draw(screen)
        reset_button.draw(screen)
        return_button.draw(screen)

        # Convert elapsed time to seconds and milliseconds format
        milliseconds = elapsed_time *1000
        seconds = elapsed_time
        
        # Draw the elapsed time 
        font = pygame.font.SysFont(None, 26)
        time_text = font.render(f"{seconds}:{milliseconds:01}", True, WHITE)
            
        # Stop the timer if all bars have reached their maximum heights
        if not all_bars_full_height: 
            screen.blit(time_text, (860, 10))
        else:
            # Draw the time value
            for i in range(num_algorithms):
                time_text = font.render(f"{times[i]:.5f} s", True, WHITE)
                screen.blit(time_text, (100 + i * 150, 530 - max_heights[i]))
            
            
        # Update the display
        pygame.display.flip()

        # Cap the frame rate to 60 FPS
        pygame.time.Clock().tick(60)
        
        
def algorithm_comparation():
    global USER_INPUT, ALGORITHMS
    
    screen.fill(BLACK)
    
    # Initialize variables for timing
    times = []
    for algo in ALGORITHMS:
        if algo == "Bubble Sort":
            times.append(time_analysis_sort(bubble_sort, USER_INPUT.copy()))
        elif  algo == "Merge Sort":
            times.append(time_analysis_sort(merge_sort, USER_INPUT.copy()))
        elif  algo == "Quick Sort":
            times.append(time_analysis_quick_sort(quick_sort, USER_INPUT.copy(), 0, len(USER_INPUT) - 1 ))
        elif  algo == "Radix Sort":
            times.append(time_analysis_sort(radix_sort, USER_INPUT.copy()))
        elif  algo == "Linear Search":
            times.append(time_analysis_search(linear_search, USER_INPUT.copy(), 1))

    draw_analysis(times, ALGORITHMS)
    
#==========================================================================



#++++++++++++++++++++
# USER_INPUT SCREEN +
#++++++++++++++++++++
def getting_user_input():
    global USER_TEXT, USER_INPUT, screen_check

    # Buttons
    generate_button = Button(400, 450, 230, 50, "Generate the array", BLUE, GRAY, WHITE)
    visual_button = Button(400, 330, 230, 50, "Start Visualization", GREEN, GRAY)
    
    USER_TEXT = pygame_gui.elements.UITextEntryLine(relative_rect=input_rect, manager=MANAGER)

    while True:
        UI_RATE = CLOCK.tick(FPS)/1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Handle button clicks
            if generate_button.is_clicked(event):
                screen_check = False
                USER_TEXT.hide()
                generate()
            
            if visual_button.is_clicked(event):
                screen_check = True
                temp = USER_TEXT.get_text()
                USER_INPUT = list(map(int, temp.split()))
                USER_TEXT.hide()
                getting_algorithms()
                
            MANAGER.process_events(event)
            
        MANAGER.update(UI_RATE)
        
        # Update the screen
        screen.fill(BLACK)
    
        # Draw buttons
        generate_button.draw(screen)
        visual_button.draw(screen)
    
        # Draw user input
        text = font.render("or", True, WHITE)
        screen.blit(text, (500, 400))
    
        text = font.render("Enter the INT Array, seperated by space: ", True, WHITE)
        screen.blit(text, (100, 260))
   
        MANAGER.draw_ui(screen)

        # Update the display
        pygame.display.flip() 
 
def getting_algorithms():
    global USER_INPUT, ALGORITHMS
    
    # Define selection list items
    selection_items = ['  Bubble Sort   ', '   Merge Sort   ', '   Quick Sort    ', '   Radix Sort    ', ' Linear Search ']
    item_rects = []  # Store rects for each item for detecting clicks
    selected_items = []  # Track selected items
    
    # Create a button to submit input
    submit_button = Button(370, 400, 300, 50, "Start Visualization", BLUE, GRAY, WHITE)
    return_button = Button(100, 500, 100, 50, "Return", GREEN, GRAY) 

    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Handle mouse clicks to select items
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_pos = event.pos
                
                    for i, rect in enumerate(item_rects):
                        if rect.collidepoint(mouse_pos):
                            item = selection_items[i]
                        
                            # Toggle selection
                            if item in selected_items:
                                selected_items.remove(item)
                            else:
                                selected_items.append(item)
    

            # Handle submition
            if submit_button.is_clicked(event) and event.button == 1:
                # Get Algorithms selections:
                if len(selected_items) == 0:
                    ALGORITHMS = ["Bubble Sort", "Merge Sort", "Quick Sort", "Radix Sort", "Linear Search"]
                else:
                    ALGORITHMS.clear()
                    for item in selected_items:
                        ALGORITHMS.append(item.strip())
                        ALGORITHMS.sort()
                    if linear_search(ALGORITHMS, "Linear Search"):
                        ALGORITHMS.remove("Linear Search")
                        ALGORITHMS.append("Linear Search")
                algorithm_comparation()
            
            # Handle return button        
            if return_button.is_clicked(event):   
                getting_user_input()  
    
        # Redraw the window
        screen.fill(BLACK) 
         
        text = font.render("Select the algorithms: ", True, WHITE)
        screen.blit(text, (400, 100))
        
        # Adding buttons
        submit_button.draw(screen)
        return_button.draw(screen)
               
        # Draw the selection list
        y_offset = 150  # Starting y position for the items
    
        for i, item in enumerate(selection_items):
            # Create a rect for each item (text)
            item_surface = font.render(item, True, WHITE)
            item_rect = item_surface.get_rect(topleft=(430, y_offset-3))
        
            # Highlight the item if it is selected
            if item in selected_items:
                pygame.draw.rect(screen, BLUE, item_rect)
        
            # Draw the text (item)
            screen.blit(item_surface, (430, y_offset))
        
            # Store the rect to detect clicks later
            if len(item_rects) < len(selection_items):
                item_rects.append(item_rect)
        
            # Move y position down for the next item
            y_offset += 40
        
        # Update the display
        pygame.display.update() 
#==========================================================================       
        

#++++++++++++++++++    
# GENERATE SCREEN +
#++++++++++++++++++       
def generate():
    global USER_INPUT, ALGORITHMS
    
    # Define selection list items
    selection_items = [' Bubble Sort    ', ' Merge Sort     ', ' Quick Sort      ', ' Radix Sort      ', ' Linear Search ']
    item_rects = []  # Store rects for each item for detecting clicks
    selected_items = []  # Track selected items
    
# Create input fields
    input_field1 = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((100, 100), (200, 50)),
        manager=MANAGER
    )
    input_field2 = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((100, 250), (200, 50)),
        manager=MANAGER
    )
    input_field3 = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((350, 250), (200, 50)),
        manager=MANAGER
    )

    # Create a button to submit input
    submit_button = Button(400, 400, 300, 50, "Start Visualization", BLUE, GRAY)
    return_button = Button(100, 500, 100, 50, "Return", GREEN, GRAY)

    # Main loop variables
    clock = pygame.time.Clock()

    while True:
        time_delta = clock.tick(60) / 1000.0  # Limit frame rate to 60 FPS
    
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Handle mouse clicks to select items
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_pos = event.pos
                
                    for i, rect in enumerate(item_rects):
                        if rect.collidepoint(mouse_pos):
                            item = selection_items[i]
                        
                            # Toggle selection
                            if item in selected_items:
                                selected_items.remove(item)
                            else:
                                selected_items.append(item)

            # Handle UI events
            if submit_button.is_clicked(event):
                if event.button == 1:
                    # Get the input from the text fields when the button is pressed
                    size = int(input_field1.get_text())
                    min_val = int(input_field2.get_text())
                    max_val = int(input_field3.get_text())
                    USER_INPUT = [random.randint(min_val, max_val) for _ in range(size)]
                    #print(USER_INPUT)
                    
                    # Update Algorithms selections:
                    if len(selected_items) == 0:
                        ALGORITHMS = ["Bubble Sort", "Merge Sort", "Quick Sort", "Radix Sort", "Linear Search"]
                    else:
                        ALGORITHMS.clear()
                        for item in selected_items:
                            ALGORITHMS.append(item.strip())
                            ALGORITHMS.sort()
                        if linear_search(ALGORITHMS, "Linear Search"):
                            ALGORITHMS.remove("Linear Search")
                            ALGORITHMS.append("Linear Search")
                    
                    # Process to visualization
                    input_field1.hide()
                    input_field2.hide()
                    input_field3.hide()
                    
                    algorithm_comparation()
                    
            if return_button.is_clicked(event):
                input_field1.hide()
                input_field2.hide()
                input_field3.hide()
                getting_user_input()
                
            MANAGER.process_events(event)

        # Update the GUI manager
        MANAGER.update(time_delta)
    
        # Redraw the window
        screen.fill(BLACK)  
        text = font.render("Enter the size of the Array: ", True, WHITE)
        screen.blit(text, (100, 60))
        text = font.render("Enter the Min-Max bound: ", True, WHITE)
        screen.blit(text, (100, 210))
        
        text = font.render("to", True, WHITE)
        screen.blit(text, (317, 260))
        
        text = font.render("Select the algorithms: ", True, WHITE)
        screen.blit(text, (690, 100))
        
        submit_button.draw(screen)
        return_button.draw(screen)
        MANAGER.draw_ui(screen)
        
        
        # Draw the selection list
        y_offset = 150  # Starting y position for the items
    
        for i, item in enumerate(selection_items):
            # Create a rect for each item (text)
            item_surface = font.render(item, True, WHITE)
            item_rect = item_surface.get_rect(topleft=(700, y_offset-3))
        
            # Highlight the item if it is selected
            if item in selected_items:
                pygame.draw.rect(screen, BLUE, item_rect)
        
            # Draw the text (item)
            screen.blit(item_surface, (700, y_offset))
        
            # Store the rect to detect clicks later
            if len(item_rects) < len(selection_items):
                item_rects.append(item_rect)
        
            # Move y position down for the next item
            y_offset += 40
        
        # Update the display
        pygame.display.flip()        
 
 
 
#==========================================================================
# Main Loop        
def main():
    getting_user_input()
