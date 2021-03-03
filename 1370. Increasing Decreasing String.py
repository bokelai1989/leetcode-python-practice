# https://leetcode.com/problems/increasing-decreasing-string/submissions/
# Given a string s. You should re-order the string using the following algorithm:

# Pick the smallest character from s and append it to the result.
# Pick the smallest character from s which is greater than the last appended character to the result and append it.
# Repeat step 2 until you cannot pick more characters.
# Pick the largest character from s and append it to the result.
# Pick the largest character from s which is smaller than the last appended character to the result and append it.
# Repeat step 5 until you cannot pick more characters.
# Repeat the steps from 1 to 6 until you pick all characters from s.
# In each step, If the smallest or the largest character appears more than once you can choose any occurrence and append it to the result.

# Return the result string after sorting s with this algorithm.

# Example 1:

# Input: s = "aaaabbbbcccc"
# Output: "abccbaabccba"
# Explanation: After steps 1, 2 and 3 of the first iteration, result = "abc"
# After steps 4, 5 and 6 of the first iteration, result = "abccba"
# First iteration is done. Now s = "aabbcc" and we go back to step 1
# After steps 1, 2 and 3 of the second iteration, result = "abccbaabc"
# After steps 4, 5 and 6 of the second iteration, result = "abccbaabccba"
# Example 2:

# Input: s = "rat"
# Output: "art"
# Explanation: The word "rat" becomes "art" after re-ordering it with the mentioned algorithm.
# Example 3:

# Input: s = "leetcode"
# Output: "cdelotee"

class Solution:
    def sortString(self, s: str) -> str:
       # 1. convert the string into a list 
        A = [a for a in s]
        
        # 2. create an empty bucket to put the new generated list 
        res = []
        
        # 3. start a loop condition,when A is not done. Deal with the elements one by one; after dealing with each element, remove it from A , and use 
        # len(A) as a control condition for the while loop, making sure each element is looped. 
        while len(A) > 0:
          
          # get an unique set of elements in A 
            M = list(set(A))
            
            # default ordering is small to large, a, b, c, d, 
            M.sort()
            
            #pick smallest -> largest
            for c in M: 
                res.append(c) # store each c into the res list 
                A.remove(c). # meanwhile remove the stored element from A 
                
            #check if something is left from the original string 
            M = list(set(A)) # get the unique set of the elements from the remanining of A 
            M.sort(). # sort again 
            
            # pick largest --> smallest from what is left 
            for c in M[::-1]:  # get elements from the opposite order 
                res.append(c) # append from the largest element
                A.remove(c)
        
        return ''.join(res) # join everything into a string 
