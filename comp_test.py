import pyomp
import time

print(pyomp.eval5(51, 48, 0, 1, 2))

s = time.time()
for i in range(10000000):
    c = i % 10
    pyomp.eval7(c, c + 10, c + 20, c + 30, c + 40, c + 15, c + 25)     
print (time.time() - s)
