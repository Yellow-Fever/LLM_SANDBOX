import argparse

### script arguments

def getScriptArguments():
    globalParser = argparse.ArgumentParser()
    subparsers = globalParser.add_subparsers(title="sandbox apps")
