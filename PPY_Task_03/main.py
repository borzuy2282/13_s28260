import math
#Task 7
from modules import square_generator as sg

#Task 1
list1 = [i ** 2 for i in range(1, 11)]

print(list1)


#Task 2

def list_square_creator(start, end):
    return [i ** 2 for i in range(start, end)]

print(list_square_creator(1, 11))


#Task 3

# class SquareGenerator:
#     def list_square_creating(start, end):
#
#         #Task 5
#         if start <= end:
#             return [i**2 for i in range(start, end)]
#         else:
#             print('Your start is greater than end!')
#             return []

print(sg.SquareGenerator.list_square_creating(1, 11))


#Task 4

list4 = sg.SquareGenerator.list_square_creating(1, 11)
for x in range(len(list4)):
    list4[x] = math.sqrt(list4[x])
print(list4)

#Task 8
class CubicGenerator(sg.SquareGenerator):
    def list_square_creating(start, end):
        if start <= end:
            return [i ** 3 for i in range(start, end)]
        else:
            print('Your start is greater than end!')
            return []

print(CubicGenerator.list_square_creating(1, 11))

