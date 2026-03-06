Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
d = {'saaketh':23,'praveen':10,'abhinandhan':16,'varsha':11}
d
{'saaketh': 23, 'praveen': 10, 'abhinandhan': 16, 'varsha': 11}
d.keys()
dict_keys(['saaketh', 'praveen', 'abhinandhan', 'varsha'])
d.values()
dict_values([23, 10, 16, 11])
d
{'saaketh': 23, 'praveen': 10, 'abhinandhan': 16, 'varsha': 11}
d.items()
dict_items([('saaketh', 23), ('praveen', 10), ('abhinandhan', 16), ('varsha', 11)])
e={}
e=dict()
e
{}
d['saaketh']
23
d['varsha']
11
d['sravanthi']
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    d['sravanthi']
KeyError: 'sravanthi'
d.get('sravanthi')
d.get('saaketh')
23
d.get('saaketh',"name is not present")
23
d.get('sravanthi',"name is not present")
'name is not present'
d
{'saaketh': 23, 'praveen': 10, 'abhinandhan': 16, 'varsha': 11}
d['praveen']=15
d
{'saaketh': 23, 'praveen': 15, 'abhinandhan': 16, 'varsha': 11}
id(d)
2082294572288
d['varsha']=18
d
{'saaketh': 23, 'praveen': 15, 'abhinandhan': 16, 'varsha': 18}
id(d)
2082294572288
d
{'saaketh': 23, 'praveen': 15, 'abhinandhan': 16, 'varsha': 18}
d['sajitha']=12
d
{'saaketh': 23, 'praveen': 15, 'abhinandhan': 16, 'varsha': 18, 'sajitha': 12}
d['bhavana']=10
d
{'saaketh': 23, 'praveen': 15, 'abhinandhan': 16, 'varsha': 18, 'sajitha': 12, 'bhavana': 10}
d.update({'rohid':0,'pavan':10})
d
{'saaketh': 23, 'praveen': 15, 'abhinandhan': 16, 'varsha': 18, 'sajitha': 12, 'bhavana': 10, 'rohid': 0, 'pavan': 10}
d.pop('pavan')
10
d
{'saaketh': 23, 'praveen': 15, 'abhinandhan': 16, 'varsha': 18, 'sajitha': 12, 'bhavana': 10, 'rohid': 0}
d.popitem()
('rohid', 0)
d.popitem()

('bhavana', 10)
d.popitem()

('sajitha', 12)
d.popitem()

('varsha', 18)
d
{'saaketh': 23, 'praveen': 15, 'abhinandhan': 16}
del d['saaketh']
d
{'praveen': 15, 'abhinandhan': 16}
d.clear()
d
{}
d={'praveen': 15, 'abhinandhan': 16}
d
{'praveen': 15, 'abhinandhan': 16}
d.get('saaket')
d
{'praveen': 15, 'abhinandhan': 16}
d.setdefault('saaket',0)
0
d
{'praveen': 15, 'abhinandhan': 16, 'saaket': 0}
\
d.setdefault('praveen',0)
15
d
{'praveen': 15, 'abhinandhan': 16, 'saaket': 0}
d.clear()
d
{}
d[1]='int'
d
{1: 'int'}
d[12.3]='float'
d
{1: 'int', 12.3: 'float'}
d['string']='string'
d
{1: 'int', 12.3: 'float', 'string': 'string'}
d[2+3j]='complex'
d
{1: 'int', 12.3: 'float', 'string': 'string', (2+3j): 'complex'}
d[[1,2,3]]='list'
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    d[[1,2,3]]='list'
TypeError: unhashable type: 'list'
\
d
{1: 'int', 12.3: 'float', 'string': 'string', (2+3j): 'complex'}
d[(1,2,3)]='tuple'
d
{1: 'int', 12.3: 'float', 'string': 'string', (2+3j): 'complex', (1, 2, 3): 'tuple'}
d[{1,2,3}]='set'
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    d[{1,2,3}]='set'
TypeError: unhashable type: 'set'
d
{1: 'int', 12.3: 'float', 'string': 'string', (2+3j): 'complex', (1, 2, 3): 'tuple'}
d[{1:1,2:2}]='dict'
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    d[{1:1,2:2}]='dict'
TypeError: unhashable type: 'dict'
d
{1: 'int', 12.3: 'float', 'string': 'string', (2+3j): 'complex', (1, 2, 3): 'tuple'}
d.clear
<built-in method clear of dict object at 0x000001E4D2C89140>
d
{1: 'int', 12.3: 'float', 'string': 'string', (2+3j): 'complex', (1, 2, 3): 'tuple'}
d.clear()
d
{}
>>> d['val1']=1
>>> d
{'val1': 1}
>>> d['val2']=12.3
... 
>>> d
{'val1': 1, 'val2': 12.3}
>>> d['val2']="string"
... 
>>> d
{'val1': 1, 'val2': 'string'}
>>> d['val2']=[1,2,3,4]
>>> d
{'val1': 1, 'val2': [1, 2, 3, 4]}
