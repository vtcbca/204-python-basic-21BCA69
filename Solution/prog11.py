# check number is armstrong number or not.
b = int(input("Enter Number : "))
sum = 0
a = b
while a > 0:
    digit = a%10
    sum += digit ** 3
    a //= 10
if b == sum:
    print(b,"is An Armstrong Number")
else:
    print(b,"is Not An Armstrong Number")
