import subdomain_finder
import domainResolve
import port_scanner
import vuln_scanner
import report_generator


# ✅ Function to display a cool banner
def show_banner():
    banner = """
██████╗ ███████╗ ██████╗ ██████╗  ██████╗ ███╗   ███╗ █████╗ ███████╗████████╗███████╗██████╗ 
██╔══██╗██╔════╝██╔════╝ ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗
██████╔╝███████╗██║  ███╗██████╔╝██║   ██║██╔████╔██║███████║███████╗   ██║   █████╗  ██████╔╝
██╔═══╝ ╚════██║██║   ██║██╔═══╝ ██║   ██║██║╚██╔╝██║██╔══██║╚════██║   ██║   ██╔══╝  ██╔══██╗
██║     ███████║╚██████╔╝██║     ╚██████╔╝██║ ╚═╝ ██║██║  ██║███████║   ██║   ███████╗██║  ██║
╚═╝     ╚══════╝ ╚═════╝ ╚═╝      ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
                               RECONMASTER - Automated Reconnaissance Tool                              
"""
    print(banner)

if __name__ == "__main__":
    show_banner()




if __name__ == "__main__":
    domain = input("Enter the domain: ").strip()
    
    
    # step1 : Find subdomains
    
    subdomains = subdomain_finder.find_subdomains(domain)
    
    
    # step 2: Resolve subdomains to IPs
    
    resolved_ips = domainResolve.resolve_subdomain_with_dnsx(subdomains)
    
   
    # Step 3: Scan for open ports
   
    print("\n[+] Starting port scanning...")
    for ip in resolved_ips:
    port_scanner.scan_ports(ip)
    
    
     # Step 4: Scan for vulnerabilities
    print("\n[+] Starting vulnerability scanning...")
    
    vuln_scanner.scan_vulnerabilities(subdomains + resolved_ips)

  
  
  # Step 5: Generate final report
    print("\n[+] Generating final report...")
    report_generator.generate_json_report()
    report_generator.generate_csv_report()
    report_generator.generate_pdf_report()

    print("\n[✔] Full reconnaissance completed! Check final_report.json, final_report.csv, and final_report.pdf")
  
    
    
    
    
    