print("Mohammed Ali, 251A007")

length = int(input("Enter word length: "))

with open("sample.txt", "r") as f:
    data = f.read().split()

for word in data:
    if len(word) == length:
        print(word)
