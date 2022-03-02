# write a function the finds the second largest integer from a list, don't use sort or max()setopt ksh_arrays

def second(numberlist):

    # defines the variables a and b to have no value
    a = b = 0
    # for each value in the array, if the number is greater than b and greater than or equal to a where a and b start as 0, 0, but later become values from the array, then the values are reassigned and the program tries again; if x is the second largest number (meaning that only a is larger), then it reassigns the value to the variable b and returns b in the terminal.
    for number in numberlist:
        if number > b and number >= a:
            b = a
            a = number
        else:
            b = number
    return b

# this changes our integer into a string so we can print it nicely in a sentence :)
x = str(second([3,1,6,8,29,10]))
print("the second largest number is " + x)