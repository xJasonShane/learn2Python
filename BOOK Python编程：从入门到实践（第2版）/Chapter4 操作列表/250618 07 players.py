players = ["charles", "martina", "michael", "florence", "eli"]
# 切片：包含左侧的索引值，不包含右侧的索引值
print(players[0:3])
print(players[1:4])

# 左侧值空值时从第一个元素开始
print(players[:4])
# 右侧值空值时直到最后一个元素
print(players[2:])
# 负数索引返回离列表末尾相应距离的元素
print(players[-3:])
# 切片第三个参数是步长，不填默认为1
print(players[0:4:2])
print(players[::2])

# 遍历切片
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
