#def soma(x,y):
#    total = x + y
#    print(f'{x} + {y} = {total}')

#soma(2,2)
#print('oi')

def find_max(nums):
 max_num = float("-inf") # smaller than all other numbers
 for num in nums:
     if num > max_num:
         max_num = num
         return max_num

nums = 4,2,1
print(find_max(nums))

 #num = max_num
 #max_num += 1
 #max_num = num
 #max_num += num