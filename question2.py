class ListNode:
    def __init__(self, item, next_node):
        self.item = item
        self.next_node = next_node

# I added i to help make the function recursive without it running forever
def lists_equal(p1, p2, i):

    # here I'm comparing the number of items in each list using item as an array.
    if len(p1.item) == len(p2.item):

        # If the lengths are equal, then we check each individual item. If the function runs into a pair of items that aren't equal, then it throws the error that the lists aren't equal.
        if p1.item[i] != p2.item[i]:
            print("these lists are not equal")
        # If the checked pair of items ARE equal, then the code prints an update to let you know how it's going so far and triggers the function to run again in a recursive fashion.
        else:
            print("List items " + str(i+1) + " are equal...")
            
            # This if statement allows the function to end when we reach the end of our lists, which will either end in a "Hooray!" when there aren't any errors, or if there are still items to be checked it starts the function over again
            if i+1 == len(p1.item):
                print("Hooray! These lists are equal!")
            else:
                return lists_equal(p1, p2, i+1)
    
    # If the lengths are not equal, then our lists can't be equal so the function prints "these lists are not equal"      
    else:
        print("these lists are not equal")
        

# these are my test items and test lists
item1 = [1, 2, 3, 4, 5]
item2 = [1, 2, 3, 4, 5]
list1 = ListNode(item1, None)
list2 = ListNode(item2, None)

#here's the function being called
lists_equal(list1, list2, 0)