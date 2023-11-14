# Fibonacci numbers and series


def Fibona():
    N = int(input("Enter your number : "))
    f1 = 1
    f2 = 1
    fn = f1 + f2
    while fn <= N:
        f1 = f2
        f2 = fn
        fn = f1 + f2
    print("The first Fibonacci number greater than N is " + str(fn))
    print(" \n" + " ")
    a = 1
    b = 1
    res = a + b
    c = a + b
    while c <= N:
        if c <= N:
            res += 1/c
            a = b
            b = c
            c = a + b
    print("The reciprocal Fibonacci constant W defined by the infinite sum " + "\n"
            + "W = sum(1/Fn) in this case is equal to : " + str(res))



Fibona()