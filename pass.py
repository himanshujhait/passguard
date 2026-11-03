print(" =========welcome to password checker========= ")

x=(input("Enter your pass: "))
rate=0
op=""
l=len(x)

if (l<10):
    rate +=0
    op="suggestion...len contain minimum 15 digits"
elif (l>=10 and l<=12):
    rate+=1
    op="suggestion...len contain minimum 15 digits"
elif (l>=13 and l<=14):
    rate +=2
    op="suggestion...len contain minimum 15 digits"
else :
    rate +=3
    op="len    passed✅"




