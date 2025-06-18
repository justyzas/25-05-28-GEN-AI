from tools import sum, uppercase

import json

def execute(functionEx):
    print(functionEx)

    args = json.loads(functionEx.arguments)

    if functionEx.name == "sum":
        return sum(**args)
    elif functionEx.name == "uppercase":
        return uppercase(**args)