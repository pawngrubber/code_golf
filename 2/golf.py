h=d=a=0
for l in open('data.txt'):
 v=int(l[-2])
 u,f={'u':(-v,0),'d':(v,0),'f':(0,v)}[l[0]]
 h,d,a=h+f,d+f*a,a+u
print(h*d)
