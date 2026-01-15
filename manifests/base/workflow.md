
Points importants du workflow
Phase : Intégration Continue

Le développeur pousse du code qui déclenche le pipeline CI
L'image Docker est buildée et poussée vers Harbor
Le pipeline met à jour automatiquement le tag dans le dépôt GitOps

Phase : GitOps avec ArgoCD

ArgoCD surveille le dépôt GitOps (branche main)
Kustomize fusionne la base avec les patches de l'overlay dev
Les manifestes finaux sont générés

Phase : Déploiement

ArgoCD applique les manifestes au cluster Kubernetes
Les pods téléchargent l'image depuis Harbor
L'application exécute les lookups DNS selon la config

Phase : Auto-guérison

Si quelqu'un modifie manuellement le cluster (kubectl edit)
ArgoCD détecte la dérive et restaure l'état depuis Git
C'est le principe selfHeal: true

Le workflow garantit que Git est la source de vérité unique et que le cluster reste toujours synchronisé avec la configuration versionnée.
