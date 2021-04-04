
cap_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
operator_chars = ['~', '&', 'v', '>', '<']
monadic_chars = ['~']
dyadic_chars = ['&', 'v', '>', '<']
obj_names = ["a", "b", "c", "d", "e", "f", "g", "h", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u"]
obj_variables = ["w", "x", "y", "z"]
quantifiers = ["3", "4"]

def infixtopolish (infix):
    stack = []
    postfix = []
# subs '<' for '<>' also subs out unicode 'for all' and 'for some' for '4' and '3' 
    character_fixer = infix.replace("<>", "<").replace('\u2203','3').replace('\u2200','4')
# make a list of the infix sentence and read it right to left
    infixmirror = list(character_fixer)
    infixmirror.reverse()

    for i in infixmirror:
        if i in cap_letters or i == '~' or  i in obj_names or i in obj_variables or i == "*":
            postfix.append(i)
        elif i in dyadic_chars or i in quantifiers or i == ')':
            stack.append(i)            
        elif i == '(':
            # use while loop to handle avoid Index errors caused when sentence has parentheses error
            while True:
                try:
                    while stack[-1] != ')':
                        postfix.append(stack.pop())
                    stack.pop()
                    break
                except Exception:
                    return 'Not a wff'
        else:
            return 'Not a wff'
    
    postfix[:] = ['<>' if x=='<' else x for x in postfix]
    polish_list = postfix
    polish_list.reverse()
    polish_string = ''.join(polish_list).replace('3','\u2203').replace('4','\u2200')
    return polish_string


def polishtoinfix (wff):
    stack = []
    character_fixer = wff.replace("<>", "<").replace('\u2203','3').replace('\u2200','4')
    # make a list and of Polish wff and read it right to left
    wffmirror = list(character_fixer)
    wffmirror.reverse()
    while True:
        try:
            for i in wffmirror:
                if i in cap_letters:
                    string = i
                    while len(stack) > 0 and (stack[-1] in obj_names or stack[-1] in obj_variables):
                        string = (string + stack.pop())
                    stack.append(string)
                elif i in obj_names or i in obj_variables:
                    stack.append(i)
                elif i == '~':
                    string = '~' + stack.pop()
                    stack.append(string)
                elif i in dyadic_chars:
                    string = '(' + stack.pop() + i + stack.pop() + ')'
                    stack.append(string)
                elif i in quantifiers:
                    string = '(' + i + stack.pop() + ')' + stack.pop()
                    stack.append(string)
                else:                    
                    return 'Not a wff'
            if len(stack) == 1:
                return stack[0].replace('3','\u2203').replace('4','\u2200')
            else:
                return 'Not a wff'
        except Exception:
            return 'Not a wff'
            
                
def infix_wff_check(wff):
    polwff = infixtopolish(wff)
    re_infix = polishtoinfix(polwff)
    if re_infix == wff.replace('3','\u2203').replace('4','\u2200'):
        return 1
    else:
        return 0

def wffcheck(wff):
    stack = []
    biconditional_fixer = wff.replace("<>", "<").replace('\u2203','3').replace('\u2200','4')
    # make a list and of Polish wff and read it right to left
    wffmirror = list(biconditional_fixer)
    wffmirror.reverse()
    while True:
        try:
            for i in wffmirror:
                if i in cap_letters:
                    string = i
                    while len(stack) > 0 and (stack[-1] in obj_names or stack[-1] in obj_variables):
                        string = (string + stack.pop())
                    stack.append(string)
                elif i in obj_names or i in obj_variables:
                    stack.append(i)
                elif i == '~':
                    string = '~' + stack.pop()
                    stack.append(string)
                elif i in dyadic_chars:
                    string = '(' + stack.pop() + i + stack.pop() + ')'
                    stack.append(string)
                elif i in quantifiers:
                    string = '(' + i + stack.pop() + ')' + stack.pop()
                    stack.append(string)
                else:                    
                    return 0
            if len(stack) == 1:
                return 1
            else:
                return 0
        except Exception:
            return 0

