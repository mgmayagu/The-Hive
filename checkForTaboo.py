tabooList = ['fudge', 'dayamn','yeet', 'die']
def check(input):
    inputText = input
    for value in tabooList:
        if (inputText.find(value) != -1):
            return True
    return False

def replaceTaboo(input):
    inputText = input
    for value in tabooList:
        if (inputText.find(value) != -1):
            # print ("Found Taboo Word ")
            inputText = inputText.replace(value, '***')
    return inputText
