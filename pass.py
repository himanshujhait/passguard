import string
print(" =========welcome to password checker========= ")

x=(input("Enter your pass: "))
pun=string.punctuation
rate=0
op=""
l=len(x)

if (l<10):
    rate -=1
    op="suggestion...len contain minimum 15 characters\n"

elif (l>=10 and l<=12):
    rate+=0
    op="suggestion...len contain minimum 15 characters\n"
elif (l>=13 and l<=14):
    rate +=2
    op="suggestion...len contain minimum 15 characters\n"
else :
    rate +=3
    op=op+"len    passed✅\n"

flag=False
flag1=False
flag2=False
flag4=False
for ch in x:
    if (ch.isupper()==True):
            flag=True
    if (ch.islower()==True):
            flag1=True
    if (ch.isnumeric()==True):
        flag2=True
    if (ch in pun):
        flag4=True

if (flag==True):
    op=op+"uppercase    passed✅\n"
    rate+=1
else :
    op=op+"Add atleast 1 uppercase \n"
    rate-=1
if (flag1==True):
    op=op+"lowercase    passed✅\n"
    rate+=1
else :
    op=op+"Add atleast 1 lowercase \n"
    rate-=1

if (flag2==True):
    op=op+"Numeric    passed✅\n"
    rate+=1
else :
    op=op+"Add atleast 1 number \n"
    rate-=1
if (flag4==True):
    op=op+"special_char    passed✅\n"
    rate+=1
else :
    op=op+"Add atleast 1 special character \n"
    rate-=1

flag3=False
with open("commonpass.txt","r") as f:
    content=f.readlines()
    for i in content:
        if i.strip()==x:
            flag3=True

if flag3==False:
    rate+=2
    op+="No_common_pass    passed✅ \n"

else:
    op+="create a unique password\n"
    rate-=2

flag5=False
for i in range (l-2):
    if(x[i]==x[i+1]==x[i+2]):
        flag5=True
        
if ((l==len(set(x)) or l==len(set(x))+1) and flag5==False):
    op+="No_repeatation    passed✅ \n"
    rate+=1

else:
    op=op+"Avoid repeatation in password \n"
    rate-=1




