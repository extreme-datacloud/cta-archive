FROM frolvlad/alpine-miniconda3:python3.6

COPY . /root
WORKDIR /root

RUN conda env create -f environment.yml
RUN source activate ctaarchiveenv
RUN conda install numpy

RUN python setup.py install

CMD [ "onedataextractor" ]
