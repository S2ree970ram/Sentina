import os

def run(domain, output_dir):
    print(f"📂 Enumerating directories for {domain}...")
    wordlist = "/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt"
    output_file = os.path.join(output_dir, "directories.txt")

    cmd = f"ffuf -u http://{domain}/FUZZ -w {wordlist} -o {output_file}"
    os.system(cmd)

    print(f"✅ Discovered directories saved in {output_file}\n")
