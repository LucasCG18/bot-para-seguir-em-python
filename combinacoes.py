import itertools

# Define the characters to be used
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

# Generate all combinations of characters up to length 2
combinations = []
for length in range(1, 3):
    combinations += itertools.product(alphabet, repeat=length)

# Write the combinations to a text file
with open("combinations.txt", "w") as f:
    for combo in combinations:
        try:
            f.write('//*[@id="mount_0_0_' + str(combo)[2] + str(combo)[7] + '"]/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/div[3]/div/div[1]/button' "\n")
            f.write('//*[@id="mount_0_0_' + str(combo)[2] + str(combo)[7] + '"]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/div[3]/div/div[1]/button' "\n")
        except:
            print()