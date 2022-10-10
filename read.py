#Provide the txt doc file you want to read from
f=open("sample.txt.txt","r+")
d=f.read()
e=open("samp2.txt", "r+")
e.write(d.replace('>', '> ')) #Ignore if your document alread contains spaced words
e.close()
s=open("samp2.txt", "r+")
t=s.readlines()
c = 0
for line in t:
   word=line.split(" ")
   for i in word:
     if i=="</soapenv:": #Replce with the word you want to count
       c+=1
print(c)



   






