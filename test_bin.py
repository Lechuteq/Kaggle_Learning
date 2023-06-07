# Codewars first task
def main():
    interlockable(input("a: "), input("b: "))
    print("Done")

def interlockable(a, b):

    #  <----  hajime!
    a=bin(int(a))
    b=bin(int(b))
    out = True

    a_len=len(a)
    b_len=len(b)

    #print(f"a: {a}")
    #print(f"b: {b}")
    k=max(a_len,b_len)-2
    #print(f"i: {i}")

    for i in range(k):
        if a(i) is b(i):
            out = True
        else:
            out = False
    return out

if __name__ == "__main__":
    main()