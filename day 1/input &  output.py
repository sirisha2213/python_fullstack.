Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
 product_name = input("Enter the product name: ")
KeyboardInterrupt
a= int(input("Enter the integer: "))
Enter the integer: 12
b= float(input("Enter the float: "))
Enter the float: sdzdrftghbjnk
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    b= float(input("Enter the float: "))
ValueError: could not convert string to float: 'sdzdrftghbjnk'
b= float(input("Enter the float: "))
Enter the float: 12.3
s = input("Enter the str: ")
Enter the str: python
s
'python'
s=varsha sanjana sravanthi komali meghana
SyntaxError: invalid syntax
names= input("Enter the names: ")
Enter the names: varsha sanjana sravanthi komali meghana
names
'varsha sanjana sravanthi komali meghana'
'
names
'varsha sanjana sravanthi komali meghana'
names.split()
['varsha', 'sanjana', 'sravanthi', 'komali', 'meghana']
n=1,2,3,4,5
n.split(',')
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    n.split(',')
AttributeError: 'tuple' object has no attribute 'split'
n='1,2,3,4,5'
n.split(',')
['1', '2', '3', '4', '5']
names = input("Enter the names: ").split()
Enter the names: varsha sanjana sravanthi komali meghana
names
['varsha', 'sanjana', 'sravanthi', 'komali', 'meghana']
rollno = input().split()
1 7 8 9 5 4
rollno
['1', '7', '8', '9', '5', '4']
k=map(int,rollno)
k
<map object at 0x000001E20D4BA230>
k=list(map(int,rollno))
k
[1, 7, 8, 9, 5, 4]
k=list(map(int,input().split()))
1 6 5 4 3 89 34 5
k
[1, 6, 5, 4, 3, 89, 34, 5]
k=list(map(float,input().split()))
4 2 4 6.5 4.2
k
[4.0, 2.0, 4.0, 6.5, 4.2]
k=input().split()
gfh fghkj gfhj k
k
['gfh', 'fghkj', 'gfhj', 'k']
k=tuple(map(int,input().split()))
1 2 3 4
k
(1, 2, 3, 4)
k=tuple(map(float,input().split()))
12.3 45.6 78.9
k
(12.3, 45.6, 78.9)
k=tuple(input().split())
dfgh gfhjk gfhj k
l
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    l
NameError: name 'l' is not defined
k
('dfgh', 'gfhjk', 'gfhj', 'k')
k=set(map(int,input().split()))
1 1 1 1 16 6 7 8 9 5
k
{1, 5, 6, 7, 8, 9, 16}
k=set(map(float,input().split()))
1.1 2.3 4.5 6.7
k
{1.1, 2.3, 4.5, 6.7}
k=set(input().split())
fdghj fghjk gfhj 
k
{'fghjk', 'fdghj', 'gfhj'}
k=eval(input())
{12:"dgfh",13:"fdgh"}
k
{12: 'dgfh', 13: 'fdgh'}
a,b,c = 10,20,30
a
10
b
20
c
30
a=10,20,30
a
(10, 20, 30)
username,password = input().split()
... varsha 123@
... username
... 'varsha'
... password
... '123@'
... >>> a=10
... >>> b=20.3
... >>> c="python"
... >>> print("a=",a,"b=",b,"c=",c)
... a= 10 b= 20.3 c= python
... >>> print("a=",a,"b=",b,"c=",c,sep='')
... a=10b=20.3c=python
... >>> print("a=",a,"b=",b,"c=",c,sep='@')
... a=@10@b=@20.3@c=@python
... >>> print("a=",a,"b=",b,"c=",c,sep='@',end='--------')
... a=@10@b=@20.3@c=@python--------
... print(f"a={a} b={b} c={c}")
... a=10 b=20.3 c=python
... print(f"a={a}\tb={b}\tc={c}")
... a=10	b=20.3	c=python
... print(f"a={a}\nb={b}\nc={c}")
... a=10
... b=20.3
... c=python
... print("a= %d\nb= %f\nc=%s"%(a,b,c))
... a= 10
... b= 20.300000
... c=python
... print("a={}\nb={}\nc={}".format(a,b,c))
... a=10
... b=20.3
... c=python
... print("a={}\nb={}\nc={}".format(b,a,c))
... a=20.3
... b=10
... c=python
... print("a={0}\nb={2}\nc={1}".format(a,b,c))
... a=10
... b=python
