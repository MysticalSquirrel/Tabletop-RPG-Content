print("Please enter the maximum amount of levels you want to be made available. (Default: 20)")
levels = input()

if levels.isdigit() is False:
    levels = 20
else:
    levels = int(levels)

print("Please enter the maximum amount of experience you want to be made available. (Default: 1\'000\'000)")
last_exp = input()
if last_exp.isdigit() is False:
    last_exp = 1000000
else:
    last_exp = int(last_exp)

print("Please enter the minimum level you want to make your players start from. (Default: 1)")
min_level = input()
if min_level.isdigit() is False:
    min_level = 1
else:
    min_level = int(min_level)

print("Please enter the fraction factor you want the exp based upon. (Default: 1.0)")
fraction = input()
if fraction.isdigit() is False:
    fraction = 1.0
else:
    fraction = float(fraction)

fraction = fraction/levels

counter = levels
counter_fraction = fraction
total = 0
needed = 0

results_file = open("../Exp_Results.txt", "w")
results_file.write("Experience Chart\n\nLevel:Total:Needed\n---------------\n")

for i in range(min_level, levels):
    result = counter_fraction * last_exp/counter
    total += result
    needed = result
    result_write = str(i) + ":" + str(int(total)) + ":" + str(int(needed))
    results_file.write(result_write + "\n")
    i += 1
    counter -= 1
results_file.close()

results_file = open("../Exp_Results.txt", "r")
print("Results written to Exp_Results.txt:")
for j in range(min_level, levels):
    print(results_file.read(j))
results_file.close()

quit()
