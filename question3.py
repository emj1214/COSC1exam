# this is our array, you can add numbers or remove them if you want. I put this here for practice, but if you want to scrap this line and the final line to just enter "sort([array])" into the command line, that would produce the same result. 
a = [7, 2, 9, 4]

# this is our function 
def sort(a):

    # for each value x in our array, we run the function inside that calls on each y value in the array (except the first value). If the value next to x in the array is smaller than x, the two values switch spots so they end up in the correct ascending order.
    for x in range(len(a)):    
        for y in range(x+1, len(a)):    
            if a[x] > a[y]:    
                a[x], a[y] = a[y], a[x]
    print(a)

# this calls the function, but if you decide to scrap the first line, cut this one too and call it in the command line with an array in place of a
sort(a)