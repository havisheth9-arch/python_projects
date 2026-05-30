num = int(input("Enter a number: "))
cubes_sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    cubes_sum += digit ** 3
    temp = temp // 10

if num == cubes_sum:
    print(f"{num} is an Armstrong Number.")
else:
    print(f"{num} is not an Armstrong Number.")