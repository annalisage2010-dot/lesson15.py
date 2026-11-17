import os
print("----Science Notes----")
with open("science.txt", "r") as f:
    for line in f:
        print(line.strip())
print()

print("----Word Count----")
with open("Maths.txt", "r")as f:
    for line in f:
        words = line.strip()
        print(len(words), "words >", line.strip())
print()

print("----Merging of Notes----")
if os.path.exists("all-notes.txt"):
    print("all-notes.txt already exists - overwritten")
else:
    print("all-notes.txt does not exist - creating a new one")

content = ""
with open("science.txt", "r") as f:
    content += f.read() + "\n"
with open("Maths.txt", "r") as f:
    content += f.read() + "\n"
with open("all-notes.txt", "w") as out:
    out.write(content)
print("Saved to all-notes.txt")
print()

if os.path.exists("all-notes.txt"):
    os.remove("all-notes.txt")
    print("all-notes.txt is deleted")
else:
    print("all-notes.txt is not deleted")