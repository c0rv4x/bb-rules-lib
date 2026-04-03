class RuleConfig:
    @classmethod
    def from_yaml(cls, path): return cls()
    source_url = ""
    output_format = "yaml"

class RuleGenerator:
    def __init__(self, source=None, config=None):
        self.source = source
    def generate(self): return []

class BountyParser:
    def __init__(self, url): pass

def format_rules(rules, fmt="yaml"): return str(rules)
