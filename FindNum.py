
def find_num(mylist):
    myDict={}
    for item in mylist:
        try:
            myDict[item]+=item
        except:
            myDict[item]=1
    return myDict

lastNumbers= find_num([1,2,4,5,6])

print(lastNumbers, ' this si last numb')