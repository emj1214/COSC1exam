# assume that n <= m
# a) the loop would go through up to m+(m-1)+(m-2)...+1 equality checks, because if there were no duplicates, every m would run through the remaining ns
# b) if the first list is in order and the second list isn't, you could either cheat the system and sort the second list and go to the next line, OR you could run the out of order list against the ordered list the same way we ran the first which would likely speed things up because the odds that the second list is the exact reerse of the first list are slim to none. Everytime you remove a duplicate or a non-duplicate, save it in the third list so that by the end you have a single list without any duplicates. this could possibly have as many comparisons as the first problem, but could have as few as the third problem if you sort or just get really lucky
# c) if both lists are in order, id compare the two by placement of each item: if there was a duplicate, I'd add it to a third list and remove it from both lists; if I found a non-duplicate, I'd add the smaller item to the third list, remove that, and then check the same place in the list for a duplicate now that a larger number has taken it's place. This would result in up to m+n-2 equlity comparisons if there were no duplicates and it alternated between the two lists of which had the smaller value, and possibly as little as just n comparisons