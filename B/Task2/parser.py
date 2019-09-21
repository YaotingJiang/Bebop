import sys, json, argparse

parser = argparse.ArgumentParser()
parser.add_argument("-up", help="sort the output in ascending order, this is the default", action="store_true", default=True)
parser.add_argument("-down", help="sort the output in descending order", action="store_true")
args = parser.parse_args()

def readJsonSeries(inputString):
    inputJson = []
    
    def munchArray():
        jsonEnd = inputString.index("]")
        array = inputString[1:jsonEnd].split(",")
        if array[0][0] != "\"":
            raise Exception("Array does not start with string")
        array[0] = array[0].replace("\"", "")
        inputJson.append(array)
        return inputString[jsonEnd+1:].strip()
    
    def munchString():
        jsonEnd = inputString[1:].index("\"") + 1
        string = inputString[1:jsonEnd]
        inputJson.append(string)
        return inputString[jsonEnd+1:].strip()
    
    def munchObject():
        jsonEnd = inputString.index("}")
        obj = json.loads(inputString[0:jsonEnd+1])
        if "this" not in obj or not isinstance(obj["this"], str):
            raise Exception("Object does not have string this property")
        inputJson.append(obj)
        return inputString[jsonEnd+1:].strip()
    
    while len(inputString) != 0:
        firstCharacter = inputString[0]
        if firstCharacter == "[":
            inputString = munchArray()
        elif firstCharacter == "\"":
            inputString = munchString()
        elif firstCharacter == "{":
            inputString = munchObject()
        else:
            raise Exception("invalid start of json", firstCharacter)
    return inputJson
                             

inputJson = sys.stdin.read()
jsonSeries = readJsonSeries(inputJson)

def getKeyString(inputtedJson):
    if isinstance(inputtedJson, list):
        return inputtedJson[0]
    elif isinstance(inputtedJson, dict):
        return inputtedJson["this"]
    else:
        return inputtedJson

jsonSeries.sort(key=getKeyString, reverse=args.down)
print(jsonSeries)
