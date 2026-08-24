num = -6
a = 10
b =30
age =25

print("positive" if num > 0 else "negative")

result = "even"if num % 2 == 0 else "odd"
print(result)

max = a if a>b else b
print(f"the maximum number is {max}")

status = "adult " if age >= 25 else " not adult"
print(f"the person is {status}")