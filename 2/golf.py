h=d=a=0
z=[(int(l[-2]),*{'u':(-1,0),'d':(1,0),'f':(0,1)}[l[0]])for l in open('data.txt')]
for v,u,f in z:
 h+=v*f
 d+=v*f*a
 a+=v*u
print(h*d)
