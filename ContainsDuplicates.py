#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
#Example 1:
#Input: nums = [1,2,3,1]
#Output: true


    def containsDuplicate(self, nums: List[int]) -> bool:
        #create a hashmap, it would take extra space i.e O(n) but the time complexity would also reduce.
        dic = set()
        #loop through array nums
        for n in nums:
          #check if n is in the set, if it exists return True
            if n in dic:
                return True
              #else, add it to the set
            dic.add(n)
            #return false, if no duplicate value exists in the dict
        return False
containsDuplicates([1,2,3,1])
        
