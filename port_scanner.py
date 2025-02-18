import subprocess

def scan_ports(ip):
  print("f\n[+] Scanning {ip} for open ports...")

  result=subprocess.run(["nmap","-p-","-sV","--open",ip], capture_output=True,text=True)

  return result.stdout


if __name__ == "__main__":
    
    #Read resolved IPs from file
    
    with open("resolved_ips.txt","r") as f:
        ips = f.read().splitlines()
        
        # Scan each IP and store results
        
        scan_results ={}
        
        for ip in ips:
            scan_results[ip] =scan_ports(ip)
            
            # Save the results in a file
            
            with open("scan_results.txt","w") as f:
                for ip, result in scan_results.item():
                    f.write(f"--- Scan Results for {ip} --\n{result}\n\n")
                    
                    Print("\n[+] Port Scanning completed ! Resulsts saved to scan_results.txt")
                    
                    