# PIA and CyberGhost IP Repository


## Overview

This project automatically scans for PIA VPN servers every hour. It identifies active PIA VPN endpoints across the internet.


## Data Files

- **pia_ips.csv**: Main database of discovered PIA IPs with timestamps
- **new_pia_ips.csv**: Newly discovered IPs from recent scans


### Data Format

| Column | Description |
|--------|-------------|
| IP Address | Server IP |
| First Seen | Initial discovery date |
| Last Seen | Most recent verification date |


## Contributing

Feel free to submit issues and pull requests for improvements.

## Updates

The IP database is automatically updated every hour. Check commit history for the latest changes.
