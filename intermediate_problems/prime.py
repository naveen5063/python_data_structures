import math


def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    num = int(input("no"))
    flag = 0
    if num > 1:
        for i in range(2, int(math.sqrt(num))):
            if num % i == 0:
                flag = 1
    if flag == 0:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()
