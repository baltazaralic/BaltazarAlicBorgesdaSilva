#Guilherme Gonzaga Silva 11621EMT021 
#prog18.py

'''
LEGB
Local, Enclosing, Global, Built-in
'''

#1)
# x = 'global x'

# def test():
#     global x
#     x = 'local x'
#     # y = 'local y'
#     # print(y)
#     print(x)

# test()
# print(x)

#2)
# import builtins
# def min(): #errado, cuidado por min ser uma função
#     pass

#3)
# m = min([5, 1, 4, 2, 3])
# print(m)

# def test(z):
#     x = 'local x'
#     print(z)

# test('local z')
# #print(z)

#4)
x = 'global x'

def outer():
    x = 'outer x'

    def inner():
        #nonlocal x
        x = 'inner x'
        print(x)
        
    inner()
    print(x)

outer()
# print(x)
