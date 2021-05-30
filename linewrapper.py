import html

def main (): 

    textFile = open("input.txt", "r")
    outputFile = open("output.txt", "w")
    escapedText = html.escape(textFile.read())
    splittedText= escapedText.splitlines()
    
    for line in splittedText:
        quotsy = "\""
        comma = ","
        linus = quotsy + line
        linus2 = linus + quotsy + comma + "\n"
        outputFile.write(linus2)
        print(linus2)
        


    textFile.close()
    outputFile.close()




if __name__ == '__main__':
    main()