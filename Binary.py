def binary(nums, tar):
    l, r =0, len(nums) -1
    while l <= r:
        mid = l + ((l+r)//2)
        if mid == tar:
            return tar
            
        elif tar < mid:
            r -= mid
            
        elif tar > mid:
            l += mid
        else:
            return mid
            
    return -1
    
print(binary([1,4,3,2,5], 3))
