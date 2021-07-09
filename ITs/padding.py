print("Geben Sie den Text fuer das Padding ein")
text = input()
print("Geben Sie die Blocklaenge ein")
padding = input()
res = text.encode("utf-8").hex()
le = int(padding) - (len(text)%int(padding))

for i in range(le):
    res+=str('{:02x}'.format(le))

print(res)
