# 访问列表不存在的元素，索引错误
motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles[3])

# IndexError: list index out of range

print(motorcycles[-1])

# 当列表为空的时候，使用索引访问任何值都会报索引错误
motorcycles = []
# print(motorcycles[0])

# 发生索引错误却找不到解决办法时，请尝试将列表或其长度打印出来。
print(len(motorcycles))
