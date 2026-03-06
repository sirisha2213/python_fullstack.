Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> python Programming
... pythonpythonpythonpythonpythonpythonpython
... '*'*50
... '**************************************************'
... names = 'SirishaVarshaAchyuthSaakethSapnil'
... names[0]
... 'S'
... names[-1]
... 'l'
... names[8]
... 'a'
... names[7]
... 
... 'V'
... names = 'SirishaVarshaAchyuthSaakethSapnil'
... 
... #s[start,stop+1,step]
... names[0,7,1]
... Traceback (most recent call last):
...   File "<pyshell#8>", line 1, in <module>
...     names[0,7,1]
... TypeError: string indices must be integers, not 'tuple'
... names[0:7:1]
... 'Sirisha'
... names[:7]
... 'Sirisha'
... names
... 'SirishaVarshaAchyuthSaakethSapnil'
... names[7:13]
... 'Varsha'
... names[13:20]
... 'Achyuth'
... names[20:27]
... 'Saaketh'
... names[27:]
... 'Sapnil'
... names[::-1]
'linpaShtekaaShtuyhcAahsraVahsiriS'
names
'SirishaVarshaAchyuthSaakethSapnil'
names[-7::-1]
'htekaaShtuyhcAahsraVahsiriS'
names[7::-1]
'VahsiriS'
names[6::-1]
'ahsiriS'
names[12:6:-1]
'ahsraV'
names[-1:-7:-1]
'linpaS'
names[-6:]
'Sapnil'
names
'SirishaVarshaAchyuthSaakethSapnil'
'Varsha' in names
True
'bharat' not in names
True
'
names
'SirishaVarshaAchyuthSaakethSapnil'
len(names)
33
max(names)
'y'
min(names)
'A'
ord('A')
65
ord('a')
97
chr(60)
'<'
chr(97)
'a'
chr(5)
'\x05'
chr(30)
'\x1e'
sorted(names)
['A', 'S', 'S', 'S', 'V', 'a', 'a', 'a', 'a', 'a', 'a', 'c', 'e', 'h', 'h', 'h', 'h', 'h', 'i', 'i', 'i', 'k', 'l', 'n', 'p', 'r', 'r', 's', 's', 't', 't', 'u', 'y']
names
'SirishaVarshaAchyuthSaakethSapnil'
names.upper()
'SIRISHAVARSHAACHYUTHSAAKETHSAPNIL'
names.lower()
'sirishavarshaachyuthsaakethsapnil'
names.swapcase()
'sIRISHAvARSHAaCHYUTHsAAKETHsAPNIL'
a='python'
a.center(30,'-')
'------------python------------'
a.ljust(30,'-')
'python------------------------'
a.rjust(30,'-')
'------------------------python'
a
'python'
a.isalpha()
True
'12'.isalpha()
False
'12'.isdigit()
True
'a12'.isalnumeric()
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    'a12'.isalnumeric()
AttributeError: 'str' object has no attribute 'isalnumeric'. Did you mean: 'isnumeric'?
'a12'.isalnum()
True
'python.py'.startswith('p')
True
'python.py'.endswith('.py')
True
'a'.isupper()
False
'a'.islower()
True
'     '.isspace()
True
'    h'.isspace()
False
s= 'python is easy'
s.replace('python','java')
'java is easy'
s.split()
['python', 'is', 'easy']
s
'python is easy'
s.title()
'Python Is Easy'
s.captilize()
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    s.captilize()
AttributeError: 'str' object has no attribute 'captilize'. Did you mean: 'capitalize'?
s.capitalize()
'Python is easy'
s='         python        '
s.strip()
'python'
s.lstrip()
'python        '
s.rstrip()
'         python'
s= 'python is easy'
s.index('y')
1
s.index('i')
7
s.find('e')
10
s.find('y')
1
s.find('z')
-1
s.index('z')
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    s.index('z')
ValueError: substring not found

= RESTART: C:/Users/Thummala Sudhakar/Desktop/New folder/Day-1/string.py
Enter the password: 123Sowm123@
1
2
3
S
o
w
m
1
2
3
@


