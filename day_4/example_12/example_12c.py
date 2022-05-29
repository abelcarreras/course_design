
def my_function(num):
    for i in range(num):
        a = 1 / (4 - i)
        print(a)


try:
    a = my_function(10)
    print(a)
except ZeroDivisionError:
    print('Error happened')

print('Code continues')