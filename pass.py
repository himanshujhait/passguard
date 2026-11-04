print(" =========welcome to password checker========= ")

x=(input("Enter your pass: "))
rate=0
op=""
l=len(x)

if (l<10):
    rate +=0
    op="suggestion...len contain minimum 15 characters "

elif (l>=10 and l<=12):
    rate+=1
    op="suggestion...len contain minimum 15 characters\n"
elif (l>=13 and l<=14):
    rate +=2
    op="suggestion...len contain minimum 15 characters\n"
else :
    rate +=3
    op=op+"len    passed✅\n"

flag =False
for ch in x:
    if (ch.isupper()==True):
        flag=True

if (flag==True):
    rate+=1
    op=op+"uppercase    passed✅\n"
else :
    op=op+"Add atleast 1 uppercase\n"






