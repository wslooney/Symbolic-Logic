import predicate_logic

rules_tuple = ('Assume', 'Premise', 'R', '&I', '&E', 'vI', 'vE', '>I', '>E', '~I', '~E', '<>I', '<>E', 'MT', 'HS', 'DS', '4I', '4E', '3I', '3E')

# class for object that will be a line in a fitch style natural deduction line
class Proofline:
    def __init__(self, lnumber, rank, sentence, rule):
        self._lnumber = lnumber
        self._rank = rank
        self._sentence = sentence
        self._rule = rule

    def lnumber(self):
        return self._lnumber

    def rank(self):
        return self._rank

    def sentence(self):
        return self._sentence
    
    def rule(self):
        return self._rule

# function for printing lines of the proof formatted a particular way
def printline(n):
    if not isinstance(n, Proofline):
        raise TypeError('printline(): requires a Proofline')
    fitchlineslist = []
    for x in range(n.rank()[0]):
        fitchlineslist.append ('|')
    fitchlinesstring = ''.join(fitchlineslist)
    if n.lnumber() < 10:
        if n.rule()[1] == None:
            print('{}.  {} {}     {}'.format(n.lnumber(), fitchlinesstring, n.sentence().replace('3','\u2203').replace('4','\u2200'), n.rule()[0]))
        elif n.rule()[0] == '>I' or n.rule()[0] == '~I' or n.rule()[0] == '~E' or n.rule()[0] == '4I' or n.rule()[0] == '3I':
            print('{}.  {} {}     {}'.format(n.lnumber(), fitchlinesstring, n.sentence().replace('3','\u2203').replace('4','\u2200'), n.rule()[0].replace('3','\u2203').replace('4','\u2200') + n.rule()[1]))
        else:
            print('{}.  {} {}     {}'.format(n.lnumber(), fitchlinesstring, n.sentence().replace('3','\u2203').replace('4','\u2200'), n.rule()[0].replace('3','\u2203').replace('4','\u2200') + ','.join(n.rule()[1])))
    else:
        if n.rule()[1] == None:
            print('{}. {} {}     {}'.format(n.lnumber(), fitchlinesstring, n.sentence().replace('3','\u2203').replace('4','\u2200'), n.rule()[0]))
        elif n.rule()[0] == '>I' or n.rule()[0] == '~I' or n.rule()[0] == '~E' or n.rule()[0] == '4I' or n.rule()[0] == '3I':
            print('{}. {} {}     {}'.format(n.lnumber(), fitchlinesstring, n.sentence().replace('3','\u2203').replace('4','\u2200'), n.rule()[0].replace('3','\u2203').replace('4','\u2200') + n.rule()[1]))
        else:
            print('{}. {} {}     {}'.format(n.lnumber(), fitchlinesstring, n.sentence().replace('3','\u2203').replace('4','\u2200'), n.rule()[0].replace('3','\u2203').replace('4','\u2200') + ','.join(n.rule()[1])))

def infix_printline(n):
    if not isinstance(n, Proofline):
        raise TypeError('printline(): requires a Proofline')
    fitchlineslist = []
    for x in range(n.rank()[0]):
        fitchlineslist.append ('|')
    fitchlinesstring = ''.join(fitchlineslist)
    if n.lnumber() < 10:
        if n.rule()[1] == None:
            print('{}.  {} {}     {}'.format(n.lnumber(), fitchlinesstring, predicate_logic.polishtoinfix(n.sentence()), n.rule()[0]))
        elif n.rule()[0] == '>I' or n.rule()[0] == '~I' or n.rule()[0] == '~E' or n.rule()[0] == '4I' or n.rule()[0] == '3I':
            print('{}.  {} {}     {}'.format(n.lnumber(), fitchlinesstring, predicate_logic.polishtoinfix(n.sentence()), n.rule()[0].replace('3','\u2203').replace('4','\u2200') + n.rule()[1]))
        else:
            print('{}.  {} {}     {}'.format(n.lnumber(), fitchlinesstring, predicate_logic.polishtoinfix(n.sentence()), n.rule()[0].replace('3','\u2203').replace('4','\u2200') + ','.join(n.rule()[1])))
    else:
        if n.rule()[1] == None:
            print('{}. {} {}     {}'.format(n.lnumber(), fitchlinesstring, predicate_logic.polishtoinfix(n.sentence()), n.rule()[0]))
        elif n.rule()[0] == '>I' or n.rule()[0] == '~I' or n.rule()[0] == '~E' or n.rule()[0] == '4I' or n.rule()[0] == '3I':
            print('{}. {} {}     {}'.format(n.lnumber(), fitchlinesstring, predicate_logic.polishtoinfix(n.sentence()), n.rule()[0].replace('3','\u2203').replace('4','\u2200') + n.rule()[1]))
        else:
            print('{}. {} {}     {}'.format(n.lnumber(), fitchlinesstring, predicate_logic.polishtoinfix(n.sentence()), n.rule()[0].replace('3','\u2203').replace('4','\u2200') + ','.join(n.rule()[1])))


# proof is the list that will contain the lines of the proof.
proof = []

