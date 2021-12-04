def f(a,i):return sum(int(l[i])*2-1 for l in a)
*a,=open('data.txt')
b=[z for z in a]
for i in range(12):
 a=[z for z in a if z[i]=='01'[0<=f(a,i)]] if len(a)-1 else a
 b=[z for z in b if z[i]=='10'[0<=f(b,i)]] if len(b)-1 else b
print(int(a[0],2)*int(b[0],2))

def f(a,i):return sum(int(l[i])*2-1 for l in a)
def g(a,i,c):return [z for z in a if z[i]=='10'[c]] if len(a)-1 else a
*a,=open('data.txt')
b=[z for z in a]
for i in range(12):
 a=g(a,i,0>f(a,i))
 b=g(b,i,0<=f(b,i))
print(int(a[0],2)*int(b[0],2))

g=lambda a,i,c:[z for z in a if z[i]==c[0>sum(int(l[i])*2-1 for l in a)]] if len(a)-1 else a
*a,=open('data.txt')
*b,=a
for i in range(12):
 a=g(a,i,'10')
 b=g(b,i,'01')
print(int(a[0],2)*int(b[0],2))

g=lambda a,i,c:[z for z in a if z[i]==c[0>sum(int(l[i])*2-1 for l in a)]] if len(a)-1 else a
*a,=open('data.txt')
b=a
for i in range(12):
 a,b=g(a,i,'10'),g(b,i,'01')
print(int(a[0],2)*int(b[0],2))

g=lambda a,c,i=0:int(a[0],2) if i==12 else g([z for z in a if z[i]==c[0>sum(int(l[i])*2-1 for l in a)]] if len(a)-1 else a,c,i+1)
print(g(a:=[*open('data.txt')],'10')*g(a,'01'))

print((g:=lambda a,c,i=0:int(a[0],2) if i==12 else g([z for z in a if z[i]==c[0>sum(int(l[i])*2-1 for l in a)]] if len(a)-1 else a,c,i+1))(a:=[*open('data.txt')],'10')*g(a,'01'))

print((g:=lambda a,c,i=0:int(a[0],2) if i==12else g([z for z in a if z[i]==c[0>sum(int(l[i])*2-1for l in a)]] if len(a)-1else a,c,i+1))(a:=[*open('data.txt')],'10')*g(a,'01'))
