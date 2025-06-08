# 创建列表
# 列表由一系列按特定顺序排列的元素组成。
# 列表通常包含多个元素，因此给列表指定一个表示复数的名称
# 在Python中，用方括号（[​]）表示列表，并用逗号分隔其中的元素。
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
# 根据索引访问列表制定元素
print(bicycles[0])
# 索引从0开始，因此第一个元素的索引为0，第二个元素的索引为1，以此类推。
print(bicycles[1])
print(bicycles[3])
# 列表元素同样可以使用字符串相关方法
print(bicycles[0].title())

# 访问列表最后一个元素，可以直接使用-1索引
print(bicycles[-1])

# 同样可以像使用其他变量一样使用列表中的各元素
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)
