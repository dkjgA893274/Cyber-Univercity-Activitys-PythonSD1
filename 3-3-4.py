import re
 
src_str = "Words, words, words."          # 分割される前の文字列
pattern = r"\s+"                          # 区切り文字列のパターン
dst_list = re.split(pattern, src_str)
print(dst_list)