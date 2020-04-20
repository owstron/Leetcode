def search(nums):
    '''
        left tree = -1 to -n
        right tree = 1 to n
        
        [4,5,6,7,8,9,0,1,2]
        
        [4,5,6,7,8,9,0,1,2]
            ^
            l               r 
                        ^   
    '''
    # find the cutoff point.
    l = 0
    r = len(nums) - 1
    
    while l< r:
        mid = (l + r) // 2
        print(nums[mid])
        
        if nums[mid-1] > nums[mid] and nums[mid] < nums[(mid+1)]:
            break
        
        if nums[mid] > nums[r]:
            l = mid + 1
        else:
            r = mid

    print('final', nums[mid], 'index', mid)

search([4,5,6,7,8,9,0,1,2])
search([0,1,2,4,5,6,7,8,9])
search([2,4,5,6,7,8,9,0,1])
