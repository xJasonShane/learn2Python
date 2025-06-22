# Q:编写一系列条件测试，将每个测试以及对其结果的预测和实际结果打印出来。详细研究实际结果，直到你明白它为何为True 或False 。创建至少10个测试，且其中结果分别为True 和False 的测试都至少有5个。
car = "subaru"
print("Is car == 'subaru'? I predict True.")
print(car == "subaru")

print("\nIs car == 'audi'? I predict False.")
print(car == "audi")

# Q:你并非只能创建10个测试。如果想尝试做更多比较，可再编写一些测试，并将它们加入conditional_tests.py中。对于下面列出的各种情况，至少编写两个结果分别为True 和False 的测试。
# 检查两个字符串相等和不等。
a1 = "hello"
a2 = "Hello"
print(a1 == a2)
# 使用方法lower() 的测试。
print(a1.lower() == a2.lower())
# 涉及相等、不等、大于、小于、大于等于和小于等于的数值测试。
num1 = 5
num2 = 10
print(num1 < num2)
print(num1 > num2)
print(num1 <= num2)
print(num1 >= num2)
print(num1 == num2)
print(num1 != num2)
# 使用关键字and 和or 的测试。
print(num1 < num2 and num1 > num2)
print(num1 < num2 or num1 > num2)
# 测试特定的值是否包含在列表中。
list = [1, 2, 3, 4, 5]
print(5 in list)
# 测试特定的值是否未包含在列表中。
list = [1, 2, 3, 4, 5]
print(6 not in list)
