# # 32

# a = {0,1,2,7,27}
# b = {0,10,20,70,27}

# c = a.union(b)
# d = a.intersection(b)

# print(c,d)

# # 33

# a = {0,1,2,7,27}
# b = {0,10,20,70,27}

# c = a.difference(b)
# d = a.symmetric_difference(b)

# print(c,d)

# # 34

# a = {0,1,2,7,27}

# a.update({100})

# print(a)

# # 35

# a={100,200,300,400,500}

# a.intersection_update({400,500,600,700,800})
# a.difference_update({400,500,600,700,800})
# a.symmetric_difference_update({400,500,600,700,800})

# print(a)

# # 36

# a={100,200,300,400,500}

# result = (a>{100,200,300,400,500})
# result2 = (a<={100,200,300,400,500})
# result3 = (a>={100,200,300,400,500})

# if (result == True):
#     print('상위')
# elif (result2 == True):
#     print('부분')
# elif (result3== True):
#     print('동시')

# # 37

# a = {0,1,2,7,27}

# a.add(1000)
# a = list(a)
# a.pop()
# a=set(a)
# print(a)

# # 38

# multiples={x for x in range(1,101)if x%3==0 and x%5==0}
# print(multiples)