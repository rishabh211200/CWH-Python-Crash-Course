i = 0
while i < 10:
    if i==3:
        continue
    print(i)
    i += 1
# while(True):
#     print("Program is not finishing")
print("Program has finished executing")

while(True):
    num = int(input("Enter a number: "))
    print(num)
    if num == 0:
        break