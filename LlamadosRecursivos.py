def impresion_iterativa():
    for i in range(10):
        print(i)

def impresion_recursiva(i):
    if i < 10:
        print(i)
        impresion_recursiva(i + 1)

print("Imperativa:")
impresion_iterativa()
print("Recursiva:")
impresion_recursiva(0)
