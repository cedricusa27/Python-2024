# countries = ["USA", "Canada", "India", "UK"]
# len(countries)
# del countries[1]
# print(countries[-1])

# list1 = [1, 2, 3, 4, 5]
# list1[0] = 10
# print(list1)

# list1 = [1, 2, 3, 4, 5]
# print(list1[4])


# numbers = [1, 2, 3, 4, 5]
# numbers[4] = 6
# print(numbers[4])

# list1 = [10, 11, 12, 13, 14]
# print(list1[::3])

# countries = ["USA","Canada","Italy","Spain"]
# countries.apprend("Spain")
# countries.insert(2, "Italy")

# ages = [56, 72, 24, 46]
# ages.sort()
# print(ages)

# num = [4, 4, 3, 1]
# num.sort()
# print(num)

# list1=['UK','India','Canada']
# list1.insert(1,8)
# print(list1)

# list1=["Go","Java","C","Rust"]
# print(min(list1))

# list1=["Go","Java","C","Python"]
# print(max(list1))

# list1 = [10, 20, 30, 40, 50]
# list1.append(60)
# print(list1)


# ages = [56, 72, 24, 46]
# ages.sort()
# print(ages)

# list1 = [4, 4, 3, 1]
# list1.pop(2)
# print(list1)


# ages = [56, 72, 24, 46]
# total = 0
# for age in ages:
#     total += age
# average = total / len(ages)
# print(average)


# for x in [0, 2, 1, 3]:
#     for y in [0, 4, 1, 2]:
#             print('*')

# for letter in 'KodeKloud':
#     if letter == 'u':
#         continue
#     print('Letter : ' + letter)


# sum = 0
# values = [2,9,1,7]
# for number in values:
#     sum += number

# print(sum)


# for x in [0, 1, 1, 3]:
#     for y in [0, 2, 1, 2]:
#             print('*')


# name = "Lydia"
# ages = [56, 72, 24, 46]
# ages2 = ages
# ages[0] = 92
# print(ages2[0])



# list1 = [10, 11, 12, 13, 14]
# list1.append(15)
# print(list1)


# list1 = [[1,2,3,2,5],[4,5,6,7],[8,9,10]]
# for i in list1:
#       if len(i)==3:
#         print(i)

# list1 = [1, 2, 3, 4]
# for i, j in enumerate(list1):
#      print(i, j)


# list1 = [10, 11, 12, 13, 14]
# print(list1[0])

# list1=[4,0,7,1]
# print(list1[::-1])


# letters = ["A", "B", "C", "D", "E"]
# print(letters[1:])



# letters = ["A","B","C","D", "E"]
# firstTwo = letters[0:2]
# print(firstTwo)
# print(letters[1:])
# print(letters[:3])
# print(letters[1:-1])


# my_list = [0, 1, 2, 3, 4]
# print(my_list[::-1])

# my_list = [0, 1, 2, 3, 4]
# print(my_list[2:4])

# my_list = [0, 1, 2, 3, 4]
# print(my_list[::3])

# my_list = [0, 1, 2, 3, 4]
# print(my_list[-1])


# my_list = [0, 1, 2, 3, 4]
# my_list.append("python")
# b = my_list[1:]
# print(b)


# my_list = [0, 1, 2, 3, 4]
# print(my_list[::2])

# my_list = [0, 1, 2, 3, 4]
# print(my_list.index(2))


# countries = ["USA", "Canada", "India"]
# countries[0], countries[1] = countries[1], countries[0]
# print(countries)


# my_list = [0, 3, 4, 1, 2]
# print(my_list.index(1))


# classroom = [["Sam", "Luck", "Sara", "Eva", "Anna", "Leo", "Guy", "Kim", "Sasha", "Anne", "Joe", "Claire"]]
# student = classroom[2][1]
# print(student)


# matrix = [[j for j in range(4)] for i in range(4)] 
# print(matrix[3][1])


# matrix = [[0, 1, 2], [0, 1, 2], [0, 1, 2]]

# matrix2 = []

# for submatrix in matrix:
#   for val in submatrix:
#     matrix2.append(val)

# print(matrix2[2])


# countries = [['Egypt', 'USA', 'India'], ['Dubai', 'America', 'Spain'], ['London', 'England', 'France']]
# countries2  = [country for sublist in countries for country in sublist if len(country) < 4]
# print(countries2)



# a = []
# for i in range(5):
#     a.append([])
#     for j in range(5):
#         a[i].append(j)

# print(a[2][3])

# countries = [['Egypt', 'USA', 'India'],
#        ['Dubai', 'America', 'Spain'], 
#        ['London', 'England', 'France']]
# countries2  = [country for sublist in countries for country in 
#                        sublist if len(country) < 6]
# print(countries2)

# Colors = [ ['Red', 'Green', 'White', 'Black'], ['Green', 'Blue', 'White', 'Yellow'] ,['White', 'Blue', 'Green', 'Red'] ]

# matrix = [[[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]]]
# print(matrix[0][0][0])

# matrix = [[[k for k in range(3)] for j in range(3)] for i in range(3)]
# print(matrix[0][0][1])

# matrix = [[[k for k in range(3)] for j in range(3)] for i in range(3)]
# print(matrix[1][1][1])

# matrix = [[[k for k in range(3)] for j in range(3)] for i in range(3)]
# print(matrix[1][1][1])



matrix = [[[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]]]

matrix2 = []

for submatrix in matrix:
  for val in submatrix:
    matrix2.append(val)

print(matrix2[2])










# Lists
# Lists methods
# Iterating Lists 
# Slicing Lists
#
#
