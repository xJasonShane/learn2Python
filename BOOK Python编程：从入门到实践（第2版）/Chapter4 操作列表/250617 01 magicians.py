magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# 在循环中执行更多的操作
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
# Python根据缩进来判断代码行与前一个代码行的关系。
print("Thank you, everyone. That was a great magic show!")

# 缩进错误
# 1. 忘记缩进，例如在for循环内本应缩进的代码没有缩进，这样可能导致报错
# 2. 忘记额外缩进，例如在for循环中有多个需要缩进的代码，其中最后忘记缩进，可能不会报错，但是会产生逻辑错误
# 3. 不必要的缩进，例如在不需要缩进的代码行使用了缩进，可能造成逻辑错误或者直接报错
message = "Hello Python world!"
# IndentationError: unexpected indent
#    print(message)

# 遗漏冒号，在for循环的代码语句中遗漏了冒号，Python会报错
# SyntaxError: expected ':'
#for magician in magicians
#    print(magician)
