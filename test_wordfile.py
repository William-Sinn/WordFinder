text = open("words.txt", "r")
# if "tca" in text.read():
#     print("yes")

# test = "2"
# print(test)
# test = test.upper()
# print(test)

lower = open("words_lower.txt", "w")

for line in text.readlines():

    lower.write("-" + line.lower().rstrip("\n") + "-\n")
