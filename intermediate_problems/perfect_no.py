import math


def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    n = int(input("no"))
    for i in range(n):
        val = int(input(" enter no "))
        sum = 0
        for i in range(1, val):
            if val % i == 0:
                sum += i
        if sum == val:
            print("YES")
        else:
            print("NO")

    return 0

if __name__ == '__main__':
    main()