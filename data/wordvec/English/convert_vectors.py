"""
Convert glove vectors into Stanza compatible format
"""

import argparse

def convert(input_glove_file, output_file):
    with open(input_glove_file) as f, open(output_file, "w") as out:
        lines = f.readlines()
        out.write(" ".join([str(len(lines)), "100"]))
        out.write("\n")
        for line in lines:
            out.write(line)


def main():
    parser = argparse.ArgumentParser(description="main training script for word2vec dynamic word embeddings...")
    parser.add_argument("--source_file", type=str, default="./glove.twitter.27B.100d.txt", help="source file path")
    parser.add_argument("--dest_file", type=str, default="./en.twitter100d.xz", help="dest file path")

    # args 
    args = parser.parse_args()

    # run
    convert(args.source_file, args.dest_file)

if __name__ == "__main__":
    main()