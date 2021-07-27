from os import listdir
from os.path import isfile, join
import sys
import json

onlyfiles = [f for f in listdir('D:/doc/ml/bajaj/archive') if isfile(join('D:/doc/ml/bajaj/archive', f))]

onlyfiles.remove('dataScript.py')
onlyfiles.remove('master.txt')
mergedData=[]
# print(onlyfiles[0])
f=open(onlyfiles[0])
# print(json.load(f))
for i in range(80000):
    mergedData.append(0)
for i in onlyfiles:
    f=open(i)
    data=json.load(f)
    for (index,j) in enumerate(data):
        for k in j:
            try:
                mergedData[index][k]=j[k]
            except:
                pass

print(json.dump(mergedData))


    