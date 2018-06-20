import string

#string.punctuation & string.digit 都是string的方法

strip = string.punctuation + string.digit # 去除符号和数字

word = word.strip(strip)
