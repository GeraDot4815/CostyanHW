
LS = '-' #line symbol
def print_with_lines(text: str, linelen=-1, symbol=LS, needspace=True) -> str:
    if linelen==-1 : linelen=len(text)

    output = (symbol * linelen + '\n' +
            text
            + '\n' + symbol * linelen
            + '\n'*needspace)

    return output

def liminput(tip:str, limit:int=10):
    inp=input(tip)[:limit]
    return inp