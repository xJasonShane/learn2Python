# Python方法sort() 让你能够较为轻松地对列表进行排序。
# 方法sort()永久性地修改列表元素的排列顺序。
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()  # 对列表进行永久性排序
print(cars)

cars.sort(reverse=True)  # 对列表进行永久性逆序排序
print(cars)

# 使用函数sorted() 对列表临时排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original order:")
print(cars)
print("\nHere is the sorted order:")
print(sorted(cars))  # 临时排序
print("\nHere is the original order again:")
print(cars)  # 原列表未变
print("\nHere is the sorted order in reverse:")
print(sorted(cars, reverse=True))  # 临时逆序排序
print("\nHere is the original order again:")
print(cars)  # 原列表未变

# 在并非所有的值都是小写时，按字母顺序排列列表要复杂些。决定排列顺序时，有多种解读大写字母的方式，要指定准确的排列顺序，可能比我们这里所做的要复杂。

# 倒打列表  注意：倒打列表并不是按照字母顺序排序，而是直接倒转列表内容
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()  # 永久性地倒打列表
print(cars)

# 确定列表的长度
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))  # 输出列表的长度
