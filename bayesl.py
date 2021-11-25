import math,random
data = open("saDataProcessed.csv","r")
dataArr = data.read().splitlines()
random.shuffle(dataArr)
trainData = dataArr[0:math.floor(2*(len(dataArr)/3))]
testData = dataArr[math.floor(2*(len(dataArr)/3)):]
frequenciesPositive = dict()
frequenciesNegative = dict()
vocabulary = dict()
ocurrencesNegative=0
ocurrencesPositive=0
for line in trainData:
    label,contents = line.split(",")
    if label=="0":
        ocurrencesNegative+=1
        for word in contents.split():
            frequenciesNegative[word]=frequenciesNegative[word]+1 if word in frequenciesNegative.keys() else 1
            vocabulary[word]=1
    else:
        ocurrencesPositive+=1
        for word in contents.split():
            frequenciesPositive[word]=frequenciesPositive[word]+1 if word in frequenciesPositive.keys() else 1
            vocabulary[word]=1
#total word frequencies
TWFPositive=0
TWFNegative=0
for keyP,keyN in zip(frequenciesPositive,frequenciesNegative):
    TWFPositive+=frequenciesPositive[keyP]
    TWFNegative+=frequenciesNegative[keyN]

for keyP,keyN in zip(frequenciesPositive,frequenciesNegative):
    keyPValue = frequenciesPositive[keyP] if keyP in frequenciesPositive.keys() else 0
    keyNValue = frequenciesNegative[keyN] if keyN in frequenciesNegative.keys() else 0
    frequenciesPositive[keyP]=(keyPValue+1)/(TWFPositive+len(vocabulary)+1)
    frequenciesNegative[keyN]=(keyNValue+1)/(TWFNegative+len(vocabulary)+1)

def predictSentiment(string):
    probNegative=ocurrencesNegative/(ocurrencesNegative+ocurrencesPositive)
    probPositive=ocurrencesPositive/(ocurrencesNegative+ocurrencesPositive)
    for word in string.split():
        freqPositive = frequenciesPositive[word] if word in frequenciesPositive.keys() else 1/(TWFPositive+len(vocabulary)+1)
        freqNegative = frequenciesNegative[word] if word in frequenciesNegative.keys() else 1/(TWFNegative+len(vocabulary)+1)
        probPositive*=freqPositive
        probNegative*=freqNegative
    return "0" if probNegative>probPositive else "1"
accuracy=0
for line in testData:
    predicted = line.split(",")[0]
    observed = predictSentiment(line.split(",")[1])
    if predicted==observed:
        accuracy+=1
print("acurácia do modelo: ",accuracy/len(testData))
while True:
    print("Testando modelo, digite a frase a ser testada:(ingles somente)")
    
    print("a palavra possui conotação ","negativa" if predictSentiment(input())=="0" else "positiva")
