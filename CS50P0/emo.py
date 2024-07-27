def main():
    x=input()
    print(emoj(x))
    

def emoj(s):
    sl = s.replace(":)","🙂") 
    sl = sl.replace(":(","🙁")
    return sl

main()