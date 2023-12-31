import argparse
import bninterpreter


def main():
    parser = argparse.ArgumentParser(description='Run a Benevis script.')
    parser.add_argument('file', type=str, help='The .bnvs file to run')
    args = parser.parse_args()

    with open(args.file, 'r') as file:
        source_code = file.read()

    bninterpreter.interpret(source_code)

if __name__ == '__main__':
    main()
