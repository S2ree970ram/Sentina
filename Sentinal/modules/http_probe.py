import os

def run(output_dir):
    print(f"🌍 Checking for live HTTP services...")
    input_file = os.path.join(output_dir, "subdomains.txt")
    output_file = os.path.join(output_dir, "live_hosts.txt")

    cmd = f"httpx -l {input_file} -o {output_file}"
    os.system(cmd)

    print(f"✅ Live hosts saved in {output_file}\n")
