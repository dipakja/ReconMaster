import json
import csv
from fpdf import FPDF

def generate_json_report():
    print("\n[+] Generating JSON Report...")
    
    # Read data from files
    with open("subdomains.txt", "r") as f:
        subdomains = f.read().splitlines()

    with open("resolved_ips.txt", "r") as f:
        resolved_ips = f.read().splitlines()

    with open("scan_results.txt", "r") as f:
        port_scan_results = f.read().split("\n\n")

    with open("nuclei_results.txt", "r") as f:
        vuln_results = f.read().splitlines()

    # Create structured data
    report = {
        "subdomains": subdomains,
        "resolved_ips": resolved_ips,
        "port_scan_results": port_scan_results,
        "vulnerabilities": vuln_results
    }

    # Save to JSON file
    with open("final_report.json", "w") as f:
        json.dump(report, f, indent=4)

    print("[✔] JSON report saved as final_report.json")

def generate_csv_report():
    print("\n[+] Generating CSV Report...")
    
    with open("final_report.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Subdomain", "IP Address", "Open Ports", "Vulnerabilities"])

        # Read subdomains and IPs
        subdomains = open("subdomains.txt").read().splitlines()
        ips = open("resolved_ips.txt").read().splitlines()
        ports = open("scan_results.txt").read().split("\n\n")
        vulns = open("nuclei_results.txt").read().splitlines()

        for i in range(len(subdomains)):
            writer.writerow([subdomains[i], ips[i] if i < len(ips) else "", ports[i] if i < len(ports) else "", vulns[i] if i < len(vulns) else ""])

    print("[✔] CSV report saved as final_report.csv")

def generate_pdf_report():
    print("\n[+] Generating PDF Report...")
    
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", style="B", size=16)
    pdf.cell(200, 10, "Reconnaissance Report", ln=True, align="C")
    pdf.ln(10)

    # Read & add data
    def add_section(title, filename):
        pdf.set_font("Arial", style="B", size=14)
        pdf.cell(200, 10, title, ln=True)
        pdf.set_font("Arial", size=12)
        with open(filename, "r") as f:
            for line in f.readlines():
                pdf.multi_cell(0, 8, line.strip())
        pdf.ln(10)

    add_section("Subdomains Found", "subdomains.txt")
    add_section("Resolved IPs", "resolved_ips.txt")
    add_section("Port Scan Results", "scan_results.txt")
    add_section("Vulnerabilities Found", "nuclei_results.txt")

    pdf.output("final_report.pdf")
    print("[✔] PDF report saved as final_report.pdf")

if __name__ == "__main__":
    generate_json_report()
    generate_csv_report()
    generate_pdf_report()
