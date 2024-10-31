#! /C:\Users\Admin\AppData\Local\Microsoft\WindowsApps\python.exe

def imprime(lista):
    """impresión recursiva de una lista
    con enfoque primero ; restantes"""
    # casos triviales ... 
    print("( ", end="")
    if len(lista) == 0:
        print(")", end="")
        return
    print(lista[0], end=", ") # ... primero
    imprime(lista[1:]) # restantes: Recursion
    print(")", end="")
    
    
    
if __name__ == "__main__":
    
    l = [33,22,11]
    imprime(l)
    print()
    
    l = [22,11]
    imprime(l)
    print()

    l = [11]
    imprime(l)
    print()
    
    l = []
    imprime(l)
    print()