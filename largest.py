fi_num = int(input("Enter first number = "))
s_num = int(input("Enter second number = "))
t_num = int(input("Enter third number = "))
fo_num = int(input("Enter fourth number = "))
if fi_num>=s_num and fi_num>=t_num and fi_num>=fo_num:
  print(f"The largest number is ={fi_num }")
elif  s_num>=t_num and s_num>=fo_num:
  print(f"the largest number is ={s_num}")
elif t_num>=fi_num and t_num>=fo_num:
  print(f"The largest number is ={t_num}")
else:
  print(f"The largest number is ={fo_num}")
#elif s_num>fi_num and s_num>t_num and s_num>fi_num:
     #if t_num>fo_num:
    #    n = {fi_num,s_num,t_num,fo_num}
     #   print("the bigest number is ", str(n))
    # else:
       # print("some thing is wrong")
