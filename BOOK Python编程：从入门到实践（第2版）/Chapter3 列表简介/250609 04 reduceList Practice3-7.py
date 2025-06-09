# Q:你刚得知新购买的餐桌无法及时送达，因此只能邀请两位嘉宾。
# Q:以完成练习3-6时编写的程序为基础，在程序末尾添加一行代码，打印一条你只能邀请两位嘉宾共进晚餐的消息。使用pop() 不断地删除名单中的嘉宾，直到只有两位嘉宾为止。每次从名单中弹出一位嘉宾时，都打印一条消息，让该嘉宾知悉你很抱歉，无法邀请他来共进晚餐。对于余下两位嘉宾中的每一位，都打印一条消息，指出他依然在受邀人之列。使用del 将最后两位嘉宾从名单中删除，让名单变成空的。打印该名单，核实程序结束时名单确实是空的。
guest_list = ['爱因斯坦', '牛顿', '达芬奇']
print(f"亲爱的{guest_list[0]}，我想邀请你来参加晚餐。")
print(f"亲爱的{guest_list[1]}，我想邀请你来参加晚餐。")
print(f"亲爱的{guest_list[2]}，我想邀请你来参加晚餐。")
print(f"很遗憾，{guest_list[1]}无法赴约。")
guest_list[1] = '特斯拉'
print(f"亲爱的{guest_list[0]}，我想邀请你来参加晚餐。")

guest_list.insert(1, '爱迪生')
guest_list.insert(2, '霍金')
guest_list.append('图灵')
print(f"亲爱的{guest_list[0]}，我想邀请你来参加晚餐。")
print(f"亲爱的{guest_list[1]}，我想邀请你来参加晚餐。")
print(f"亲爱的{guest_list[2]}，我想邀请你来参加晚餐。")
print(f"亲爱的{guest_list[3]}，我想邀请你来参加晚餐。")
print(f"亲爱的{guest_list[4]}，我想邀请你来参加晚餐。")
print(f"亲爱的{guest_list[5]}，我想邀请你来参加晚餐。")

print("很抱歉，我只能邀请两位嘉宾共进晚餐。")
removed_guest = guest_list.pop()
print(f"很抱歉，{removed_guest}，我无法邀请你来共进晚餐。")
removed_guest = guest_list.pop()
print(f"很抱歉，{removed_guest}，我无法邀请你来共进晚餐。")
removed_guest = guest_list.pop()
print(f"很抱歉，{removed_guest}，我无法邀请你来共进晚餐。")
removed_guest = guest_list.pop()
print(f"很抱歉，{removed_guest}，我无法邀请你来共进晚餐。")
print(f"亲爱的{guest_list[0]}，我依然邀请你来参加晚餐。")
print(f"亲爱的{guest_list[1]}，我依然邀请你来参加晚餐。")

del guest_list[0]
del guest_list[0]
print(guest_list)