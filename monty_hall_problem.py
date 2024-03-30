import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt

# non winning door revealed
def losing_door(host, num_doors, chosen_door):
    i = 1
    while(i == host or i == chosen_door ):
        i = (i+1)%(num_doors)
    return i

# player switches to unopened door
def switch_function(shown_door, num_doors, chosen_door):
    i = 1
    while( i == shown_door or i == chosen_door):
        i = (i+1)%(num_doors)
    return i

def Monty_Hall_Game(switch, num_tests):
    # counters to keep track of results
    win_with_switch = 0
    win_without_switch = 0
    lose_with_switch = 0
    lose_without_switch = 0

    # create doors
    doors = ['A', 'B', 'C']
    num_doors = len(doors)

    for i in range(0, num_tests):
        # assign a door with a prize
        w_door = random.randint(0, num_doors-1)
        
        # player chooses a door at random
        player_choice = random.randint(0,num_doors-1)
        chosen_door = player_choice
        
        shown_door = losing_door(w_door, num_doors, chosen_door)

        if switch == True:
            chosen_door = switch_function(shown_door, num_doors, chosen_door)

        if chosen_door == w_door and switch == False:
            win_without_switch += 1

        elif chosen_door == w_door and switch == True:
            win_with_switch += 1

        elif chosen_door != w_door and switch == False:
            lose_without_switch += 1

        elif chosen_door != w_door and switch == True:
            lose_with_switch += 1

        else:
            print(f"ERROR!")

    return win_with_switch, win_without_switch, lose_with_switch, lose_without_switch, num_tests

# Run simulation with switching 1 million times
x = Monty_Hall_Game(True, 1_000_000)

# Run simulation without switching
y = Monty_Hall_Game(False, 1_000_000)


print(f"Number of wins with switching: {x[0]}")
print(f"Number of loses with switching: {x[2]}")
win_with_switch_percentage = (x[0] / x[4]) * 100
lose_percentage_with_switch = (x[2] / x[4]) * 100

print(f"percentage of winning with switching: {win_with_switch_percentage:.2f}%")
print(f"Percentage of loses with switching: {lose_percentage_with_switch:.2f}%\n")
print(f"Number of wins without swithing: {y[1]}")
print(f"Number of loses without switching: {y[3]}")
win_percentage_without_switching = (y[1]/y[4]) * 100
lose_percentage_without_switching = (y[3] / y[4]) * 100

print(f"Percentage of winning without switching: {win_percentage_without_switching:.2f}%")
print(f"Percentage of losing without switching: {lose_percentage_without_switching:.2f}%\n")


# Print pie graph of wins
wins = [x[0], y[1]]
result_labels = ['Wins with switch', 'wins without switch']

plt.title('Results for Monty Hall Problem')
plt.pie(wins, labels = result_labels)
plt.show()


num_tests = []
w_percent = []
switch = True
for i in range(1, 200):
    num_tests.append(i)
    z = Monty_Hall_Game(switch, i)
    r = (z[0]/z[4]) * 100
    w_percent.append(r)

# Set width and height
plt.figure(figsize = (10, 5))
plt.plot(num_tests, w_percent)
plt.title('Results for Monty Hall Problem Running Several Thousand Times')

plt.xlabel('Number of Tests',fontsize=14)
plt.ylabel('Win %',fontsize=14)
plt.show()