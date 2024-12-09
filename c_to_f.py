# Ethan Lawrence
# Dec 9 2024
# C to F

continue_looping = True
temps1 = []
temps2 = []
while continue_looping:
    temps1.append(int(input('Enter a temp in C. Enter "-9999" to show the calculations:     ')))
    if temps1[-1] == -9999:
        for temp_c in temps1:
            temps2.append((temp_c * 2) + 30)
        else:
            print(temps2)
            continue_looping = False