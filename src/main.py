from machine import Machine, run
from sys import argv
import pickle
import unicodedata

def gather_states():
    print("Enter label of states (end to stop): ")
    states = []
    while (label := input(" > ")) != "end":
        if len(label) == 0:
            print("Not a valid label!")
            exit(1)
        
        states.append(label)
    
    return states



def gather_alphabet():
    print("Enter symbols of alphabet (end to stop): ")
    alphabet = []
    while (symbol := input(" > ")) != "end":
        if len(symbol) != 1:
            print("Not a valid symbol!")
            exit(1)
            
        alphabet.append(symbol)
        
    return alphabet



def define_trans_func(states, alphabet):
    print("Enter transition state for each state and symbol: ")
    trans_func = {}
    for state in states:
        for symbol in alphabet:
            trans_state = input(" (" + str(state) + ", " + str(symbol) + ") -> ")
            
            if trans_state not in states:
                print("Not a valid state!")
                exit(1)
            
            trans_func[(state, symbol)] = trans_state
            
    return trans_func



def define_start_state(states):
    print("Enter the start state: ")
    start_state = input(" > ")
    
    if start_state not in states:
        print("Not a valid state!")
        exit(1)
    
    return start_state



def define_accept_states(states):
    print("Enter the accept states (end to stop): ")
    accept_states = []
    while (state := input(" > ")) != "end":
        if state not in states:
            print("Not a valid state!")
            exit(1)
            
        accept_states.append(state)
        
    return accept_states



def main():
    if len(argv) != 1:
        print("usage: python main.py")
        
    print("Enter new to create a new machine or enter load to load from a .model file: ")
    while (command := input("  > ")) not in ("new", "load"):
        print("  Not a valid command. Try again.")
    
    
    m = None
    if command == "new":
        states = gather_states()
        alphabet = gather_alphabet()
        trans_func = define_trans_func(states, alphabet)
        start_state = define_start_state(states)
        accept_states = define_accept_states(states)
    
        m = Machine(states, alphabet, trans_func, start_state, accept_states)
        
    elif command == "load":
        print("Enter the .model filename: ")
        filename = input("  > ")
        with open("models/" + filename + ".model", "rb") as file:
            m = pickle.load(file)
            
    print("Enter commands (help for help, quit to exit): ")
    while (command := input("  > ")) != "quit":
        if command == "help":
            print("  help - prints the help menu")
            print("  quit - exits the program")
            print("  run - run a string through the machine")
            print("  print - print the tuple represetation of the machine")
            print("  save - save the model")
        elif command == "run":
            print("  Enter string to test: ")
            string = input("  > ")
            result = run(string, m)
            
            if string == "":
                string = "\xCE"
            
            print("    Machine( " + string + " ) = " + str(result))
        elif command == "print":
            print("    M ( " + str(m.states) + 
                  ",\n        " + str(m.alphabet) + 
                  ",\n        " + str(m.trans_func) + 
                  ",\n        " + str(m.start_state) +
                  ",\n        " + str(m.accept_states) + " )\n")
        elif command == "save":
            print("  Enter a filename to save to (exclude any extension): ")
            filename = input("    > ")
            with open("models/" + filename + ".model", "wb") as file:
                pickle.dump(m, file)
        else:
            print("  Not a valid command (help for help).")
            
    
    

if __name__ == "__main__":
    main()
    
