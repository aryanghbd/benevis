import interpreter

def main():
    source_code = '''
    x = 45
    y = x menhaye 4
    
    chiye(y)
    '''

    interpreter.interpret(source_code)

if __name__ == "__main__":
    main()