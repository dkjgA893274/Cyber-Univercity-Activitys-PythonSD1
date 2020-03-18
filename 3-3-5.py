import re
 
string = "It is fine today."
pattern = r"[a-zA-Z]+"
match_list = re.findall(pattern,string)
print(match_list)