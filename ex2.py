print('Введите трехзначное число: ')
n = int(input())
m = (n % 10) + ((n % 100) // 10) + (n //100)
print(m)