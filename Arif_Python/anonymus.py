# numbers = [1,2,3,4]

# # returns the square of a number
# def square(number):
#   return number * number

# # apply square() to each item of the numbers list
# squared_numbers = map(square, numbers)

# # converting to list for printing
# result = list(squared_numbers)
# print(result) 



# # returns True if the argument passed is even
# def check_even(number):
#     if number % 2 == 0:
#           return True  
#     return False

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # if an element passed to check_even() returns True, select it
# even_numbers_iterator = filter(check_even, numbers)

# # converting to list
# even_numbers = list(even_numbers_iterator)
# print(even_numbers)

# # Output: [2, 4, 6, 8, 10]

# from functools import reduce
# people = (1,2,3,4,5)
# multi = reduce (lambda b,d: b*d , people)
# print (multi)

# rafna_rafeek= lambda name :print ("Hey there,", name)
# rafna_rafeek("Rafna")

# def check_even(number):
#     if number % 2 == 0:
#         return True
#     return False 

# numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13]

# even_numbers_iterator = filter (check_even, numbers)

# even_number = list (even_numbers_iterator)
# print (even_number)

# def check_odd(number):
#     if number % 2 != 0 :
#         return True 
#     return False 
# numbers = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)
# odd_num_iter =filter (check_odd, numbers)

# odd_number = list (odd_num_iter)
# print (odd_number)

# number = [3,6,9,4,8]
# def find_sqr (number):
#     return number*number
# sqr_number = map (find_sqr,number)
# result = list (sqr_number)
# print (result)

# number = [6,4,2,8]
# def sqr (number):
#     return number*number 
# squared_num = map (sqr,number)
# result =list (squared_num)
# print (result)



