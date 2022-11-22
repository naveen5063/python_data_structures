def nthMagicNo(n):
    pow = 1
    answer = 0
    while (n):
        pow = pow * 5
        print("pow", pow)
        # If last bit of n is set
        if (n & 1):
            print("and", n & 1)
            answer += pow
            print("answer", answer)
        # proceed to next bit
        n >>= 1  # or n = n/2
        print("n", n)
    return answer


# Driver program to test above function
n = 7
print("nth magic number is", nthMagicNo(n))