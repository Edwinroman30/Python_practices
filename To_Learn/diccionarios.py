
users = [
    {
    'name': 'Gaust',
    'state': True,
    'email': 'GT.gmail.com'
    },
    {
    'name': 'Lorenso',
    'state': True,
    'email': 'DolenZO.gmail.com'
    },
    {
    'name': 'Mathew',
    'state': True,
    'email': 'Wesdowm.gmail.com'
    }
]

#print(users[0])

#ENUMERATE PERMITE RECORRER MODO KEY VALUE
#for key,value in enumerate(users):
 #   print(key, value)


for value in users:

    for v in value.items():
        print(v)


tupla_test = (1,2,3,2,3)

print(tupla_test)
