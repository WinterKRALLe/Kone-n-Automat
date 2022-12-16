def ka(slovo, Q, I, f, q0, P):
    for znak in slovo:
        if znak not in I:
            return False
    stav = q0
    for znak in slovo:
        if (stav, znak) not in f:
            return False
        stav = f[(stav, znak)]
    return stav in P


# print(ka('abc', Q, I, f, q0, P))
# print(ka('abcabc', Q, I, f, q0, P))
# print(ka('abcb', Q, I, f, q0, P))
# print(ka('abca', Q, I, f, q0, P))

# Q = {'q0', 'q1', 'q2'}
# I = {'0', '1'}
# f = {
#     ('q0', '0'): 'q0',
#     ('q0', '1'): 'q1',
#     ('q1', '0'): 'q2',
#     ('q1', '1'): 'q1',
#     ('q2', '0'): 'q2',
#     ('q2', '1'): 'q1'
# }
# q0 = 'q0'
# P = {'q2'}

# print(ka('001', Q, I, f, q0, P))
# print(ka('010', Q, I, f, q0, P))
# print(ka('011', Q, I, f, q0, P))
# print(ka('100', Q, I, f, q0, P))

# Q = {'q0', 'q1', 'q2', 'q3', 'q4'}
# I = {'a', 'b', 'c'}
# f = {
#     ('q0', 'a'): 'q1', 
#     ('q1', 'b'): 'q2', 
#     ('q2', 'c'): 'q3',
#     ('q3', 'a'): 'q4',
#     ('q4', 'b'): 'q4',
#     ('q4', 'c'): 'q4'
# }
# q0 = 'q0'
# P = {'q3', 'q4'}

Q = {'q0', 'q1', 'q2', 'q3'}
I = {'a', 'b'}
f = {
    ('q0', 'a'): 'q1',
    ('q0', 'b'): 'q2',
    ('q1', 'a'): 'q1',
    ('q1', 'b'): 'q3',
    ('q2', 'a'): 'q3',
    ('q2', 'b'): 'q2',
    ('q3', 'a'): 'q3',
    ('q3', 'b'): 'q3'
}
q0 = 'q0'
P = {'q3'}

print(ka('ab', Q, I, f, q0, P))
print(ka('ba', Q, I, f, q0, P))
print(ka('abc', Q, I, f, q0, P))
print(ka('cba', Q, I, f, q0, P))

