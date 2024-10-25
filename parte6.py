f = open("practicas.txt", "w")
f.write("ya no tengo fans!")
f.close()

#open and read the file after the overwriting:
f = open("practicas.txt", "r")
print(f.read())
