#Guilherme Gonzaga Silva 11621EMT021 
#prog06.py

# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is

# and
# or 
# not

# language = 'Python'
# if language=='Python':
#     print('Language is Python')
# else:
#     print('No match')

# language = 'Java'
# if language=='Python':
#     print('Language is Python')
# elif language == 'Java':
#     print('Language is Java')
# elif language == 'JavaScript':
#     print('Language is JavaScript')
# else:
#     print('No match')

# user = 'Admin'
# logged_in = True
# if user == 'Admin' and logged_in:
#     print('Admin Page')
# else:
#     print('Bad Creds' )

# user = 'Admin'
# logged_in = False
# if not logged_in:
#     print('Please Log In')
# else:
#     print('Welcome')

# a = [1, 2, 3]
# b = [1, 2, 3]
# print(id(a)) #7794472
# print(id(b)) #15007304
# print(a is b) #False

# a = [1, 2, 3]
# b = [1, 2, 3]
# print(id(a)) #7794472
# print(id(b)) #15007304
# print(a == b) #True

# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.

condition = False
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')