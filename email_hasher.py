#!/usr/bin/env python3
"""
Email Hasher Script

This script takes an email address as a command line argument,
hashes it using the SHA-256 algorithm, and writes the hash to a file.

Usage:
    python email_hasher.py <email_address>

Example:
    python email_hasher.py example@email.com
"""

import sys
import hashlib
import re

def hash_email(email):
    """
    Hash an email address using SHA-256 and return the hexadecimal digest.
    
    Args:
        email (str): The email address to hash
        
    Returns:
        str: The SHA-256 hash of the email in hexadecimal format
    """
    # TODO: Implement this function
    # 1. Convert the email string to bytes
    # 2. Create a SHA-256 hash of the email
    # 3. Return the hash in hexadecimal format

    byte_email = email.encode('UTF-8')
    hash = hashlib.sha256()
    hash.update(byte_email)
    hash = hash.hexdigest()
    return hash

def write_hash_to_file(hash_value, filename = "hash.email"):
    """
    Write a hash value to a file.
    
    Args:
        hash_value (str): The hash value to write
        filename (str): The name of the file to write to (default: "hash.email")
    """
    # TODO: Implement this function
    # 1. Open the file in write mode
    # 2. Write the hash value to the file
    # 3. Close the file
    with open(filename, "w") as f:
        print(hash_value, file = f)

def main():
    """
    Main function to process command line arguments and execute the script.
    """
    # TODO: Implement this function
    # 1. Check if an email address was provided as a command line argument
    # 2. If not, print an error message and exit with a non-zero status
    # 3. If yes, hash the email address
    # 4. Write the hash to a file named "hash.email"

    if len(sys.argv) < 2:
        print("Error! Please provide an email address!")

    else:
        email = sys.argv[1]
        # Check to see that the input is indeed an email address
        # pattern = re.compile(r"^(?!\.)(?!.*\.\.)[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+"
        #                      r"@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$")
        # if not re.match(pattern, email):
        #     print("Warning! Please provide a valid email address!")

        # else:
        hash_value = hash_email(email)
        write_hash_to_file(hash_value, filename = "hash.email")
        print(hash_value)

if __name__ == "__main__":
    main()
