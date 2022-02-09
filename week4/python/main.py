plainnya=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C"," "]
ciphernya=["D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S",
"T","U","V","W","X","Y","Z"," "]

bil_huruf=[]
sente=input("Sentence :")
sentence_up=sente.upper()
for i in range(len(sentence_up)):
    for j in range(len(plainnya)):
        if (sentence_up[i]==" "):
            bil_huruf.append(26)
            break
        
        if plainnya[j]==sentence_up[i]:
            bil_huruf.append(j)
print("Result :")
for k in range(len(bil_huruf)):
    print(ciphernya[bil_huruf[k]],end=" ")


#Decryptage


plainnya=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q",
          "R","S","T","U","V","W","X","Y","Z"," "]
ciphernya=["D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S",
           "T","U","V","W","X","Y","Z","A","B","C"," "]
bil_huruf=[]
sente=input("Sentence :")
sentence_up=sente.upper()
for i in range(len(sentence_up)):
    for j in range(len(ciphernya)):
        if (sentence_up[i]==" "):
            bil_huruf.append(26)
            break
        
        if ciphernya[j]==sentence_up[i]:
            bil_huruf.append(j)
print("Hasil :")
for k in range(len(bil_huruf)):
    print(plainnya[bil_huruf[k]],end=" ")