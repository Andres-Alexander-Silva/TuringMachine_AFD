from MT_PDA_AFDM.PushdownAutomaton import PDA


def main():
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

if __name__ == '__main__':
    main()