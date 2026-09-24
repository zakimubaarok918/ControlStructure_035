nilai = input("Masukkan nilai siswa:")
if nilai >= 90:
    print("Excellent performance")
elif nilai >= 80:
    print("Very Good performance")
elif nilai >= 70:
    print("Good performance")
elif nilai >= 60:
    print("Average performance")  
else:
    print("Needs improvement")

for steps in range(1,4):
    print(Steps)      

n = int(input("Masukkan n:"))

a = 0
b = 1

for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c

n = int(input("Masukkan n:"))

for i in range(n):
    for j in range(i + 1):
        print("*", end="")
    print()