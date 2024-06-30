from MT_PDA_AFDM.turing_machine import TuringMachine
from MT_PDA_AFDM.transition_formalization_diagram import generate_transition_diagram, formalize_turing_machine

def parse_transitions(transitions_str):
    transitions = {}
    for transition in transitions_str.split(';'):
        parts = transition.split(',')
        if len(parts) == 5:
            state, read_symbol, next_state, write_symbol, direction = parts
            transitions[(state, read_symbol)] = (next_state, write_symbol, direction)
    return transitions

def get_input(prompt):
    return input(prompt)

def main():
    states = set(input('Enter states (comma separated): ').split(','))
    input_alphabet = set(input('Enter input alphabet (comma separated): ').split(','))
    tape_alphabet = set(input('Enter tape alphabet (comma separated): ').split(','))
    transitions = parse_transitions(input('Enter transitions (semicolon separated, format: state,read_symbol,next_state,write_symbol,direction): '))
    initial_state = input('Enter initial state: ')
    blank_symbol = input('Enter blank symbol: ')
    final_states = set(input('Enter final states (comma separated): ').split(','))
    input_string = input('Enter input string: ')

    # Create a Turing machine
    tm = TuringMachine(states, input_alphabet, tape_alphabet, transitions, initial_state, blank_symbol, final_states)
    
    try:
        result = tm.run(input_string)
        tm.print_tape()
        print(f"Resultado: {result}")
    except ValueError as e:
        print(e)
    
    # Generate transition diagram and formalization
    generate_transition_diagram(tm)
    formalization = formalize_turing_machine(tm)
    print(formalization)
    
if __name__ == '__main__':
    main()