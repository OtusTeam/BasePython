import os

print(os.name)
print(os.getcwd())
print(os.listdir())

filename = "example.txt"

if os.path.isfile(filename):
    # os.remove(filename)
    os.unlink(filename)
print(f"file {filename} exists? {os.path.exists(filename)}")

# file = open(filename, 'w')
# file.write("Hello world!\n")
# file.close()

with open(filename, "w") as file:
    file.write("Hello world!\n")
    file.write("Hello again!\n")
    file.write("Bye bye!\n")
    print("file is still open")
print("file closed")

with open(filename, "r") as file:
    for line in file:
        print(f"line: {line!r}")

with open(filename, "a") as file:
    file.write("Thank you!\n")


print(f"file {filename} exists? {os.path.exists(filename)}")
