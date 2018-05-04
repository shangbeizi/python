# while True:
#     try:
#         x = int(input('Enter the first number:'))
#         y = int(input('Enter the second number:'))
#         value = x/y
#         print('x/y is ',value)
#     except Exception as e:
#         print('Invalid input',e)
#         print('please try again')
#
#     else:
#         break
# class Bird:
#     def __init__(self):
#         self.hungry = True
#     def eat(self):
#         if self.hungry:
#             print('Aaaah.....')
#             self.hungry = False
#         else:
#             print('No,Thinks')
#
# class SongBird(Bird):
#     def __init__(self):
#         super().__init__()
#
#         self.sound = 'Squawk'
#     def sing(self):
#         print(self.sound)
#
# sb = SongBird()
# print(sb.sing())
# print(sb.eat())
# print(sb.eat())
#
# class Rectangle:
#     def __init__(self):
#         self.width = 0
#         self.height = 0
#     def setsize(self,size):
#         self.width,self.height  =size
#     def getsize(self):
#         return self.width,self.height
#     size = property(getsize,setsize)
#
# r = Rectangle()
# r.width = 10
# r.height = 5
# # print(r.size)
# r.size = 150,100
# print(r.height)
# print(r.width)

# class A:
#     value = 0
#     def __next__(self):
#         self.value +=1
#
#         if self.value >10:
#             raise StopIteration
#         return self.value
#     def __iter__(self):
#         return self
#
# ti = A()
# print(list(ti


# class Fibs:
#     def __init__(self):
#         self.a = 0
#         self.b = 1
#     def __next__(self):
#         self.a,self.b  =self.b,self.a+self.b
#         return self.a
#     def __iter__(self):
#         return self
#
# fibs = Fibs()
# for f in fibs:
#     if f > 1000:
#         print(f)
#         break

# def flatten(nested):
#     try:
#         try: nested+''
#         except TypeError:pass
#         else: raise TypeError
#
#         for sublist in nested:
#             for element in sublist:
#                 yield element
#     except TypeError:
#         yield nested
#
#

#八皇后问题
# import random
# def conflict(state,nextX):
#     nextY = len(state)
#     for i in range(nextY):
#         if abs(state[i]-nextX) in (0,nextY-i):
#             return True
#     return False
#
# def queens(num=8,state=()):
#     for pos in range(num):
#         if not conflict(state,pos):
#             if len(state) == num-1:
#                 yield (pos,)
#             else:
#                 for result in queens(num,state+(pos,)):
#                     yield (pos,)+result
#
# def prettyprint(solution):
#     def line(pos,lenght=len(solution)):
#         return '. '*(pos)+'X'+'. '*(lenght-pos-1)
#     for pos in solution:
#         print(line(pos))

# prettyprint(random.choice(list(queens(12))))
# print(len(list(queens(100))))
#八皇后问题

# for i in range(1,10):
#     for j in range(i,10):
#         print('{}*{}={}'.format(i,j,i*j),end='\t')
#     print('\n')

