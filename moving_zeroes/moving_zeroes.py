'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    zero_counter = 0
    mock_arr = arr.copy()
    if len(arr) == 0:
        return arr
    for i in mock_arr:
        if i == 0:
            arr.remove(i)
            arr.append(i)
            zero_counter += 1

    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
