# print("Hello World")
#
# color = "Red"
# thing = "Liverpool FC"
# print(color + " is the color of " + thing)
#
# # print is a python function "the PRINT function"
# # whenever we use keywords or functions that are part of the language,
# # we're using the programming language's syntax to tell the computer what to do.
#
# print(4+5)
# print(9*7)
# print(-1/4)
# print(1/3)
# print
# # Use Python to calculate (((1+2)*3)/4)^5(((1+2)∗3)/4)
# print((((1+2)*3)/4)**5)


# def area_triange(base, height):
#     return base*height/2
#
# area_a = area_triange(5,4)
# area_b = area_triange(7,3)
#
# sum = area_a + area_b
# print("The sum of both area is: " + str(sum))


# multiple return values

# def convert_seconds(seconds):
#     hours = seconds // 3600
#     minutes = (seconds - hours * 3600) // 60
#     remaining_seconds = seconds - hours * 3600 - minutes * 60
#     return hours, minutes, remaining_seconds
#
# hours, minutes, seconds = convert_seconds(5000)
# print(hours, minutes, seconds)

# def goal_result(score):
#     reds = score + 1
#     blues = (score - reds) - 3
#     whites = score - reds + 1
#     return reds, blues, whites
#
# reds, blues, score = goal_result(10)
# print(reds, blues, score)




# def is_power_of_two(n):
#     if n == 0:
#         return False
#     while n != 1:
#         if n % 2 != 0:
#             return False
#         n = n / 2
#     return True
#
# print(is_power_of_two(0))  # Should be False
# print(is_power_of_two(1))  # Should be True
# print(is_power_of_two(8))  # Should be True
# print(is_power_of_two(9))  # Should be False

# def sum_divisors(n):
#   sum = 0
#   x = n // 2
#   y = 1
#   while (y <= x):
#       if (n % y == 0):
#           sum += y
#       y +=1
#   return sum
# print(sum_divisors(6)) # Should be 6 (sum of 1+2+3)
# print(sum_divisors(12)) # Should be 16 (sum of 1+2+3+4+6)



#Boolean
# def is_positive(number):
#     if number > 0:
#         return True
#
# def hint_username(username):
#     if len(username) < 3:
#         print("Invalid username. Must be at least 3 characters lone")

# def lucky_number(name):
#     number = len(name) * 9
#     print("Hello " + name + ". Your lucky number is " + str(number))
#
# lucky_number("John")
# lucky_number("Cameron")


# def print_monthly_expense(month, hours):
#     monthly_cost = float(hours) * 0.65
#     print("In " + month + " we spent: " + str(monthly_cost))
#
# print_monthly_expense("June", 243)
# print_monthly_expense("July", 325)
# print_monthly_expense("August", 298)


# def convert_distance(miles):
#     km = miles * 1.6
#     print("hello " + str(km))
#
# convert_distance(55)
















