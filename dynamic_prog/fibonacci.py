def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    n = int(input())
    a = 0
    b = 1
    c = 0
    for j in range(2, n+1):
        c = a + b
        a = b
        b = c
    if c == 0:
        print(a+b)
    else:
        print(c)

if __name__ == '__main__':
    main()