f = open("practicas.txt", "a")
f.write("ahora tengo mas fans!")
f.close()

#open and read the file after the appending:
f = open("practicas.txt", "r")
print(f.read())
