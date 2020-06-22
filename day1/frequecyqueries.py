def freqQuery(queries):
    # Create an array to store output
    output = []
    # Create a dictionary to store key: value, value: frequency of value
    freqByVal = {}

    # iterate through the queries
    for q in queries:

        if q[0] is 1:

            # if the value is in the dictionary, increment the frequency
            # if not, initialize the frequency for the value to one
            if q[1] in freqByVal:
                freqByVal[q[1]] += 1
            else:
                freqByVal[q[1]] = 1

        elif q[0] is 2:

            # if the value exists in our dictionary, decrement its frequency
            if q[1] in freqByVal:

                #if its frequency is already at 0, don't decrement
                if freqByVal[q[1]] > 0:
                    freqByVal[q[1]] -= 1
        else:
            freqIsPresent = 0
            # if the frequency is in the values of our dictionary, return 1
            if q[1] in set(freqByVal.values()):
                freqIsPresent = 1
            output.append(freqIsPresent)

    return output