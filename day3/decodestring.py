def decodeString(self, s: str) -> str:
    if s is None:
        return None
    
    repeats = []
    
    # intialize the output as array with a single empty string
    # We'll be adding to it as we move through the encoded string
    output = [""]
    num = 0

    for char in s:
        if char.isdigit():

            # check for double digits
            num = num * 10 + int(char)

        elif char == "[":

            # We've reached the end of our number,
            # so append to repeats array
            repeats.append(num)
            num = 0

            # [ will not display on the output, so append empty string
            output.append("")

        elif char.isalpha():

            # add chars to string at last index
            output[-1] += char

        elif char == "]":

            # pop the string we've been builing out of the output array
            string = output.pop()

            # pop the number of times it should be repeated from repeats array
            # and add the repeats to the string
            string = string * repeats.pop()

            # add the string to the last string in the output array 
            # (the string previous to the one we were just working on)
            output[-1] += string

    # rebuild the decoded string from the output array.
    return "".join(output)