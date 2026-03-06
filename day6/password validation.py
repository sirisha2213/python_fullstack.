#password validation

pwd = input("Enter the password:")

if len(pwd)>8:
    s=set()
    for i in pwd:
        if i.isupper():
            s.add('upper')
        elif i.islower():
            s.add('lower')
        elif i.isdigit():
            s.add('digit')
        else:
            s.add('spl char')
    if len(s)==4:
        print("strong password")
    else:
        print('weak password password needs to have upper,lower,digit,splchar')
else:
    print('lenghts needs to be >=8')
