#Question 1
#Write a function to print "hello_USERNAME!" USERNAME is the input of the #function. The first line of the code has been defined as below. def #hello_name(user_name):

username = "hello_USERNAME!"
print(username)

#Question 2
#Write a python function, first_odds that prints the odd numbers from 1-#100 and returns nothing.

odd_numbers = list(range(1,100))
print(odd_numbers)

first_odds =(range(1,3,100))
print(first_odds)

first_odds = (range())
print(first_odds)

#Question 3
#Please write a Python function, max_num_in_list, to return the max #number of a given list. The first line of the code has been defined as #below.
   Digits = [3,5,7,9]
   min(digits)
   3
   max(digits
   9
   sum(digits)
   24

    def max_num_in_list(a_list):
example_list = [8, 10, 20]
result = max_num_in_list(example_list)
print(f"The maximum number in the list is: {result}")


#Question 4
#Write a function to return if the given year is a leap year. A leap year #is divisible by 4, but not divisible by 100, unless it is also divisible #by 400. The return should be boolean Type (true/false).

def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

year = int(input("Enter the year: ")) 
print(leap_year(year))

True

#Question 5
#Write a function to check to see if all numbers in list are consecutive #numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but #[1,2,4,5] are not consecutive numbers. The return should be boolean #Type.

def are_consecutive_numbers(lst):
    # Check if the list is empty
    if not lst:
        return False

    # Sort the list
    sorted_lst = sorted(lst)

    # Check if the difference between consecutive elements is 1
    for i in range(len(sorted_lst) - 1):
        if sorted_lst[i] + 1 != sorted_lst[i + 1]:
            return False

    return True

# Example usage:
list1 = [2, 3, 4, 5, 6, 7]
list2 = [1, 2, 4, 5]

result = are_consecutive_numbers(list1)
print(result)

True
