from stack import Stack

matchDict = {"(":")", "[":"]", "{":"}", ")":"(", "]":"[", "}":"{"}

def validP(inputString):
    tracker = Stack()
    for char in inputString:
        if char in list(matchDict.keys())[:3]:
            tracker.push(char)
        elif char in list(matchDict.keys())[3:] and matchDict[char] in tracker.returnAsList():
            tracker.pop()
        elif char in matchDict.values() and tracker.is_empty():
            return False
    return tracker.is_empty()
        
            
    
    
