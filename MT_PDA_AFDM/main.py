from finite_deterministic_automaton import AFD
from turing_machine import TuringMachine
from transition_formalization_diagram import generate_transition_diagram, formalize_turing_machine
from PushdownAutomaton import PDA

welcome_text = r"""
  ____    _                                         _       _               
 | __ )  (_)   ___   _ __   __   __   ___   _ __   (_)   __| |   ___    ___ 
 |  _ \  | |  / _ \ | '_ \  \ \ / /  / _ \ | '_ \  | |  / _` |  / _ \  / __|
 | |_) | | | |  __/ | | | |  \ V /  |  __/ | | | | | | | (_| | | (_) | \__ \
 |____/  |_|  \___| |_| |_|   \_/    \___| |_| |_| |_|  \__,_|  \___/  |___/                                                                                                          
"""

name_text = r"""
            _____    ____     __  __                  _       _                
   __ _    |_   _|  / ___|   |  \/  |   __ _    ___  | |__   (_)  _ __     ___ 
  / _` |     | |   | |       | |\/| |  / _` |  / __| | '_ \  | | | '_ \   / _ \
 | (_| |     | |   | |___    | |  | | | (_| | | (__  | | | | | | | | | | |  __/
  \__,_|     |_|    \____|   |_|  |_|  \__,_|  \___| |_| |_| |_| |_| |_|  \___|
"""

authors_text = """
By:
    - Andrés Alexander Silva Pelaez - 1152231
    - Andrés Felipe Beltran Assaf - 1152262
"""

title = welcome_text + "\n" + name_text + "\n" + authors_text


def parse_transitions_AFD(transitions_str):
    transitions = {}
    for transition in transitions_str.split(';'):
        parts = transition.split(',')
        if len(parts) == 3:
            state, symbol, next_state = parts
            transitions[(state, symbol)] = next_state
    return transitions


def parse_transitions_MT(transitions_str):
    transitions = {}
    for transition in transitions_str.split(';'):
        parts = transition.split(',')
        if len(parts) == 5:
            state, read_symbol, next_state, write_symbol, direction = parts
            transitions[(state, read_symbol)] = (
                next_state, write_symbol, direction)
    return transitions


def get_input(prompt):
    return input(prompt)

def run_afd():
    print("\nIngrese la información del AFD a Minimizar:\n")
    states = set(input('Enter states (comma separated): ').split(','))
    alphabet = set(input('Enter alphabet (comma separated): ').split(','))
    transitions = parse_transitions_AFD(input(
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

def run_mt():
    print("\nIngrese la información de la Máquina de Turing:\n")
    states = set(input('Enter states (comma separated): ').split(','))
    input_alphabet = set(input('Enter input alphabet (comma separated): ').split(','))
    tape_alphabet = set(input('Enter tape alphabet (comma separated): ').split(','))
    transitions = parse_transitions_MT(input('Enter transitions (semicolon separated, format: state,read_symbol,next_state,write_symbol,direction): '))
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

def run_pda():
    print("\nIngrese la información del PDA:\n")
    # Obtener información del PDA
    states = input("Ingrese los estados separados por comas: ").split(',')
    input_alphabet = input(
        "Ingrese el alfabeto de entrada separado por comas: ").split(',')
    stack_alphabet = input(
        "Ingrese el alfabeto de la pila separado por comas: ").split(',')
    start_state = input("Ingrese el estado inicial: ")
    start_stack = input("Ingrese el símbolo inicial de la pila: ")
    accept_states = input(
        "Ingrese los estados de aceptación separados por comas: ").split(',')

    # Obtener transiciones
    transitions = {}
    print("Ingrese las transiciones en el formato 'estado,entrada -> estado_siguiente,operación_pila'")
    print("Ingrese 'fin' para terminar:")
    while True:
        transition = input()
        if transition == 'fin':
            break
        state_symbol, next_state_op = transition.split(' -> ')
        state, symbol = state_symbol.split(',')
        next_state, op = next_state_op.split(',')
        if state not in transitions:
            transitions[state] = {}
        transitions[state][symbol] = (next_state, op)
    
    #Crear el PDA
    pda = PDA(states, input_alphabet, stack_alphabet, transitions, start_state, start_stack, accept_states)

    # Procesar entrada
    input_string = input("Ingrese la cadena de entrada: ")
    result = pda.process_input(input_string)

    if result:
        print(f"La cadena '{input_string}' es aceptada por el PDA.")
    else:
        print(f"La cadena '{input_string}' no es aceptada por el PDA.")

    # Visualizar PDA
    pda.visualize("PDA Diagram")


def main():
    while True:
        print(title)
        print("Seleccione el tipo de autómata a utilizar:\n")
        print("\t1. Autómata Finito Determinista (AFD)")
        print("\t2. Máquina de Turing (MT)")
        print("\t3. Autómata de Pila Determinista (PDA)")
        print("\t4. Salir")
        option = int(input("\nOpción: "))

        if option == 1:
            run_afd()
        elif option == 2:
            run_mt()
        elif option == 3:
            run_pda()
        elif option == 4:
            print("\nGracias por usar TC Machine. ¡Adiós!")
            break
        else:
            print("\nOpción no válida. Por favor, intente de nuevo.")

        input("\nPresione Enter para volver al menú principal...")


if __name__ == '__main__':
    main()