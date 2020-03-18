def print_greeting(weather):
    greeting = "こんにちは。今日は" + weather + "ですね。"
    return greeting
 
print(print_greeting("晴れ"))
print(print_greeting("雨"))
print(print_greeting("曇り"))