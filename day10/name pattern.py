#s
rows = 7
cols = 5

for i in range(rows):
    for j in range(cols):
        # Top row
        if i == 0:
            print("*", end=" ")
        # Upper left vertical
        elif i < 3 and j == 0:
            print("*", end=" ")

        # Middle row
        elif i == 3:
            print("*", end=" ")

        # Lower right vertical
        elif i > 3 and j == cols - 1:
            print("*", end=" ")

        # Bottom row
        elif i == rows - 1:
            print("*", end=" ")

        else:
            print(" ", end=" ")

    print()

print('\n\n')
#I
rows = 6
cols = 5

for i in range(rows):
    for j in range(cols):

        # Top and bottom horizontal line
        if i == 0 or i == rows - 1:
            print("*", end=" ")

        # Middle vertical line
        elif j == cols // 2:
            print("*", end=" ")

        else:
            print(" ", end=" ")

    print()
print('\n\n')

#R
rows = 6
cols = 5

for i in range(rows):
    for j in range(cols):

        # Left vertical line
        if j == 0:
            print("*", end=" ")

        # Top and middle horizontal lines
        elif (i == 0 or i == 3) and j < cols - 1:
            print("*", end=" ")

        # Right vertical line (upper part)
        elif j == cols - 1 and i < 3:
            print("*", end=" ")

        # Slant line for R
        elif i - j == 1:
            print("*", end=" ")

        else:
            print(" ", end=" ")

    print()
print('\n\n')

#I
rows = 6
cols = 5

for i in range(rows):
    for j in range(cols):

        # Top and bottom horizontal line
        if i == 0 or i == rows - 1:
            print("*", end=" ")

        # Middle vertical line
        elif j == cols // 2:
            print("*", end=" ")

        else:
            print(" ", end=" ")

    print()
print('\n\n')
#S
rows = 7
cols = 5

for i in range(rows):
    for j in range(cols):
        # Top row
        if i == 0:
            print("*", end=" ")
        # Upper left vertical
        elif i < 3 and j == 0:
            print("*", end=" ")

        # Middle row
        elif i == 3:
            print("*", end=" ")

        # Lower right vertical
        elif i > 3 and j == cols - 1:
            print("*", end=" ")

        # Bottom row
        elif i == rows - 1:
            print("*", end=" ")

        else:
            print(" ", end=" ")

    print()
print('\n\n')
#H
rows = 5
cols = 5

for i in range(rows):
    for j in range(cols):

        # Left and right vertical lines
        if j == 0 or j == cols - 1:
            print("*", end=" ")

        # Middle horizontal line
        elif i == rows // 2:
            print("*", end=" ")

        else:
            print(" ", end=" ")

    print()
print('\n\n')
#A
rows = 5
cols = 5

for i in range(rows):
    for j in range(cols):

        # Left and right slant lines
        if (j == 0 and i != 0) or (j == cols - 1 and i != 0):
            print("*", end=" ")

        # Top middle star
        elif i == 0 and j == cols // 2:
            print("*", end=" ")

        # Middle horizontal line
        elif i == rows // 2:
            print("*", end=" ")

        else:
            print(" ", end=" ")

    print()

































    
























    
