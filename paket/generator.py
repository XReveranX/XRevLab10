def func(N):
    print(N)

def besk_posl(Num_of_repeat):
    numb = 2
    while True:
        b=0
        for i in range(8):
            if ((numb % (i+2)) == 0) and (b==0):
                b=1
            elif (b==0):
                for i in range(Num_of_repeat):
                    yield (func(numb))
                    b=1
        numb += 1

#a=besk_posl(2)
#for i in a:
#    None