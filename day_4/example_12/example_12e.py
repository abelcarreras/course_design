
def my_function(num):
    for i in range(num):
        if i > 5:
            raise Exception('My error message')


a = my_function(10)


print('Code continues')
