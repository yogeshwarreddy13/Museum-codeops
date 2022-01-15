import zipfile
import os
import shutil


def generate_zip(source_dir, target_path):
    """
    Generates a zip file from a given directory.
    :param source_dir: path of source directory.
    :param target_path: path where the new zip file must be generated
    """

    if os.path.exists(source_dir):
        if os.path.isdir(source_dir):
            shutil.make_archive(target_path, 'zip', source_dir)


def unzip_file(source_file, target_dir):
    """
    function to unzip a given file.
    :param source_file: path of the zip file.
    :param target_dir: path where the file must be unzipped.
    """

    if os.path.exists(source_file) and os.path.exists(target_dir):
        if os.path.isdir(target_dir):
            with zipfile.ZipFile(source_file, 'r') as zip_ref:
                zip_ref.extractall(target_dir)

