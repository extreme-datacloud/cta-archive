FROM frolvlad/alpine-miniconda3:python3.6

COPY . /root
WORKDIR /root

RUN conda env create -f environment.yml
RUN source activate ctaarchiveenv
RUN conda install numpy protobuf astropy
RUN pip install https://github.com/cta-sst-1m/protozfitsreader/archive/v1.0.2.tar.gz astropy

RUN python setup.py install

ENTRYPOINT [ "onedataextractor" ]
