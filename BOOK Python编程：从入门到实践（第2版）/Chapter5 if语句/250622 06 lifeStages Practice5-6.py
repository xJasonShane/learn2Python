# Q:设置变量age 的值，再编写一个if-elif-else 结构，根据age 的值判断一个人处于人生的哪个阶段。如果年龄小于2岁，就打印一条消息，指出这个人是婴儿。如果年龄为2（含）～4岁，就打印一条消息，指出这个人是幼儿。如果年龄为4（含）～13岁，就打印一条消息，指出这个人是儿童。如果年龄为13（含）～20岁，就打印一条消息，指出这个人是青少年。如果年龄为20（含）～65岁，就打印一条消息，指出这个人是成年人。如果年龄超过65岁（含）​，就打印一条消息，指出这个人是老年人。

age = 12
if age < 2:
    print("You are a baby.")
elif age < 4:
    print("You are a toddler.")
elif age < 13:
    print("You are a kid.")
elif age < 20:
    print("You are a teenager.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are an elder.")
