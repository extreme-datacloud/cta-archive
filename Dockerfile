FROM frolvlad/alpine-miniconda3:python3.6

COPY . /app
WORKDIR /app

RUN conda env create -f environment.yml
RUN echo "source activate ctaarchiveenv" > ~/.bashrc
ENV PATH /opt/conda/envs/env/bin:$PATH
RUN python setup.py install

CMD [ "onedataextractor", "onedataextractorCtaContainer"   ]
