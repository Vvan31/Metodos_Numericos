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
import random

def manage_file(file): 
    f = open(file,'r')
    counter = 0
    n_binary_variables = 0
    n_clauses = 0
    clauses = []

    for line in f:
        # Comments  starts with c. 
        counter += 1
        # Information. p cnf 20  91 
        if counter == 8: 
            x = line.split()
            n_binary_variables = x[2]
            n_clauses = x[3]
        # Clauses 
        if counter > 8 and counter < 100: 
            clause_var = line.split()
            clause = []
            for n in clause_var:
                if n != '0':
                    clause.append(n)

            clauses.append(clause)
    f.close()
    return n_binary_variables,n_clauses,clauses

# Generate a random bit. 
def generate_random(): 
    return (random.randint(0,1))

# Guess an initial assignment at random. 
def initial_guess(arr):
    return 0

def main(): 
    n_binary_variables,n_clauses,clauses = manage_file("Instance3SATExample.txt")
    print(n_binary_variables )
    print( n_clauses) 
    print(clauses)
    
main()