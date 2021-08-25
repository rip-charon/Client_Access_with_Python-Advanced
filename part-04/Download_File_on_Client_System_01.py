#CHARON :
# Too simple program for writeing and reading .txt file content

# Write something on .txt file : 

f = open("text.txt" , "w")

f.write("hello !")

f.close()

# READ .txt File and print :

f = open("text.txt" , "r")

print(f.read())

f.close()