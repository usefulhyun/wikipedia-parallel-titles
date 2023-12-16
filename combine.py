import argparse


def load_wiki_parallel_titles(file_path):
    parallel_corpus = []
    with open(file_path) as f_in:
        for line in f_in:
            src_text, tgt_text = line.strip().split(" ||| ")
            parallel_corpus.append((src_text, tgt_text))
    return parallel_corpus


def main(input_prefix, src_lang, tgt_lang, output_prefix):
    src_to_tgt = load_wiki_parallel_titles(f"{input_prefix}.{src_lang}-{tgt_lang}")
    tgt_to_src = load_wiki_parallel_titles(f"{input_prefix}.{tgt_lang}-{src_lang}")

    src_to_tgt = set(src_to_tgt)

    cnt = 0
    for tgt_text, src_text in tgt_to_src:
        if src_text == tgt_text:
            continue
        if (src_text, tgt_text) in src_to_tgt:
            print(f"{cnt} ||| {src_text} ||| {tgt_text}")
            cnt += 1


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_prefix")
    parser.add_argument("--src_lang")
    parser.add_argument("--tgt_lang")
    parser.add_argument("--output_prefix")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    main(args.input_prefix, args.src_lang, args.tgt_lang, args.output_prefix)
