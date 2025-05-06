def gcd(a, b):
    if b == 0: 
        return abs(a)
    else:
        return gcd(b, a % b)

a = int(input())
b = int(input())
result = gcd(a, b)
print(f"НОД({a}, {b}) = {result}")
 
# Сложность = O(log(n)), каждый шаг сокращает одно из числел, поэтому сложность O(log(n))