# string w/ rule abreviation and citation is split into tuple, if it doesn't match one of our rules it returns (0,0), doesn't check for formating though after a rule is correctly called eg >Ig74 would get the output (>I, g74). &I2,4 would return (&I,[2,4])

def rulesplitter(string):
    if string == 'Assume' or string == 'Premise':
        return (string, None)
    elif string[0] == 'R':
        return ('R', string[1:])
    elif string[:2] == '&E' or string[:2] == 'vI' or string[:2] == '>I' or string[:2] == '~I' or string[:2] == '~E' or string[:2] == '4I' or string[:2] == '3I' or string[:2] == '4E':
        return (string[:2], string[2:])
    elif string[:2] == '&I' or string[:2] == 'vE' or string[:2] == '>E' or string[:2] == 'MT' or string[:2] == 'HS' or string[:2] == 'DS' or string[:2] == '3E':
        return (string[:2], string[2:].split(','))
    elif string[:3] == '<>I' or string[:3] == '<>E':
        return (string[:3], string[3:].split(','))
    else:
        return (0,0)

# This function takes a wff with a dyadic main operator and outputs a tuple with the two major constituents in it. e.g. from &AB ig tives you (A,B), gives (None,None) if there's no dyadic main operator
def dyadic_breaker(dyadic):
    senlength = len(dyadic)
    default = (None,None)
    dyadic = dyadic.replace('<>','<')
    if dyadic[0] not in predicate_logic.monadic_chars and dyadic[0] not in predicate_logic.quantifiers:
        for n in range(2,senlength+1):        
            if predicate_logic.wffcheck(dyadic[1:n]) == 1 and (dyadic[n]) not in predicate_logic.obj_names and (dyadic[n]) not in predicate_logic.obj_variables and (dyadic[n]) != '*':
                default = (dyadic[1:n].replace('<','<>'), dyadic[n:].replace('<','<>'))
                break
    return default

# This function when employed in nextline() after scope1 and scope2 are assigned returns all the line ranks that you can use R, &I, &E, vI, >E,<>E, MT, HS, DS on for that line. ie on a fitch proof it makes sure that you're not citing a line on a closed off sub derivation. Make scope1,scope1 be the inputs.
def accessibility(x,y):
    accessiblescopes = [(1,1),(x,y)]
    if x > 2:
        for n in range(x - 1,1,-1): 
            for line in reversed(proof):
                if line.rank()[0] == n:
                    accessiblescopes.append((n,line.rank()[1]))
                    break
    return accessiblescopes

# This function returns a one if a list of sentences contains at least one pair of sentences 'x' and '~x' otherwise it returns 0.
def contradiction_finder(list):
    default = 0
    for string in list:
        if list.count('~'+string):
            default = 1
    return default

# This function takes a string and returns a list where each character is an item, but asterisk are appended to the previous non-asterisk item: so Bx** becomes ('B', 'x**'), will cause error if first characgter is an asterisk
def star_collector (string):
    senlist = []
    for c in string:
        if c == "*":
            senlist[-1] = senlist[-1] + c
        else:
            senlist.append(c)
    return senlist

