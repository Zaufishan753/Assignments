Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for i in range(1,6):
...     for j in range(1,i+1):
...         print(j, end="")
...     print()
... 
...     
1
12
123
1234
12345
