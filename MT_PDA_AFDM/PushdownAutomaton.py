import networkx as nx
import matplotlib.pyplot as plt


class PDA:
    def __init__(self, states, input_alphabet, stack_alphabet, transitions,
                 start_state, start_stack, accept_states) -> None:
        self.states = states
        self.input_alphabet = input_alphabet
        self.stack_alphabet = stack_alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.start_stack = start_stack
        self.accept_states = accept_states
        self.stack = [start_stack]

    def process_input(self, input_string) -> bool:
        current_state = self.start_state
        for char in input_string:
            if char not in self.input_alphabet:
                return False

            if current_state not in self.transitions or char not in self.transitions[current_state]:
                return False

            next_state, stack_op = self.transitions[current_state][char]
            current_state = next_state

            if stack_op == 'push':
                self.stack.append(char)
            elif stack_op == 'pop':
                if not self.stack:
                    return False
                self.stack.pop()
            elif stack_op == 'noop':
                pass

        return current_state in self.accept_states

    def visualize(self, title="PDA Diagram"):
        G = nx.DiGraph()

        for state in self.states:
            if state in self.accept_states:
                G.add_node(state, shape='doublecircle', color='green')
            elif state == self.start_state:
                G.add_node(state, shape='circle', color='red')
            else:
                G.add_node(state, shape='circle', color='lightblue')

        for state, transitions in self.transitions.items():
            for char, (next_state, stack_op) in transitions.items():
                label = f"{char}, {stack_op}"
                G.add_edge(state, next_state, label=label)

        pos = nx.spring_layout(G)
        edge_labels = nx.get_edge_attributes(G, 'label')
        node_colors = [G.nodes[node].get(
            'color', 'lightblue') for node in G.nodes()]

        plt.figure(figsize=(12, 8))
        nx.draw(G, pos, with_labels=True, node_shape='o', node_size=3000,
                node_color=node_colors, font_size=10, font_weight='bold')
        nx.draw_networkx_edge_labels(
            G, pos, edge_labels=edge_labels, font_color='red')
        plt.title(title)
        plt.show()