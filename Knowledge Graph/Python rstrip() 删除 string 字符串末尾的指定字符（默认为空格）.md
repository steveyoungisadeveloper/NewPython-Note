Python rstrip() 删除 string 字符串末尾的指定字符（默认为空格）

语法：
  str.rstrip([chars])

参数： chars 是要删除的指定字符

实例：

这是code
``` Python
#!/usr/bin/python

str = "     this is string example....wow!!!     ";
print str.rstrip();
str = "88888888this is string example....wow!!!8888888";
print str.rstrip('8');
```

这是结果
```Python
this is string example....wow!!!
88888888this is string example....wow!!!

```
