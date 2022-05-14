import re

def transpileRMS(SkinScriptString: str)-> str:
    # remove empty lines
    TranspiledString = SkinScriptString.replace('\n\n','\n')

    # match arrays
    arrayMatches = re.finditer(r';@;arr (?P<varName>[a-zA-Z0-9]*) = (?P<arrItems>.*?);@;', TranspiledString)
    # match loops
    loopMatches = re.finditer(r'(?s);@;loop (?P<loopVar>[a-zA-Z0-9]*).*?\n(?P<loopText>.*?)\n;@;', TranspiledString)

    # dict to store script arrays
    scriptArrs: dict[str, list] = {}

    # split string into array items
    def getArrayItemsFromString(itemsStr: str)-> list[str]:
        # remove whitespace
        itemsStr = itemsStr.replace(" ", "")
        return itemsStr.split(",")

    for match in arrayMatches:
        matchedText = match.group()

        varName = match["varName"]
        arrItems = getArrayItemsFromString(match["arrItems"])

        # store array in dict
        scriptArrs[varName] = arrItems

        # remove matched string
        TranspiledString = TranspiledString.replace(matchedText, "")

    for match in loopMatches:
        matchedText = match.group()

        loopVar = match["loopVar"]
        loopText = match["loopText"]

        output: str = ""
        # loop over looptext or template string and replace placeholders with values
        for idx, item in enumerate(scriptArrs[loopVar]):
            output += loopText.replace("{item}", item).replace("{idx}", str(idx + 1))
            output += "\n"
        
        # replace matched string with generated string
        TranspiledString = TranspiledString.replace(matchedText, output)
    
    return TranspiledString