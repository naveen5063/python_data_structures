def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    num = int(input("enter a no"))
    if num == 1:
        print(num)
    else:
        for i in range(1, num):
            orgnum = i
            res = 0
            num = i
            while num:
                cubenum = int(num % 10)
                num = int(num / 10)
                res += cubenum ** 3
            if res == orgnum:
                print(orgnum)

    return 0

if __name__ == '__main__':
    main()