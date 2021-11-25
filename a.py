a = open("saDataProcessed.csv","r")

b=open("saDataProcessedSmall.csv","w")
l = ""
i=0
for line in a:
    if i>1000:
        break;
    l+=line
    i+=1
b.writelines(l)