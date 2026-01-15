
manifests/
├── base/                          # Configuration commune
│   ├── kustomization.yaml
│   ├── deployment.yaml            # Deployment générique
│   ├── service.yaml               # Service générique
│   └── configmap.yaml
│
└── overlays/                      # Personnalisations par environnement
    ├── dev/
    │   ├── kustomization.yaml     # Hérite de base + patches dev
    │   └── env-patch.yaml         # Variables d'env pour dev
    │
    ├── staging/
    │   ├── kustomization.yaml
    │   ├── env-patch.yaml
    │   └── replicas-patch.yaml    # 3 réplicas en staging
    │
    └── prod/
        ├── kustomization.yaml
        ├── env-patch.yaml
        ├── replicas-patch.yaml    # 10 réplicas en prod
        ├── resources-patch.yaml   # CPU/RAM plus élevés
        └── ingress.yaml           # Ingress avec certificat TLS
