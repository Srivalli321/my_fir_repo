my_list_int = [ *range(1,16) ]
print(my_list_int)
list_1 =[]
list_2 = []
list_3 = []
list_4 =[]
for number in my_list_int:
    if number % 3 == 0:
        #list_1.append(number)
        #print(list_1)
        if number % 5 == 0:
          print("FizzBuzz",str(number))
        else:
             print("Fizz",str(number))
          #list_2.append(number)
          #print(list_2)
    elif (number % 5)==0:
           print("Buzz",str(number))
          #list_3.append(number)
          #print(list_3)
    else:
     print(number)
          
    