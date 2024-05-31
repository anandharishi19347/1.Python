class MultipleFunction():
    def Subfields():
        print("Sub-fields in AI are:")
        Lists=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        for temp in Lists:
            print(temp)

    def OddEven():
        num=int(input("enter a number:"))
        if((num%2)==0):
            print("52452 is even number")
        else:
            print("is not even number")       

    def Eligible():
        gender=input("your gender:")
        age=int(input("your age:"))
        if age>=18 and gender=='female':
            print("Eligible")
        elif age>21 and gender=='male':
            print("Eligible")
        else:
            print("Not ELIGIBLE")   

    def percentage():
        subject1=int(input("subject1="))
        subject2=int(input("subject2="))
        subject3=int(input("subject3="))
        subject4=int(input("subject4="))
        subject5=int(input("subject5="))   
        add=(subject1 + subject2 + subject3 + subject4 + subject5)
        print("Total:",add)
        avg=add/5
        percentage=(add*100)/500
        print("percentage:",percentage)

    def triangle():
        height=int(input("Height:"))
        breadth=int(input("Breadth:"))
        A_F=input("Area formula:")
        A_F=(32*34)/2
        print("Area of Triangle:",A_F)

        height1=int(input("Height1:"))
        height2=int(input("Height2:"))
        breadth3=int(input("Breadth:"))
        P_F=input("perimeter formula:")
        P_F=2+4+4
        print("perimeter of triangle:",P_F)