
### 2. **Find the Missing Number**
"""
- **Problem**: Given an array containing `n-1` distinct numbers in the range `[1, n]`, find the missing number.
   - **Example**:
     ```python
     Input: [3, 0, 1]
     Output: 2
"""

def find_missing_number1(input):
    input.sort()

    startingIndexValue = input[0]
    endingIndexValue = input[len(input)-1]+1
    missing_num = [item for item in range(startingIndexValue,endingIndexValue) if item not in input ]
    return missing_num
 
def find_missing_number2(input):
    input.sort()
    for item in range(input[0], input[len(input)-1]+1):
        if item not in input:
            print(f"missing : {item}")
            return item 
    
    ## 2nd Way
    startingIndexValue = input[0]
    endingIndexValue = input[len(input)-1]+1
    missing_num = [item for item in range(startingIndexValue,endingIndexValue) if item not in input ]
    print(missing_num)

    ## 3rd way
    set1 = set(input)
    set2 = {item for item in range(startingIndexValue,endingIndexValue) }
    print(set1)
    print(set2)

    difference = set2.difference(set1)
    print(f"Missing : {difference}")

def find_missing_number3(input):
    input.sort()
    for item in range(input[0], input[len(input)-1]+1):
        if item not in input:
            print(f"missing : {item}")
            return item 

input = [3, 0, 1]
find_missing_number3(input)

# python3 prob1_missing_number.py