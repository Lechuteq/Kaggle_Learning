# Codewars first task
def main():
    interlockable(input("a: "), input("b: "))
    print("Done")

def interlockable(a, b):

    #  <----  hajime!
    a=bin(int(a))
    b=bin(int(b))

    a_len=len(a)
    b_len=len(b)

    print(f"a: {a}")
    print(f"b: {b}")
    i=max(a_len,b_len)
    print(f"i: {i}")

if __name__ == "__main__":
    main()