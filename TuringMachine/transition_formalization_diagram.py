import networkx as nx
import matplotlib.pyplot as plt
from turing_machine import TuringMachine

def generate_transition_diagram(tm):
    G = nx.MultiDiGraph()
    
    for state in tm.states:
        if state in tm.final_states:
            G.add_node(state, shape='doublecircle')
        else:
            G.add_node(state, shape='circle')
    
    for (state, symbol), (new_state, new_symbol, direction) in tm.transitions.items():
        label = f'{symbol} -> {new_symbol}, {direction}'
        G.add_edge(state, new_state, label=label)
    
    pos = nx.spring_layout(G)
    edge_labels = nx.get_edge_attributes(G, 'label')
    
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_shape='o', node_size=2000, node_color='lightblue', font_size=10, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
    plt.title("Transition Diagram of the Turing Machine")
    plt.show()

def formalize_turing_machine(tm: TuringMachine) -> str:
    formalization = f"Estados: {tm.states}\n"
    formalization += f"Alfabeto de entrada: {tm.input_alphabet}\n"
    formalization += f"Alfabeto de cinta: {tm.tape_alphabet}\n"
    formalization += f"Transiciones:\n"
    for (state, symbol), (new_state, new_symbol, direction) in tm.transitions.items():
        formalization += f"  δ({state}, {symbol}) = ({new_state}, {new_symbol}, {direction})\n"
    formalization += f"Estado inicial: {tm.initial_state}\n"
    formalization += f"Símbolo en blanco: {tm.blank_symbol}\n"
    formalization += f"Estados finales: {tm.final_states}\n"
    return formalization