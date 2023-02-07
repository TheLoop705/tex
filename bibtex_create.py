import os

existing_bib = open("./reports/mybib.source", "r").readlines()

# remove empty lines
existing_bib = [line for line in existing_bib if line.strip() != ""]
# remove lines that begin with %
existing_bib = [line for line in existing_bib if line.strip()[0] != "%"]

# separte each line by space and store in a list
existing_bib = [line.split() for line in existing_bib]

# create dict from existing_bib list
bib_dict = {}

for line in existing_bib:
    try:
        name = line[0]
        url = line[1]
        url = url.replace("_", "\_")
        bib_dict[name] = url
    except Exception:
        pass

# print(bib_dict)
form = """
@online{%s,
\t url = {%s}
}
"""

with open("./reports/mybib.bib", "w") as f:
    for k, v in bib_dict.items():
        f.write(form % (k, v))
