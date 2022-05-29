

for i in range(10):
    try:
        a = 1/(4-i)
    except ZeroDivisionError:
        a = 0
    print(a)

