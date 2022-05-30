
class CustomError(Exception):
    def __init__(self, message, index):
        self.message = message
        self.index = index

    def __str__(self):
        return 'Custom Error : {}'.format(self.message)



def my_function(num):
    for i in range(num):
        if i > 5:
            raise CustomError('My error message', i)


try:
    a = my_function(10)

except CustomError as e:
    print('Error captured in index {}'.format(e.index))


print('Code continues')
