# PaperWorld

Projecting the space of scientific publications into three dimensions.

![exemplary pointcloud](docs/pointcloud.png)

## Pipeline description

To run the whole pipeline simply execute

```bash
$ snakemake -pr
```

This will:

* Download PMC manuscripts
* Analyze their topics (e.g. using tf-idf)
* Project this high-dimensional space to something more manageable (e.g. using umap)
* Visualize the result interactively in the browser (e.g. using potree)
