s = input()
stack = []
count = 0
for i in s:
    if i == '(':
        stack.append(i)
    else:
        count+=1
    if len(stack) > 0 and stack[-1] == '(' and i == ')':
        stack.pop()
        count-=1
print(len(stack)+count)
