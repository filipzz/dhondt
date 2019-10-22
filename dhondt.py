import json
from heapq import heappush, nlargest, nsmallest
from math import ceil

#2015 parties = ["PIS", "PO", "PSL", "KUK", "PET"]
parties = ["KOB", "KON", "PSL", "PIS", "LEW", "NIE"]
winnerParty = "PIS"
noOfSwitches = 6
#divs = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]
divs = []
for i in range(460):
    divs.append(i+1)

totalSwaps = 0
switch = []

#with open('results2015.json') as f:
with open('results2019.json') as f:
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
                print("\n\tLast: " + partyName + "\t" + "{:,.2f}".format(val).replace(","," ") + '\t' + str(div))
            results[partyNumber] = results[partyNumber] + 1
            seatNumber = seatNumber + 1
            lastSeatVal = val
            lastSeatPartyNumber = partyNumber
            lastSeatPartyName = partyName
            lastSeatDiv = div
            #resultsLoc[lastSeatPartyNumber] = results[lastSeatPartyNumber] + 1

    #for i in range(len(parties)):
    #    print(parties[i] + "\t" + str(results[i]))




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



    print("\n\tLost: " + loserSeatPartyName + "\t" + "{:,.2f}".format(loserSeatVal).replace(","," ") + "\t" + str(loserSeatDiv))
    print("\nDecyduje: **" + str(ceil(currentMargin)) + "** głosów\n\n\n\n")

    print('```\n\n\n\n```')

    ## rysowanie tabeli d'hondta

    strg = "x"
    for partyNumber in range(len(partyList)):
        strg += "|\t" + parties[partyNumber] + "\t"
    print(strg)

    strg = ":---: "
    for partyNumber in range(len(partyList)):
        strg += "|\t---:\t"
    print(strg)

    strg = "\# mandatów"
    for partyNumber in range(len(partyList)):
        strg += "|\t" + str(results[partyNumber]) + "\t"
    print(strg)

    for i in range(numOfSeats):
        div = divs[i]
        strg = "" + str(div) + "\t"
        for partyNumber in range(len(partyList)):
            if votes[partyNumber]/div >= lastSeatVal:
                strg += "|\t**" + "{:,.2f}".format(votes[partyNumber]/div).replace(","," ") + "**\t"
            else:
                strg += "|\t"  + "{:,.2f}".format(votes[partyNumber]/div).replace(","," ") + "\t"
        print(strg)

    ## koniec rysowania


    #swapping results
    #results[lastSeatPartyNumber] = results[lastSeatPartyNumber] - 1
    #results[loserSeatPartyNumber] = results[lastSeatPartyNumber] + 1


    foundRealLoser =  0
#    #else:
     #   chng = round(lastSeatDiv * margin)
      #  print(str(round(lastSeatDiv * margin)))

    return (currentMargin, results, lastSeatPartyName, loserSeatPartyName)



recount = []
repeatIn = 0

results = []
for i in range(len(parties)):
    results.append(0)


for row in data:
#if len(parties) > 0:
 #   row = data[0]
    okrNr = str(row["field1"])#str(row["FIELD1"])
    okrName = str(row["field2"])#row["FIELD2"]
    okrSeats = row["field3"]#row["FIELD3"]
    votesInvalid = row["field21"] #row["FIELD22"]
    votesValid = row["field20"] #row["FIELD26"]
    votesOut = row["field27"] + row["field30"]+row["field32"] + row["field34"]#row["FIELD29"] + row["FIELD30"] + row["FIELD32"] + row["FIELD35"] + row["FIELD36"] + row["FIELD37"] + row["FIELD38"] + row["FIELD39"] + row["FIELD40"] + row["FIELD41"] + row["FIELD42"] + row["FIELD43"]
    pr = '\n#' + okrNr + '\t' + okrName + '\t\n\nLiczba mandatów: **' + str(okrSeats) + '**\n\nliczba głosów ważnych: **' + "{:,}".format(votesValid).replace(","," ") + '**\n\n'
    print(pr)
    print("\nLiczba głosów nieważnych: **" +  "{:,}".format(votesInvalid).replace(","," ") + "**")
    print("\nLiczba głosów oddanych na partie, poza sejmem: **" +  "{:,}".format(votesOut).replace(","," ") + "**" )
    votes = []
    votes.append(row["field26"]) #KOB
    votes.append(row["field28"]) #KON
    votes.append(row["field29"]) # PSL
    votes.append(row["field31"]) #PIS
    votes.append(row["field33"]) # LEW
    votes.append(row["field35"]) # NIE
    #2015
    #votes.append(row["FIELD27"]) #pis 2015
    #votes.append(row["FIELD28"]) #po
    #votes.append(row["FIELD31"]) #psl
    #votes.append(row["FIELD33"]) #kukiz
    #votes.append(row["FIELD34"]) #petru
    #for i in range(len(votes)):
        #print("\t" + parties[i] + "\t" + str(votes[i]))

    (margin, res, lwinner, loser) = findSeats(parties, okrSeats, votes)

    if margin <= votesInvalid:
        recount.append((margin,  okrNr,  okrName, votesInvalid, lwinner, loser))
        repeatIn = repeatIn + 1

    if lwinner == winnerParty:
        switch.append((margin, loser, okrNr, okrName))


    for i in range(len(res)):
        results[i] = results[i] + res[i]

print("\n\nWyniki wyborów\n")
print("x|\# posłów")
print(":---:|---:")
for i in range(len(parties)):
    print( parties[i] + ' | ' + str(results[i]))

print("\n\n")


print("\nCo by było gdyby...")
print("\nokręg wyborczy\tpartia\tliczba głosów")
for (margin, loser, okrNr, okrName) in nsmallest(noOfSwitches, switch):
    print("\n" + okrNr + "\t" + okrName + "\t" + loser + "\t" + str(ceil(margin)))
    totalSwaps = totalSwaps + ceil(margin)


print(str(totalSwaps))


print("\n# Powtórka potrzebna " + str(repeatIn) + " okręgach:\n\n")
print("nr |okrąg | różnica | \# nieważnych | ostatni | nie wszedł")
print("---: | :--- | ---: | ---: | ---: | ---:")
for (margin, okrNr, okrName, votesInvalid, lwinner, loser) in nsmallest(repeatIn, recount):
    print(str(okrNr) + "\t|" + okrName + "\t|" + "{:,}".format((ceil(margin))).replace(","," ") + "\t|" + "{:,}".format((votesInvalid)).replace(","," ") + "\t|" + lwinner + "\t|" + loser)
