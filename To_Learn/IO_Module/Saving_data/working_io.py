import io
import json
    
open('/home/edwin/Documents/Python/Python_practices/To_Learn/IO Module/INTRODUCTION PART/PART-2/user.txt','a')
userData = open('/home/edwin/Documents/Python/Python_practices/To_Learn/IO Module/INTRODUCTION PART/PART-2/user.txt','w')

userData.write('Edwin Roman\t18\n')
userData.write('Moises David\t17\n')
userData.write('Nena Perez\t18\n')

userData.close()

try:
    m = open('/home/edwin/Documents/Python/Python_practices/To_Learn/IO Module/INTRODUCTION PART/PART-2/user.txt','r')
    users = m.read().split('\n')
except FileExistsError as ef:
    print(ef)
except FileNotFoundError as fnf:
    print('Sorry we could not find this FILE.')

users.pop()
    
#print(users)

list_user = []

for user in users:
   dict_user = {
        'username': user.split('\t')[0],
        'age': user.split('\t')[1] 
    }
   list_user.append(json.dumps(dict_user))
    
print(list_user[0])