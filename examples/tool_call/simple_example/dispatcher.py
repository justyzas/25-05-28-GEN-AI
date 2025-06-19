from tools import sum, uppercase

# f-jos pavadinimas, parametrai buna perduodami į šią funkciją
def execute(name: str, **kwargs):
    if name == "sum":
        return sum(**kwargs)
    elif name == "uppercase":
        return uppercase(**kwargs)