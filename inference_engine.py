class ForwardEngine:
    def __init__(self, kb):
        self.kb = kb

    def run(self):
        """Runs until no new facts can be derived."""
        changed = True
        while changed:
            changed = False
            for rule in self.kb.rules:
                if rule.conclusion not in self.kb.facts:
                    if all(cond in self.kb.facts for cond in rule.conditions):
                        self.kb.add_fact(rule.conclusion)
                        changed = True
        return self.kb.facts


class BackwardEngine:
    def __init__(self, kb):
        self.kb = kb

    def solve(self, goal):
        """Returns whether goal can be proven."""
        if goal in self.kb.facts:
            return True

        for rule in self.kb.rules:
            if rule.conclusion == goal:
                if all(self.solve(cond) for cond in rule.conditions):
                    self.kb.add_fact(goal)
                    return True

        return False
