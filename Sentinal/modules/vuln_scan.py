import os

def run(output_dir):
    print(f"🛡️ Scanning for vulnerabilities...")
    input_file = os.path.join(output_dir, "live_hosts.txt")
    output_file = os.path.join(output_dir, "vulnerabilities.txt")

    cmd = f"nuclei -l {input_file} -t ~/nuclei-templates/ -o {output_file}"
    os.system(cmd)

    print(f"✅ Vulnerabilities saved in {output_file}\n")
