# List of Lists: Function 

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats(list_of_universities):
    total_student_enroll = []
    total_fees = []
    for list in list_of_universities:
        total_student_enroll.append(list[1])
        total_fees.append(list[2])
    
    return total_student_enroll, total_fees


def mean(list): 
    return sum(list) / len(list)

def median(list): 
    if len(list) % 2 != 0: 
        index_of_item = len(list) // 2
        return list[index_of_item]
    else: 
        right_list_index = (list // 2) - 1
        left_list_index = (list // 2) + 1 
        return ((list[right_list_index] + list[left_list_index]) / 2)

total_student, total_fees = enrollment_stats(universities)
print(f"Total students: {sum(total_student): .2f}")
print(f"Total fees: ${sum(total_fees): .2f}")

print(f"Student mean: {mean(total_student): .2f}")
print(f"Student median: {median(total_student): .2f}")

print(f"Fees mean: ${mean(total_fees): .2f}")
print(f"Fees median: ${median(total_fees): .2f}")

