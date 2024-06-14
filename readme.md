# VNC Configuration Script

This script automates the generation of VNC configuration files, encodes the passwords using DES encryption, and creates a zip archive of the generated files. Additionally, it computes and saves the SHA-256 checksum of the zip file.

VNC uses a well known and public encryption key. Below is the hex string.
```
E84AD660C4721AE0
```


## Requirements

- Python 3.x
- pyDes library
- hashlib library (included in Python's standard library)

## Pre-Installation (Optional)

### Windows:

```sh
python -m venv venv
venv\Scripts\activate
```
### Unix or MacOS:
```sh
python -m venv venv
source venv/bin/activate
```
Using a single backslash is the correct way to specify paths on Windows in this context.

## Installation

1. Install Python 3.x if it's not already installed. You can download it from [python.org](https://www.python.org).

2. Install the pyDes library. Run the following command to install the required library:
```sh
pip install pyDes
```
or
```sh
pip install -r requirements.txt
```
## Directory Structure

Ensure the following directory structure:

- `project_root/`
  - `src/`
    - `vnc_servers.csv` : CSV file containing the server names and passwords.
    - `template.vnc` : Template VNC file to be customized for each server.
    - `make_vnc_files.py`
  - `test/`
    - `test_DES_encoding.py`

## Usage

- `src/vnc_servers.csv`: CSV file containing the server names and passwords.
- `src/template.vnc`: Template VNC file to be customized for each server.

- `src/vnc_servers.csv`: CSV file containing the server names and passwords.
- `src/template.vnc`: Template VNC file to be customized for each server.

## Usage

1. Prepare the CSV file:
   - The CSV file (`vnc_servers.csv`) should have two columns: the first column for server names and the second column for passwords.

2. Prepare the VNC template file:
   - The VNC template file (`template.vnc`) should contain placeholders for the server name and password.

3. Run the script:
   - Place the script in the root directory (same level as `src`). Run the script:
     ```
     python make_vnc_files.py
     ```

4. Output:
   - The script will generate VNC files in a temporary directory, zip the files, delete the temporary directory, and create a SHA-256 checksum of the zip file.
   - The zip file (`vnc_files.zip`) and checksum file (`vnc_files_sha256.txt`) will be saved in the root directory.

## Script Explanation

The script performs the following steps:

1. Define DES Key: Uses a well-known DES key for UltraVNC.
2. Encode Passwords: Truncates passwords to 8 characters and encodes them using DES encryption.
3. Generate VNC Files: Creates VNC configuration files by replacing placeholders in the template with actual server names and encoded passwords.
4. Zip the Files: Creates a zip archive of the generated VNC files.
5. Delete Temporary Directory: Removes the temporary directory containing the VNC files.
6. Compute SHA-256 Checksum: Calculates the SHA-256 checksum of the zip file and saves it to a text file.

## Example

An example of the expected output:

- `vnc_files.zip`: Contains the generated VNC configuration files.
- `vnc_files_sha256.txt`: Contains the SHA-256 checksum of the zip file.