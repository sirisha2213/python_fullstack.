Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s={1,2,3,4,5}
s[0]
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    s[0]
TypeError: 'set' object is not subscriptable
s[1:2]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    s[1:2]
TypeError: 'set' object is not subscriptable
s
{1, 2, 3, 4, 5}
s
{1, 2, 3, 4, 5}
s.add(1)
s.add(34.5)
s
{1, 2, 3, 4, 5, 34.5}
{1, 2, 3, 4, 5, 34.5}
{1, 34.5, 3, 2, 4, 5}
s.add("string")
s
{1, 2, 3, 4, 5, 34.5, 'string'}
s.add((1,2,3))
s
{1, 2, 3, 4, 5, 34.5, (1, 2, 3), 'string'}
s.add(2+3j)
s
{1, 2, 3, 4, 5, (2+3j), 'string', 34.5, (1, 2, 3)}
s.add(True)
s
{1, 2, 3, 4, 5, (2+3j), 'string', 34.5, (1, 2, 3)}
>>> s.add(False)
>>> s
{False, 1, 2, 3, 4, 5, (2+3j), 'string', 34.5, (1, 2, 3)}
>>> s.add(True)
>>> s
{False, 1, 2, 3, 4, 5, (2+3j), 'string', 34.5, (1, 2, 3)}
>>> s.add([1,2,3])
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    s.add([1,2,3])
TypeError: unhashable type: 'list'
>>> s.add({1,2,3})
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    s.add({1,2,3})
TypeError: unhashable type: 'set'
s.add({1:1,2:2,3:3})
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    s.add({1:1,2:2,3:3})
TypeError: unhashable type: 'dict'
s
{False, 1, 2, 3, 4, 5, (2+3j), 'string', 34.5, (1, 2, 3)}
s
{False, 1, 2, 3, 4, 5, (2+3j), 'string', 34.5, (1, 2, 3)}
s
{False, 1, 2, 3, 4, 5, (2+3j), 'string', 34.5, (1, 2, 3)}
s.add(40)
s.pop()
False
s.pop()
1
s
{2, 3, 4, 5, (2+3j), 'string', 34.5, 40, (1, 2, 3)}
s.remove(4)
s
{2, 3, 5, (2+3j), 'string', 34.5, 40, (1, 2, 3)}
s.remove(4)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    s.remove(4)
KeyError: 4
s.discard(4)
s
{2, 3, 5, (2+3j), 'string', 34.5, 40, (1, 2, 3)}
s.clear()
s
set()
l=[]
t=()
d={}
s=set()
s
set()
{1,2}+{3,4}
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    {1,2}+{3,4}
TypeError: unsupported operand type(s) for +: 'set' and 'set'
{1,2}*2
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    {1,2}*2
TypeError: unsupported operand type(s) for *: 'set' and 'int'
[1,2]*2
[1, 2, 1, 2]
s
set()
s={1,2,3,4,5}
2 in s
True
6 not in s
True
a={1,2,3,4,19,20,34}
a
{1, 2, 3, 4, 34, 19, 20}
guys = {'saaketh','sapnil','nikil','vardhan','abhinandhan'}
guys
{'sapnil', 'nikil', 'abhinandhan', 'vardhan', 'saaketh'}
online = {'saaketh','poojitha','pavan'}
online
{'poojitha', 'pavan', 'saaketh'}
girls = {'varsha','poojitha','bhavana','madhupriya'}
guys | girls
{'bhavana', 'sapnil', 'nikil', 'abhinandhan', 'varsha', 'poojitha', 'madhupriya', 'vardhan', 'saaketh'}
guys.union(girls)
{'bhavana', 'sapnil', 'nikil', 'abhinandhan', 'varsha', 'poojitha', 'madhupriya', 'vardhan', 'saaketh'}
girls & guys
set()
girls.isdisjoint(guys)
True
guys & online
{'saaketh'}
girls.isdisjonit(guys)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    girls.isdisjonit(guys)
AttributeError: 'set' object has no attribute 'isdisjonit'. Did you mean: 'isdisjoint'?
girls.isdisjoint(online)

False
girls
{'varsha', 'poojitha', 'bhavana', 'madhupriya'}
online
{'poojitha', 'pavan', 'saaketh'}
girls - online
{'varsha', 'bhavana', 'madhupriya'}
girls ^ online
{'bhavana', 'pavan', 'varsha', 'madhupriya', 'saaketh'}
guys ^ online
{'sapnil', 'nikil', 'abhinandhan', 'pavan', 'poojitha', 'vardhan'}
girls
{'varsha', 'poojitha', 'bhavana', 'madhupriya'}
girls.update({'meghana','sanjana','sirisha'})
girls
{'varsha', 'sanjana', 'poojitha', 'bhavana', 'madhupriya', 'meghana', 'sirisha'}
guys
{'sapnil', 'nikil', 'abhinandhan', 'vardhan', 'saaketh'}
online
{'poojitha', 'pavan', 'saaketh'}
guys.intersection(online)
{'saaketh'}
guys
{'sapnil', 'nikil', 'abhinandhan', 'vardhan', 'saaketh'}
online
{'poojitha', 'pavan', 'saaketh'}
guys.intersection_update(online)
guys
{'saaketh'}
onlinee
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    onlinee
NameError: name 'onlinee' is not defined. Did you mean: 'online'?
online
{'poojitha', 'pavan', 'saaketh'}
a={1,2,3,4,5,6,7,8}
b={7,8,9,1,10,11,12}
a
{1, 2, 3, 4, 5, 6, 7, 8}
b
{1, 7, 8, 9, 10, 11, 12}
a.intersection(b)
{8, 1, 7}
a
{1, 2, 3, 4, 5, 6, 7, 8}
b
{1, 7, 8, 9, 10, 11, 12}
a.intersection_update(b)
a
{8, 1, 7}
b
{1, 7, 8, 9, 10, 11, 12}
s={1,2,3,4}
#{}{1}{2}{3}{4}{1,2}{2,3}{3,4}{4,1}{1,3}{2,4}{1,2,3}{2,3,4},{4,1,2}

{1,2}.issubset(s)
True
{6,10}.issubset(s)
False
s.issuperset({1})
True
s.issuperset({10,11})
False
s.issuperset({1,2,4,3})
True
a
{8, 1, 7}
b
{1, 7, 8, 9, 10, 11, 12}
len(b)
7
max(b)
12
min(b)
1
sorted(b)
[1, 7, 8, 9, 10, 11, 12]
sum(b)
58
a={1,2,3,4}
id(a)
2577373027840
b=a
id(b)
2577373027840
b.add(20)
b
{1, 2, 3, 4, 20}
a
{1, 2, 3, 4, 20}
c=a.copy()
id(c)
2577368383776
c.add(22)
c
{1, 2, 3, 4, 20, 22}
a
{1, 2, 3, 4, 20}
