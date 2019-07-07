a = {'Name': 'Ailn'}
try:
    with open('data.csv' , 'r'):
        pass
    print('i am after open file')
    print(a['Name'])

except KeyError:
    print('this key does not exist in this ADT')
except FileNotFoundError as e:
    print(e)
    print('file does not exist')
except Exception:
    print('this is un-known exception')
finally:
    print('i am finally block!!')
print('ending')

