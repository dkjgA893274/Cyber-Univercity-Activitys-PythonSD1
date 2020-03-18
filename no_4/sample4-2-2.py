def print_greeting(weather="晴れ"):
    greeting = "こんにちは。今日は" + weather + "ですね。"
    return greeting

string = print_greeting()
print(string)

string = print_greeting("雨")
print(string)

