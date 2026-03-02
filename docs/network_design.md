# 🏗️ Network Design Document

## Topologie Générale

```
                    [INTERNET]
                        │
                   [Routeur R1]
                  /            \
           [SW-CORE]          [R2-Branch]
          /    |    \               |
       [SW1] [SW2] [SW3]         [SW4]
        |      |     |              |
      VLAN10 VLAN20 VLAN30        VLAN40
      Admin  Dev    RH           Direction
```

## Segmentation par VLAN

| VLAN | Nom        | Réseau           | Passerelle      | Nb Hôtes |
|------|------------|------------------|-----------------|----------|
| 10   | Admin      | 192.168.10.0/24  | 192.168.10.1    | 50       |
| 20   | Dev        | 192.168.20.0/24  | 192.168.20.1    | 100      |
| 30   | RH         | 192.168.30.0/24  | 192.168.30.1    | 30       |
| 40   | Direction  | 192.168.40.0/24  | 192.168.40.1    | 20       |
| 99   | Management | 192.168.99.0/24  | 192.168.99.1    | Infra    |

## Équipements

| Équipement | Modèle (PT)       | Rôle                     |
|------------|-------------------|--------------------------|
| R1         | Cisco 2911        | Routeur principal / NAT  |
| R2         | Cisco 2911        | Routeur secondaire       |
| SW-CORE    | Cisco 3560        | Switch Layer 3 (routing) |
| SW1-SW3    | Cisco 2960        | Switches d'accès         |
| SW4        | Cisco 2960        | Switch branche           |