def nextline (text):
    newline = text.split()
    if len(newline) != 4:
        print ('Error: must have line number, scope lines, sentence, and rule all separated by a space. Do not separate line citation from rule.')
        return 0
    if newline[0][-1] == '.':
        newline[0] = newline[0][:-1]
    #this (below) handles the input if it's the first line of the proof, ie proof is an empty list. It handles scope line issues and only possible line 1 rule: Premise and Assume
    if not proof:
        try:
            if int(newline[0]) != 1:
                print ('Started proof with line other than "1".')
                return 0
            if len(newline[1].replace('|','')) != 0:
                print('Can only use "|" in scopelines.')
                return 0
            if newline[1] != '|' and newline[1] != '||':
                print ('Error on scope line. Must have 1 or 2 scope lines on first line.')
                return 0
            if newline[1] == '||' and newline[3] != 'Assume':
                print ('Error on line. Can only start with 2 scope lines if line 1 is an Assumption')
                return 0
            if newline[3] == 'Assume' and newline[1] != '||':
                print('If line 1 is an Assumption, must have 2 scope lines.')
                return 0
            if newline[3] != 'Assume' and newline[3] != 'Premise':
                print("First line's rule must be either 'Premise' or 'Assume'")
                return 0
            if predicate_logic.wffcheck(newline[2]) == 0:
                print('Sentence is not well-formed.')
                return 0
            return Proofline(int(newline[0]), (len(newline[1]),1), newline[2], (newline[3], None))
        except:
            print ('Please make sure the line is formatted properly.')
            return 0

    # this (below) handles the input if there exists a previous line. it it kicks in for all lines of proof after the first.
    else:
        ruple = rulesplitter(newline[3])
        if int(newline[0]) != (len(proof) + 1):
            print('Error on line number.')
            return 0
        if len(newline[1].replace('|','')) != 0:
            print('Can only use "|" in scopelines.')
            return 0
        
        #scope1 is the number of scope lines.
        scope1 = newline[1].count("|")

        #prevents assuming without at least 2 scopelines.
        if newline[3] == 'Assume' and scope1 == 1:
            print('All assumptions must have at least 2 scope lines.')
            return 0
        
        prevscope1 = proof[-1].rank()[0]
        prevscope2 = proof[-1].rank()[1]
        if scope1 > (prevscope1 +1):
            print ('Can only add 1 scope line at a time.')
            return 0 
        if scope1 < (prevscope1 -1):
            print ('Can only remove one scope line at at time')
            return 0
        if scope1 == (prevscope1 + 1):
            if newline[3] == 'Assume':
                scope2 = 1
                for line in reversed(proof):
                    if line.rank()[0] == scope1:
                        scope2 = line.rank()[1] + 1
                        break
            else:
                print ('Can only add scope line if rule is "Assume"')
                return 0
        if scope1 == prevscope1:
            if newline[3] == 'Assume':
                scope2 = prevscope2 + 1
            else:
                scope2 = prevscope2
        if scope1 == prevscope1 - 1:
            if scope1 == 1:
                scope2 = 1
            else:
                for line in reversed(proof):
                    contscope2 = line.rank()[1]
                    if line.rank()[0] == scope1:
                        break
                if newline[3] != 'Assume':
                    scope2 = contscope2
                else:
                    scope2 = contscope2 + 1
        if predicate_logic.wffcheck(newline[2]) == 0:
            print('Sentence is not well-formed.')
            return 0
        if newline[3] == 'Assume' or newline[3] == 'Premise':
            return Proofline(int(newline[0]),(scope1,scope2),newline[2],(newline[3], None))

        if ruple[0] == 'R':
            try:
                if proof[int(ruple[1])-1].rank() not in accessibility(scope1,scope2):
                    print('You cited a line number from a discharged assumption.')
                    return 0
                if newline[2] == proof[int(ruple[1])-1].sentence():
                    return Proofline(int(newline[0]),(scope1,scope2),newline[2],(ruple))
                else:
                    print('Rule not applied correctly.')
                    return 0
            except:
                print("There's an error possibly with the line numbers cited for that rule.")
                return 0

        if ruple[0] == '&I':
            try:
                if proof[int(ruple[1][0])-1].rank() not in accessibility(scope1,scope2) or proof[int(ruple[1][1])-1].rank() not in accessibility(scope1,scope2):
                    print('You cited a line number from a discharged assumption.')
                    return 0
                if newline[2] == '&'+ proof[int(ruple[1][0])-1].sentence() + proof[int(ruple[1][1])-1].sentence():
                    return Proofline(int(newline[0]),(scope1,scope2),newline[2],(ruple))
                elif newline[2] == '&'+ proof[int(ruple[1][1])-1].sentence() + proof[int(ruple[1][0])-1].sentence():
                    return Proofline(int(newline[0]),(scope1,scope2),newline[2],(ruple))
                else:
                    print ('Rule not applied correctly.')
                    return 0
            except:
                print("There's an error possibly with the line numbers cited for that rule.")
                return 0

        if ruple[0] == '&E':
            try:
                if proof[int(ruple[1])-1].rank() not in accessibility(scope1,scope2):
                    print('You cited a line number from a discharged assumption.')
                    return 0
                conjunction = proof[int(ruple[1][0])-1].sentence()
                if conjunction[0] != '&':
                    print("You can't apply &E on line that isn't a conjunction.")
                    return 0
                # this is to use a loop to get to the first full sentence after the main operator is removed in order to find the two conjuncts
                if newline[2] == dyadic_breaker(conjunction)[0] or newline[2] == dyadic_breaker(conjunction)[1]:
                    return Proofline(int(newline[0]),(scope1,scope2),newline[2],(ruple))
                else:
                    print('Rule not applied correctly.')
                    return 0
            except:
                print("There's an error possibly with the line numbers cited for that rule.")
                return 0

        if ruple[0] == 'vI':
            try:
                if proof[int(ruple[1])-1].rank() not in accessibility(scope1,scope2):
                    print('You cited a line number from a discharged assumption.')
                    return 0
                if (dyadic_breaker(newline[2])[0] == proof[int(ruple[1][0])-1].sentence() or dyadic_breaker(newline[2])[1] == proof[int(ruple[1][0])-1].sentence()) and newline[2][0] == 'v':
                    return Proofline(int(newline[0]),(scope1,scope2),newline[2],(ruple))
                else:
                    print ('Rule not applied correctly.')
                    return 0
            except:
                print("There's an error possibly with the lines cited for that rule.")
                return 0

        if ruple[0] == 'vE':
            try:
                sub1 = ruple[1][1].split('-')
                sub2 = ruple[1][2].split('-')
                disjunction = proof[int(ruple[1][0])-1].sentence()
                if proof[int(ruple[1][0])-1].sentence()[0] != 'v':
                    print ("The line you cited as a disjuction is not a disjunction.")
                    return 0
                
                if proof[int(sub1[0])-1].rule()[0] != 'Assume' or proof[int(sub2[0])-1].rule()[0] != 'Assume':
                    print('The first line of your cited subderivation must be an assumption.')
                    return 0

                if (dyadic_breaker(disjunction)[0] == proof[int(sub1[0])-1].sentence() and dyadic_breaker(disjunction)[1] == proof[int(sub2[0])-1].sentence()) or (dyadic_breaker(disjunction)[1] == proof[int(sub1[0])-1].sentence() and dyadic_breaker(disjunction)[0] == proof[int(sub2[0])-1].sentence()):
                    
                    # checks if end of both subderivations matches newline
                    if proof[int(sub1[1])-1].sentence() == newline[2] and proof[int(sub2[1])-1].sentence() == newline[2]:  # checks if end of both subderivations matches newline

                        #checks if disjunction is accessibile
                        if proof[int(ruple[1][0])-1].rank() in accessibility(scope1,scope2):

                            # checks if the assumption and end of the subderivations each respectively have identical ranks
                            if proof[int(sub1[0])-1].rank() == proof[int(sub1[1])-1].rank() and proof[int(sub2[0])-1].rank() == proof[int(sub2[1])-1].rank():

                                # checks if the subderivations have one more scope line than newline
                                if proof[int(sub1[0])-1].rank()[0] == proof[int(sub2[0])-1].rank()[0] and proof[int(sub1[0])-1].rank()[0] == scope1 + 1:

                                    return Proofline(int(newline[0]),(scope1,scope2),newline[2],(ruple))
                                    
                                else:
                                    print('Rule not applied correctly.')
                                    return 0
                            else:
                                print("Rule not applied correctly. There seems to be a problem with the subderivations.")
                                return 0                            
                        else:
                            print('The disjuction you cited is from a discharged assumption.')
                            return 0
                    else:
                        print ('Rule not applied correctly')
                        return 0
                else:
                    print ('Rule not applied correctly')
                    return 0
            except:
                print ("There's an error possibly with the lines cited for that rule.")
                return 0

        if ruple[0] == '>E':
            try:
                # checks to see if the cited lines are accessible
                if proof[int(ruple[1][0])-1].rank() not in accessibility(scope1,scope2) or proof[int(ruple[1][1])-1].rank() not in accessibility(scope1,scope2):
                    print('You cited a line number from a discharged assumption.')
                    return 0

                # checks if first cited line is the conditional and second is antecedent
                if newline[2] == dyadic_breaker(proof[int(ruple[1][0])-1].sentence())[1] and dyadic_breaker(proof[int(ruple[1][0])-1].sentence())[0] == proof[int(ruple[1][1])-1].sentence() and proof[int(ruple[1][0])-1].sentence()[0] == '>':
                    return Proofline(int(newline[0]),(scope1,scope2),newline[2],(ruple))

                # checks if second cited line is the conditional and 1st is antecedent    
                elif newline[2] == dyadic_breaker(proof[int(ruple[1][1])-1].sentence())[1] and dyadic_breaker(proof[int(ruple[1][1])-1].sentence())[0] == proof[int(ruple[1][0])-1].sentence() and proof[int(ruple[1][1])-1].sentence()[0] == '>':
                    return Proofline(int(newline[0]),(scope1,scope2),newline[2],(ruple))
                else:
                    print ('Rule not applied correctly.')
                    return 0
            except:
                print("There's an error possibly with the line numbers cited for that rule.")
                return 0

        if ruple[0] == '>I':
            try:
                sub1 = ruple[1].split('-')
                antecdent = dyadic_breaker(newline[2])[0]
                consequent = dyadic_breaker(newline[2])[1]
                if newline[2][0] != '>':
                    print('Rule not applied correctly, lined derived by >I must have > as main operator.')
                    return 0

                if proof[int(sub1[0])-1].rule()[0] != 'Assume':
                    print('The first line of your cited subderivation must be an assumption.')
                    return 0

                if antecdent == proof[int(sub1[0])-1].sentence() and consequent == proof[int(sub1[1])-1].sentence():
                    if proof[int(sub1[0])-1].rank()[0] == scope1 + 1 and proof[int(sub1[1])-1].rank() == proof[int(sub1[0])-1].rank():
                        return Proofline(int(newline[0]),(scope1,scope2),newline[2],(ruple))
                    else:
                        print("Rule not applied correctly.")
                        return 0
                else:
                    print ("Rule not applied correctly.")
                    return 0
            except:
                print("There's an error possibly with the line numbers cited for that rule.")
                return 0
        
        if ruple[0] == '~I':
            try:
                sub1 = ruple[1].split('-')
                
                if proof[int(sub1[0])-1].rule()[0] != 'Assume':
                    print('The first line of your cited subderivation must be an assumption.')
                    return 0
                
                # Creating a list here of the all the sentences in the subproof to run the contradiciton finder function on
                subprooflist = []
                for n in range(int(sub1[0]),int(sub1[1])+1):
                    subprooflist.append(proof[n-1].sentence())
                    
                if newline[2] == '~' + proof[int(sub1[0])-1].sentence():
                    if proof[int(sub1[0])-1].rank()[0] == scope1 + 1 and proof[int(sub1[1])-1].rank() == proof[int(sub1[0])-1].rank():
                        if contradiction_finder(subprooflist) == 1:
                            return Proofline(int(newline[0]),(scope1,scope2),newline[2],(ruple))
                        else:
                            print ('Rule not applied correctly check for contradiction in subderivation.')
                            return 0
                    else:
                        print('Rule not applied correctly.')
                        return 0
                else:
                    print('Rule not applied correctly.')
                    return 0
            except:
                print("There's an error possibly with the line numbers cited for that rule.")
                return 0

        if ruple[0] == '~E':
            try:
                sub1 = ruple[1].split('-')

                if proof[int(sub1[0])-1].rule()[0] != 'Assume':
                    print('The first line of your cited subderivation must be an assumption.')
                    return 0

                # Creating a list here of the all the sentences in the subproof to run the contradiciton finder function on
                subprooflist = []
                for n in range(int(sub1[0]),int(sub1[1])+1):
                    subprooflist.append(proof[n-1].sentence())
                    
                if '~' + newline[2] == proof[int(sub1[0])-1].sentence():
                    if proof[int(sub1[0])-1].rank()[0] == scope1 + 1 and proof[int(sub1[1])-1].rank() == proof[int(sub1[0])-1].rank():
                        if contradiction_finder(subprooflist) == 1:
                            return Proofline(int(newline[0]),(scope1,scope2),newline[2],(ruple))
                        else:
                            print ('Rule not applied correctly check for contradiction in subderivation.')
                            return 0
                    else:
                        print('Rule not applied correctly.')
                        return 0
                else:
                    print('Rule not applied correctly.')
                    return 0
            except:
                print("There's an error possibly with the line numbers cited for that rule.")
                return 0

        if ruple[0] == '<>I':
            try:
                sub1 = ruple[1][0].split('-')
                sub2 = ruple[1][1].split('-')
                leftside = dyadic_breaker(newline[2])[0]
                rightside = dyadic_breaker(newline[2])[1]
                if newline[2][:2] != '<>':
                    print('You can only derive a biconditional "<>" with <>E.')
                    return 0

                if proof[int(sub1[0])-1].rule()[0] != 'Assume' or proof[int(sub2[0])-1].rule()[0] != 'Assume':
                    print('The first line of your cited subderivation must be an assumption.')
                    return 0

                # checks to make sure the cited subderivation are one line higher than newline and on equal ranks w/ each other, first for the first cited, then the second
                if (proof[int(sub1[0])-1].rank()[0] == (scope1 + 1) and proof[int(sub1[1])-1].rank() == proof[int(sub1[0])-1].rank()) and (proof[int(sub2[0])-1].rank()[0] == (scope1 + 1) and proof[int(sub2[1])-1].rank() == proof[int(sub2[0])-1].rank()):

                    #checks is assumption of first cited suberivation is left side of bico and conclusion of second cited subderviation; next line handles the right side of bico
                    if leftside == proof[int(sub1[0])-1].sentence() and leftside == proof[int(sub2[1])-1].sentence():
                        if rightside == proof[int(sub1[1])-1].sentence() and rightside == proof[int(sub2[0])-1].sentence():
                            return Proofline(int(newline[0]),(scope1,scope2),newline[2],(ruple))
                        else:
                            print ('Rule not applied correctly.')
                            return 0
                    
                    #checks if assumption of first cited suberviation is right side of bico...
                    elif rightside == proof[int(sub1[0])-1].sentence() and rightside == proof[int(sub2[1])-1].sentence():
                        if leftside == proof[int(sub1[1])-1].sentence() and leftside == proof[int(sub2[0])-1].sentence():
                            return Proofline(int(newline[0]),(scope1,scope2),newline[2],(ruple))
                        else:
                            print ('Rule not applied correctly.')
                            return 0                            

                    else:
                        print("Rule not applied correctly.")
                        return 0
                else:
                    print ("Rule not applied correctly. BOY")
                    return 0
            except:
                print("There's an error possibly with the line numbers cited for that rule.")
                return 0

        if ruple[0] == '<>E':
            try:
                if proof[int(ruple[1][0])-1].rank() not in accessibility(scope1,scope2) or proof[int(ruple[1][1])-1].rank() not in accessibility(scope1,scope2):
                    print('You cited a line number from a discharged assumption.')
                    return 0

                # if first cited line is the bico:
                if ((newline[2] == dyadic_breaker(proof[int(ruple[1][0])-1].sentence())[0] and dyadic_breaker(proof[int(ruple[1][0])-1].sentence())[1] == proof[int(ruple[1][1])-1].sentence()) or (newline[2] == dyadic_breaker(proof[int(ruple[1][0])-1].sentence())[1] and dyadic_breaker(proof[int(ruple[1][0])-1].sentence())[0] == proof[int(ruple[1][1])-1].sentence())) and proof[int(ruple[1][0])-1].sentence()[:2] == '<>':
                    return Proofline(int(newline[0]),(scope1,scope2),newline[2],(ruple))

                # if second cited line is the bico:    
                elif ((newline[2] == dyadic_breaker(proof[int(ruple[1][1])-1].sentence())[1] and dyadic_breaker(proof[int(ruple[1][1])-1].sentence())[0] == proof[int(ruple[1][0])-1].sentence()) or (newline[2] == dyadic_breaker(proof[int(ruple[1][1])-1].sentence())[0] and dyadic_breaker(proof[int(ruple[1][1])-1].sentence())[1] == proof[int(ruple[1][0])-1].sentence())) and proof[int(ruple[1][1])-1].sentence()[:2] == '<>':
                    return Proofline(int(newline[0]),(scope1,scope2),newline[2],(ruple))

                else:
                    print ('Rule not applied correctly.')
                    return 0
            except:
                print("There's an error possibly with the line numbers cited for that rule.")
                return 0

        if ruple[0] == '4E':
            try:
                if proof[int(ruple[1])-1].sentence()[0] != '4':
                    print("Must cite a universally quantified sentence to use \u2200 Elimination")
                    return 0

                if proof[int(ruple[1])-1].rank() not in accessibility(scope1,scope2):
                    print ('You cited a line number from a discharged assumption.')
                    return 0

                #create lists of the new sentence and cited sentence and finds what varible is replaced
                newlinelist = star_collector(newline[2])
                unilinelist = star_collector(proof[int(ruple[1][0])-1].sentence())
                var_to_replace = unilinelist[1]

                #next line deletes the quantifier and its variable, making that quantifier's vairalbes unbound
                del unilinelist[:2]
                # makes empty list to print indices for where the unbound variables are
                occurrences = []
                for count,element in enumerate(unilinelist):
                    if element == var_to_replace:
                        occurrences.append(count)
                
                #replaces the unbound variables with the first character that replaced it 
                for count, i in enumerate(unilinelist):
                    if count in occurrences:
                        unilinelist[count] = newlinelist[occurrences[0]]
                
                #checks if the sentece w/ replaced variables is identical to input sentence
                if unilinelist == newlinelist:
                    return Proofline(int(newline[0]),(scope1,scope2),newline[2],(ruple))
                else:
                    print ('Rule not applied correctly')
                    return 0
            except:
                print ('Rule not applied correctly.')
                return 0

        if ruple[0] == '3I':
            try:
                if newline[2][0] != '3':
                    print("Must cite a universally quantified sentence to use \u2203 Elimination")
                    return 0

                if proof[int(ruple[1][0])-1].rank() not in accessibility(scope1,scope2):
                    print ('You cited a line number from a discharged assumption.')
                    return 0                

                # exilinelist is a list of the new sentence w/ the existential quantifer. oldlinelist is the sentence 3I is being applied to
                exilinelist = star_collector(newline[2])
                oldlinelist = star_collector(proof[int(ruple[1][0])-1].sentence())
                var_to_replace = exilinelist[1]

                #next line deletes the quantifier and its variable, making that quantifier's vairalbes unbound
                del exilinelist[:2]
                # makes empty list to print indices for where the unbound variables are
                occurrences = []
                for count,element in enumerate(exilinelist):
                    if element == var_to_replace:
                        occurrences.append(count)
                
                #replaces the unbound variables with the first character that replaced it 
                for count, i in enumerate(exilinelist):
                    if count in occurrences:
                        exilinelist[count] = oldlinelist[occurrences[0]]
                
                #checks if the sentece w/ replaced variables is identical to input sentence
                if exilinelist == oldlinelist:
                    return Proofline(int(newline[0]),(scope1,scope2),newline[2],(ruple))
                else:
                    print ('Rule not applied correctly')
                    return 0
            except:
                print ('Rule not applied correctly.')
                return 0

        if ruple[0] == '4I':
            try:
                if newline[2][0] != '4':
                    print("Must cite a universally quantified sentence to use \u2200 Introduction")
                    return 0

                if proof[int(ruple[1][0])-1].rank() not in accessibility(scope1,scope2):
                    print ('You cited a line number from a discharged assumption.')
                    return 0
                                
                assumptions = []                
                dischargedassumptions = []
                #create list of indices and ranks in proof where line is an assumption or pemise
                for count, line in enumerate(proof):
                    if line.rule()[0] == 'Premise' or line.rule()[0] == 'Assume':
                        assumptions.append((count, line.rank()))
                
                #this creates a list of discharged assumptions/premises
                for item in assumptions:
                    testA = 0
                    for line in proof:
                        if line.rank() == item[1]:
                            testA= 1
                        if testA == 1 and ((line.rank()[0] < item[1][0] or line.rank()[1] > item[1][1]) or (scope1 < item[1][0] or  scope2 > item[1][1])):
                            dischargedassumptions.append(item)

                # undischargedassumptions is a list w/ the indices and ranks of undischarged assumptions/premises                
                undischargedassumptions = list(set(assumptions) - set(dischargedassumptions))

                # unilinelist is a list of the new sentence w/ the universal quantifer. oldlinelist is the sentence 4I is being applied to
                unilinelist = star_collector(newline[2])
                oldlinelist = star_collector(proof[int(ruple[1][0])-1].sentence())
                var_to_replace = unilinelist[1]

                #next line deletes the quantifier and its variable, making that quantifier's viarables unbound
                del unilinelist[:2]
                # makes empty list to store indices for where the unbound variables are in the sentence
                occurrences = []
                for count, element in enumerate(unilinelist):
                    if element == var_to_replace:
                        occurrences.append(count)

                #replaces the unbound variables with the first character that replaced it 
                for count, i in enumerate(unilinelist):
                    if count in occurrences:
                        unilinelist[count] = oldlinelist[occurrences[0]]
                # Making sure replaced object name not in quantified sentence or undischarged assumptions/premises.
                if oldlinelist[occurrences[0]] in star_collector(newline[2]):
                    print ('Rule not followed. Replaced object name cannot occur in quanitifed sentence.')
                    return 0
                
                for pair in undischargedassumptions:
                    if oldlinelist[occurrences[0]] in star_collector(proof[pair[0]].sentence()):
                        print('Rule not followed. Replaced object name cannot occur in an undischarged assumption or premise.')
                        return 0

                #checks if the sentece w/ replaced variables is identical to input sentence
                if unilinelist == oldlinelist:
                    return Proofline(int(newline[0]),(scope1,scope2),newline[2],(ruple))
                else:
                    print ('Rule not applied correctly')
                    return 0
            except:
                print ('Rule not applied correctly.')
                return 0

        if ruple[0] == '3E':
            try:
                if proof[int(ruple[1][0])-1].sentence()[0] != '3':
                    print("Must cite a universally quantified sentence to use \u2203 Introduction")
                    return 0

                assumptions = []                
                dischargedassumptions = []
                #create list of indices and ranks in proof where line is an assumption or pemise
                for count, line in enumerate(proof):
                    if line.rule()[0] == 'Premise' or line.rule()[0] == 'Assume':
                        assumptions.append((count, line.rank()))
                
                #this creates a list of discharged assumptions/premises
                for item in assumptions:
                    testA = 0
                    for line in proof:
                        if line.rank() == item[1]:
                            testA= 1
                        if testA == 1 and ((line.rank()[0] < item[1][0] or line.rank()[1] > item[1][1]) or (scope1 < item[1][0] or  scope2 > item[1][1])):
                            dischargedassumptions.append(item)

                # undischargedassumptions is a list w/ the indices and ranks of undischarged assumptions/premises                
                undischargedassumptions = list(set(assumptions) - set(dischargedassumptions))

                sub1 = ruple[1][1].split('-')
                exilinelist = star_collector(proof[int(ruple[1][0])-1].sentence())
                asslinelist = star_collector(proof[int(sub1[0])-1].sentence())
                newlinelist = star_collector(newline[2])
                var_to_replace = exilinelist[1]

                if proof[int(sub1[0])-1].rule()[0] != 'Assume':
                    print('The first line of your cited subderivation must be an assumption.')
                    return 0

                # ensure the conclusion of the subderivation matches the new sentence
                conline = proof[int(sub1[1])-1].sentence()
                if conline != newline[2]:
                    print('Sentence must match sentence at end of subderivaiton.')
                    return 0

                #checks if existential sentence is accessibile
                if proof[int(ruple[1][0])-1].rank() not in accessibility(scope1,scope2):
                    print ('Exisential sentence cited is in a closed off subderivation.')
                    return 0

                # checks if the assumption and end of the subderivation have identical ranks
                if proof[int(sub1[0])-1].rank() != proof[int(sub1[1])-1].rank():
                    print('The assumption and end of subderivation are not in the same scope line.')
                    return 0

                # checks if the subderivations has one more scope line than newline
                if proof[int(sub1[0])-1].rank()[0] != scope1 + 1:
                    print('Subderivation can only have one more scope line than the new sentence.')
                    return 0

                #next line deletes the quantifier and its variable, making that quantifier's viarables unbound
                del exilinelist[:2]
                # makes empty list to store indices for where the unbound variables are in the sentence
                occurrences = []
                for count, element in enumerate(exilinelist):
                    if element == var_to_replace:
                        occurrences.append(count)

                #replaces the unbound variables with the first character that replaced it 
                for count, i in enumerate(exilinelist):
                    if count in occurrences:
                        exilinelist[count] = asslinelist[occurrences[0]]

                # Making sure replaced object name not in derived sentence or quantified sentence
                if asslinelist[occurrences[0]] in star_collector(newline[2]) or asslinelist[occurrences[0]] in star_collector(proof[int(ruple[1][0])-1].sentence()):
                    print ('Rule not followed. Name that replaces the varible in the existential sentence cannot occur in the existential sentence or the derived line.')
                    return 0
                # Making sure replaced object name not in undischarged assumption                   
                for pair in undischargedassumptions:
                    if asslinelist[occurrences[0]] in star_collector(proof[pair[0]].sentence()):
                        print('Rule not followed. Replaced object name cannot occur in an undischarged assumption or premise.')
                        return 0
                
                #checks if the sentece w/ replaced variables is identical to input sentence
                if exilinelist == asslinelist:
                    return Proofline(int(newline[0]),(scope1,scope2),newline[2],(ruple))
                else:
                    print ('Rule not applied correctly')
                    return 0

            except:
                print('Rule not applied correctly')
                return 0

