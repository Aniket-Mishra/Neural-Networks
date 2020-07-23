x1=int(input("enter x1"))
x2=int(input("enter x2"))
w11=int(input("enter w11"))
w21=int(input("enter w21"))

yin1=(1+(x1*w11+x2*w21))
print("Yin1 is", yin1)
y=1/(1+(2.71828**yin1))
print("y is ", y)
wi1=y*x1
wi2=y*x2
w11new=w11+wi1
w21new=w21+wi2

print("w11new is ", w11new)
print("w21new is ", w21new)

yin1new=(1+(x1*w11new+x2*w21new))
ynew=1/(1+(2.71828**yin1new))
print("value of y in second iteration is: ", ynew)