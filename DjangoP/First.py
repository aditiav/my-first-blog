print('My first try at', 'Python')

membership = {'name':'Aditi','DOB':'25-07-75','period':'yearly'}
print(len(membership))

if membership['period'] == 'yearly':
     print(membership)

else:
     print('not an annual membership')


#print(membership)

# Learning how to write functions in Python
def HelloName(Name,Surname):
    print('Hi ' + Name + Surname + ' ! How are you?')
#HelloName(membership['name'])

girls = ("aaa","bbb","ccc","ddd","eeee")
Surname = ("zzz","yyy","xxx","www","vvvv")
for i in range(1,5):
    HelloName(girls[i],Surname[i])
    
