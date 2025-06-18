# Q:将同一个数乘三次称为立方 。例如，在Python中，2的立方用2**3 表示。请创建一个列表，其中包含前10个整数（1～10）的立方，再使用一个for 循环将这些立方数打印出来。
# Q:使用列表解析生成一个列表，其中包含前10个整数的立方。
cubics = [value**3 for value in range(1, 11)]
for cubic in cubics:
    print(cubic)
