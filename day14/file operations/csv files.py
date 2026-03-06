# csv
'''
import csv


with open ('sample.csv','r') as file:
    data = csv.reader(file)

    for row in data:
        print(row)

#append
import csv


with open('sample.csv','a') as file:
    data = csv.writer(file)
    data.writerow(['5','saaketh'])
    data.writerow(['6','swapnil'])

#write
import csv


with open('sample.csv','w',newline='') as file:
    data = csv.writer(file)
    data.writerow(['product_Ids','product','price'])
    data.writerow(['1','laptop','52000'])
    data.writerow(['2','charger','2000'])
    data.writerow(['3','mouse','500'])
    data.writerow(['4','tab','32000'])
    data.writerow(['5','head phones','2000'])
#read
import csv
with open('sample.csv','r',newline='') as file:
    data=csv.reader(file)
    for i in data:
        print(i)


    

