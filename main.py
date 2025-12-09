from __future__ import annotations

from inference_engine import BackwardEngine, ForwardEngine
from knowledge_base import KnowledgeBase, Rule

kb = KnowledgeBase()

# forward-style rules
kb.add_rule(Rule(["pain_high"], "severe_pain"))
kb.add_rule(Rule(["xray_severe"], "advanced_arthrosis"))
kb.add_rule(Rule(["severe_pain", "conservative_failed"], "surgery_indicated"))

# risk assessment rules
kb.add_rule(Rule(["BMI_over_35"], "surgery_high_risk"))

# backward-style rules
kb.add_rule(Rule(["surgery_indicated", "NOT_surgery_high_risk"], "proceed_surgery"))
kb.add_rule(Rule(["surgery_high_risk"], "delay_surgery"))


# adding facts

kb.add_fact("pain_high")
kb.add_fact("conservative_failed")
kb.add_fact("xray_severe")
kb.add_fact("BMI_over_35")  # someone who is overweight has an increased surgery risk


# run fwd eng

fwd = ForwardEngine(kb)
derived = fwd.run()

print("Facts after forward chaining:")
for fact in sorted(derived):
    print("-", fact)

# run the backward eng

bwd = BackwardEngine(kb)

print("\nBackward chaining queries:")
print("Is surgery indicated?       ", bwd.solve("surgery_indicated"))
print("Is this patient high-risk?  ", bwd.solve("surgery_high_risk"))
print("Should we proceed?          ", bwd.solve("proceed_surgery"))
print("Should surgery be delayed?  ", bwd.solve("delay_surgery"))
