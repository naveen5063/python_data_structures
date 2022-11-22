def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    no_of_testcase = int(input())
    array_elements = input()
    ele_to_find = int(input())
    array_elements = array_elements.strip()
    array_elements = array_elements.split(" ")
    array_elements.pop(0)
    res = 0
    for t in range(0, no_of_testcase):
        for i in range(0, len(array_elements)):
            if int(array_elements[i]) == int(ele_to_find):
                res = 1
        print(res)

if __name__ == '__main__':
    main()