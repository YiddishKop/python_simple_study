import re

def Main():
    line = "I think I understand regular expression"

    matchResult = re.match('think', line, re.M|re.I)
    if matchResult:
        # matchResult.group() is result matched
        print("Match Found: " + matchResult.group())
    else:
        print("No Match Found")
    searchResult = re.search('think', line, re.M|re.I)
    if searchResult:
        print("Search Found: " + searchResult.group())
    else:
        print("Nothing found in search")

if __name__ == "__main__":
    Main()
