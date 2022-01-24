PIP:=pip3
PROMTOOL:=promtool

all: groups test

python-deps:
	$(PIP) install pyyaml

groups:
	./bin/group.py --rules './rules/*.rule' --tests './rules/tests/*.test' --out group.yml --test_out group_test.yml

test: groups
	$(PROMTOOL) test rules ./group_test.yml
