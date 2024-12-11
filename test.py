def otvoreny_stvorec(a):
    for i in range (a):
        print("#", end="")
    print()
    
    for j in range(a-2):
        print("#", end="")
        for k in range(a-2):
            print(" ", end="")
        print("#", end="")
        print()
    
    for l in range (a):
        print("#", end="")


otvoreny_stvorec(6)
