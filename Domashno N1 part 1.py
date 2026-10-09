n = input("Enter string: ")
result = ""
count = 1
for i in range(1, len(n)):
    if n[i] == n[i-1]:
        count = count + 1
    else:
        result = result + n[i-1] + str(count)
        count = 1
result = result + n[-1] + str(count)
print(result)