def PolishProofBuilder():
    conclusion = ''
    while conclusion == '':
        first_attempt = input('What is the conclusion to your argument? \n')
        if predicate_logic.wffcheck(first_attempt) == 1:
            conclusion = first_attempt
        else:
            print ('Your sentence is not well-formed.')

    while not proof:
        response = input('Input your first line. \n')
        if nextline(response) !=0:
            proof.append(nextline(response))

    while proof[-1].sentence() != conclusion:
        for line in proof:
            printline(line)
        response = input('Input next line. \n')
        if nextline(response) !=0:
            proof.append(nextline(response))

    print ('Proof completed.')


def InfixProofBuilder():
    
    def transformer(string):
        inputlist = string.split()
        if len(inputlist) != 4:
            print('Line must have a line number, scope lines "|" sentence, and rule all separated by spaces. Dont separate rule and lines cited by rule.')
            return 0
        if predicate_logic.infix_wff_check(inputlist[2]) == 1:
            inputlist[2] = predicate_logic.infixtopolish_nosub(inputlist[2])
            return ' '.join(inputlist)
        elif predicate_logic.infix_wff_check('(' + inputlist[2] +')') == 1:
            inputlist[2] = predicate_logic.infixtopolish_nosub('(' + inputlist[2] +')')
            return ' '.join(inputlist)
        else:
            print('Check to make sure your sentence is well-formed.')
            return 0

    conclusion = ''
    while conclusion == '':
        first_attempt = input('What is the conclusion to your argument? \n')
        if predicate_logic.infix_wff_check(first_attempt) == 1:
            conclusion = predicate_logic.infixtopolish_nosub(first_attempt)
        elif predicate_logic.infix_wff_check('(' + first_attempt + ')') == 1:
            conclusion = predicate_logic.infixtopolish_nosub('(' + first_attempt + ')')
        else:
            print ('Your sentence is not well-formed.')

    while not proof:
        response = input('Input your first line. \n')
        if transformer(response) != 0:
            if nextline(transformer(response)) != 0:
                proof.append(nextline(transformer(response)))

    while proof[-1].sentence() != conclusion:
        for line in proof:
            infix_printline(line)
        response = input('Input next line. \n')
        if transformer(response) != 0:
            if nextline(transformer(response)) != 0:
                proof.append(nextline(transformer(response)))

    for line in proof:
        infix_printline(line)
    print ('Proof completed.')

