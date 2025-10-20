# 과제 11
a = input("숫자를 5개 입력하시오: ")
list_a = list(map(int,a.split()))
print(list_a)
b= int(input("숫자 1개를 입력하시오: "))
list_a.append(b)
print(list_a)

# 과제12
b  = input("숫자를 5개 입력하세요: ")
list_b = list(map(int,b.split()))
del list_b[3:]
print(list_b)

# 과제 13
c = list(map(int, input("숫자를 5개 입력하세요: ").split()))

for index, value in enumerate(c, start = 101):
    print(index, value)

# 과제 14
a = [ 10, 20, 30, 40, 30, 20, 10]
result = a.count(20)

print(result)

# 과제 15
a = list(map(int,input("숫자 10개를 입력하세요: ").split()))
min_value = min(a)
max_value = max(a)

print(min_value, " and ", max_value)

# 과제 16
a = list(map(int,input("숫자 10개를 입력하세요: ").split()))
a.remove(max(a))
a.remove(min(a))

result = sum(a)
print(result)

# 과제 17
a = [10, 20, 30, 40, 30, 20, 10]
while 20 in a:
    a.remove(20)
print(a)

# 과제 18
a = [i for i in range(1,6)]
print(a)

# 과제 19
a = [i for i in range(1,21,2)]
print(a)

# 과제 20
a, b = map(int,input("정수를 2개 입력하세요:").split())
result = [2 ** i for i in range(a, b+1)]

del result[1]
del result[-2]

print(result)

# 과제 21
a = input("Hello,World!를 입력하세요: ")
result = a.replace("Hello", "Hi")
print(result)

# 과제 22
a = input("문자 4개를 입력하세요: ")
a = " / ".join(a)
print(a)

# 과제 23

name = input(" 이름의 성을 영어로 입력하세요: ")
change_name = name.rjust(10).lower()
print(change_name)

# 과제 24
prices = input("가격을 입력하세요: ").split(";")
prices = [int(i) for i in prices]
prices.sort(reverse=True)

for i in prices:
    print(str(i).rjust(9))



