def main():
    m=int(input("M:"))
    print("E:", light(m))
    
    

def light(s):
    E = s*(300000000**2)
    return E

main()