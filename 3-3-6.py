import re
 
string = "It is fine today."
pattern = re.compile(r"[a-zA-Z]+")
match_list = pattern.findall(string)
print(match_list)