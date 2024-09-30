
# PS5. Group Anagrams
"""
-- Write a function that takes a list of strings and groups anagrams together.
-- INPUT    : ["eat", "tea", "tan", "ate", "nat", "bat"]
-- OUTPUT   :  [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
-- WA Test Case as well 
"""

# Description : sorted() 
# Syntax : 

def find_anagaram(input_list):
    aDict={}
    for item in input_list:
        sitem = ''.join(sorted(item)) 
        if sitem in aDict:
            aDict[sitem].append(item)
        else: 
            aDict[sitem] = [item]
    anagram_group_list = list(aDict.values())
    return anagram_group_list

if __name__ == '__main__':
    input_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
    anagram_group_list = find_anagaram(input_list=input_list)
    print(anagram_group_list)


# Next Test cases 
# Optimize/Refactor with GTP 
# Alternative suggestion , of variabel or naming conversion , input variable , output variable of intermeidaute variable 
# function name
