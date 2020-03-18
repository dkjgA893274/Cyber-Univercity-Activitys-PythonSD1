import re
 
src_str = "abcdefgABCDEFG"          # 置き換える前の文字列
pattern = r"[a]"                   # 置き換えられる文字列のパターン
dst_str = re.sub(pattern, "1", src_str, 0, re.I)   # 第4引数を「0」に変更し、第5引数に「re.I」追加
print(dst_str);