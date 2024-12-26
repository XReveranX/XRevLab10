def zamican():
    iashik = 0
    count = 0
    
    def sredn(Add_number):
        nonlocal iashik, count
        count += 1
        iashik += Add_number
        return (iashik / count)
    return sredn
