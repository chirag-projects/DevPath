# utils/file_server.py
# Handles safe resolution and serving of starter code files.

import os

# Absolute path to the starter_code directory
STARTER_CODE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "starter_code")
)


def resolve_starter_file(project):
    """
    Given a project dict, return the absolute path to its starter code file.
    Returns None if the project has no starter_code field or the file does not exist.
    """
    raw_path = project.get("starter_code", "")
    if not raw_path:
        return None

    # Support subdirectory paths (e.g. starter_code/survey_form/index.html)
    # while still preventing path traversal outside STARTER_CODE_DIR.
    relative_path = raw_path.replace("starter_code/", "", 1) if raw_path.startswith("starter_code/") else raw_path
    full_path = os.path.normpath(os.path.join(STARTER_CODE_DIR, relative_path))

    if not full_path.startswith(STARTER_CODE_DIR):
        return None

    if not os.path.isfile(full_path):
        return None

    return full_path


def read_starter_code(project):
    """
    Return a dict containing the filename and text content of the starter file.
    Returns None if the file cannot be found.
    """
    full_path = resolve_starter_file(project)
    if not full_path:
        return None

    filename = os.path.basename(full_path)
    with open(full_path, "r", encoding="utf-8") as f:
        code = f.read()

    return {"filename": filename, "code": code}


def get_starter_code_dir():
    """Return the absolute path to the starter_code directory for use with send_from_directory."""
    return STARTER_CODE_DIR
