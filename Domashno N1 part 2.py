n = input("Enter encoded string: ")
result = ""
for i in range(0, len(n), 2):
    result = result + n[i] * int(n[i + 1])
print(result)