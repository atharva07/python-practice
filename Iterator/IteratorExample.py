nums = [10, 20, 30]

it = iter(nums)
for i in range(len(nums)-1):
    print(next(it))

print(next(it))

# for num in it:
#     print(next(it))

gen = (x*x for x in range(5))

#print(next(gen))
#print(next(gen))