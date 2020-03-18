import re
 
src_str = "abcdefgABCDEFG"          # 置き換える前の文字列
pattern = r"[aA]"                   # 置き換えられる文字列のパターン
dst_str = re.sub(pattern, "1", src_str, 1)   # 第4引数に「1」を追加
print(dst_str);