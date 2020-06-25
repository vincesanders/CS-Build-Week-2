def decodeString(s: str, output='') -> str:
    '''
    This is a recursive function to findt the decoded string.
    '''
    # set the index to 0
    i = 0

    # if an empty string is passed, we're at the end of our string
    if s == '':
        return ''

    # set letter to be the first character in the string
    letter = s[i]
    print(s)
    if letter.isdigit():

        #initialize repeats to an empty string, this will later be cast to an int
        repeats = ''

        # set the current character
        current = s[i]

        # get full number, in case it's multiple digits
        while current != '[':
            repeats += current
            i +=1
            current = s[i]

        # once we have the full number, cast it to an int
        repeats = int(repeats)

        # get the substring to be repeated
        # set the beginning index of the next substring to send to the decode string function
        # we don't want to send the opening bracket
        beginning_index = i + 1
        i += 1

        num_brackets = 1
        # loop till we find the end of the substring to be repeated
        while num_brackets > 0:
            if current == '[':
                num_brackets += 1
            elif current == ']':
                num_brackets -= 1
            if i < len(s) - 1:
                i += 1
            current = s[i]

        # set the ending index of the substring
        ending_index = i

        # We want the substring to include the ], so we set ending index of the substring to ending_index + 1
        return repeats * decodeString(s[beginning_index:ending_index + 1]) + decodeString(s[ending_index + 1:])

    elif letter.isalpha():

        #keep track of the values that will be added to the output
        val_to_add = ''

        # set the current character
        current = s[i]

        # loop through the characters, to ensure you add all alpha charaters to the output
        while not current.isdigit() and i < len(s) and current != ']':
            val_to_add += current
            i += 1
            if i < len(s):
                current = s[i]
        
        # if we end on a digit, we need to calculate the rest of the value to add
        # by sending the remainder of the substring to the decodeString function
        if current.isdigit():
            return val_to_add + decodeString(s[i:])

        # else we return the value
        return val_to_add
    return output

string = "3[a]2[bc]"
string2 = "3[a2[c]]"
string3 = "2[abc]3[cd]ef"
string4 = "abc3[cd]xyz"
string5 = "3[a]2[b4[F]c]"

print(decodeString(string5))