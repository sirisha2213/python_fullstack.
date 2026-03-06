# control statements
#looping statements
#forloop 
'''
products = ['bread','butter','milk','sugar','salt',]

for product in products:
    print(f'{product}-add to fav | buy now | add to cart|')

sizes = ('XS','S','M','L','XL','XXL')

for S in sizes:
    print(f".....|{S}|....")

followers = {'saaketh','sapnil','dileep','varsha','sathvik',}


for i in followers:
    print(f'{i}- |follow back|remove|message|')

data={
    'varsha' :['c','python','java'],
    'bhavana':['ui/ux','python','java'],
    'sapnil':['ml','python','java'],
    'saaketh':['ml','python','java']
}

for i in data:
    print(f"{i}: {data[i]}")
    
s='python programming'

for i in s:
    print(i)
    
#range(start,stop+1,step)=range(0,n,1)
for i in range(1,11):
    print(i)

for i in range(2,101,2):
    print(i)

for i in range(1,100,2):
    print(i)
for i in range(10,0,-1):
    print(i)
n=int(input("enter the number"))

print(f"{n}-table")
for i in range(1,11):
      print(f'{n}*{i}={n*i}')

for i in range(1,10):
    if i==7:
        break
    print(i)
for i in range(1,10):
    if i==7:
        continue
    print(i)
# while loop
i=1 #intialization
while i<10:  #condition
    print(i)  #statement
    i=i+1    #increment/decrement

moves = 15
winning_point = int(input("tell me how many moves is required to finish the game "))

while moves >= 1:
    if 15- winning_point == moves:
        print("you won the game")
        break
    print(f"{moves} are left")
    moves-=1

else:
    print("game over")

bullets = 10

while bullets > 0 :
    print(f"you have {bullets} bullets, shoot them!")
    bullets-=1
else:
    print("game over")
'''



