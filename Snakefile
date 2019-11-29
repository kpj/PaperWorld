configfile: 'config.yaml'
workdir: config['workdir']


rule all:
    input:
        'potree'


rule download_corpus:
    output:
        raw_dir = directory('raw_corpus/'),
        extracted_dir = directory('extracted_corpus/')
    shell:
        """
        wget \
            -P {output.raw_dir} \
            --recursive \
            --no-parent \
            -A "*.xml.tar.gz" \
            ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/manuscript/

        find \
            {output.raw_dir} \
            -name "*.xml.tar.gz" \
            -exec tar -C {output.extracted_dir} -xf "{{}}" \;
        """


rule process_corpus:
    input:
        extracted_dir = 'extracted_corpus/'
    output:
        processed_dir = directory('processed_corpus/')
    script:
        'scripts/process_corpus.py'


rule compute_features:
    input:
        processed_dir = 'processed_corpus/'
    output:
        fname = 'features.npz'
    script:
        'scripts/compute_features.py'


rule compute_embedding:
    input:
        fname = 'features.npz'
    output:
        fname = 'embedding.xyz'
    script:
        'scripts/compute_embedding.py'


rule prepare_potree:
    input:
        fname = 'embedding.xyz'
    output:
        potree_dir = directory('potree')
    script:
        'scripts/prepare_potree.py'
