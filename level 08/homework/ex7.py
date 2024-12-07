P = True
Q = False

P_and_not_Q = P and not Q
not_P_and_Q = not P and Q
P_xor_Q = (P and not Q) or (not P and Q)

print("P:", P)
print("Q:", Q)
print("P_and_not_Q:", P_and_not_Q)
print("not_P_and_Q:", not_P_and_Q)
print("P_xor_Q:", P_xor_Q)