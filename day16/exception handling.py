#exception handling
'''
try: # whetether error is present or not
    if a>10:
        print('good')

except NameError: # handles the error
    print('a is not defined')
except ValueError:
    print('enter the requested data type')
except TypeError:
    print('data types are different')
except ZeroDivisionError:
    print("can't divide with zero ")
except IndexError:
    print('the index is not presnt')
except KeyError:
    print('in dic this key is not present')
else:
    print('no errors')
finally:
    print('end of the block')
# or
try:
    a=[1,2,3]
    print(a[4])
except(NameError,ValueError,TypeError,ZeroDivisionError,IndexError,else:
    print('no errors')
finally:
    ("end the block")

#or
try:
    a=int(input())
    print(a[4])
except Exception as e:
    print(f'error occurred:{e}')

else:
    print('no error')
finally:
    print('end of the block')

try:
    a=int(input())
    if a<0:
        raise Exception('enter the positive numbers')

except Exception as e:
    print(f'error occurred:{e}')

else:
    print('no error')
finally:
    print('end of the block')



































    
    

    
    
