PIP:=pip3
PROMTOOL:=promtool

all: groups test

python-deps:
	$(PIP) install pyyaml

groups:
	./bin/group.py --rules ./rules/*.rules --out ./rules/tests/group.yml

test:
	$(PROMTOOL) test rules ./tests/group_test.yml
