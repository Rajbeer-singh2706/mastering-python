# 9. Find All Duplicates in an Array
'''
Problem: Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once. 
Find all the elements that appear twice.

Input: [4,3,2,7,8,2,3,1]
Output: [2, 3]
Hint: Use the array itself as a hash map by negating the values at the indices corresponding to the numbers.
'''


def find_duplicates(nums):
    value_count = {}
    output_list = []
    for item in nums:
        if item not in value_count:
            value_count[item] = 1
        else:
            value_count[item]+=1
            output_list.append(item)
    return output_list


if __name__ == '__main__':
    input_list = [4,3,2,7,8,2,3,1]
    output_list = find_duplicates(input_list)
    print(output_list)
    