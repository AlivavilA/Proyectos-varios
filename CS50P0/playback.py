def main():
    x=input()
    print(slow(x))
    

def slow(s):
    sl = s.replace(" ","...")
    return sl

main()