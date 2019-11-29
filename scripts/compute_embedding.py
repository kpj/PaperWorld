import numpy as np
from scipy import sparse

import umap
from sklearn.decomposition import PCA

import matplotlib.pyplot as plt


def main(fname_in, fname_out):
    # load file
    mat_csr = sparse.load_npz(fname_in)

    # embed data
    # pca = PCA(n_components=30)
    # mat_csr = pca.fit_transform(mat_csr.toarray())

    reducer = umap.UMAP(n_components=3)
    embedding = reducer.fit_transform(mat_csr)

    # plt.scatter(embedding[:, 0], embedding[:, 1])
    # plt.show()

    # save result
    np.savetxt(fname_out, embedding, fmt='%f')


if __name__ == '__main__':
    main(snakemake.input.fname, snakemake.output.fname)
