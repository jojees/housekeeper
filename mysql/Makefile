include .env_make
NS = jojees
VERSION ?= mysql

REPO = opslab
NAME = mysql
INSTANCE = shnops

build:
	docker build -t $(NS)/$(REPO):$(VERSION) .

push:
	docker push $(NS)/$(REPO):$(VERSION)

shell:
	docker run --privileged --rm --name $(NAME)-$(INSTANCE) -i -t $(PORTS) $(VOLUMES) $(ENV) $(LINKS) $(ARG) $(NS)/$(REPO):$(VERSION) bash -l

run:
	docker run --privileged --rm --name $(NAME)-$(INSTANCE) $(PORTS) $(VOLUMES) $(ENV) $(LINKS) $(ARG) $(NS)/$(REPO):$(VERSION)

start:
	docker run -d --privileged --name $(NAME)-$(INSTANCE) $(PORTS) $(VOLUMES) $(ENV) $(ARG) $(LINKS) $(NS)/$(REPO):$(VERSION)

stop:
	docker stop $(NAME)-$(INSTANCE)

rm:
	docker rm $(NAME)-$(INSTANCE)

release: build
	make push -e VERSION=$(VERSION)

default: build
