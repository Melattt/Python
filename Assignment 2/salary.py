# A function that gives the median from the list
def median(lst):
    lst.sort()
    length = len(lst)
    # If even
    if length % 2 == 0: 
        return median([lst[length//2-1], lst[length//2]])
    # If odd  
    else:
        return lst[length//2]

# A function that gives the average by dividing the sum 
# of the list by the length of the list
def average(lst):
    avg = sum(lst) / len(lst)
    return avg


# A function that gives the difference between
# the highest and lowest salary
def gap(lst):
    lst.sort()
    length = len(lst)
    gp = lst[length-1]-lst[0]
    return gp

# Prompting the user to input and
# Split the given input when there is space(' ')
salary = input("Enter salaries separated with a space: ")
salary = salary.split(' ') 

list_ = []
# Appending them into the list
for sal in salary:
    list_.append(int(sal))

print(f'Median: {median(list_)}')
print(f'Average: {(average)(list_)}')
print(f'Gap: {gap(list_)}')