lower
lower
lower
lower
lower
lower
lower
lower
lower
lower

lower
lower
lower
lower
lower
lower
splchar
digit
digit
digit




------ Welcome to Grocery Store ------
Here are the available products:

Index	Product			Price (Rs.)
1 	 Rice 			 60
2 	 Wheat Flour 		 45
3 	 Sugar 			 40
4 	 Milk 			 25
5 	 Eggs (12 pcs) 		 70
6 	 Cooking Oil 		 130
7 	 Tea Powder 		 90
8 	 Salt 			 20
9 	 Bread 			 30
10 	 Soap 			 25

Enter the product indexes you want to buy (you can repeat indexes)
Enter indexes (e.g. 1 2 2 5): 9 9 8 6 3 3 1 1 1 7
[9, 9, 8, 6, 3, 3, 1, 1, 1, 7]

-------- Your Bill --------
Product		Qty	Price	Total
Bread 		 2 	 30 	 60
Salt 		 1 	 20 	 20
Cooking Oil 	 1 	 130 	 130
Sugar 		 2 	 40 	 80
Rice 		 3 	 60 	 180
Tea Powder 	 1 	 90 	 90

Total Amount to Pay: Rs. 560
Thank you for shopping with us!
>>> 
1
2
3
4
5
6
7
8
9
10


1 {'product': 'Rice', 'price': 60}
2 {'product': 'Wheat Flour', 'price': 40}
3 {'product': 'Sugar', 'price': 80}
4 {'product': 'Milk', 'price': 25}
5 {'product': 'Eggs (12 pcs)', 'price': 70}
6 {'product': 'Cooking Oil', 'price': 130}
7 {'product': 'Tea Powder', 'price': 90}
8 {'product': 'Salt', 'price': 20}
9 {'product': 'Bread', 'price': 30}
10 {'product': 'Soap', 'price': 25}


1 Rice 60
2 Wheat Flour 40
3 Sugar 80
4 Milk 25
5 Eggs (12 pcs) 70
6 Cooking Oil 130
7 Tea Powder 90
8 Salt 20
9 Bread 30
10 Soap 25







1       Rice                 60        
2       Wheat Flour          40        
3       Sugar                80        
4       Milk                 25        
5       Eggs (12 pcs)        70        
6       Cooking Oil          130       
7       Tea Powder           90        
8       Salt                 20        
9       Bread                30        
10      Soap                 25        


Index   Product Name         Price     
1       Rice                 60        
2       Wheat Flour          40        
3       Sugar                80        
4       Milk                 25        
5       Eggs (12 pcs)        70        
6       Cooking Oil          130       
7       Tea Powder           90        
8       Salt                 20        
9       Bread                30        
10      Soap                 25        


Index   Product Name         Price     
1       Rice                 60        
2       Wheat Flour          40        
3       Sugar                80        
4       Milk                 25        
5       Eggs (12 pcs)        70        
6       Cooking Oil          130       
7       Tea Powder           90        
8       Salt                 20        
9       Bread                30        
10      Soap                 25        
Enter the indexes: 1 2 3 4 5
[1, 2, 3, 4, 5]


Index   Product Name         Price     
1       Rice                 60        
2       Wheat Flour          40        
3       Sugar                80        
4       Milk                 25        
5       Eggs (12 pcs)        70        
6       Cooking Oil          130       
7       Tea Powder           90        
8       Salt                 20        
9       Bread                30        
10      Soap                 25        
Enter the indexes: 7 8 5 3 2 2 2 2 2 1
-------------Bill-------------
Tea Powder - &90
Salt - &20
Eggs (12 pcs) - &70
Sugar - &80
Wheat Flour - &40
Wheat Flour - &40
Wheat Flour - &40
Wheat Flour - &40
Wheat Flour - &40
Rice - &60
Your Bill: 520
s=[1,2,2,3,4,2,2,2,2,2,3]
s.count(1)
1
s.count(2)
7
s.count(3)
