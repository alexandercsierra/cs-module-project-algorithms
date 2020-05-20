'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    list_of_nums = {}
    for i in range(len(arr)):
        if arr[i] in list_of_nums:
            list_of_nums[arr[i]] += 1
        else: 
            list_of_nums[arr[i]] = 1
    for entry in list_of_nums:
        if list_of_nums[entry] == 1:
            return entry


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")