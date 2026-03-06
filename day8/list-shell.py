Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: C:\Users\Thummala Sudhakar\Desktop\New folder\Day-1\string.py
Welcome to the ATM
Enter the account number: 123456
Enter the pin: 1234
Login Successful
1.Check Balance
2.Deposit
3.Withdraw
4.Set Pin
5.View Transactions
6.Exit

Enter the choice: 4
Enter the new pin: 2345
Your Pin is Updated to 2345 successfully
1.Check Balance
2.Deposit
3.Withdraw
4.Set Pin
5.View Transactions
6.Exit

Enter the choice: 
= RESTART: C:\Users\Thummala Sudhakar\Desktop\New folder\Day-1\string.py
Enter the exp: 12+13
Traceback (most recent call last):
  File "C:\Users\Thummala Sudhakar\Desktop\New folder\Day-1\string.py", line 16, in <module>
    exp = int(input("Enter the exp: "))
ValueError: invalid literal for int() with base 10: '12+13'
\
>>> 
= RESTART: C:\Users\Thummala Sudhakar\Desktop\New folder\Day-1\string.py
Enter the exp: 12-9
Traceback (most recent call last):
  File "C:\Users\Thummala Sudhakar\Desktop\New folder\Day-1\string.py", line 16, in <module>
    exp = float(input("Enter the exp: "))
ValueError: could not convert string to float: '12-9'
>>> 
= RESTART: C:\Users\Thummala Sudhakar\Desktop\New folder\Day-1\string.py
Enter the exp: 12+13
12+13
>>> 
= RESTART: C:\Users\Thummala Sudhakar\Desktop\New folder\Day-1\string.py
Enter the exp: 12-14
12-14
1
2
-
1
4

= RESTART: C:\Users\Thummala Sudhakar\Desktop\New folder\Day-1\string.py
Enter the exp: 12+13
25

= RESTART: C:\Users\Thummala Sudhakar\Desktop\New folder\Day-1\string.py
Enter the exp: 78/2
80

= RESTART: C:\Users\Thummala Sudhakar\Desktop\New folder\Day-1\string.py
Enter the exp: 75/2
37.5
l=[1,12.3,"string",[1,2,3],(1,2,3),{1,23},{1:1,2:4,3:9},False,None,2+9j]
l
[1, 12.3, 'string', [1, 2, 3], (1, 2, 3), {1, 23}, {1: 1, 2: 4, 3: 9}, False, None, (2+9j)]
names = ['saaketh','sapnil','bharat','pushwanth','sravanthi','varsha','srinidhi']
names
['saaketh', 'sapnil', 'bharat', 'pushwanth', 'sravanthi', 'varsha', 'srinidhi']
names[1]
'sapnil'
names[-1]
'srinidhi'
names[2]
'bharat'
names[3]
'pushwanth'
names[-3:]
['sravanthi', 'varsha', 'srinidhi']
names[:4]
['saaketh', 'sapnil', 'bharat', 'pushwanth']
names[2:4]
['bharat', 'pushwanth']
names[::-1]
['srinidhi', 'varsha', 'sravanthi', 'pushwanth', 'bharat', 'sapnil', 'saaketh']
names[-1:-4:-1]
['srinidhi', 'varsha', 'sravanthi']
names
['saaketh', 'sapnil', 'bharat', 'pushwanth', 'sravanthi', 'varsha', 'srinidhi']
id(names)
2825516200832
names[-2]='nikhil'
names
['saaketh', 'sapnil', 'bharat', 'pushwanth', 'sravanthi', 'nikhil', 'srinidhi']
id(names)
2825516200832
names[-1]='praveen'
names
['saaketh', 'sapnil', 'bharat', 'pushwanth', 'sravanthi', 'nikhil', 'praveen']
names[-3]='sathvik'
names
['saaketh', 'sapnil', 'bharat', 'pushwanth', 'sathvik', 'nikhil', 'praveen']
names.append('shanmukha')
names
['saaketh', 'sapnil', 'bharat', 'pushwanth', 'sathvik', 'nikhil', 'praveen', 'shanmukha']
names.append('abid')
names
['saaketh', 'sapnil', 'bharat', 'pushwanth', 'sathvik', 'nikhil', 'praveen', 'shanmukha', 'abid']
names.extend(['abhinandhan','ravi','vardhan','umesh'])
names
['saaketh', 'sapnil', 'bharat', 'pushwanth', 'sathvik', 'nikhil', 'praveen', 'shanmukha', 'abid', 'abhinandhan', 'ravi', 'vardhan', 'umesh']
names,insert(3,"Satya")
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    names,insert(3,"Satya")
NameError: name 'insert' is not defined
names.insert(3,"Satya")

