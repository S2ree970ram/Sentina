import os

def run(domain, output_dir):
    print(f"📡 Scanning open ports for {domain}...")
    input_file = os.path.join(output_dir, "subdomains.txt")
    output_file = os.path.join(output_dir, "ports.txt")

    cmd = f"naabu -iL {input_file} -o {output_file}"
    os.system(cmd)

    print(f"✅ Open ports saved in {output_file}\n")
