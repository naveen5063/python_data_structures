def swap_positions(array_elements, pos1, pos2):
    array_elements[pos1], array_elements[pos2] = array_elements[pos2], array_elements[pos1]
    return array_elements

def reverse(array_elements, s_index, e_index):
    start_index = s_index
    ending_index = e_index
    while start_index < ending_index:
        array_elements = swap_positions(array_elements, start_index, ending_index)
        start_index += 1
        ending_index -= 1
    return array_elements

def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    array_elements = input()
    array_elements = array_elements.strip()
    array_elements = array_elements.split(" ")
    array_elements.pop(0)
    rotate_value = int(input())
    array_len = len(array_elements)
    if rotate_value >= array_len:
        rotate_value %= array_len
    array_elements = reverse(array_elements, 0, array_len - 1)
    array_elements = reverse(array_elements, 0, rotate_value - 1)
    array_elements = reverse(array_elements, rotate_value, array_len - 1)
    print(*array_elements, end=" ")

if __name__ == '__main__':
    main()