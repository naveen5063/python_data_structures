class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        count = 0
        # tmp_arr = A
        i = 0
        # for i in range(0, len(A)):
        if i >= 0 and i < len(A):
            while (A[i] != i + 1):
                val = A[i] - 1
                A[i], A[val] = A[val], A[i]
                count += 1
            i += 1
            if count == 2:
                return "Yes"
        return "No"


def merge(arr, temp, left, mid, right):
    inv_count = 0

    i = left  # i is index for left subarray
    j = mid  # j is index for right subarray
    k = left  # k is index for resultant merged subarray
    while (i <= mid - 1) and (j <= right):

        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            k, i = k + 1, i + 1

        else:
            temp[k] = arr[j]
            k, j = k + 1, j + 1
            inv_count = inv_count + (mid - i)

    # Copy the remaining elements of left
    # subarray (if there are any) to temp
    while i <= mid - 1:
        temp[k] = arr[i]
        k, i = k + 1, i + 1

    # Copy the remaining elements of right
    # subarray (if there are any) to temp
    while j <= right:
        temp[k] = arr[j]
        k, j = k + 1, j + 1

    # Copy back the merged elements to original array
    for i in range(left, right + 1):
        arr[i] = temp[i]

    return inv_count


# An auxiliary recursive function that
# sorts the input array and returns the
# number of inversions in the array.
def _mergeSort(arr, temp, left, right):
    inv_count = 0
    if right > left:
        # Divide the array into two parts
        # and call _mergeSortAndCountInv()
        # for each of the parts
        mid = (right + left) // 2

        # Inversion count will be sum of
        # inversions in left-part, right-part
        # and number of inversions in merging
        inv_count = _mergeSort(arr, temp, left, mid)
        inv_count += _mergeSort(arr, temp, mid + 1, right)

        # Merge the two parts
        inv_count += merge(arr, temp, left, mid + 1, right)

    return inv_count


# This function sorts the input array and
# returns the number of inversions in the array
def mergeSort(arr, array_size):
    temp = [None] * array_size
    return _mergeSort(arr, temp, 0, array_size - 1)


# method returns minimum number of
# swaps to reach permuted array 'arr'
def minSwapToReachArr(arr, N):
    # loop over all elements to check
    # Invalid permutation condition
    for i in range(0, N):

        # if an element is at distance more than 2
        # from its actual position then it is not
        # possible to reach permuted array just
        # by swapping with 2 positions left elements
        # so returning -1
        if (arr[i] - 1) - i > 2:
            return -1

    # If permuted array is not Invalid, then number
    # of Inversion in array will be our final answer
    numOfInversion = mergeSort(arr, N)
    return numOfInversion


# Driver code to test above methods
if __name__ == "__main__":

    # change below example
    arr = [1, 2, 5, 3, 4]
    arr = [2, 3, 3]
    N = len(arr)
    res = minSwapToReachArr(arr, N)
    if res == -1:
        print("Not Possible")
    else:
        print("Possible")
        print(res)
# A = [2, 3, 1]
# #A = [3, 2, 1]
# A = [2, 3, 3]
# s = Solution()
# print(s.solve(A))
