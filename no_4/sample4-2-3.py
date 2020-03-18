def print_greeting(*weather_list):
    for weather in weather_list:
        string = "こんにちは。今日は" + weather + "ですね。\n"
        print(string)

print_greeting("雨")

print_greeting("雨","晴れ","曇り")

w_list = ["雨","晴れ","曇り"]
print_greeting(*w_list)