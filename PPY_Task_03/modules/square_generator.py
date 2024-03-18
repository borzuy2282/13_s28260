#Task 6
class SquareGenerator:
    def list_square_creating(start, end):

        #Task 5
        if start > end:
            print('Your start is greater than end!')
            return []

        else:
            return [i ** 2 for i in range(start, end)]