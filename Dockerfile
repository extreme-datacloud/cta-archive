FROM frolvlad/alpine-miniconda3:python3.6

COPY . /app
WORKDIR /app


RUN conda config --env --add channels cta-observatory
RUN conda install ctapipe
RUN conda install simplejson
RUN conda install requests
RUN conda install
RUN python setup.py install

CMD [ "onedataextractor", "onedataextractorCtaContainer"   ]
