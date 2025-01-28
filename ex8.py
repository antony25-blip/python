employmentYears= int(input("enter the employment years: "))
employeeKids= int(input("enter number of kids: "))
leave= str(input("did you take any leave..?(yes/no): "))
if leave == "no" :
    totalAmount=400+(20*employmentYears)+(30*employeeKids)+100
else:
    totalAmount=400+(20*employmentYears)+(30*employeeKids)
print("total amount+"+str(totalAmount))
    