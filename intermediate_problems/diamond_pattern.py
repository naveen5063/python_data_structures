def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    a = int(input())

    for i in range(a):  # Printing Upper half of the pattern
        print((a - i) * '*', end="")
        print(2 * i * ' ', end="")
        print((a - i) * '*', end="")
        print("")

    for i in range(1, a + 1):  # Printing lower half of the pattern
        print(i * '*', end="")
        print(2 * (a - i) * ' ', end="")
        print(i * '*', end="")
        print("")

    return 0


if __name__ == '__main__':
    main()

# ********
# ***  ***
# **    **
# *      *
# *      *
# **    **
# ***  ***
# ********
