import collections

Machine = collections.namedtuple('Machine', 'states, alphabet, trans_func, start_state, accept_states')

def run(tape, machine):
    curr_state = machine.start_state
    
    for symbol in tape:
        if symbol not in machine.alphabet:
            print("FATAL! Symbol '" + symbol + "' not in the alphabet!")
            exit(1)
        curr_state = machine.trans_func[(curr_state, symbol)]
        
    if curr_state in machine.accept_states:
        return True
    else:
        return False
    


def main():
    m = Machine('test', 'test', 'test', 'test', 'test')
    print(m)
    
    

if __name__ == '__main__':
    main()
    
