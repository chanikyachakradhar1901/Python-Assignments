#Section 1: Loop Basics (1–10)

# 1. Print numbers from 1 to 50
for i in range(1, 51):
    print(i)

# 2. Even numbers from 1 to 100
for i in range(1, 101):
    if i % 2 == 0:
        print(i)

# 3. Odd numbers from 1 to 100
for i in range(1, 101):
    if i % 2 != 0:
        print(i)

# 4. Multiplication table of 7
for i in range(1, 11):
    print(7 * i)

# 5. Sum of 1 to 100
total = 0
for i in range(1, 101):
    total += i
print(total)

# 6. Reverse from 50 to 1
for i in range(50, 0, -1):
    print(i)

# 7. Count numbers divisible by 3
count = 0
for i in range(1, 101):
    if i % 3 == 0:
        count += 1
print(count)

# 8. Squares 1 to 10
for i in range(1, 11):
    print(i*i)

# 9. Cubes 1 to 10
for i in range(1, 11):
    print(i**3)

# 10. Input n, print 1 to n
n = int(input("Enter number: "))
for i in range(1, n+1):
    print(i)

 #Section 2: While Loop (11–15)

 # 11. Print 1 to 20
i = 1
while i <= 20:
    print(i)
    i += 1

# 12. Factorial
n = int(input("Enter number: "))
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print(fact)

# 13. Reverse number
num = int(input("Enter number: "))
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num //= 10
print(rev)

# 14. Count digits
num = int(input("Enter number: "))
count = 0
while num > 0:
    count += 1
    num //= 10
print(count)

# 15. Input until "stop"
while True:
    user = input("Enter something: ")
    if user == "stop":
        break

#Section 3: Nested Loop (16–20)
# 16. Pattern *
for i in range(1, 5):
    print("*" * i)

# 17. Pattern numbers
for i in range(1, 5):
    for j in range(1, i+1):
        print(j, end="")
    print()

# 18. Table 1 to 5
for i in range(1, 6):
    for j in range(1, 11):
        print(i*j, end=" ")
    print()

# 19. A B C pattern
for i in range(3):
    for j in ["A", "B", "C"]:
        print(j, end=" ")
    print()

# 20. 1 to 9 matrix
num = 1
for i in range(3):
    for j in range(3):
        print(num, end=" ")
        num += 1
    print()

#Section 4: String Basics (21–25)
# 21. Count characters
s = input("Enter string: ")
count = 0
for i in s:
    count += 1
print(count)

# 22. Count vowels
vowels = "aeiouAEIOU"
count = 0
for ch in s:
    if ch in vowels:
        count += 1
print(count)

# 23. Count consonants
count = 0
for ch in s:
    if ch.isalpha() and ch not in vowels:
        count += 1
print(count)

# 24. Reverse string
rev = ""
for ch in s:
    rev = ch + rev
print(rev)

# 25. Palindrome check
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

#Section 5: String Slicing (26–30)
s = input("Enter string: ")

# 26. First 5 chars
print(s[:5])

# 27. Last 3 chars
print(s[-3:])

# 28. Reverse string
print(s[::-1])

# 29. Every 2nd char
print(s[::2])

# 30. Remove first & last
print(s[1:-1])

#Section 6: List Basics (31–35)

# 31. Sum of list
lst = [1, 2, 3, 4, 5]
print(sum(lst))

# 32. Max value
print(max(lst))

# 33. Min value
print(min(lst))

# 34. Count elements
count = 0
for i in lst:
    count += 1
print(count)

# 35. Check element exists
x = int(input("Enter element: "))
if x in lst:
    print("Exists")
else:
    print("Not Exists")

#Section 7: List Operations (36–40)

lst = []

# 36. Append 3 elements
lst.append(10)
lst.append(20)
lst.append(30)
print(lst)

# 37. Insert at index
lst.insert(1, 15)
print(lst)

# 38. Remove element
lst.remove(20)
print(lst)

# 39. Reverse without reverse()
rev = []
for i in range(len(lst)-1, -1, -1):
    rev.append(lst[i])
print(rev)

# 40. Sort without sort()
for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]
print(lst)


