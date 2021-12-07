# ClickView Docker Files
This repo contains docker files used at ClickView build scripts to generate them from templates


# Generating Dockerfiles

## Requirements
- Python3
  - pip
  - virtualenv


## Installation

1. Create a new virtual environment

```bash
python3 -m venv env
```

2. Activate the virtual environment

Windows:
```bash
env\Scripts\activate.bat
```

Unix/MacOs:
```bash
source env/bin/activate
```

3. Install dependencies

```bash
python3 -m pip install -r requirements.txt
```

## Running the template script

```bash
python3 template.py [type]
```

Where type is one of the following template types:
- dotnet


# Updating the templates
The templates are split into multiple areas:

## manifest.yaml
This contains a list of all the template types, the versions associated with that template type, and then any data for each of the versions.

The data listed under each version is injected into the templated defined in the `_template` folder (see below).

Versions can be defined with a `/` which will create nested directories.

### Example

Here is an example `manifest.yaml` file which contains a `test` template type and 2 versions which will create the following directory structure:

- test
  - 1.0
    - a
  - 1.1
    - b

```yaml
test:
  versions:
    '1.0/a':
      data:
    '1.1/b':
      data:
```

## Template type directory
Every template type needs a matching directory in the root directory (eg `dotnet`). Within this directory, there should be a `_templates` directory that contains all the templates used for generating the output files. The templates should be suffixed with `.template` (which will be removed during the templating process).

The versions defined in `manifest.yaml` will have directories created within this directory, and the contents of those will contain the generated dockerfiles.