names
['saaketh', 'sapnil', 'bharat', 'Satya', 'pushwanth', 'sathvik', 'nikhil', 'praveen', 'shanmukha', 'abid', 'abhinandhan', 'ravi', 'vardhan', 'umesh']
id(names)
2825516200832
names.remove("ravi")
names
['saaketh', 'sapnil', 'bharat', 'Satya', 'pushwanth', 'sathvik', 'nikhil', 'praveen', 'shanmukha', 'abid', 'abhinandhan', 'vardhan', 'umesh']
names.pop(1)
'sapnil'
names
['saaketh', 'bharat', 'Satya', 'pushwanth', 'sathvik', 'nikhil', 'praveen', 'shanmukha', 'abid', 'abhinandhan', 'vardhan', 'umesh']
names.pop(3)
'pushwanth'
names
['saaketh', 'bharat', 'Satya', 'sathvik', 'nikhil', 'praveen', 'shanmukha', 'abid', 'abhinandhan', 'vardhan', 'umesh']
names.pop(3)
'sathvik'
names
['saaketh', 'bharat', 'Satya', 'nikhil', 'praveen', 'shanmukha', 'abid', 'abhinandhan', 'vardhan', 'umesh']
names.remove('abid')
names
['saaketh', 'bharat', 'Satya', 'nikhil', 'praveen', 'shanmukha', 'abhinandhan', 'vardhan', 'umesh']
names.pop()
'umesh'
names.pop()
'vardhan'
names
['saaketh', 'bharat', 'Satya', 'nikhil', 'praveen', 'shanmukha', 'abhinandhan']
del names[2]
names
['saaketh', 'bharat', 'nikhil', 'praveen', 'shanmukha', 'abhinandhan']
names.clear()
names
[]
id(names)
2825516200832
names=['saaketh', 'sapnil', 'bharat', 'Satya', 'pushwanth', 'sathvik', 'nikhil', 'praveen', 'shanmukha', 'abid', 'abhinandhan', 'ravi', 'vardhan', 'umesh']
names
['saaketh', 'sapnil', 'bharat', 'Satya', 'pushwanth', 'sathvik', 'nikhil', 'praveen', 'shanmukha', 'abid', 'abhinandhan', 'ravi', 'vardhan', 'umesh']
names.index('bharat')
2
names.count('adid')
0
names.count('abid')
1
sorted(names)
['Satya', 'abhinandhan', 'abid', 'bharat', 'nikhil', 'praveen', 'pushwanth', 'ravi', 'saaketh', 'sapnil', 'sathvik', 'shanmukha', 'umesh', 'vardhan']
names
['saaketh', 'sapnil', 'bharat', 'Satya', 'pushwanth', 'sathvik', 'nikhil', 'praveen', 'shanmukha', 'abid', 'abhinandhan', 'ravi', 'vardhan', 'umesh']
names.sort()
names
['Satya', 'abhinandhan', 'abid', 'bharat', 'nikhil', 'praveen', 'pushwanth', 'ravi', 'saaketh', 'sapnil', 'sathvik', 'shanmukha', 'umesh', 'vardhan']
names.reverse()
names
['vardhan', 'umesh', 'shanmukha', 'sathvik', 'sapnil', 'saaketh', 'ravi', 'pushwanth', 'praveen', 'nikhil', 'bharat', 'abid', 'abhinandhan', 'Satya']
names
['vardhan', 'umesh', 'shanmukha', 'sathvik', 'sapnil', 'saaketh', 'ravi', 'pushwanth', 'praveen', 'nikhil', 'bharat', 'abid', 'abhinandhan', 'Satya']
max(names)
'vardhan'
min(names)
'Satya'
len(names)
14
l=[1,2,3,4,5]
sum(l)
15
a=[1,2,3,4,5]
b=a
a
[1, 2, 3, 4, 5]
b
[1, 2, 3, 4, 5]
a.append(6)
a
[1, 2, 3, 4, 5, 6]
b
[1, 2, 3, 4, 5, 6]
b.append(15)
b
[1, 2, 3, 4, 5, 6, 15]
a
[1, 2, 3, 4, 5, 6, 15]
id(a)
2825516201216
id(b)
2825516201216
c=a.copy()
c
[1, 2, 3, 4, 5, 6, 15]
a
[1, 2, 3, 4, 5, 6, 15]
c.append(10)
c
[1, 2, 3, 4, 5, 6, 15, 10]
a
[1, 2, 3, 4, 5, 6, 15]

