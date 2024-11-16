import json
import csv
from typing import List

def read_json_file(filename: str) -> List[str]:
    """Read JSON file and return list of lines."""
    try:
        with open(filename) as f:
            return f.read().splitlines()
    except FileNotFoundError:
        print(f"Error: File {filename} not found")
        return []

def parse_ip_addresses(data: List[str], org_names: List[str]) -> List[str]:
    """Extract IP addresses for specified organizations."""
    ip_addresses = []
    for line in data:
        try:
            json_data = json.loads(line)
            if json_data.get("issuer_org"):
                if any(org in json_data["issuer_org"][0] for org in org_names):
                    ip_addresses.append(json_data["ip"])
        except json.JSONDecodeError:
            print(f"Error parsing JSON: {line}")
    return ip_addresses

def write_to_csv(filename: str, data: List[str]) -> None:
    """Write data to CSV file."""
    try:
        with open(filename, "w") as f:
            for item in data:
                f.write(f"{item}\n")
    except IOError:
        print(f"Error writing to file {filename}")

def main():
    INPUT_FILE = "pia-out.json"
    
    # Read JSON data
    data = read_json_file(INPUT_FILE)
    
    # Parse IP addresses for different organizations
    pia_ips = parse_ip_addresses(data, ["Private Internet Access"])
    cyberghost_ips = parse_ip_addresses(data, ["CyberGhost"])
    
    # Write results to CSV files
    write_to_csv("pia_ips_temp.csv", pia_ips)
    write_to_csv("cyberghost_ips_temp.csv", cyberghost_ips)

if __name__ == "__main__":
    main()
