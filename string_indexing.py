#sting indexing program
#[start:end:step]

card_number = "123456789"

print(card_number[0])
print(card_number[-1])
print(card_number[0 : 5])
print(card_number[0:8:2])
print(card_number[::2])
print("---------------------")
#program to get 4 digit of card number

last_digits = card_number[5:]

print(last_digits)
print(f"last 4 digits of card number is {last_digits[-4:]}")
