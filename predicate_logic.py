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
                    while len(stack) > 0 and (stack[-1][0] in obj_names or stack[-1][0] in obj_variables):
                        string = (string + stack.pop())
                    stack.append(string)
                elif i == '*':
                    stack.append(i)
                elif i in obj_names or i in obj_variables:
                    string = i
                    while len(stack) > 0 and (stack[-1] == '*'):
                        string = (string + stack.pop())
                    stack.append(string)
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
            
# checks if a polish notation sentence is well-formed.
def wffcheck (sentence):    
# wffcheck_pt_1 () takes a sentence as an input and returns 1 iff it meets certain criteria. if it returns 0, then the sentence is not well-formed.
# If it returns 1 it might not be well-formed if an object or varaible or star is in the place of a Sentence Letter, so running it a second time after the stars an any objects
# or variables except the onese following quantifiers can rule out that case.
# basically does the same thing as Polish to infix if it can generate a single sentence w/ no leftovers,
    def wffcheck_pt_1(wff):
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
                        while len(stack) > 0 and (stack[-1][0] in obj_names or stack[-1][0] in obj_variables):
                            string = (string + stack.pop())
                        stack.append(string)
                    elif i == '*':
                        stack.append(i)
                    elif i in obj_names or i in obj_variables:
                        string = i
                        while len(stack) > 0 and (stack[-1] == '*'):
                            string = (string + stack.pop())
                        stack.append(string)
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
#removes stars and any non-first place objects/variables
    def star_and_relata_remover(wff):
        biconditional_fixer = wff.replace("<>", "<").replace('\u2203','3').replace('\u2200','4')
        no_star = biconditional_fixer.replace('*','')
        no_star_list = list(no_star)
        relata_remover_stack = []
        for x in no_star_list:
            if x not in obj_names and x not in obj_variables:
                relata_remover_stack.append(str(x))
            else:
                if len(relata_remover_stack) > 0 and relata_remover_stack[-1] in quantifiers:
                    relata_remover_stack.append(x)
        out = ''.join([str(element) for element in relata_remover_stack])
        return out
    if wffcheck_pt_1(sentence) == 1 and wffcheck_pt_1(star_and_relata_remover(sentence)) == 1:
        return 1
    else:
        return 0
    
# takes an sentence as an input and returns 1 iff well-formed infix sentence 0 iff not well-formed                
def infix_wff_check(wff):
    polwff = infixtopolish(wff)
    if wffcheck(polwff) == 1:
        re_infix = polishtoinfix(polwff)
        if re_infix == wff.replace('3','\u2203').replace('4','\u2200'):
            return 1
        else:
            return 0
    else :
        return 0
