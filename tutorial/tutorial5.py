import re
print(dir(re))
for x in dir(re):
    if 'find' in x:
        print x
