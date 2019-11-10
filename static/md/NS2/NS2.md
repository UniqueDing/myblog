#网络安全 2

##注册机
```python
name = input()
count = 0
for i in name:
    if ord(i) > 97:
        i = chr(ord(i) - 32)
    count += ord(i)
print(count^0x1234^0x5678)
```