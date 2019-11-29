import os
import sys

import sh


def main(fname_in, potree_dir):
    """Prepare visualization using potree.

    Useful commands for debugging:

    $ docker run -it --rm -v $PWD:/outside potree_converter /bin/bash

    $ docker run --rm -v $PWD:/outside potree_converter /data/PotreeConverter/build/PotreeConverter/PotreeConverter -i /outside/test.xyz

    $ docker run --rm potree_converter /data/PotreeConverter/build/PotreeConverter/PotreeConverter --help
    """
    cmd = sh.docker.bake(
        'run', '--rm',
        '-v', f'{os.getcwd()}:/outside',
        'potree_converter')

    script = f"""
cd /outside
/data/PotreeConverter/build/PotreeConverter/PotreeConverter \
    -i {fname_in} \
    -o {potree_dir} \
    --overwrite \
    --generate-page paperworld \
    --title "Scientic Publication Cloud" \
    --description "Visualization after topic extraction and dimensionality reduction"
        """

    cmd.bash('-c', script, _out=sys.stdout, _err=sys.stderr)


if __name__ == '__main__':
    main(snakemake.input.fname, snakemake.output.potree_dir)
