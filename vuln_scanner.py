import subprocess

def scan_vulnerabilities(targets):
    print("\n[+] Scanning for vulnerabilities using Nuclei...")
    
    # Convert list of targets into a string format for Nuclei
    targets_str = "\n".join(targets)
    
    # Run Nuclei with default templates
    result = subprocess.run(["nuclei", "-silent"], input=targets_str, capture_output=True, text=True)
    
    return result.stdout.strip().split("\n")

if __name__ == "__main__":
    # Read resolved IPs and subdomains from files
    with open("resolved_ips.txt", "r") as f:
        ips = f.read().splitlines()
    
    with open("subdomains.txt", "r") as f:
        subdomains = f.read().splitlines()
    
    # Combine both for scanning
    targets = subdomains + ips

    # Run Nuclei scanning
    scan_results = scan_vulnerabilities(targets)

    # Save results
    with open("nuclei_results.txt", "w") as f:
        f.write("\n".join(scan_results))

    print("\n[+] Nuclei scanning completed! Results saved to nuclei_results.txt")
