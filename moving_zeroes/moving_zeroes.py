'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    zeroes = 0
    newArr = []
    for i in range(len(arr)):
        if arr[i] == 0:
            zeroes += 1
        else:
            newArr.append(arr[i])
    for i in range (zeroes):
        newArr.append(0)
    return newArr
    


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")