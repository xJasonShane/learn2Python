# 在字符串中使用变量
# 要在字符串中插入变量的值，可在前引号前加上字母f​，再将要插入的变量放在花括号内。
# f是format（设置格式）的简写，因为Python通过把花括号内的变量替换为其值来设置字符串的格式。
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

# 利用与变量关联的信息来创建完整的消息
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")

# 使用f字符串来创建消息，再把整条消息赋给变量
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)

# f字符串是Python 3.6引入的。