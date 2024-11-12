import os
import zipfile
import tempfile
import re
from urllib.request import urlopen, Request
from io import BytesIO

class PIAServerList:
    def __init__(self):
        self.servers = set()
        self.temp_dir = tempfile.mkdtemp()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

    def download_and_extract(self):
        try:
            request = Request('https://www.privateinternetaccess.com/openvpn/openvpn.zip', headers=self.headers)
            print("Downloading OVPN configurations...")
            with urlopen(request) as response:
                zip_data = BytesIO(response.read())
            print("Extracting files...")
            with zipfile.ZipFile(zip_data) as zip_ref:
                zip_ref.extractall(self.temp_dir)
            return True
        except Exception as e:
            print(f"Error downloading/extracting files: {str(e)}")
            return False

    def parse_ovpn_files(self):
        pattern = re.compile(r'remote\s+([a-zA-Z0-9\-\.]+)\s+\d+')
        try:
            for filename in os.listdir(self.temp_dir):
                if filename.endswith('.ovpn'):
                    self._parse_file(os.path.join(self.temp_dir, filename), pattern)
            return True
        except Exception as e:
            print(f"Error parsing OVPN files: {str(e)}")
            return False

    def _parse_file(self, filepath, pattern):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            matches = pattern.findall(content)
            if matches:
                self.servers.update(matches)

    def cleanup(self):
        try:
            for filename in os.listdir(self.temp_dir):
                filepath = os.path.join(self.temp_dir, filename)
                if os.path.isfile(filepath):
                    os.unlink(filepath)
            os.rmdir(self.temp_dir)
        except Exception as e:
            print(f"Error cleaning up: {str(e)}")

    def save_servers(self, filename="pia_servers.txt"):
        try:
            with open(filename, 'w') as f:
                for server in sorted(self.servers):
                    f.write(f"{server}\n")
            print(f"\nServer list saved to {filename}")
            return True
        except Exception as e:
            print(f"Error saving server list: {str(e)}")
            return False


def main():
    pia = PIAServerList()
    try:
        if pia.download_and_extract() and pia.parse_ovpn_files():
            
            pia.save_servers()
    finally:
        pia.cleanup()

if __name__ == "__main__":
    main()
