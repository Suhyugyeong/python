import re

def match_check(regex, string):
    if re.search(re.compile(regex), string):
        print(f"{regex}, {string} is Match!")
    else:
        print(f"{regex}, {string} is" +'\033[101m' + "NOT" + '\033[0m' + "Match!")
    