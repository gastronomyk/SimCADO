"""
A code snippet to generate the Keywords document
"""

import os

text = """
# List of Keywords for Controlling SimCADO
"""

f = open("../data/default.config", "r")
data = f.readlines()
f.close()

i=0
while i < len(data)-1:
    if "#####" in data[i]:
        i += 1
        text += "#" + data[i]
        text += """
```
Keyword                 Default     [units] Explanation
-----------------------------------------------------------------------------------------------
"""
        i += 1
    elif data[i] == "\n" and data[i+1] == "\n":
        text += "```\n"
        i += 1
    else:
        text += data[i]
        i += 1
    
    
f = open("./source/Keywords.md", "w")
f.write(text) 
f.close()