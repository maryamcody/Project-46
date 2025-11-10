f1 = open("firstfile.txt", "r")
f2 = open("secondfile.txt", "r")

print("Content of the first file before appending:\n",f1.read())
print("Content of the second file before appending:\n", f2.read())


f1.close()
f2.close()


f1 = open("firstfile.txt", "r")
f2 = open("secondfile.txt", "w")

f2.write(f1.read())



f2.seek(0)
f1.seek(0)

print("Content of first file after appending:\n", f1.read())
f1.close()
f2.close()