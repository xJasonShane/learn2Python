# Q:想想可存储到列表中的东西，如山川、河流、国家、城市、语言或你喜欢的任何东西。编写一个程序，在其中创建一个包含这些元素的列表，然后，对于本章介绍的每个函数，都至少使用一次来处理这个列表。
location = ['北京', '江苏', '浙江', '新疆', '奈良']
print(location)

print(sorted(location))  # 按字母顺序打印
print(sorted(location, reverse=True))  # 按与字母顺序相反的顺序打印

location.reverse()  # 修改列表元素的排列顺序
print(location)  # 打印修改后的列表
location.reverse()  # 再次修改列表元素的排列顺序
print(location)  # 打印恢复后的列表

location.sort()  # 按字母顺序排列
print(location)  # 打印按字母顺序排列的列表
location.sort(reverse=True)  # 按与字母顺序相反的顺序排列
print(location)  # 打印按与字母顺序相反的顺序排列的列表

# 打印列表长度
print(f"列表中包含{len(location)}个元素。")
# 打印列表的第一个元素
print(f"列表的第一个元素是：{location[0]}")
# 打印列表的最后一个元素
print(f"列表的最后一个元素是：{location[-1]}")
# 打印列表的中间元素
middle_index = len(location) // 2
print(f"列表的中间元素是：{location[middle_index]}")
