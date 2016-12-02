import math
print('Please enter a date: ')
m = int(input('Month: '))


d = int(input('Day: '))

C = int(input('Enter the first two digits of the year: '))
D = int(input('Enter the last two digits of the year: '))
if m == 'January' or m == 'February':
    D -= 1

weekDay = d + math.floor(((m + 1) * 26) / 10)+ D + math.floor(D / 4) + math.floor(C / 4) - 2 * C
remainder = weekDay % 7

if m == 3:
    m = 'March'
elif m == 4:
    m = 'April'
elif m == 5:
    m = 'May'
elif m == 6:
    m = 'June'
elif m == 7:
    m = 'July'
elif m == 8:
    m = 'August'
elif m == 9:
    m = 'September'
elif m == 10:
    m = 'October'
elif m == 11:
    m = 'November'
elif m == 12:
    m = 'December'
elif m == 13:
    m = 'January'
elif m == 14:
    m = 'Fenruary'

C = str(C)
D = str(D)

if remainder < 0:
    remainder += 7

elif remainder == 0:
    print('Your date was Saturday',m,',',d,',',C + D)
elif remainder == 1:
    print('Your date was Sunday',m,',',d,',',C + D)
elif remainder == 2:
    print('Your date was Monday',m,',',d,',',C + D)
elif remainder == 3:
    print('Your date was Tuesday',m,',',d,',',C + D)
elif remainder == 4:
    print('Your date was Wednesday',m,',',d,',',C + D)
elif remainder == 5:
    print('Your date was Thursday',m,',',d,',',C + D)
elif remainder == 6:
    print('Your date was Friday',m,',',d,',',C + D)