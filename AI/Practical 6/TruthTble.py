# from itertools import product

# def implication(P, Q):
#     return (not P) or Q

# def truth_table():
#     print("P  Q    P->Q")
#     for P, Q in product([True, False], repeat=2):
#         print (P,Q, implication(P, Q))

# truth_table()


from itertools import product

# Define the expression
def expression(p, q):
    return (p or not q) and (not p)

# Generate truth table
def truth_table():
    print("p     q     (p ∨ ¬q) ∧ ¬p")
    print("---------------------------")
    for p, q in product([True, False], repeat=2):
        result = expression(p, q)
        print(f"{p!s:<5} {q!s:<5} {result!s:<5}")

# Call the function
truth_table()