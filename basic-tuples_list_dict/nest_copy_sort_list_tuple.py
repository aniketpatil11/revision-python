# Nest copy sort tuples, lists: 

data = ((1, 2), (3, 4))

for i in data: 
    print(sum(i))

numbers = [4, 3, 2, 1]
copy_numbers = numbers[:]

numbers.sort()
print(f"numbers: {numbers}")
print(f"copy numbers: {copy_numbers}")