print('Введите длину шоколадки')
n = int(input())
print('Введите ширину шоколадки')
m = int(input())

print('Сколько кусочков вы хотите отломить?')
k = int(input())

if (k % n == 0) or (k % m == 0):
    print('yes')
else:
    print('no')