import json
import re
a = "15년"
new_a = re.findall('[0-9]+', a)
print(new_a[0])
print(type(int(new_a[0])))
a = 10
for i in range(10):
    print (i)