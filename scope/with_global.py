x = 10
print("Initial value of x (global):", x)

def modify_global():
    global x
    x = 20

modify_global()
print("Changed variable to local:",  x)
