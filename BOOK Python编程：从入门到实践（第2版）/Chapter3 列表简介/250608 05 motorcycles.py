motorcycles = ['honda', 'yamaha', 'suzuki', 'kawasaki', 'ducati']
print(motorcycles)

# 修改列表中的第一个元素
motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'kawasaki', 'ducati']
# 在列表末尾添加元素
motorcycles.append('ducati')
print(motorcycles)

# 创建空列表
motorcycles = []
# 在空列表中添加元素
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# 在列表中间插入值
# .insert(index, value)方法第一个参数是插入位置的索引，第二个参数是插入的值，自插入位置开始，后面的元素会向后移动
motorcycles.insert(0, 'ducati')
print(motorcycles)

# 删除列表元素
motorcycles = ['honda', 'yamaha', 'suzuki', 'kawasaki', 'ducati']
# 使用del语句删除元素，需要指明要删除的元素的索引，如果没有指明索引，则会删除整个列表
del motorcycles[0]
print(motorcycles)

# 弹出元素
motorcycles = ['honda', 'yamaha', 'suzuki', 'kawasaki', 'ducati']
# 使用pop()方法删除列表末尾的元素，并返回该元素
last_motorcycle = motorcycles.pop()
print(last_motorcycle)
print(motorcycles)
# 使用pop()方法删除列表中指定位置的元素，并返回该元素
first_motorcycle = motorcycles.pop(0)
print(first_motorcycle)
print(motorcycles)

# 如果你要从列表中删除一个元素，且不再以任何方式使用它，就使用del 语句；如果你要在删除元素后还能继续使用它，就使用方法pop()

# 根据值删除元素
motorcycles = ['honda', 'yamaha', 'suzuki', 'kawasaki', 'ducati']
# 使用remove()方法删除列表中第一个匹配的值
motorcycles.remove('suzuki')
print(motorcycles)
# 如果要删除的值在列表中不存在，会引发ValueError异常
# 方法remove()只删除第一个指定的值。如果要删除的值可能在列表中出现多次，就需要使用循环来确保将每个值都删除。
