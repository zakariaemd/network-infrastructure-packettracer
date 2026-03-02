# 📋 Plan d'Adressage IP

## Interfaces Routeurs

| Équipement | Interface    | Adresse IP        | Masque          | Description         |
|------------|-------------|-------------------|-----------------|---------------------|
| R1         | Gi0/0       | 203.0.113.1       | /30             | WAN (vers Internet) |
| R1         | Gi0/1       | 10.0.0.1          | /30             | LAN vers SW-CORE    |
| R1         | Gi0/2       | 10.0.0.5          | /30             | WAN vers R2         |
| R2         | Gi0/0       | 10.0.0.6          | /30             | WAN vers R1         |
| R2         | Gi0/1       | 10.0.0.9          | /30             | LAN vers SW4        |
| SW-CORE    | VLAN 10 SVI | 192.168.10.1      | /24             | Passerelle VLAN 10  |
| SW-CORE    | VLAN 20 SVI | 192.168.20.1      | /24             | Passerelle VLAN 20  |
| SW-CORE    | VLAN 30 SVI | 192.168.30.1      | /24             | Passerelle VLAN 30  |
| SW-CORE    | VLAN 99 SVI | 192.168.99.1      | /24             | Management          |

## Pool DHCP

| VLAN | Pool DHCP              | Exclusions           |
|------|------------------------|----------------------|
| 10   | 192.168.10.10–.200     | .1–.9 (infra)        |
| 20   | 192.168.20.10–.200     | .1–.9 (infra)        |
| 30   | 192.168.30.10–.100     | .1–.9 (infra)        |
| 40   | 192.168.40.10–.50      | .1–.9 (infra)        |
