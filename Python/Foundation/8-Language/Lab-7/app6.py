
print("=============Sir===================")
for x in range(5):
    for i in range(5):
         print("*", end=" ")
    print()


print("==============Sir==================")
for x in range(5):
    for i in range(x + 1):
         print("*", end=" ")
    print()

print("=============Sir===================")
for x in range(5):
    for i in range(5 - x):
         print("*", end=" ")
    print()

print("=============Sir===================")
for p in range(10):
    for q in range(5-p if p<5 else p+1-5):
        print("*", end=" ")
    print()


print("================================")
for m in range(6, 0, -1):
    for n in range(1, m + 1):
        print("*", end=" ")
    print()

print("================================")

for k in range(1, 8):
       for l in range(0, k-1):
            print("*", end=" ")
       print()

print("================================")

for i in range(1, 6):
    for j in range(1, 6):
        print("*", end=" ")
    print()