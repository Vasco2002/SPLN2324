import jinja2
from glob import glob
import ast

# Extract dependencies from a Python file
def extract_dependencies(filename):
    with open(filename, 'r') as file:
        tree = ast.parse(file.read(), filename=filename)
    
    dependencies = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                dependencies.add(alias.name)
        elif isinstance(node, ast.ImportFrom):
            dependencies.add(node.module)
    
    return list(dependencies)

#List of Python files on this directory
modes = glob("*.py")

# Extract dependencies from all the Python files from this directory
all_dependencies = set()
for mode in modes:
    dependencies = extract_dependencies(mode)
    all_dependencies.update(dependencies)

#Choose primary Module
if len(modes) >= 1:
    print("Choose the primary Python file:")
    for i, mode in enumerate(modes, start=1):
        print(f"{i}. {mode}")

    choice_num = input("Enter the number of the primary file: ")
    if choice_num.isdigit() and 1 <= int(choice_num) <= len(modes):
        primary_index = int(choice_num) - 1
        name = modes[primary_index].replace(".py", "")
    else:
        print("Invalid choice. Using the first file as default.")
        name = modes[0].replace(".py", "")
else:
    name = "Modulo?"

# Create Jinja2 template
pp = jinja2.Template("""[build-system]
requires = ["flit_core >=3.2,<4"]
build-backend = "flit_core.buildapi"

[project]
name = "{{name}}"
authors = [
    {name = "{{autor}}", email = "{{email}}"},
]
classifiers = [
    "License :: OSI Approved :: MIT License",
]
requires-python = ">=3.8"
dynamic = ["version", "description"]
dependencies = [
    {% for dependency in dependencies %}
    "{{ dependency }}",
    {% endfor %}
]

[project.scripts]
{{name}} = "{{name}}:main"
""")

# Render the template with dependencies
rendered_content = pp.render(name=name, autor="Vasco", email="pg54269@alunos.uminho.pt", dependencies=all_dependencies)

print(rendered_content)