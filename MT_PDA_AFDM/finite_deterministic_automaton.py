import networkx as nx
import matplotlib.pyplot as plt

class AFD:
    # Constructor for the AFD class
    def __init__(self, states, alphabet, transitions, initial_state, final_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.initial_state = initial_state
        self.final_states = final_states
    
    # Method to remove unreachable states from the AFD
    def remove_unreachable_states(self):
        reachable_states = set()
        stack = [self.initial_state]

        while stack:
            state = stack.pop()
            if state not in reachable_states:
                reachable_states.add(state)
                for symbol in self.alphabet:
                    next_state = self.transitions.get((state, symbol))
                    if next_state and next_state not in reachable_states:
                        stack.append(next_state)

        new_transitions = {k: v for k, v in self.transitions.items() if k[0] in reachable_states}
        new_final_states = self.final_states.intersection(reachable_states)
        return AFD(reachable_states, self.alphabet, new_transitions, self.initial_state, new_final_states)
    
    # Method to minimize the AFD
    def minimize_afd(self, log_file: str):
        with open(log_file, 'w') as log:
            P = [frozenset(state_set) for state_set in [self.final_states, self.states - self.final_states]]
            W = [frozenset(state_set) for state_set in [self.final_states, self.states - self.final_states]]
            
            log.write(f"Initial partition: {P}\n")

            while W:
                A = W.pop()
                log.write(f"\nProcessing set: {A}\n")
                for c in self.alphabet:
                    X = {state for state in self.states if self.transitions.get((state, c)) in A}
                    log.write(f"Symbol: {c}, Set: {X}\n")
                    for Y in P[:]:
                        intersection = X & Y
                        difference = Y - X
                        if intersection and difference:
                            P.remove(Y)
                            P.append(frozenset(intersection))
                            P.append(difference)
                            log.write(f"Partition updated: {P}\n")
                            if Y in W:
                                W.remove(Y)
                                W.append(frozenset(intersection))
                                W.append(difference)
                            else:
                                if len(intersection) <= len(difference):
                                    W.append(frozenset(intersection))
                                else:
                                    W.append(difference)
            
            log.write(f"\nFinal partition: {P}\n")
            
            new_states = {frozenset(part): 'q' + str(i) for i, part in enumerate(P)}
            new_initial_state = new_states[next(part for part in P if self.initial_state in part)]
            new_final_states = {new_states[part] for part in P if any(state in self.final_states for state in part)}
            new_transitions = {}
            
            log.write(f"\nNew states mapping: {new_states}\n")
            log.write(f"New initial state: {new_initial_state}\n")
            log.write(f"New final states: {new_final_states}\n")

            for part in P:
                repr_state = next(iter(part))
                for symbol in self.alphabet:
                    next_state = self.transitions.get((repr_state, symbol))
                    if next_state:
                        for part_ in P:
                            if next_state in part_:
                                new_transitions[(new_states[part], symbol)] = new_states[part_]

            log.write(f"New transitions: {new_transitions}\n")
            
            minimized_afd = AFD(set(new_states.values()), self.alphabet, new_transitions, new_initial_state, new_final_states)
            return minimized_afd
    
    # Method to show the AFD
    def show_afd(self, title: str):
        G = nx.DiGraph()

        for state in self.states:
            if state in self.final_states:
                G.add_node(state, shape='doublecircle', color='green')
            elif state == self.initial_state:
                G.add_node(state, shape='circle', color='red')
            else:
                G.add_node(state, shape='circle', color='lightblue')

        for (state, symbol), next_state in self.transitions.items():
            G.add_edge(state, next_state, label=symbol)

        pos = nx.spring_layout(G)
        edge_labels = nx.get_edge_attributes(G, 'label')
        node_colors = [G.nodes[node].get('color', 'lightblue') for node in G.nodes()]

        plt.figure(figsize=(12, 8))
        nx.draw(G, pos, with_labels=True, node_shape='o', node_size=3000, node_color=node_colors, font_size=10, font_weight='bold')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
        plt.title(title)
        plt.show()