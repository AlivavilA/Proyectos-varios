def main():
    hello()
    name = input("What's your name?: ").strip().title()
    hello(name)
    #Obtener el area de un circulo
    pi = 3.14
    radius = 2.2
    area = pi*(radius**2)
    print(area) 
    #Small Calculator
    x = float(input("x ="))
    y= float(input("y ="))
    z = x + y
    a = x - y
    b = x * y
    c = x / y
    print("suma= ",z)
    print("resta=", a)
    print("mult=",b)
    print(f"div={c:.2f}")
    sq = square(x)
    print("square =", sq)

def hello(n="world"):
    print("Hello, ", n)

def square(m):
    return m ** 2
main()