student={"Name":"Maya","Age":21,"Branch":"CSE","Reg no":256}
for x in student:
    print(x)
    print("Values are: ")
    print(student[x])
    print("Key and values are: ")
    for x,y in student.items():
        print(x,y)
