# Q:通过给函数range() 指定第三个参数来创建一个列表，其中包含1～20的奇数，再使用一个for 循环将这些数打印出来。
odds = list(range(1, 21, 2))
for value in odds:
    print(value)
