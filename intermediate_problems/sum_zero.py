class Solution:
	# @param A : list of integers
	# @return a list of integers
	def lszero(self, arr):
		pf_arr = [arr[0]]
		for i in range(1, len(arr)):
			pf_arr.append(pf_arr[i - 1] + arr[i])
			#pf_arr.append(sum(arr[: i + 1]))
		print(pf_arr)
		arr_hash_set = set(pf_arr)
		if len(arr_hash_set) < len(pf_arr) or 0 in pf_arr:
			return 1
		else:
			return 0

A = [1, 2, -2, 4, -4]
#A = [2, 2, 1, -3, 4, 3, 1, -2, -3, 2]
#1,3,1,5,1
#A = [ 1, 2, 3, 4, 5 ]
#A = [ 88, 2, 46, 66, 89, -79, 36, 72, 30, 60, 89, 23, 60, 26, -43, -14, 20, 92, -48, 45, 84, -22, 65, -57, 7 ]

s = Solution()
print(s.lszero(A))