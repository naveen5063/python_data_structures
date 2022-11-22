import math

def isprime(num):
    c = 0
    num_val = int(math.sqrt(num))
    for i in range(1, num_val + 1):
        if num % i == 0:
            if i == int(num / i):
                c += 1
            else:
                c += 2
    if c == 2:
        return True
    else:
        return False

class Solution:
    # @param A : list of integers
    # @return a list of integers
	def primesum(self, A):
		sum_val = []
		list_prime = []
		spf_arr = list(range(0, A + 1))
		for i in range(2, math.ceil(math.sqrt(A)) + 1):
			if i == spf_arr[i]:
				for j in range(i * i, A + 1, i):
					if spf_arr[j] == j:
						spf_arr[j] = i

		for i in range(1, A + 1):
			c = 0
			x = i
			while x >= 2:
				if isprime(spf_arr[x]):
					#sum_val.add(spf_arr[x])
					list_prime.append(spf_arr[x])
					x = int(x / spf_arr[x])
					c += 1
		print("sum val", sum_val)
		n = len(list_prime)
		count = 0
		for i in range(0, n):
			for j in range(i + 1, n):
				if list_prime[i] + list_prime[j] == A:
					sum_val.append(list_prime[i])
					sum_val.append(list_prime[j])
					count += 1
		print("sum", sum_val)
		return sum_val[0:2]
A = 4
A = 10
#A = 1048574
s = Solution()
print(s.primesum(A))
