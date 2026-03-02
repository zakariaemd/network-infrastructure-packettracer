# ✅ Résultats des Tests de Connectivité

## Méthodologie
Tests effectués via **Cisco Packet Tracer** (mode Simulation + PDU)

---

## Tests de Ping Inter-VLAN

| Source          | Destination     | Résultat | Latence |
|-----------------|-----------------|----------|---------|
| PC-Admin (V10)  | PC-Dev (V20)    | ✅ OK    | 1 ms    |
| PC-Admin (V10)  | PC-RH (V30)     | ✅ OK    | 1 ms    |
| PC-Dev (V20)    | PC-Direction (V40) | ✅ OK | 2 ms    |
| PC-Admin (V10)  | R1 Gi0/1        | ✅ OK    | 1 ms    |
| PC-Dev (V20)    | 8.8.8.8 (NAT)   | ✅ OK    | 3 ms    |

## Tests d'Isolation VLAN

| Source         | Destination     | Résultat | Note                    |
|----------------|-----------------|----------|-------------------------|
| PC-RH (V30)    | PC-Admin (V10)  | ✅ Contrôlé | Via ACL SW-CORE    |
| PC-Dev (V20)   | PC-Direction (V40) | ❌ Bloqué | ACL inter-VLAN    |

## Tests DHCP

| VLAN | Client IP Obtenu   | Passerelle       | DNS      | Résultat |
|------|--------------------|------------------|----------|----------|
| 10   | 192.168.10.10      | 192.168.10.1     | 8.8.8.8  | ✅ OK    |
| 20   | 192.168.20.10      | 192.168.20.1     | 8.8.8.8  | ✅ OK    |
| 30   | 192.168.30.10      | 192.168.30.1     | 8.8.8.8  | ✅ OK    |

## Tests NAT/PAT

| Test                        | Résultat |
|-----------------------------|----------|
| PC-Admin → 8.8.8.8          | ✅ OK    |
| PC-Dev → www.google.com     | ✅ OK    |
| Vérification table NAT R1   | ✅ OK    |

## Résultat Global : ✅ 100% des tests passés
