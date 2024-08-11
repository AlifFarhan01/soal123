def singleNumber(nums):
    item = {}
    for angka in nums:
        if angka in item:
            item[angka] += 1
        else:
            item[angka] = 1
    
   
    for angka, jumlah in item.items():
        if jumlah == 1:
            return angka


nums1 = [2, 2, 1]
print(singleNumber(nums1))  

nums2 = [4, 1, 2, 1, 2]
print(singleNumber(nums2))  
