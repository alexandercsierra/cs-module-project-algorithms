'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    total_product = 1
    zeroes = []
    newArr = [0 for _ in range(len(arr))]
    for i in range(len(arr)):
        if arr[i] == 0:
            zeroes.append(i)
        else:
            total_product *= arr[i]
    if len(zeroes) > 0:
        for i in range(len(zeroes)):
            newArr[zeroes[i]] = total_product
    else:
        for i in range(len(arr)):
            newArr[i] = (total_product//arr[i])
    
    return newArr



if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
