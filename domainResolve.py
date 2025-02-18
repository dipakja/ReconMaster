import subprocess

def resolve_subdomain_with_dnsx(subdomains):
    
    subdomains_str = "\n".join(subdomains) # convert list to newline-sperated string
    
    result = subprocess.run(["dnsx", "-silent"], input=subdomains_str,capture_output=True,text=True)
    
    return result.stdout.strip().split("\n")


if __name__=="__main__":
    
    # Read subdomain from the file savecd by subdomain_finder.py
    
    with open("subdomain.txt", "r") as f:
        subdomains = f.read().splitlines()
        
        
        resolved_ips  = resolve_subdomain_with_dnsx(subdomains)
        
        print("\n[+] Resolved Subdomains to IPs: ")
        
        for entry in resolved_ips:
            print(entry)
            
            
            
     # Save results to a file for the next module
     
        with open("resolved_ips.txt", "w") as f:
         f.write("\n".join(resolved_ips))


        
   
    
   
        