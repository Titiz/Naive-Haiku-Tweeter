import os
import argparse

import wordify

parser = argparse.ArgumentParser()
parser.add_argument(
    "-run", help="activate or deactivate the scheduling service",
    choices=("run", "stop"))
parser.add_argument("-haiku", help="generate example haiku")
parser.add_argument("-poem", help="generate example poem")
parser.add_argument(
    "-interval", help="set scheduled time interval (in mins)", type=int)

if __name__ == '__main__':
    args = parser.parse_args()
    if not os.path.exists("corpus.json"):
        print(("Generating linguistic corpus for first time use."
               "Please be patient. This might take a while."))
        wordify.build_corpus()

    if args.haiku:
        pass
    if args.poem:
        pass
    if args.interval:
        print("The new interval will be {} minutes".format(args.interval))

    if args.run == "run":
        raise NotImplementedError(
            "This functionality has not been implemented yet!")
    elif args.run == "stop":
        raise NotImplementedError(
            "This functionality has not been implemented yet!")
