from knowledge_base import KnowledgeBase

class ForwardEngine:
    def __init__(self, kb: KnowledgeBase):
        self._kb = kb

    def run(self) -> set:
        """Runs until no new facts can be derived."""
        changed = True
        while changed:
            changed = False
            for rule in self._kb._rules:
                if rule._conclusion not in self._kb._facts:
                    if all(cond in self._kb._facts for cond in rule._conditions):
                        self._kb.add_fact(rule._conclusion)
                        changed = True
        return self._kb._facts


class BackwardEngine:
    def __init__(self, kb: KnowledgeBase):
        self._kb = kb

    def solve(self, goal: str) -> bool:
        """Returns whether goal can be proven."""
        if goal in self._kb._facts:
            return True

        for rule in self._kb._rules:
            if rule._conclusion == goal:
                if all(self.solve(cond) for cond in rule._conditions):
                    self._kb.add_fact(goal)
                    return True
        return False
