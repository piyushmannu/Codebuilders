user = int(input('enter a prime number'))
for i in range(1,user):
    if user-1 % i == 0:
        print("NOt prime")
        break
    else:
        print('prime')
        break
