import os, sys, shutil

if len(sys.argv) < 2 :
    print("Usage: python new_project.py <dst_folder> (proj_name)")
    sys.exit(1)

prc_folder = os.path.dirname(__file__)
dst_folder = os.path.abspath(sys.argv[1])
project_name = os.path.basename(dst_folder) if len(sys.argv) <= 2 else sys.argv[2]

def get_files(folder: str, dst: str, proj_name: str, *, files: list[str] = [], ignore: list[str] = []) -> list[tuple[str,str]]:
    for i in os.listdir(folder):
        if i not in ignore:
            if os.path.isdir(i):
                get_files(os.path.abspath(i), os.path.join(dst, i), proj_name, files=files)
            else:
                files.append((os.path.join(folder, i), os.path.join(dst, i.replace('KiCad-template', proj_name))))
    return files

for src, dst in get_files(prc_folder, dst_folder, project_name, ignore=[".git"]):
    if not os.path.exists(path := os.path.dirname(dst)):
        os.makedirs(path)
    shutil.copyfile(src, dst)