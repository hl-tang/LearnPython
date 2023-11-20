# Sorting
arr = [5,4,7,3,8]
arr.sort()  # ascending by default
print(arr)

arr.sort(reverse=True)  #descending order
print(arr)

arr = ["bob", "alice", "jane", "doe"]
arr.sort()  # in alphabetical order
print(arr)

# Custom sort (by length of string)
# key要指定只有一个参数的函数，并且只有一个返回值用来排序
arr.sort(key=lambda x: len(x))  #lambda表达式
print(arr)  # sorts are stable


student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
print(sorted(student_tuples, key=lambda student: student[2], reverse=True))  # sort by age, big to small


# 还有一种sorted()函数，不会在原数组上修改位置
# https://docs.python.org/3/howto/sorting.html?highlight=sort
arr = [5,4,7,3,8]
print(sorted(arr))
print(arr) #不变


# 定义结构体类
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

# 创建结构体对象列表
students = [
    Student('Alice', 21, 85),
    Student('Bob', 22, 92),
    Student('Charlie', 21, 98),
    Student('David', 21, 90)
]

""" # 定义排序函数，根据年龄进行排序
def sort_by_age(student):
    return student.age """
# 定义排序函数，按年龄从小到大排序，年龄相同时按成绩从大到小排序
def sort_by_age_and_grade(student):
    return (student.age, -student.grade)    # return 元组

# 使用普通函数作为key参数进行排序
# 和C++的cmp函数返回值是bool不同，python就直接根据返回值的大小排
sorted_students = sorted(students, key=sort_by_age_and_grade)

# 打印排序结果
for student in sorted_students:
    print(student.name, student.age, student.grade)


# input()相当于C++的getline，默认是string
""" N = input().split()
a = []
for i in N:
    a.append(int(i)) """
# 用map()把参数1的函数施加于参数2的可迭代对象的每个元素
a = list(map(int, input().split())) # 1行读入多个数字
print(a)
a.sort(reverse=True)
print(a)