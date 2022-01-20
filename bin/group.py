#!/usr/bin/env python3

import argparse
import sys
from glob import glob

import yaml


class Group:
    alerts = {"name": "alerts", "rules": []}

    def __init__(self, rules_path, out_path):
        self.rules_path = rules_path
        self.out_path = out_path

    def load_rules(self):
        for rule in glob(self.rules_path):
            with open(rule) as f:
                rule_content = yaml.load(f.read(), Loader=yaml.FullLoader)
                self.add_rule(rule_content)

    def add_rule(self, rule):
        self.alerts["rules"].extend(rule)

    def to_yaml(self):
        with open(self.out_path, 'w') as f:
            f.write(yaml.dump({"groups": [self.alerts]}))


def main():
    parser = argparse.ArgumentParser(description="Builds a groups file for direct prometheus use of rules")
    parser.add_argument("--rules", help="blob path for rules files to be loaded from")
    parser.add_argument("--out", help="full path to output the file to")

    args = parser.parse_args(sys.argv[1:])
    
    group = Group(args.rules, args.out)
    group.load_rules()
    group.to_yaml()


if __name__ == "__main__":
    main()
