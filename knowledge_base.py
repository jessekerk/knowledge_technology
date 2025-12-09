class Rule:
    def __init__(self, conditions, conclusion):
        self.conditions = conditions
        self.conclusion = conclusion


class KnowledgeBase:
    def __init__(self):
        self.rules = []  # all rules
        self.facts = set()  # current known facts

    def add_rule(self, rule):
        self.rules.append(rule)

    def add_fact(self, fact):
        self.facts.add(fact)
