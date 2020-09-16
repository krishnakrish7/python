def swaplist(newlist) :
    newlist[0], newlist[-1] = newlist[-1], newlist[0]
    return newlist
newlist = [12,13,15,25]
print(swaplist(newlist))