= RESTART: C:\Users\Thummala Sudhakar\Desktop\New folder\Day-1\string.py
Satya
abhinandhan
abid
bharat
nikhil
praveen
pushwanth
ravi
saaketh
sapnil
sathvik
shanmukha
umesh
vardhan

= RESTART: C:\Users\Thummala Sudhakar\Desktop\New folder\Day-1\string.py
Satya
Abhinandhan
Abid
Bharat
Nikhil
Praveen
Pushwanth
Ravi
Saaketh
Sapnil
Sathvik
Shanmukha
Umesh
Vardhan

= RESTART: C:\Users\Thummala Sudhakar\Desktop\New folder\Day-1\string.py
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
11
12
13
14

= RESTART: C:\Users\Thummala Sudhakar\Desktop\New folder\Day-1\string.py
1 Satya
2 abhinandhan
3 abid
4 bharat
5 nikhil
6 praveen
7 pushwanth
8 ravi
9 saaketh
10 sapnil
11 sathvik
12 shanmukha
13 umesh
14 vardhan

= RESTART: C:\Users\Thummala Sudhakar\Desktop\New folder\Day-1\string.py
(0, 'Satya')
(1, 'abhinandhan')
(2, 'abid')
(3, 'bharat')
(4, 'nikhil')
(5, 'praveen')
(6, 'pushwanth')
(7, 'ravi')
(8, 'saaketh')
(9, 'sapnil')
(10, 'sathvik')
(11, 'shanmukha')
(12, 'umesh')
(13, 'vardhan')

= RESTART: C:\Users\Thummala Sudhakar\Desktop\New folder\Day-1\string.py
0. Satya
1. abhinandhan
2. abid
3. bharat
4. nikhil
5. praveen
6. pushwanth
7. ravi
8. saaketh
9. sapnil
10. sathvik
11. shanmukha
12. umesh
13. vardhan

= RESTART: C:\Users\Thummala Sudhakar\Desktop\New folder\Day-1\string.py
1,Satya
2,abhinandhan
3,abid
4,bharat
5,nikhil
6,praveen
7,pushwanth
8,ravi
9,saaketh
10,sapnil
11,sathvik
12,shanmukha
13,umesh
14,vardhan

= RESTART: C:\Users\Thummala Sudhakar\Desktop\New folder\Day-1\string.py
1. Satya
2. abhinandhan
3. abid
4. bharat
5. nikhil
6. praveen
7. pushwanth
8. ravi
9. saaketh
10. sapnil
11. sathvik
12. shanmukha
13. umesh
14. vardhan

= RESTART: C:\Users\Thummala Sudhakar\Desktop\New folder\Day-1\string.py
Enter the number of students: 4
Enter the name: vardhan
Enter the gpa: 8.2
Enter the name: sathvik
Enter the gpa: 9.2
Enter the name: umesh
Enter the gpa: 7.2
Enter the name: saaketh
Enter the gpa: 8.6
['vardhan', 'sathvik', 'umesh', 'saaketh'] [8.2, 9.2, 7.2, 8.6]

= RESTART: C:\Users\Thummala Sudhakar\Desktop\New folder\Day-1\string.py
Enter the number of students: 3
Enter the name: fdghjk
Enter the gpa: 1
Enter the name: dfhgm
Enter the gpa: 2
Enter the name: sfdfbg
Enter the gpa: 3
Names          GPA  
fdghjk 1.0
dfhgm 2.0
sfdfbg 3.0

