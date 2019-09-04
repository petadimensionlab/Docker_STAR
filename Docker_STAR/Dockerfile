FROM continuumio/miniconda3:4.7.10

MAINTAINER petadimensionlab

RUN apt-get update -y && \
	apt-get install -y wget bzip2 tar nano && \
	wget -P / "http://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/2.9.2/sratoolkit.2.9.2-ubuntu64.tar.gz" && \
	tar zxf sratoolkit.2.9.2-ubuntu64.tar.gz && \
	cp -r sratoolkit.2.9.2-ubuntu64/bin/* /usr/bin/ && \
	rm -rf sratoolkit.2.9.2-ubuntu64*

RUN conda config --add channels defaults && \
	conda config --add channels conda-forge && \
	conda config --add channels r && \
	conda config --add channels bioconda && \
	conda install -y -c bioconda parallel-fastq-dump=0.6.5 && \
	conda install -y -c bioconda fastp=0.20.0 && \
	conda install -y -c bioconda star=2.7.2b && \
	conda install -y -c r r

RUN echo 'local({r <- getOption("repos"); r["CRAN"] <- "http://cran.r-project.org"; options(repos=r)})' > ~/.Rprofile && \
	R -e 'if (!requireNamespace("BiocManager", quietly = TRUE))install.packages("BiocManager");BiocManager::install("Rsubread")' && \
	R -e 'if (!requireNamespace("BiocManager", quietly = TRUE))install.packages("BiocManager");BiocManager::install("edgeR")'

ADD script /script

WORKDIR /