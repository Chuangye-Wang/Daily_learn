from pathlib import Path


def replace_text(dir_path, from_text, to_text, file_type=".py"):
    """Replace the text with the other text in the files.

    Notes
    -----
    # Except using "r" and "w+" mode; writing to a file using "r+" mode.
    with open(file, "r+", encoding="utf-8") as f:
        lines = f.readlines()
        f.seek(0)  # set the file's cursor at the beginning of the file.
        f.truncate()  # truncate all content in the file.
        updated_lines = [line.replace(from_text, to_text) for line in lines]
        f.writelines(updated_lines)  # write new content to the file.

    Parameters
    ----------
    dir_path: str or Path
        The path to the folder or file.
    from_text: str
        The text to be replaced.
    to_text: str
        The text used to replace the from_text.
    file_type: str
        The file type/suffix.

    Returns
    -------
    None
    """
    dir_path = Path(dir_path)
    if dir_path.is_file():
        files = [dir_path]
    else:
        files = list(dir_path.glob("*"))
    while files:
        file = files.pop()
        if file.suffix == file_type:
            with open(file, "r", encoding="utf-8") as f:
                lines = f.readlines()
            updated_lines = [line.replace(from_text, to_text) for line in lines]
            with open(file, "w+", encoding="utf-8") as f:
                f.writelines(updated_lines)
        elif file.is_dir():
            files = list(file.glob("*")) + files


if __name__ == "__main__":
    # # Replace "Heart Curve" with "Heart of Love" in all .py files.
    # folder_path = Path(r"pseudo_folder")
    # from_text1 = "Heart Curve"
    # to_text1 = "Heart of Love"
    # replace_text(folder_path, from_text1, to_text1, file_type=".py")

    # Replace "Sun" with "Great Sun" in all .txt files.
    folder_path = Path(r"pseudo_folder")
    from_text1 = "Sun"
    to_text1 = "SUN"
    replace_text(folder_path, from_text1, to_text1, file_type=".txt")
