'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    #for n of 3
    # 1 1 1 - each one individually
    # 1 2 - one and then two
    # 2 1 - two and then one 
    # 3 - three all at once

    #n-1 + 1 - 2 times
    #2 - n-1 +1 -2 times

    #5
    # n- 1 + 1 X 2

    if n <=1:
        return 1
    else:
        print('recursing', n)
        return eating_cookies((n-1))


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
