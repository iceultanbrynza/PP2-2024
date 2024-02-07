def has_33(nums):
    z = 1
    i = 0
    while i < len(nums):
        if(nums[i] == 3):
            if(nums[i+1] == 3):
                i+=2
                continue
            elif(nums[i+1]!=3):
                z = 0
                print("False")
                break
        i += 1
    if z == 1:
        print(True)
        
            
nums = [1, 2, 3, 3, 4, 5, 6,3, 3,3, 7, 8]
has_33(nums)
