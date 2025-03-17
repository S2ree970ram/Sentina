import argparse
import os
import modules.subdomains as subdomains
import modules.ports as ports
import modules.http_probe as http_probe
import modules.directory_enum as directory_enum
import modules.vuln_scan as vuln_scan

# Output Directory
RESULTS_DIR = "results"
os.makedirs(RESULTS_DIR, exist_ok=True)

def main():
    parser = argparse.ArgumentParser(description="Sentinal - Automated Reconnaissance Tool")
    parser.add_argument("-d", "--domain", required=True, help="Target domain for reconnaissance")
    args = parser.parse_args()
    domain = args.domain

    print(f"🔍 Starting reconnaissance on {domain}...\n")

    # Run each module
    subdomains.run(domain, RESULTS_DIR)
    ports.run(domain, RESULTS_DIR)
    http_probe.run(RESULTS_DIR)
    directory_enum.run(domain, RESULTS_DIR)
    vuln_scan.run(RESULTS_DIR)

    print("\n✅ Reconnaissance completed. Check the 'results/' directory.")

if __name__ == "__main__":
    main()
