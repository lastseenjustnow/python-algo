from Stack import MyStack


# Challenge 6: Evaluate Postfix Expression Using a Stack
def evaluate_post_fix(exp):
    # Write your code here
    v = MyStack()
    for ch in exp:
        try:
            v.push(int(ch))
        except ValueError:
            int1, int2 = v.pop(), v.pop()
            v.push(eval(str(int2) + ch + str(int1)))

    return v.peek()


# Challenge 7: Next Greater Element Using a Stack
def next_greater_element(lst):
    stack = MyStack()
    res = [-1] * len(lst)
    # Reverse iterate list
    for i in range(len(lst) - 1, -1, -1):
        ''' While stack has elements and current element is greater 
        than top element, pop all elements '''
        while not stack.is_empty() and stack.peek() <= lst[i]:
            stack.pop()
        ''' If stack has an element, top element will be 
        greater than ith element '''
        if not stack.is_empty():
            res[i] = stack.peek()
        # push in the current element in stack
        stack.push(lst[i])
    for i in range(len(lst)):
        print(str(lst[i]) + " -- " + str(res[i]))
    return res