def Polishtextreader():
    filename = input('Enter file with extension to txt file that contains proof.')
    file = open(filename, 'r')
    for line in file:
        if nextline(line) != 0:
            proof.append(nextline(transformer(line)))
    file.close
    for line in proof:
        infix_printline(line)

def Infixtextreader():
    filename = input('Enter file to txt file that contains proof.')
    def transformer(string):
        inputlist = string.split()
        if len(inputlist) != 4:
            print('Line must have a line number, scope lines "|" sentence, and rule all separated by spaces. Dont separate rule and lines cited by rule.')
            return 0
        if predicate_logic.infix_wff_check(inputlist[2]) == 1:
            inputlist[2] = predicate_logic.infixtopolish_nosub(inputlist[2])
            return ' '.join(inputlist)
        elif predicate_logic.infix_wff_check('(' + inputlist[2] +')') == 1:
            inputlist[2] = predicate_logic.infixtopolish_nosub('(' + inputlist[2] +')')
            return ' '.join(inputlist)
        else:
            print('Check to make sure your sentence is well-formed.')
            return 0

    file = open(filename, 'r')
    for line in file:
        if transformer(line) != 0:
            if nextline(transformer(line)) != 0:
                proof.append(nextline(transformer(line)))
    file.close
    for line in proof:
        infix_printline(line)


