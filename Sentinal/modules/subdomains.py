import os

def run(domain, output_dir):
    print(f"🌐 Enumerating subdomains for {domain}...")
    output_file = os.path.join(output_dir, "subdomains.txt")
    
    cmd = f"subfinder -d {domain} -o {output_file}"
    os.system(cmd)

    print(f"✅ Subdomains saved in {output_file}\n")
