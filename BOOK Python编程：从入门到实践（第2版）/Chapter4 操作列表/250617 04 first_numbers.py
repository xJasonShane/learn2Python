# 利用range()函数批量生成数字
# 第一个参数是起始数，第二个参数是终点数(不包括)，第三个参数是步长(忽略默认为1)
for value in range(1, 5):
    print(value)

# 创建列表
numbers = list(range(1, 6))
print(numbers)

# 指定步长
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# 乘方程序
squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)
print(squares)

# 不使用临时变量乘方程序
squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)
