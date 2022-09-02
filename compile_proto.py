import os
import re
from glob import glob
from os.path import dirname
from pathlib import Path

from grpc_tools import command

os.chdir("interfaces")
command.build_package_protos(".")

dir_names = {dirname(x) for x in glob("**/*.proto")}
generated = glob("**/*pb2*.py")

search = rf'^from ({"|".join(dir_names)}) import'
replace = rf"^from .\1 import"

for source in generated:
    path = Path(source)
    parts = list(path.absolute().parts)
    parts[-3] = "proto"
    out_path = Path(*parts)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    text = re.sub(search, replace, path.read_text())
    out_path.write_text(text)
