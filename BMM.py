a = int(input("Number1 "))
b = int(input("Number2 "))

if a > b:
    print("Errer!!!")

else:
    for i in range(1,a+1):
        if a % i == 0 and b % i == 0:
            bmm = i
print(f"BMM:  {bmm}")

