import re
s1 = "SiliconLabs"

for i in s1:
    print i

match = re.match ("lab", "siliconlab")

match.group(1)
