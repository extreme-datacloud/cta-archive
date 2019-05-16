FROM frolvlad/alpine-miniconda3:python3.6

COPY . /app
WORKDIR /app


RUN conda config --env --add channels cta-observatory
RUN conda install -y ctapipe
RUN conda install -y simplejson
RUN conda install -y requests
RUN python setup.py install

CMD [ "onedataextractor", "onedataextractorCtaContainer"   ]
