
import re

file = '''---
this is one
---    
this two
---  
this is three
---
'''

parts = re.split('^--- *$', file)
print(parts)
print("Part 1: " + parts[1])
print("Part 2: " + parts[2])


parts2 = file.split("---")
print(parts2)
print("Part2 1: " + parts2[1])
print("Part2 2: " + parts2[2])