= RESTART: C:\Users\Thummala Sudhakar\Desktop\New folder\Day-1\string.py
Enter the number of students: 
= RESTART: C:\Users\Thummala Sudhakar\Desktop\New folder\Day-1\string.py
Enter the number of students: 10
--------Student-1----------
Enter the name: abhinandhan
Enter the gpa: 7.5
--------Student-2----------
Enter the name: praveen
Enter the gpa: 9.0
--------Student-3----------
Enter the name: pushwanth
Enter the gpa: 8
--------Student-4----------
Enter the name: saaketh
Enter the gpa: 9
--------Student-5----------
Enter the name: bharat
Enter the gpa: 6.2
--------Student-6----------
Enter the name: nikhil
Enter the gpa: 7.8
--------Student-7----------
Enter the name: umesh
Enter the gpa: 8.6
--------Student-8----------
Enter the name: sapnil
Enter the gpa: 4.5
--------Student-9----------
Enter the name: ravi
Enter the gpa: 5.6
--------Student-10----------
Enter the name: Satya
Enter the gpa: 8.9
Names          GPA  
Traceback (most recent call last):
  File "C:\Users\Thummala Sudhakar\Desktop\New folder\Day-1\string.py", line 34, in <module>
    print(f'{names[i].ljust(14)}|{gpas[i].ljust(5)}')
AttributeError: 'float' object has no attribute 'ljust'

= RESTART: C:\Users\Thummala Sudhakar\Desktop\New folder\Day-1\string.py
Enter the number of students: 10
--------Student-1----------
Enter the name: rtyu
Enter the gpa: 12
--------Student-2----------
Enter the name: jhgfd
Enter the gpa: 43
--------Student-3----------
Enter the name: ewrhtj
Enter the gpa: 56
--------Student-4----------
Enter the name: fdghjk
Enter the gpa: 567
--------Student-5----------
Enter the name: rtyui
Enter the gpa: 345
--------Student-6----------
Enter the name: dfui
Enter the gpa: gh
Traceback (most recent call last):
  File "C:\Users\Thummala Sudhakar\Desktop\New folder\Day-1\string.py", line 26, in <module>
    gpa = float(input("Enter the gpa: "))
ValueError: could not convert string to float: 'gh'

= RESTART: C:\Users\Thummala Sudhakar\Desktop\New folder\Day-1\string.py
Enter the number of students: 5
--------Student-1----------
Enter the name: vardhan
Enter the gpa: 7,5
Traceback (most recent call last):
  File "C:\Users\Thummala Sudhakar\Desktop\New folder\Day-1\string.py", line 26, in <module>
    gpa = float(input("Enter the gpa: "))
ValueError: could not convert string to float: '7,5'

= RESTART: C:\Users\Thummala Sudhakar\Desktop\New folder\Day-1\string.py
Enter the number of students: 5
--------Student-1----------
Enter the name: vardhan
Enter the gpa: 7.8
--------Student-2----------
Enter the name: sathvik
Enter the gpa: 8.9
--------Student-3----------
Enter the name: saakeeth
Enter the gpa: 9.0
--------Student-4----------
Enter the name: sapnil
Enter the gpa: 8.6
--------Student-5----------
Enter the name: dileeep
Enter the gpa: 9.0
Names          GPA  
vardhan       |7.8  
sathvik       |8.9  
saakeeth      |9.0  
sapnil        |8.6  
dileeep       |9.0  

= RESTART: C:\Users\Thummala Sudhakar\Desktop\New folder\Day-1\string.py
Enter the number of students: 7
--------Student-1----------
Enter the name: dfhjk
Enter the gpa: 4
--------Student-2----------
Enter the name: dfgh
Enter the gpa: 7
--------Student-3----------
Enter the name: kjhgf
Enter the gpa: 7
--------Student-4----------
Enter the name: dfghj
Enter the gpa: 9
--------Student-5----------
Enter the name: gfhjk
Enter the gpa: 6
--------Student-6----------
Enter the name: fgh
Enter the gpa: 5
--------Student-7----------
Enter the name: dtfyu
Enter the gpa: 8
Names          GPA  
--------------------
dfhjk         |4.0  
dfgh          |7.0  
kjhgf         |7.0  
dfghj         |9.0  
gfhjk         |6.0  
fgh           |5.0  
dtfyu         |8.0  
