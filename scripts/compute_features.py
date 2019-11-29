from scipy import sparse

from sklearn.feature_extraction.text import HashingVectorizer#, TfidfVectorizer

from utils import scantree


def stream_corpus(entry_list):
    for entry in entry_list:
        if not entry.name.endswith('.txt'):
            continue

        with open(entry.path) as fd:
            yield fd.read()


def main(input_dir, fname_out):
    entry_list = scantree(input_dir)
    corpus = stream_corpus(entry_list)

    vectorizer = HashingVectorizer(
        decode_error='ignore', n_features=2 ** 18, alternate_sign=False)
    mat_csr = vectorizer.transform(corpus)

    print('Feature matrix:', mat_csr.shape)
    sparse.save_npz(fname_out, mat_csr)


if __name__ == '__main__':
    main(snakemake.input.processed_dir, snakemake.output.fname)
