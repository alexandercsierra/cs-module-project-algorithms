'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max_day1(nums, k):
    
    #iterate through the array with two pointers
        #start will be 0
        #end will be k-1
        #find max in that range
        #push max to new array
        #increment start and end until end is == end of array

    end = k-1
    maxes = []
    for i in range(len(nums)):
        if end < len(nums):
            start = i
            greatest = nums[i]
            for j in range(start, end+1):
                if nums[j] > greatest:
                    greatest = nums[j] 
            maxes.append(greatest)
            end +=1
        print('one loop complete', i)
    return maxes


def sliding_window_max(nums, k):
    maxes = []
    current = []
    for i in range(len(nums)):
        start = i
        #there are less than k elements in the current array
        if len(current) <= k:
            current.append(nums[i])
            if len(current) == k:
                maxes.append(max(current))
                current.pop(0) 
    return maxes





  



if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    #expect to get [3,3,5,5,6,7]

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")

    # arr1 = [0, 1, 2, 3, 4]

    # def get_max(arr):
    #     ph = []
    #     ph.append(max(arr))
    #     return ph

    # print('get max', get_max(arr1))
