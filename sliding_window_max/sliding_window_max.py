'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


def sliding_window_max(nums, k):

    nw_arr = []
    first_item = 0
    last_item = k

    while last_item <= len(nums):
        max = nums[first_item]
        if k == len(nums):
            return nums
        for i in range(first_item, last_item):
            if nums[i] > max:
                max = nums[i]
        nw_arr.append(max)
        first_item += 1
        last_item += 1
    return nw_arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
