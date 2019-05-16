FROM frolvlad/alpine-miniconda3:python3.6

COPY . /app
WORKDIR /app

RUN conda env create -f environment.yml
RUN conda init xonsh
RUN conda activate ctaarchiveenv
RUN python setup.py install

CMD [ "onedataextractor" ]
