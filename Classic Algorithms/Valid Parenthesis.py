

def isValid(s):
    stack = []

    for item in s:

        if item in ["(", "{", "["]:

            stack.append(item);

        elif len(stack) == 0:

            return False

        else:

            poppedItem = stack.pop()

            if item == ")" and poppedItem != "(":
                return False

            if item == "}" and poppedItem != "{":
                return False

            if item == "]" and poppedItem != "[":
                return False

    else:

        if len(stack) == 0:
            return True
        else:
            return False


# Driver Code

# True
result = isValid("([])")
print(result)

# False
result = isValid("(((")
print(result)

# True
result = isValid("(){}[]")
print(result)

# False
result = isValid("({}([]")
print(result)