emp_salary = int(input("Enter employe yearly salary = "))
if emp_salary <= 67000:
    tax_per1 = (emp_salary *24)/100
    print("Didecte the tax from the empsalary! ",str(tax_per1))
elif emp_salary < 97000:
    tax_per2 = (emp_salary *31)/100
    print("Dedecte the tax from the empsalary! ", str(tax_per2))
else:
    tax_per3 = (emp_salary*34)/100
    print("Didecte the tax from the empsalary",str(tax_per3))