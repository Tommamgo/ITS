abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] 
new = ""
index = 0

print("Bitte geben sie Rotationzahl ein")
count = input()
count = int(count)%len(abc)
print("Geben Sie das zu verschlüsselne Wort ein")
text =input()
text = text.upper()
#print(count)
for i in text:
    try:
        index = abc.index(i)
        if(index+int(count) >= len(abc)):
            new += abc[index + int(count) - (len(abc))]
        else:
            new+=abc[index+int(count)]
    except:
        new+=i

print(new)

