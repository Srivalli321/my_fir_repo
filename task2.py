text = "Python programming is powerful and versatile"
print()
print(text[6:18],"\n")

text_1 = text.split()

print(text_1 , "\n")

print('-'.join(text_1),"\n")

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
squers = []
for s in numbers:
    s =s**2
    squers.append(s)
print(f"squers list is = {squers}")