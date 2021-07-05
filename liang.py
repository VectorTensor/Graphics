

# x1=input("Enter x1:")
# x2=input("Enter x2:")
# y1=input("Enter y1:")
# y2=input("Enter y2")
# xmin=input("xmin:")
# xmax=input("xmax:")
# ymin=input("ymin:")
# ymax=input("ymax:")
# x1=int(x1)
# x2=int(x2)
# y1=int(y1)
# y2=int(y2)
# xmin=int(xmin)
# xmax=int(xmax)
# ymin=int(ymin)
# ymax=int(ymax)
x1=10
x2=60
y1=10
y2=30
xmax=25
ymax=25
xmin=15
ymin=15

p=[0,0,0,0]
q=[0,0,0,0]
p[0]=-(x2-x1)
p[1]=x2-x1
p[2]=-(y2-y1)
p[3]=y2-y1
q[0]=x1-xmin 
q[1]=xmax-x1
q[2]=y1-ymin
q[3]=ymax-y1
r=[0]*4
for i in range (0,4):
    r[i]=q[i]/p[i]

a=[]
b=[]
for i in range(0,4):
    if (p[i]<0):
        a.append(r[i])
    else:
        b.append(r[i])
u1=max(a)
u2=min(b)
xx1=x1+u1*p[1]
yy1=y1+u1*p[3]
print(xx1)
print(yy1)
xx2=x1+u2*p[1]
yy2=y1+u2*p[3]
print(xx2)
print(yy2)
