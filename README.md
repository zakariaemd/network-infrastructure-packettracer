# 🖧 Infrastructure Réseau — Packet Tracer 2023

> **Stack :** Cisco Packet Tracer · TCP/IP · VLAN · DHCP · NAT · Routing  
> **Type :** Network Engineering · Infrastructure Design · Security

---

## 🎯 Objectif

Concevoir et valider un parc informatique complet sur Cisco Packet Tracer :
adressage IP, segmentation VLAN, routage inter-VLAN, DHCP centralisé et NAT.

---

## 🏗️ Architecture

| Couche       | Équipement   | Technologie         |
|--------------|--------------|---------------------|
| WAN          | R1 (Cisco 2911) | NAT/PAT, routage statique |
| Distribution | SW-CORE (3560) | Inter-VLAN routing (SVI) |
| Accès        | SW1/SW2/SW3 (2960) | VLANs, port security |
| Branche      | R2 + SW4     | Routage statique    |

---

## 📊 Plan d'Adressage

| VLAN | Réseau           | Hôtes | Usage     |
|------|------------------|-------|-----------|
| 10   | 192.168.10.0/24  | 50    | Admin     |
| 20   | 192.168.20.0/24  | 100   | Dev       |
| 30   | 192.168.30.0/24  | 30    | RH        |
| 40   | 192.168.40.0/24  | 20    | Direction |

---

## ✅ Tests Validés

- ✅ Connectivité inter-VLAN (ping 100%)
- ✅ DHCP fonctionnel sur 4 VLANs
- ✅ NAT/PAT vers Internet
- ✅ Isolation VLAN Direction (ACL)
- ✅ Port Security sur switches d'accès

---

## 🚀 Visualiser le diagramme

```bash
pip install plotly kaleido
python diagrams/topology_diagram.py
```
