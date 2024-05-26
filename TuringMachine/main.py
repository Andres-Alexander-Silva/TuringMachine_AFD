
from turing_machine import TuringMachine
from transition_formalization_diagram import generate_transition_diagram, formalize_turing_machine

def main():
    # Example 1
    #states = {'q0', 'q1', 'qf'}
    #input_alphabet = {'0', '1'}
    #tape_alphabet = {'0', '1', '_'}
    #transitions = {
    #    ('q0', '0'): ('q1', '1', 'R'),
    #    ('q1', '0'): ('qf', '0', 'R')
    #}
    #initial_state = 'q0'
    #blank_symbol = '_'
    #final_states = {'qf'}
    
    # Example 2
    states = {'q0', 'q1', 'q2', 'q_accept', 'q_reject'}
    input_alphabet = {'a', 'b'}
    tape_alphabet = {'a', 'b', 'X', 'Y', '_'}
    transitions = {
        ('q0', 'a'): ('q1', 'X', 'R'),
        ('q1', 'a'): ('q1', 'a', 'R'),
        ('q1', 'b'): ('q2', 'Y', 'R'),
        ('q1', 'Y'): ('q1', 'Y', 'R'),
        ('q2', 'b'): ('q2', 'b', 'R'),
        ('q2', 'Y'): ('q2', 'Y', 'R'),
        ('q2', '_'): ('q_accept', '_', 'R'),
        ('q2', 'a'): ('q_reject', 'a', 'R'),
        ('q0', '_'): ('q_reject', '_', 'R'),
    }
    initial_state = 'q0'
    blank_symbol = '_'
    final_states = {'q_accept', 'q_reject'}

    # Create a Turing machine
    tm = TuringMachine(states, input_alphabet, tape_alphabet, transitions, initial_state, blank_symbol, final_states)
    input_string = 'aaabbb'
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