def split_and_join(line):
    line_split = line.split(" ")
    return  "-".join(line_split)

if __name__ == '__main__':
    str = "my name is naveen"
    res = split_and_join(str)
    print(res)