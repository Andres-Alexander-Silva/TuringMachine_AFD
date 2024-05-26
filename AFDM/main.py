from finite_deterministic_automaton import AFD

#Example 1
states = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6'}
alphabet = {'0', '1'}
transitions = {
    ('q0', '0'): 'q1',
    ('q0', '1'): 'q2',
    ('q1', '0'): 'q3',
    ('q1', '1'): 'q4',
    ('q2', '0'): 'q4',
    ('q2', '1'): 'q5',
    ('q3', '0'): 'q3',
    ('q3', '1'): 'q6',
    ('q4', '0'): 'q3',
    ('q4', '1'): 'q6',
    ('q5', '0'): 'q4',
    ('q5', '1'): 'q5',
    ('q6', '0'): 'q6',
    ('q6', '1'): 'q6'
}
initial_state = 'q0'
final_states = {'q3', 'q4', 'q6'}

# Creación del AFD
afd = AFD(states, alphabet, transitions, initial_state, final_states)

# Visualización del AFD original
afd.show_afd("AFD Original")

# Eliminación de estados inalcanzables y visualización del AFD sin estados inalcanzables
reachable_afd = afd.remove_unreachable_states()
reachable_afd.show_afd("AFD Sin Estados Inalcanzables")

# Minimización del AFD y visualización del AFD minimizado
minimized_afd = afd.minimize_afd('minimization_steps.txt')
minimized_afd.show_afd("AFD Minimizado")