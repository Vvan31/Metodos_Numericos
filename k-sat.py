# input: a formula in  -CNF with variables
# Guess an initial assignment a E {0,1}n,
    # uniformly at random

# Repeat 3n times:
    # If the formula is satisfied by the actual 
    # assignment: stop and accept

    # Let C be some clause not being satisfied by
    # the actual assignment

    # Pick one of the <=k literals in the clause
    # at random and flip its value
    # in the current assignment
from operator import contains
import random

def manage_file(file): 
    f = open(file,'r')
    counter = 0
    n_binary_variables = 0
    n_clauses = 0
    clauses = []

    for line in f:
        x = line.split()
        if len(x) > 0:
            if x[0] == "p": #cnf info
                #print("info")
                n_binary_variables = x[2]
                n_clauses = x[3]
            elif (x[0] != "%") and (x[0] != "0") and (x[0] != "c"):
                numbers = []
                for n in x:
                    print(n)
                    if (n != "0"):
                        numbers.append(int(n))
                clauses.append(numbers)
    print(f"Clauses: {clauses}")
    f.close()
    return n_binary_variables,n_clauses,clauses

# Generate a random bit. 
def generate_random(min, max): 
    return (random.randint(min,max))

def generate_input(n_binary_variables):
    input = []
    for n in range (0,int(n_binary_variables)):
        input.append(random.choice([-1,1]))
    return input

# Guess an initial assignment at random. 
def guess(input,clauses):
    llave = -1
    bad_clauses = []
    good_clauses = []
    for clause in  clauses:
        llave += 1
        result = 0
        for variable in clause: 
            var_result = input[abs(variable)-1] * variable
            if var_result < 0: 
                result +=1

        if result > 2: 
            bad_clauses.append(clause)
        else:
            good_clauses.append(clause)
    return bad_clauses,good_clauses


def flip_variable(bad_clause, input): 
    n_toflip = generate_random(0,2)
    variable_toflip = bad_clause[n_toflip]
    new_input = input
    new_input[abs(variable_toflip)-1] *= -1 
    return new_input

def create_txt_result(instanceTest, initialInput, badClause, goodClause):

    textoNuevo = open("resulto3Sat.txt", "a")
    textoNuevo.write("Now the file has more content!")
    textoNuevo.close()
    return 0


def main(): 
    create_txt_result()
    n_binary_variables,n_clauses,clauses = manage_file("Instance3SATExample.txt")
    input= generate_input(n_binary_variables)
    bad_clauses, good_clauses = guess(input,clauses)
    n = 0
    while n < 3*int(n_binary_variables):
         n +=1
         print(f"bad_clauses:{bad_clauses}")
         print(f"good_clauses:{good_clauses}")
         if len(bad_clauses) <= 0: # not true
            print(f"Se llego a una solucion: {new_input}")
            break
         else: 
            new_input = flip_variable(bad_clauses[0], input)
            bad_clauses,good_clauses = guess(new_input,clauses)
        
    
    

main()