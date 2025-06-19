# 元组：无法修改的列表
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# 尝试修改元组元素会报错
# TypeError: 'tuple' object does not support item assignment
# dimensions[0] = 300
# print(dimensions[0])

# 遍历元组
for dimension in dimensions:
    print(dimension)

# 可以采用覆盖元组方式改变元组元素
dimensions = (400, 100)
for dimension in dimensions:
    print(dimension)
