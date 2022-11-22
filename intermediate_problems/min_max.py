def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    array_elements = input()
    array_elements = strip_and_pop_first_element(array_elements)
    max_ele = get_max_element(array_elements)
    min_ele = get_min_element(array_elements)
    print(max_ele)
    print(min_ele)
    return 0


def get_min_element(array_elements):
    min_ele = array_elements[0]
    for i in range(0, len(array_elements)):
        if array_elements[i] < min_ele:
            min_ele = array_elements[i]
    return min_ele

def get_max_element(array_elements):
    max_ele = int(array_elements[0])
    for i in range(0, len(array_elements)):
        if max_ele < array_elements[i]:
            max_ele = array_elements[i]
            #print(max_ele)
    return max_ele


def strip_and_pop_first_element(array_elements):
    array_elements = array_elements.strip()
    array_elements = array_elements.split(" ")
    array_elements.pop(0)
    return array_elements


if __name__ == '__main__':
    main()