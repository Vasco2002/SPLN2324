#!/usr/bin/env python3
"""python makepyproject.py"""

import jinja2
import jjcli
from glob import glob
import os
import json

def main():
    #project name
    modes = glob("*.py")
    if len(modes)>=1:
        name = modes[0].replace(".py","")
    else:
        name = input("Modulo?")

    v = jjcli.qx(f"grep name '{name}.py'")
    print("Debug: ", len(v))

    version = "0.0.1"

    # Create Jinja2 template
    pp = jinja2.Template("""[build-system]
    requires = ["flit_core >=3.2,<4"]
    build-backend = "flit_core.buildapi"

    [project]
    name = "{{name}}"
    authors = [
        {name = "{{autor}}", email = "{{email}}"},
    ]
    version = "{{version}}"
    classifiers = [
        "License :: OSI Approved :: MIT License",
    ]
    requires-python = ">=3.8"
    dynamic = ["description"]
    dependencies = [
        "jjcli"
    ]

    [project.scripts]
    {{name}} = "{{name}}:main"
    """)


    metadata_path = str(os.path.expanduser("~/.METADATA.json"))
    file = open(metadata_path)
    #FIXME criar se não existir
    data = json.load(file)
    autor = data["Username"]
    email = data["Email"]

    out = pp.render({"name":name,"autor":autor,"email":email})
    print("Debug: ",out)

    #rendered_content = pp.render(name=name, autor="Vasco", email="pg54269@alunos.uminho.pt", version=version)
    #print("Debug: ",rendered_content)

    file_output = open("pyproject.toml","w")
    #file_output.write(rendered_content)
    file_output.write(out)

if __name__ == "__main__":
    main()