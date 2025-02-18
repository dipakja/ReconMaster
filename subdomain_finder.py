import subprocess


#This function will take the domain as a argument and give the subdomain
def find_subdomains(domain):
    result =subprocess.run(["subfinder","-d",domain],capture_output=True,text=True)
    subdomains = result.stdout.strip().split("\n")
    return subdomains

# Example usage

# domain ="example.com"
# subdomains = find_subdomains(domain)
# print(subdomains)

# Taking input from the user

domain = input("Enter the domain for reconnaissance: ").strip()


# Running the function with user input
subdomains = find_subdomains(domain)

# printing results

print("\n[+] Found Subdomains: ")

for sub in subdomains:
    print(f" - {sub}")
    
    
    # Save subdomains to a file for the next module
    
    with open("subdomains.txt", "w") as f:
        f.write("\n".join(subdomains))


