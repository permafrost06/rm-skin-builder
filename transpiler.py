import re

def transpileRMS(SkinScriptString: str)-> str:
    TranspiledString = SkinScriptString.replace('\n\n','\n')

    arrayMatches = re.finditer(r';@;arr (?P<varName>[a-zA-Z0-9]*) = (?P<arrItems>.*?);@;', TranspiledString)
    loopMatches = re.finditer(r'(?s);@;loop (?P<loopVar>[a-zA-Z0-9]*).*?\n(?P<loopText>.*?)\n;@;', TranspiledString)

    scriptArrs = {}

    def getArrayItemsFromString(itemsStr: str):
        itemsStr = itemsStr.replace(" ", "")
        return itemsStr.split(",")

    for x in arrayMatches:
        scriptArrs[x["varName"]] = getArrayItemsFromString(x["arrItems"])
        TranspiledString = TranspiledString.replace(x.group(), "")

    for x in loopMatches:
        output: str = ""
        for idx, item in enumerate(scriptArrs[x["loopVar"]]):
            output += x["loopText"].replace("{item}", item).replace("{idx}", str(idx + 1))
            output += "\n"
        
        TranspiledString = TranspiledString.replace(x.group(), output)
    
    return TranspiledString