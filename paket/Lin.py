import typer

app = typer.Typer()

@app.command
def linearize_rec(massive: list):     #massive - массив для линериализации
    otv = []
    for key_1 in massive:
        if  isinstance(key_1, list):
            buf=linearize_rec(key_1)
            for key_2 in buf:
                otv.append(key_2)
        else:
            otv.append(key_1)
    return otv
