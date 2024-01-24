# test_set={1,2,3,4,5,6,7}
# print("the original set is"+str(test_set))
# update_ele=[2,4,9]
# test_set.update(update_ele)
# print("the updated set is"+str(test_set))


# def remove(initial_set):
#     while initial_set:
#         initial_set.pop()
#         print(initial_set)

# initial_set=set([2,4,5,6,7])
# remove(initial_set)

# my_set=set([2,3,4,5,2])
# for i in range(len(my_set)):
#     my_set.remove(next(iter(my_set)))
#     print(my_set)

# D={}

# L=[['a',1],['b',2],['c',3],['d',4],['e',2],['f',3],['g',5]]
# for i in range(len(L)):
#     if L[i][0] in D:
#         D[L[i][0]].append[L[i][1]]
#     else:    
#         D[L[i][0]]= []
#         D[L[i][0]].append(L[i][1])
# print(D)
 #exeception handling
# marks=100
# a=marks/0
# print(a)

# def fun(a):
#     if(a<4):
#         b=a/(a-3)
#     print(b)

# try:
#     fun(3)
#     fun(0)
# except ZeroDivisionError:
#     print("ZeroDivisionError occur")
# except NameError:
#     print("name error occur")


# # define Python user-defined exceptions
# class Error(Exception):
# 	"""Base class for other exceptions"""
# 	pass

# class zerodivision(Error):
# 	"""Raised when the input value is zero"""
# 	pass

# try:
# 	i_num = int(input("Enter a number: "))
# 	if i_num == 0:
# 		raise zerodivision
# except zerodivision:
# 	print("Input value is zero, try again!")
# 	print()
sum=0
for i in range(1,51):
    if i%2 == 0:
        sum+=i
print(sum)




