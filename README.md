# Docker_STAR
RNAseq(STAR) analysis for docker.

Reference URL:https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4631051/

## Usage

### Docker pull image

```
docker pull petadimensionlab/docker_star
```

### Docker run

```
docker run -it --name container_name -v /yourlocal_dir:/condir --rm  petadimensionlab/docker_functree2
```

Copy your local "genome file", "annotation file" and "sample ID file(fastq_files.txt)" into "/yourlocal_dir".

### Run this docker python script
#### 1.Download sras

```
# cd script
# python exec_download_sras.py
```

#### 2.Make STARindex

```
# python exec_make_STARindex.py
```

line 5 or 6 = Change the 'species'.

#### 3.Run RNAseq(STAR) analysis

```
# python  seq_exec_sra2readcount_STAR.py
```

line 3 to 15 = Change these as needed.

### Exit docker

```
# exit
```

### Caution
Need to limit the resource available to  docker engine.

Reference URL:https://docs.docker.com/docker-for-mac/
