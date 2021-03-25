''' If...else inside while Loops '''
n = 92
if n >= 12:
    while n >= 12:
        n -= 1
        print(n)
        if n == 22:
            break
else:
    while n < 12:
        n -= 1
        print(n)
        if n == 0:
            break
        # print('n==0')