def Menu():
    selection = '0'
    while selection != 'x' and selection != 'X':
        selection = input('Enter "a" to run the proof builder in Polish notation.\nEnter "b" to run the proof builder in infix (standard) notation.\nEnter "c" to test txt file proof in Polish notation.\nEnter "d" to test txt file proof in infix notation.\nEnter "i" for instructions.\nEnter "x" to Exit.\n')
        if selection == 'a' or selection == 'A':
            PolishProofBuilder()
        if selection == 'b' or selection == 'B':
            InfixProofBuilder()
        if selection == 'i' or selection == 'i':
            print('INSTRUCTIONS \n')
            print('For lines you must enter a number (with or without period following), a space, a pipe ("|") for the number of scope lines, a space, the sentence with no spaces, a space, then the rule followed by the citation with no spaces.\nIt looks like: ')
            print('1. | Rab  Premise \n2. | Rba  Premise \n3. | (Rab&Rba)  &I1,2 \n4. | (3x)(Rxb&Rbx)  3E2 \n5. || (4x)(Rxx)  Assume \n ...')
            print("It doesn't matter how many spaces you use to separate these elments, but within these four elements there can be no spaces.")
            print('The operators: negation (~), conjuction(&), disjunction (v), material conditional (>), biconditional, (<>), existential quanitifer ((3x)), universal quantifer ((4x)).')
            print('The rules are Premise, Assume, R, &E, &I, vI, vE, >I, >E, ~I, ~E, <>I, <>E, 4I, 4E, 3I, and 3E.')
            print('For a description of the rules see: https://wslooney.expressions.syr.edu/logic-rules/')
            print('a-u are object names. w-z are variables. For additional variables you add *. For example x, x*, and x** will all count as different variables.')
            infoselection = input('Enter "x" to Exit. Enter any other character to return to main menu.\n')
            if infoselection == 'x' or infoselection == "X":
                selection == 'x'
        if selection == 'c' or selection == 'C':
            Polishtextreader()
        if selection == 'd' or selection == 'D':
            InfixProofBuilder()

if __name__ == "__main__":
    Menu()