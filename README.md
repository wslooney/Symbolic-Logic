GUIDE FOR
predicate_logic.py 

For use in Predicate Logic or Sentence Logic, it includes the following functions
infixtopolish(wff) is a function that takes infix notation wff and outputs Polish notation (also replaces the (3x) and (4x) with the quantifiers' unicodes.)
polishtoinfix (wff) is a function that takes a Polish notation wff and outputs infix notation (also replaces the (3x) and (4x) with the quantifiers' unicodes.)
infix_wff_check(wff) check to see if an infix notation sentence is well-formed
wffcheck(wff) checks to see if a Polish notation sentence is well-formed 
polishtoinfix_nosub(wff) same as polishtoinfix() but does not replace the 3x and 4x with quantifiers.
infixtopolish_nosub (infix) same as infixtopolish but does not replace the 3x and 4x with quantifiers.

operators are : ~, &, v, >, <>, (3x) [existential], (4x) [universal quantifier]. You can also input the unicode characters for the quantifiers. Note that you cannot use "v" as a variable or name because it's used for the disjunction. In infix quantifiers must have parens around them, eg "(4x)" in Polish they do have parens around them eg "4x"
names are a-u, variables are w-z. You can also use * to create new variables, so x** will be treated as a distinct variable from x or x*.

you may also use any number of astericks after a variable or object name to create new variable or object names, though practically speaking this only useful for variables.

Does not currently accomodate identity (x=y) or functions (f(x)), but I hope to add these features in the future as well as an ability to export a code to write the proof in LaTeX.

GUIDE FOR
Fitch_Proofs.py

When the program is run it will open a menu that has options for checking the validity of a proof, line by line in either Polish or infix notation, or to load a text file with the whole proof set up.
If you run one with the whole proof, it is valid if the entire proof is printed to the terminal. If it stops there is a mistake with the line not printed.

if you run the file reader it will give you an option to generate the LaTeX code for that argument using the fitch.sty package. I'll add this feature to the proof contructor soon.

For a descripton of the rules see: https://wslooney.expressions.syr.edu/logic-rules/
but they are standard Fitch rules:
Premise, Assume, R, &E, &I, vI, vE, >I, >E, ~I, ~E, <>I, <>E, 4I, 4E, 3I, and 3E.
for some of the rules the order of the lines cited doesn't matter: &E, >E, <>E (as in most textbooks).

Here is an example of a proof done in infix:

1. | (4x)(Hx>Gx) Premise
2. | (3y)Hy Premise
3. || Hg Assume
4. || Hg>Gg  4E1
5. || Gg   >E3,4
6. || (3x)Gx 3I5
7. | (3x)Gx 3E2,3-6

each line must posses a line number, the appropriate number of scope lines, the sentence, and the rule cited.
if putting a proof in a text file, proof should start on line 1.

the program initializes an empty list called proof then uses the function called "nextline()" to convert a given string to an object in a defined class Proofline,"
and if the new line is a valid next step, the function outputs a Proofline object, if it's not a valid step, and message is printed to the terminal, and the output is 0.

The main bit of the program is built using Polish notation, and for using it with infix, it merely translates the sentences into Polish for the functions,
then translates them back into infix when printed to the terminal.
