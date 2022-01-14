# Auhtor: CMOB 1/14/2022

def count_e(string):
    count = 0
    whats = 0
    e = "E"
    for index, value in enumerate(string):
        if "E" in value:
            count += 1
            print(value)
        elif "e" in value:
            count += 1
            print(value)
    return count


print(count_e("REEEEEEEEEEEEEEEEEeeeeeeeeeee"))
