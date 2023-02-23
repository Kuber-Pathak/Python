def strip_replace(string, word):
    newstr = string.replace(word, " ")
    return newstr.strip()


this = "  kuber is  Hero  "
str = strip_replace(this, "kuber")
print(str)
