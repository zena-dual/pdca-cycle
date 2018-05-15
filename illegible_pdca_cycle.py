import os,time;s=5;t=s-1;v=s-2;u=[];b=str;r=range(s);c=' '*v;p=c.join('PDCA')+c;m='{0[';n=']}';o=n+m;q=o.join;[u.append(m+(q(b(x)for x in r) if i==0 else q(b(t*3-x)for x in r) if i==t else b(t*4-i)+n+'{1}'*v+m+b(t+i))+n)for i in r]
while 1:os.system('clear');[print(u[i].format(p,' '))for i in r];p=p[1:]+p[0];time.sleep(.1)
