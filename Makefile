TAG = $(shell git describe --tags --always)
PREFIX = $(shell git config --get remote.origin.url | rev | cut -d '/' -f 2 | rev)
REPO_NAME = $(shell git config --get remote.origin.url | tr ':.' '/'  | rev | cut -d '/' -f 2 | rev)

install:
	conda env create -f environment.yml
	conda activate ctaarchiveenv
	conda install numpy protobuf astropy
	#pip install https://github.com/cta-sst-1m/protozfitsreader/archive/v1.0.2.tar.gz
	python setup.py install
	python -m unittest discover -v
	
docker-image:
	docker build -t $(PREFIX)/$(REPO_NAME) . # Build new image and automatically tag it as latest
	docker tag $(PREFIX)/$(REPO_NAME) $(PREFIX)/$(REPO_NAME):$(TAG) # Add the version tag to the latest image

docker-test:
	docker run $(PREFIX)/$(REPO_NAME) onedatacustom/test/ressources/example_9evts_NectarCAM.fits.fz
	docker run $(PREFIX)/$(REPO_NAME) onedatacustom/test/ressources/gamma_test.hdf5
	