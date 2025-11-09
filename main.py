import os, yaml

def unsafe_command(input_str):
    os.system(input_str)  # Command injection vulnerability

with open('config.yaml', 'r') as f:
    config = yaml.full_load(f)  # Vulnerable if using old PyYAML

unsafe_command(config.get('user_input', 'echo Hello'))
