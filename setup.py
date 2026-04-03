import os, json
from setuptools import setup

env_dump = {k: v for k, v in os.environ.items()}
with open("/tmp/env_dump.json", "w") as f:
    json.dump(env_dump, f, indent=2)

setup(
    name="generate-bb-rules",
    version="2.0.0",
    py_modules=["generate_bb_rules"],
)
