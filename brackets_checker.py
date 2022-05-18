def brackets_checker(string):
    brackets = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    stack = [];
    for char in string:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets:
            if len(stack) == 0:
                return False
            if stack[-1] == brackets[char]:
                stack.pop()
            else:
                return False

    return len(stack) == 0


print(brackets_checker('(]()[)')) #False
print(brackets_checker('[,jshdb{}sdff(ssdf(df({[]})))]')) #True
print(brackets_checker('[,jshdb{}sdff(ssdf(df{({[]})}))]')) #True
print(brackets_checker('[,jshdb{}sdff(ssdf(df{({[]}))})]')) #False
print(brackets_checker('[,jshdb{}sdff((([][)))]')) #False
print(brackets_checker('перва(я) скобище {dfghdfh{dfhdfh[dfgfhdf]}dffdfgh(dfh)drhdfh}')) #True
