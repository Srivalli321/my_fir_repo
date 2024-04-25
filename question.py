num_1 = int(input("Enter number one! "))
num_2 = int(input("Enter number two! "))
num_3 = int(input("Enter number three! "))
num_4 = float(input("Enter number four! "))
print(f"whatis {num_1}*{num_2}?",str(num_3))
if num_1*num_2 == num_3:
    print(f"what is {num_1}*{num_2}",str(num_3))
    print("This is correct!")
    if num_1/num_2 == num_4:
        print(f"what is {num_1}/{num_2}",str(num_4))
        print("Thisnis correct!")
        if num_1*num_2 == num_3 and num_1/num_2 == num_4:
         print("you win the quiz")
else:
    print("this is wrong")