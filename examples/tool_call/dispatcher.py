from tools import sum, uppercase


def execute(name: str, **kwargs):
    if name == "sum":
        return sum(**kwargs)
    elif name == "uppercase":
        return uppercase(**kwargs)