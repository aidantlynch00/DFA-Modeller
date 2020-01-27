import collections

Machine = collections.namedtuple('Machine', 'states, alphabet, trans_func, start_state, accept_states')

def run(tape, machine):
    return True
    


def main():
    m = Machine('test', 'test', 'test', 'test', 'test')
    print(m)
    
    

if __name__ == '__main__':
    main()
    
