data={
'sathvik':{'status':True,'python':100,'mysql':99,'softskills':85},
'ravi':{'status':False,'python':None,'mysql':None,'softskills':None},
'dillep':{'status':True,'python':33,'mysql':20,'softskills':30},
'praveen':{'status':True,'python':70,'mysql':82,'softskills':64},
'saaketh':{'status':True,'python':45,'mysql':55,'softskills':39},
}

user = input("enter the student name:")

if user in data:
    if data[user]['status']:
        sum = data[user]['pthon']+data[user]['mysql']+data[user]['softskills']
        avg = sum/3
        if avg > 80:
            print(f"congrats {user}!!!\n you got'A'grade")
        elif avg > 60:
            print(f"better luck {user}!!!\n you got'B'grade")
        elif avg > 40:
            print(f"need improvement {user}!!!\n you got 'C'grade")
        else:
            print(f" {user}failed in exam.\n Bring your parents")
    else:
        print(f"{user} didn't write any exams")
    
else:
    print(f"{user} not found")
