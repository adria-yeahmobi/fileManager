from pathlib import Path
import os
import subprocess

base_dir = Path("test")


def read_file(name: str) -> str:
    """Return file content. If not exist, return error message.
    """
    print(f"(read_file {name})")
    try:
        with open(base_dir / name, "r") as f:
            content = f.read()
        return content
    except Exception as e:
        return f"An error occurred: {e}"

def list_files() -> list[str]:
    print("(list_file)")
    file_list = []
    for item in base_dir.rglob("*"):
        if item.is_file():
            file_list.append(str(item.relative_to(base_dir)))
    return file_list

def rename_file(name: str, new_name: str) -> str:
    print(f"(rename_file {name} -> {new_name})")
    try:
        new_path = base_dir / new_name
        if not str(new_path).startswith(str(base_dir)):
            return "Error: new_name is outside base_dir."

        os.makedirs(new_path.parent, exist_ok=True)
        os.rename(base_dir / name, new_path)
        return f"File '{name}' successfully renamed to '{new_name}'."
    except Exception as e:
        return f"An error occurred: {e}"

def create_text_file(filename: str, content: str) -> str:
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    return f"Text file '{filename}' created successfully."

def create_python_file(filename: str, code: str) -> str:
    if not filename.endswith('.py'):
        filename += '.py'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(code)
    return f"Python file '{filename}' created successfully."


def get_directory_structure(path: str) -> dict:
    structure = {}
    for root, dirs, files in os.walk(path):
        rel_path = os.path.relpath(root, path)
        key = rel_path if rel_path != "." else os.path.basename(path)
        structure[key] = {
            "dirs": dirs,
            "files": files
        }
    return structure


def rename_file(old_path: str, new_path: str) -> str:
    if not os.path.exists(old_path):
        return f"File '{old_path}' does not exist."
    os.rename(old_path, new_path)
    return f"Renamed '{old_path}' to '{new_path}'."

def execute_windows_command(command: str) -> str:
    try:
        result = subprocess.run(command, shell=True, check=True,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                encoding='utf-8')
        return result.stdout or "Command executed successfully with no output."
    except subprocess.CalledProcessError as e:
        return f"Error executing command:\n{e.stderr}"
