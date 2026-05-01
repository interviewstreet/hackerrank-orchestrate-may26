import argparse
from agent import SupportAgent

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)

    args = parser.parse_args()

    agent = SupportAgent()
    agent.run(args.input, args.output)

if __name__ == "__main__":
    main()
