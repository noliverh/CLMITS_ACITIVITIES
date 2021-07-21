def for_loop():
    '''
    This is to print a pattern of right arrow using
    the for loop with letter "f"
    No parameters needed.
    '''
    print("This will print pattern using for loop...")
    rows = int(input("Enter the number of rows: "))

    for row in range(0, rows):
        for col in range(0, row + 1):
            print("f", end=" ")
        print()

    for row in range(rows, 0, -1):
        for col in range(0, row - 1):
            print("f", end=" ")
        print()

for_loop()

def while_loop():
    '''
    This is to print a pattern of right arrow using
    the while loop with letter "w"
    No parameters needed.
    '''
    print("This will print pattern using while loop")
    rows = int(input("Enter the number of rows: "))

    i = 1
    while i <= rows:
        j = i
        while j < rows:
            # display space
            print(" ", end=" ")
            j += 1
        k = 1
        while k <= i:
            print("w", end=" ")
            k += 1
        print()
        i += 1

    i = rows
    while i >= 1:
        j = i
        while j <= rows:
            print(" ", end=" ")
            j += 1
        k = 1
        while k < i:
            print("w", end=" ")
            k += 1
        print()
        i -= 1

while_loop()
