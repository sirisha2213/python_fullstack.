
# functions
def student_details(info):
    print(f'name:{info[0]}')
    print(f'course:{info[1]}')
    print(f'year:{info[2]}')
    print("-----end--------")

data = [['varsha','PFS','2026'],
        ['bhavana','JFS','2026'],
        ['sajana','DA','2026'],
        ['sirisha','DS','2025'],
        ]
for i in data:
    student_details(i)
#functional positional arguments

def display(uname,email,password):
    print(f'Username :{uname}')
    print(f'Email :{email}')
    print(f'Passsword :{password}')
    print('\n\n')

display('varsha','varsha@gmail.com','varsha@123')
display('varsha@123','varsha','varsha@gmail.com')
display('varsha@gmail.com','varsha@123','varsha')

#functional keyword arguments

def display(uname,email,password):
    print(f'Username :{uname}')
    print(f'Email :{email}')
    print(f'Passsword :{password}')
    print('\n\n')

display(uname='varsha',email='varsha@gmail.com',password='varsha@123')
display(password='varsha@123',uname='varsha',email='varsha@gmail.com')
display(email='varsha@gmail.com',password='varsha@123',uname='varsha')

# fuctional default arguments
def display(uname,email,password,status='absent'):
    print(f'Username :{uname}')
    print(f'Email :{email}')
    print(f'Passsword :{password}')
    print(f'Status :{status}')
    print('\n\n')

display('varsha','varsha@gmail.com','varsha@123','present')

# funtional variable length argument
def display(*names):
    for i in names:
        print(i)
    else:
        print('---------------End of the List--------------------')

display('varsha')
display('saaketh','krishna','nikhil','dileep')
display('sapnil','adil','meghana')
display('sirisha','bhavana')





























    






    
    
