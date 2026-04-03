class RuleConfig:
    @classmethod
    def from_yaml(cls, path):
        return cls()

class RuleGenerator:
    def __init__(self, source=None, config=None):
        self.source = source
        self.config = config
    
    def generate(self):
        return []
