h=d=a=0
for line in open('data.txt'):
    direction, val = line.split(' ')
    val = int(val)
    if direction=='forward':
        h+=val
        d+=val*a
    else:
        a+={'up':-1,'down':1}[direction]*val
print(h*d)

h=d=a=0
for line in open('data.txt'):
    direction, val = line.split(' ')
    val = int(val)
    u={'up':-1,'down':1,'forward':0}[direction]
    f=abs(abs(u)-1)
    h+=val*f
    d+=val*a*f
    a+=u*val
print(h*d)

h=d=a=0
for line in open('data.txt'):
    i,v=line.split(' ')
    v=int(v)
    u={'up':-1,'down':1,'forward':0}[i]
    f=abs(abs(u)-1)
    h+=v*f
    d+=v*a*f
    a+=v*u
print(h*d)

h=d=a=0
for line in open('data.txt'):
    v=int(line[-2])
    u={'u':-1,'d':1,'f':0}[line[0]]
    f=abs(abs(u)-1)
    h+=v*f
    d+=v*a*f
    a+=v*u
print(h*d)

h=d=a=0
z=[(int(l[-2]),u:={'u':-1,'d':1,'f':0}[l[0]],abs(abs(u)-1))for l in open('data.txt')]
for v,u,f in z:
    h+=v*f
    d+=v*a*f
    a+=v*u
print(h*d)

h=d=a=0
z=[(int(l[-2]),*{'u':(-1,0),'d':(1,0),'f':(0,1)}[l[0]])for l in open('data.txt')]
for v,u,f in z:
    h+=v*f
    d+=v*a*f
    a+=v*u
print(h*d)

h=d=a=0
for l in open('data.txt'):
 v,u,f=(int(l[-2]),*{'u':(-1,0),'d':(1,0),'f':(0,1)}[l[0]])
 h+=v*f
 d+=v*f*a
 a+=v*u
print(h*d)

h=d=a=0
for l in open('data.txt'):
 v=int(l[-2])
 u,f={'u':(-v,0),'d':(v,0),'f':(0,v)}[l[0]]
 h,d,a=h+f,d+f*a,a+u
print(h*d)
