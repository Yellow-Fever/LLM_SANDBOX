import argparse

### script arguments

def getScriptArguments():
    globalParser = argparse.ArgumentParser(add_help=False)
    subparsers = globalParser.add_subparsers(title="Available Commands")

    # Global parser args
    globalParser.add_argument("-v", "--verbose", help="output in verbose mode")
    globalParser.add_argument("-t", "--outtype", help="output filetype")
   
    # Tokenizer Subparser
    tokenizer_parser = subparsers.add_parser("token", help="Various tokenizers", parents=[globalParser])

    # Read in corpus
    corpus_parser = subparsers.add_parser("corpus", help="Text preprocessing", parents=[globalParser])

    args = globalParser.parse_args()
    return args
