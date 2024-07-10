import paramiko

def download_file_via_ssh(ssh_host, ssh_port, ssh_username, ssh_password, remote_file_path, local_file_path):
    # Connect to the SSH server
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ssh_host, port=ssh_port, username=ssh_username, password=ssh_password)
    
    # Use SFTP to download the file
    sftp = ssh.open_sftp()
    sftp.get(remote_file_path, local_file_path)
    sftp.close()
    ssh.close()

def extract_last_matching_line(file_path, search_string):
    last_matching_line = ""
    # Open the local file to read its content
    with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
        # Iterate through each line in the file
        for line in file:
            # If the search string is found in the line, update the last matching line
            if search_string in line:
                last_matching_line = line.strip()
    return last_matching_line

def extract_desired_value(line, search_string):
    # Find the starting index of the desired value in the line
    start_index = line.find(search_string) + len(search_string)
    # Return the extracted value after the search string
    return line[start_index:].strip()

def test_ssh_connection(ssh_host, ssh_port, ssh_username, ssh_password):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ssh_host, port=ssh_port, username=ssh_username, password=ssh_password)
        ssh.close()
        return True
    except Exception as e:
        print(f"Failed to connect to SSH server: {e}")
        return False

def update_config_file(file_path, new_client_id):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    with open(file_path, 'w') as file:
        for line in lines:
            if line.startswith('CLIENT_ID'):
                file.write(f'CLIENT_ID = "{new_client_id}"\n')
            else:
                file.write(line)

