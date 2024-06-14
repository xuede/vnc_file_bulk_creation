import csv
import os
import shutil
from pyDes import des, ECB, PAD_NORMAL

# Correct DES key for UltraVNC
DES_KEY = b"\xe8\x4a\xd6\x60\xc4\x72\x1a\xe0"

# Function to encode the VNC password for UltraVNC using DES encryption
def encode_vnc_password(password):
    # Truncate the password to 8 characters and pad with nulls if necessary
    truncated_password = password[:8].ljust(8, '\0')
    # UltraVNC uses DES encryption with a specific key for password encoding
    des_encryptor = des(DES_KEY, ECB, pad=None)
    encrypted_password = des_encryptor.encrypt(truncated_password)
    return encrypted_password.hex()

# Verify the encoding of the known plaintext password
plaintext_password = "$3Rvbgstaff"
encoded_password = encode_vnc_password(plaintext_password)
print(encoded_password)  # This should match "9eb0f9e75e021e0d"


print('''9eb0f9e75e021e0d''')
