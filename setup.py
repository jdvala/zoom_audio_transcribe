import io
import os.path as path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

requirements_path = path.join(here, "requirements", "prod.txt")
readme_path = path.join(here, "README.md")


def read_requirements(path):
    try:
        with io.open(path, mode="rt", encoding="utf-8") as fp:
            return list(filter(None, (line.split("#")[0].strip() for line in fp)))
    except IndexError:
        raise RuntimeError("{} is broken".format(path))


def read_readme(path):
    with io.open(path, mode="rt", encoding="utf-8") as fp:
        return fp.read()


setup(
    name="zoom_audio_transcribe",
    python_requires=">=3.6",
    setup_requires=["setuptools_scm"],
    install_requires=read_requirements(requirements_path),
    long_description=read_readme(readme_path),
    long_description_content_type="text/markdown",
    use_scm_version={
        "version_scheme": "guess-next-dev",
        "local_scheme": "dirty-tag",
        "write_to": "src/zoom_audio_transcribe/_repo_version.py",
        "write_to_template": 'version = "{version}"\n',
        "relative_to": __file__,
    },
    include_package_data=True,
    package_data={},
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": ["zoom_audio_transcribe = zoom_audio_transcribe.cli:main"]
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Operating System :: linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Archiving :: Packaging",
        "Topic :: System :: Systems Administration",
        "Topic :: System :: Installation/Setup",
        "Topic :: Utilities",
    ],
    author="Jay Vala",
    author_email="jay.vala@msn.com",
    url="https://github.com/jdvala/zoom_audio_transcribe",
)
