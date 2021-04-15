a = int(input("Number1 "))
b = int(input("Number2 "))

if a > b:
    print("Errer!!!")

else:
    for i in range(b, a * b + 1):
        if i % a == 0 and i % b == 0:
            kmm = i
            break
print(f"KMM:  {kmm}")

