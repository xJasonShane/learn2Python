# 在程序中，额外的空白可能令人迷惑。
# 可以使用.rstrip()方法删除字符串末尾的空白。
favorite_language = 'python  '
print(favorite_language.rstrip())
# 这种方法只是暂时的，重新打印仍然会显示空格
# 可以使用重新赋值方法覆盖内容
favorite_language = favorite_language.rstrip()
print(favorite_language)
# 删除字符串开头的空白可以使用.lstrip()方法
favorite_language = '  python'
print(favorite_language.lstrip())
# 删除字符串两端的空白可以使用.strip()方法
favorite_language = '  python  '
print(favorite_language.strip())
