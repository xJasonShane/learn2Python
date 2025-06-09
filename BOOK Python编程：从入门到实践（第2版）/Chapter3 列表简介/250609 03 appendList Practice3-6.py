# Q:你刚找到了一个更大的餐桌，可容纳更多的嘉宾。请想想你还想邀请哪三位嘉宾。
# Q:以完成练习3-4或练习3-5时编写的程序为基础，在程序末尾添加一条print 语句，指出你找到了一个更大的餐桌。使用insert() 将一位新嘉宾添加到名单开头。使用insert() 将另一位新嘉宾添加到名单中间。使用append() 将最后一位新嘉宾添加到名单末尾。打印一系列消息，向名单中的每位嘉宾发出邀请。
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
