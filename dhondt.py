import json
from heapq import heappush, nlargest, nsmallest
from math import ceil

parties = ["PIS", "PO", "PSL", "KUK", "PET"]
winnerParty = "PIS"
noOfSwitches = 6
#divs = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]
divs = []
for i in range(20):
    divs.append(i+1)

totalSwaps = 0
switch = []

with open('results2015.json') as f:
    data = json.load(f)


def findSeats(partyList, numOfSeats, votes):
    dhondt = []
    results = []
    for i in range(len(partyList)):
        results.append(0)

    for i in range(numOfSeats):
        div = divs[i]
        for partyNumber in range(len(partyList)):
            item = (votes[partyNumber]/div, partyList[partyNumber], partyNumber, div)
            heappush(dhondt,item)

    seatNumber = 1

    results = []
    for i in range(len(parties)):
        results.append(0)

    for (val, partyName, partyNumber, div) in nlargest(numOfSeats,dhondt):
            if seatNumber == numOfSeats:
                print('\tLast: ' + partyName + '\t' + str(val) + '\t' + str(div))
            results[partyNumber] = results[partyNumber] + 1
            seatNumber = seatNumber + 1
            lastSeatVal = val
            lastSeatPartyNumber = partyNumber
            lastSeatPartyName = partyName
            lastSeatDiv = div
            #resultsLoc[lastSeatPartyNumber] = results[lastSeatPartyNumber] + 1

    currentMargin = 1000000

    for i in range(len(parties)):
        if i != lastSeatPartyNumber:
            div = results[i] + 1
            value = votes[i] / div
            marginNow = div * (lastSeatVal - value)
            marginNowLast = lastSeatDiv * (lastSeatVal - value)
            marginNow = min(marginNow, marginNowLast)
            if marginNow < currentMargin:
                loserSeatVal = value
                loserSeatPartyNumber = i
                loserSeatPartyName = parties[i]
                loserSeatDiv = div
                currentMargin = marginNow



    print("\tLost: " + loserSeatPartyName + "\t" + str(loserSeatVal) + "\t" + str(loserSeatDiv))
    print("Decyduje: " + str(ceil(currentMargin)) + " głosów")

    #swapping results
    #results[lastSeatPartyNumber] = results[lastSeatPartyNumber] - 1
    #results[loserSeatPartyNumber] = results[lastSeatPartyNumber] + 1


    foundRealLoser =  0
#    #else:
     #   chng = round(lastSeatDiv * margin)
      #  print(str(round(lastSeatDiv * margin)))

    return (currentMargin, results, lastSeatPartyName, loserSeatPartyName)





results = []
for i in range(len(parties)):
    results.append(0)


for row in data:
#if len(parties) > 0:
    #row = data[22]
    okrNr = str(row["FIELD1"])
    okrName = row["FIELD2"]
    okrSeats = row["FIELD3"]
    votesValid = row["FIELD26"]
    pr = '\n' + okrNr + '\t' + okrName + '\t' + str(okrSeats) + '\t' + str(votesValid)
    print(pr)
    votes = []
    votes.append(row["FIELD27"]) #pis 2015
    votes.append(row["FIELD28"]) #po
    votes.append(row["FIELD31"]) #psl
    votes.append(row["FIELD33"]) #kukiz
    votes.append(row["FIELD34"]) #petru
    #for i in range(len(votes)):
        #print("\t" + parties[i] + "\t" + str(votes[i]))

    (margin, res, lwinner, loser) = findSeats(parties, okrSeats, votes)

    if lwinner == winnerParty:
        switch.append((margin, loser, okrNr, okrName))


    for i in range(len(res)):
        results[i] = results[i] + res[i]

print("\n\nWyniki wyborów")
for i in range(len(parties)):
    print(parties[i] + '\t' + str(results[i]))

print("\n\n")


print("Co by było gdyby...")
print("okręg wyborczy\tpartia\tliczba głosów")
for (margin, loser, okrNr, okrName) in nsmallest(noOfSwitches, switch):
    print(okrNr + "\t" + okrName + "\t" + loser + "\t" + str(ceil(margin)))
    totalSwaps = totalSwaps + ceil(margin)


print(str(totalSwaps))
