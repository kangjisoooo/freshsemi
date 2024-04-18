Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> thumbdrive edition
SyntaxError: invalid syntax
>>> def rain_water(lists):
...     if not lists:
...         return 0
... 
...     n = len(lists)
...     left_max = [0] * n
...     right_max = [0] * n
... 
...     left_max[0] = lists[0]
...     for i in range(1, n):
...         left_max[i] = max(left_max[i-1], lists[i])
... 
...     right_max[n-1] = lists[n-1]
...     for i in range(n-2, -1, -1):
...         right_max[i] = max(right_max[i+1], lists[i])
... 
...     water_amount = 0
...     for i in range(n):
...         water_amount += min(left_max[i], right_max[i]) - lists[i]
...     return water_amount
... # 예시
... list1 = [0,1,0,2,1,0,1,3,2,1,2,1]
... print(rain_water(list1))  # 출력: 6
... list2 = [4,1,0,1,1,3,1,3,2,0,0,2,3]
... print(rain_water(list2))  # 출력: 19
... list3 = [8,0,2,4,6,8,10]
