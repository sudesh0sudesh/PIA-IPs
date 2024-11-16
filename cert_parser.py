import json
import csv
from typing import List, Dict

def read_json_file(filename: str) -> List[Dict]:
    """Read JSON file and return list of JSON objects."""
    try:
        with open(filename) as f:
            return [json.loads(line) for line in f]
    except FileNotFoundError:
        print(f"Error: File {filename} not found")
        return []
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        return []

def parse_ip_addresses(data: List[Dict], org_names: List[str]) -> List[str]:
    """Extract IP addresses for specified organizations."""
    ip_addresses = []
    for json_data in data:
        issuer_org = json_data.get("issuer_org", [])
        if any(org in issuer_org for org in org_names):
            ip_addresses.append(json_data.get("ip", ""))
    return ip_addresses

def write_to_csv(filename: str, data: List[str]) -> None:
    """Write data to CSV file."""
    try:
        with open(filename, "w", newline='') as f:
            writer = csv.writer(f)
            for item in data:
                writer.writerow([item])
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