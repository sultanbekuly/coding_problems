
def countdown(i):
    print(i)
    #base case
    if(i <= 1):
        return 0
    #recursive case
    else:
        countdown(i-1)

countdown(5)
