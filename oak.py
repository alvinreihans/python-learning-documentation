# misal, variabel a = 10 dan b = 5. variabel c sengaja diberi nilai 0 agar dianggap sebagai variabel
a = 10
b = 5
c = 0

if a > b:
    c = a
elif a < b:
    c = b

print("value of address " + str(id(a)) + " is " + str(a))
print("value of address " + str(id(b)) + " is " + str(b))
print("the biggest value between address a and b is " + str(c))
print("so, the value of address " + str(id(c)) + " will be " + str(c))
