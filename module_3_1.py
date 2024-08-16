calls = 0
count_calls = calls
globals()

def string_info(string):
    len_string = len(string)
    string_upper = string.upper
    string_lower = string.lower
    count_calls
    return len_string, string.upper, string.lower



def is_contains(string: str, list_: list):
    count_calls()
    if string.lower() in (i.lower for i in list_):
        return True

    else: False





print(string_info("Capybara"))
print(string_info("Armageddon"))
print(is_contains("Urban", ["ban", "BaNaN", "uRBAN"]))  # Urban ~urBAN
print(is_contains("cycle", ["recycling", "cyclic"]))  # matches
print(calls)












