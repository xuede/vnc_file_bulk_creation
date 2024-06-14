import csv
import os
import shutil
import hashlib
from pyDes import des, ECB

# Correct DES key for UltraVNC, UVNC has a well-known key. 
#The well-known DES key for UltraVNC is 0xE84AD660C4721AE0. 
#The DES_KEY below as a byte string from the hex string
#DES_KEY = b"\xe8\x4a\xd6\x60\xc4\x72\x1a\xe0"
DES_KEY = bytes.fromhex("E84AD660C4721AE0")
# Function to encode the VNC password for UltraVNC using DES encryption
def encode_vnc_password(password):
    # Truncate the password to 8 characters and pad with nulls if necessary
    truncated_password = password[:8].ljust(8, '\0')
    # UltraVNC uses DES encryption with a specific key for password encoding
    des_encryptor = des(DES_KEY, ECB, pad=None)
    encrypted_password = des_encryptor.encrypt(truncated_password)
    return encrypted_password.hex()

# Function to create a new VNC file content
def create_vnc_file_content(template, server_name, encoded_password):
    new_content = template.replace("server_name", server_name)
    new_content = new_content.replace("host=server_name", f"host={server_name}")
    new_content = new_content.replace("encoded_password", encoded_password)
    new_content = new_content.replace("folder=", "folder=%userprofile%/documents/UltraVNC")
    return new_content

# Get the current working directory
cwd = os.getcwd()

# Path to your CSV file
csv_file_path = os.path.join(cwd, "src", "ss.csv")
vnc_template_path = os.path.join(cwd, "src", "template.vnc")

# Directory to save VNC files
output_dir = os.path.join(cwd, "vnc_files_corrected")
os.makedirs(output_dir, exist_ok=True)

# Load the VNC file to use as a template
with open(vnc_template_path, "r") as file:
    vnc_template = file.read()

# Read the CSV file
vnc_servers = []
with open(csv_file_path, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        server_name, password = row
        encoded_password = encode_vnc_password(password)
        vnc_servers.append((server_name, encoded_password))



# Generate and save VNC files
for server, encoded_password in vnc_servers:
    vnc_content = create_vnc_file_content(vnc_template, server, encoded_password)
    with open(f"{output_dir}/{server}.vnc", "w") as file:
        file.write(vnc_content)
# Zip the directory containing the corrected VNC files
shutil.make_archive(output_dir, 'zip', output_dir)

print(f"VNC files have been generated and zipped in {output_dir}.zip")
# Delete the directory after creating the zip file
#shutil.rmtree(output_dir)

# Compute the SHA-256 checksum of the zip file
zip_file_path = f"{output_dir}.zip"
sha256_hash = hashlib.sha256()
with open(zip_file_path, "rb") as f:
    for chunk in iter(lambda: f.read(4096), b""):
        sha256_hash.update(chunk)
sha256_checksum = sha256_hash.hexdigest()

# Save the SHA-256 checksum to a text file
sha256_file_path = "vnc_files_corrected_sha256.txt"
with open(sha256_file_path, "w") as f:
    f.write(f"SHA-256 checksum: {sha256_checksum}\n")

print(f"SHA-256 checksum saved to {sha256_file_path}")

print(f"SHA-256 checksum saved to {sha256_file_path}")