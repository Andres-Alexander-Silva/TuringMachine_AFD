from MT_PDA_AFDM.finite_deterministic_automaton import AFD


def parse_transitions(transitions_str):
    transitions = {}
    for transition in transitions_str.split(';'):
        parts = transition.split(',')
        if len(parts) == 3:
            state, symbol, next_state = parts
            transitions[(state, symbol)] = next_state
    return transitions


def main():
    states = set(input('Enter states (comma separated): ').split(','))
    alphabet = set(input('Enter alphabet (comma separated): ').split(','))
    transitions = parse_transitions(input(
        'Enter transitions (semicolon separated, format: state,symbol,next_state): '))
    initial_state = input('Enter initial state: ')
    final_states = set(
        input('Enter final states (comma separated): ').split(','))

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

if __name__ == '__main__':
    main()