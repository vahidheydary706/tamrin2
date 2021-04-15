a = float(input("Hour: "))
b = float(input("Minute: "))
c = float(input("Second: "))

print("{hour} : {minute} : {second}")

d = a * 3600
e = b * 60

x = d + e + c

print(f"Seconds: {x}")
