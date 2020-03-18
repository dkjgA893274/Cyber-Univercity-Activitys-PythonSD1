try:
    input1 = input('1つ目の整数を入力してください：>> ')
    x = int(input1) #文字列として入力された引数を整数に変換
except ValueError:
    print("整数を入力してください")
    sys.exit()
if(x%5==0):
    print("割り切れる")
else:
    print("だめ")
