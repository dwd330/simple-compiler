#based on :https://github.com/llSourcell/Lets_Build_a_Compiler_LIVE/blob/main/compiler.py

#regular expression library (search pattern)
import re

#Tokenizer function receives starting input
# i.e (add 2 (subtract 4 2))
def tokenizer(input_expression):
    #counter variable for iterating through input array 
    current = 0
    #array to store computed tokens
    tokens = []
    ##use regex library to create search patterns for
    #letters a,z
    alphabet = re.compile(r"[a-z]", re.I);
    #numbers 1-9
    numbers = re.compile(r"[0-9]");
    #white space
    whiteSpace = re.compile(r"\s");
    #iterate through input
    while current < len(input_expression):
        #track position
        char = input_expression[current]
        #If white space is detected, no token created
        if re.match(whiteSpace, char):
            current = current+1
            continue
        #create + add token to array for open parens
        if char == '(':
            tokens.append({
                'type': 'left_paren',
                'value': '('
            })
            #continue iterating
            current = current+1
            continue
        #create + add token to array for closed parens
        if char == ')':
            tokens.append({
                'type': 'right_paren',
                'value': ')'
            })
            #continue iterating
            current = current+1
            continue
        #create + add token to array for numbers
        if re.match(numbers, char):
            value = ''
            #nested iteration if a number is multi-num 
            while re.match(numbers, char):
                value += char
                current = current+1
                if current ==len(input_expression):
                    break
                char = input_expression[current];
            tokens.append({
                'type': 'number',
                'value': value
            })
            continue
        #create + add token to array for letters
        if re.match(alphabet, char):
            value = ''
            #nested iteration if a word is multi-char (all are in this case)
            while re.match(alphabet, char):
                value += char
                current = current+1
                if current ==len(input_expression):
                    break
    
                char = input_expression[current]
            tokens.append({
                'type': 'text',
                'value': value
            })
            continue
        #error condition if we find an unknown value in the input
        raise ValueError('what are THOSE?: ' + char);
    return tokens

while(True):   
    i=input('input (q to quit): ')
    print(tokenizer(i) ,'\n')
    if(i=='q'):
        break