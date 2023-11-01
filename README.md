[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](code_of_conduct.md)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/2bc51fd762814c1c8a17f836e88e65de)](https://app.codacy.com/gh/jhaenel/Dr-Alchemy-Doc-Gen/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
<table align="center">
  <tr>
    <td>
      <img src="https://github.com/jhaenel/Dr-Alchemy-Docs/blob/main/images/dr-alechemy.png?raw=true" alt="A confident woman mad scientist with African descent in a startup-like lab workspace, accompanied by a hovering self-writing quill." width="400"/>
    </td>
  </tr>
</table>

# Dr. Alchemy Docs

Dr. Alchemy Docs aims to redefine the way developers approach code documentation by harnessing the power of AI while ensuring the expertise of a human remains central to the process.

# Premise

Even the best of codes can become enigmatic without proper documentation. The objective of CodeCompanion Docs is to ensure that codebases are always accompanied by accessible, transparent, updated, and context-aware comments and documentation.

# Tenants

- When reading code, read code
- Keep documentation fresh, without exception
- Code has a hierarchy, so should documentation
- Neither humans nor AI can document code well alone

# Roadmap

## v0

- [ ] Generate a clone of a file with inline comments
- [ ] Integrate as a VSCode extension
- [ ] Only regenerate relevant changes
- [ ] Persist human added comments
- [ ] Prompt to verify relevant human-added comments are still fresh

## future

- Create more complex and insightful hierarchies, aggregations, and abstractions
- Chat about the documentation
- Generate a docs site

# Setting Up the Development Environment

## First Time Setup

To set up a Python development environment, we'll use the built-in `venv` module, which is available in Python 3.3 and later.

### 1. Ensure Python is Installed

Before you begin, ensure you have Python installed:

- **Linux/Unix**:
  ```bash
  python3 --version
  ```

- **Windows**:
  ```bash
  python --version
  ```

If Python isn't installed, download it from the [official Python website](https://www.python.org/downloads/).

### 2. Create a Virtual Environment

The virtual environment allows you to have an isolated space on your computer for Python projects, ensuring that each project can have its own set of dependencies.

- **Linux/Unix**:
  ```bash
  python3 -m venv myenv
  ```

- **Windows**:
  ```bash
  python -m venv myenv
  ```

This command creates a virtual environment named `myenv`. You can replace `myenv` with any name you prefer.

### 3. Activate the Virtual Environment

Before installing any packages, you need to activate the virtual environment:

- **Linux/Unix**:
  ```bash
  source myenv/bin/activate
  ```

- **Windows**:
  ```bash
  .\myenv\Scripts\activate
  ```

Once activated, your terminal or command prompt should show the name of the virtual environment, indicating that it's currently active.


### 4. Install Your Dependencies

```bash
pip install -r requirements-dev.txt
```


### 5. Deactivate the Virtual Environment

When done, deactivate your virtual environment:

```bash
deactivate
```

## Adding a requirement
1. If not already done install pip-tools with `pip install pip-tools`
2. Add a new dev requirements by adding the pip package name as a new line to `requirements-dev.in`
3. Compile requirements with `pip-compile requirements-dev.in`
4. Install dependencies with `pip install -r requirements-dev.txt`

## Setting Editable mode
If desired, using setup.py you can run  `pip install -e .`. You can read about the benefits here [stackoverflow](https://stackoverflow.com/questions/35064426/when-would-the-e-editable-option-be-useful-with-pip-install)

## Running tests
You can simply run all tests with `pytest`. Run a specific test file with `pytest path/to/file.py`
