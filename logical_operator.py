#AND,OR, NOT logical operators
temp = 40
is_raining = True
it_sunny = False

if temp >20 and temp <30 and is_raining:
    print("cancel the outdoor event")

else:
    print("the outdoor event will go on")


if temp >20 and it_sunny:
    print("the outdoor event will go on")
else:
    print("cancel the outdoor event its sunny")

if not is_raining:
    print("the outdoor event will go on")
elif it_sunny:
    print("the outdoor event will go on")   