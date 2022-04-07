number = int(input('enter a number:'))
if number % 2 == 1:
    print(f'{number} is a odd number')
elif number % 2 == 0:
    print(f'{number} is a even number')
else:
    print("this number isnt even or odd")