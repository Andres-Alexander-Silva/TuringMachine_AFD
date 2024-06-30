class TuringMachine:
    # Constructor for the TuringMachine class
    def __init__(self, states, input_alphabet, tape_alphabet, transitions, initial_state, blank_symbol, final_states):
        self.states = states
        self.input_alphabet = input_alphabet
        self.tape_alphabet = tape_alphabet
        self.transitions = transitions
        self.initial_state = initial_state
        self.blank_symbol = blank_symbol
        self.final_states = final_states
        self.tape = []
        self.head_position = 0
        self.current_state = initial_state
        
    # Method to initialize the tape with the input string
    def initialize_tape(self, input_string):
        self.tape = list(input_string) + [self.blank_symbol]
        self.head_position = 0
    
    # Method to run the Turing machine
    def step(self):
        try:
            current_symbol = self.tape[self.head_position]
            if (self.current_state, current_symbol) in self.transitions:
                new_state, new_symbol, direction = self.transitions[(self.current_state, current_symbol)]
                self.tape[self.head_position] = new_symbol
                self.current_state = new_state
                if direction == 'R':
                    self.head_position += 1
                elif direction == 'L':
                    self.head_position -= 1
            else:
                raise ValueError(f"No transition defined for state {self.current_state} and symbol {current_symbol}.")
        except IndexError:
            raise ValueError("Head position moved out of tape bounds.")

    # Method to run the Turing machine with the input string
    def run(self, input_string) -> str:
        self.initialize_tape(input_string)
        while self.current_state not in self.final_states:
            self.step()
        return ''.join(self.tape).strip(self.blank_symbol)
    
    def print_tape(self):
        tape_str = ''.join(self.tape).strip(self.blank_symbol)
        head_marker = ' ' * self.head_position + '^'
        print(tape_str)
        print(head_marker)