import typer

app = typer.Typer()

@app.command
def zamican():
    iashik = 0
    count = 0
    
    def sredn(Add_number: int):
        nonlocal iashik, count
        count += 1
        iashik += Add_number
        return (iashik / count)
    return sredn
