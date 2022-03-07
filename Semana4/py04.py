#Guilherme Gonzaga Silva 11621EMT021 
#prog04.py

#courses = ['History', 'Math', 'Physics', 'CompSci']
#print(courses) #['History', 'Math', 'Physics', 'CompSci']
#print(len(courses)) #4 valores na lista
#print(courses[0]) #History
#print(courses[3]) #CompSci
#print(courses[-1]) #CompSci
#print(courses[0:2]) #['History', 'Math'] não inclui o 2
#print(courses[:2]) #['History', 'Math'] não inclui o 2
#print(courses[2:]) #['Physics', 'CompSci'] 
#courses.append('Art')
#print(courses) #['History', 'Math', 'Physics', 'CompSci', 'Art']

#courses = ['History', 'Math', 'Physics', 'CompSci']
#courses.insert(0, 'Art')
#print(courses) #['Art', 'History', 'Math', 'Physics', 'CompSci']
#courses_2 = ['Art', 'Education']
#courses.insert(0, courses_2)
#print(courses) #[['Art', 'Education'], 'Art', 'History', 'Math', 'Physics', 'CompSci']
#print(courses[0]) #['Art', 'Education']

#courses = ['History', 'Math', 'Physics', 'CompSci']
#courses_2 = ['Art', 'Education']
#courses.extend(0, courses_2)
#print(courses) #['History', 'Math', 'Physics', 'CompSci', 'Art', 'Education']

#courses = ['History', 'Math', 'Physics', 'CompSci']
#courses.remove('Math')
#print(courses) #['History', 'Physics', 'CompSci']

#courses = ['History', 'Math', 'Physics', 'CompSci']
#courses.pop()
#print(courses) #['History', 'Math', 'Physics'] remove ultimo item

#courses = ['History', 'Math', 'Physics', 'CompSci']
#popped = courses.pop()
#print(popped) #CompSci

#courses = ['History', 'Math', 'Physics', 'CompSci']
#courses.reverse()
#print(courses) #['CompSci', 'Physics', 'Math', 'History']

#courses = ['History', 'Math', 'Physics', 'CompSci']
#courses.sort()
#print(courses) #['CompSci', 'History', 'Math', 'Physics'] ordem alfabetica

#nums = [1, 5 , 2, 4, 3]
#nums.sort()
#print(nums) #[1, 2, 3, 4, 5]

#nums = [1, 5 , 2, 4, 3]
#nums.sort(reverse=True)
#print(nums) #[5, 4, 3, 2, 1]

#courses = ['History', 'Math', 'Physics', 'CompSci']
#sorted_courses = sorted(courses)
#print(sorted_courses) #['CompSci', 'History', 'Math', 'Physics']

#nums = [1, 5 , 2, 4, 3]
#print(min(nums)) #1
#print(max(nums)) #5
#print(sum(nums)) #15

#courses = ['History', 'Math', 'Physics', 'CompSci']
#print(courses.index('CompSci')) #3
#print('Art' in courses) #false
#print('Math' in courses) #true

#courses = ['History', 'Math', 'Physics', 'CompSci']
#for course in courses:
#    print(course) #Segue abaixo o resultado
#History
#Math
#Physics
#CompSci

#courses = ['History', 'Math', 'Physics', 'CompSci']
#for index, course in enumerate(courses):
#    print(index, course) #Segue abaixo o resultado
#0 History
#1 Math
#2 Physics
#3 CompSci

#courses = ['History', 'Math', 'Physics', 'CompSci']
#for index, course in enumerate(courses, start=1):
#    print(index, course) #Segue abaixo o resultado
#1 History
#2 Math
#3 Physics
#4 CompSci

#courses = ['History', 'Math', 'Physics', 'CompSci']
#courses_str = ', '.join(courses)
#new_list = course_str.split(' - ')
#print(courses_str) #History, Math, Physics, CompSci
#print(new_list) #['History', 'Math', 'Physics', 'CompSci']

# list_1 = ['History', 'Math', 'Physics', 'CompSci']
# list_2 = list_1
# list_1[0] = 'Art'
# print(list_1) #['Art', 'Math', 'Physics', 'CompSci']
# print(list_2) #['Art', 'Math', 'Physics', 'CompSci']

# tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
# tuple_2 = tuple_1
# print(tuple_1) #('History', 'Math', 'Physics', 'CompSci')
# print(tuple_2) #('History', 'Math', 'Physics', 'CompSci')

# cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
# print(cs_courses) #{'History', 'Math', 'Physics', 'CompSci'} aleatório

# cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
# print('Math' in cs_courses) #True

# cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
# ar_courses = {'History', 'Math', 'Art', 'Design'}
# print(cs_courses.intersection(ar_courses)) #{'Math', 'History'}
# print(cs_courses.difference(ar_courses)) #{'CompSci', 'Physics'}
# print(cs_courses.union(ar_courses)) #{'History', 'Design', 'Art', 'Physics', 'CompSci', 'Math'}

#listas vazias
empty_list = []
empty_list = list()

#tuples vazias
empty_tuple = ()
empty_tuple = tuple()

#sets vazias
empty_set = {} #isso n é certo
empty_set = set() #certo