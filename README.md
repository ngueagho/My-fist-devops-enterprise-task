# Projet : Infrastructure de monitoring et CI/CD complète pour une stack microservices
Contexte
Tu vas créer l'infrastructure complète pour une entreprise fictive qui a 3 microservices (API Gateway, Service User, Service Order) avec une base de données, et qui veut une solution de monitoring, logging, et CI/CD robuste.
Architecture cible

# Applications : 3 microservices en containers (tu peux utiliser des apps simples Node.js/Python/Go)
Orchestration : Kubernetes local (minikube ou k3s)
CI/CD : GitLab CE auto-hébergé avec runners
Monitoring : Stack Prometheus + Grafana + AlertManager
Logging : ELK Stack (Elasticsearch + Logstash + Kibana)
Sécurité : Vault pour les secrets, scanning de vulnérabilités
Infrastructure as Code : Terraform + Ansible
Service Mesh : Istio pour la communication inter-services

Livrables attendus
# Phase 1 (Jour 1-2) : Infrastructure de base

Code Terraform pour provisionner les VMs locales (ou conteneurs simulant des VMs)
Playbooks Ansible pour l'installation et configuration de Kubernetes
Déploiement des 3 microservices avec leurs bases de données
Configuration du réseau et des politiques de sécurité Kubernetes

# Phase 2 (Jour 3-4) : CI/CD Pipeline

Installation et configuration de GitLab CE
Création de 3 repositories pour les microservices
Pipelines GitLab CI avec :

Tests unitaires et d'intégration
Build et push des images Docker
Scan de sécurité des images (Trivy ou Clair)
Déploiement automatique sur Kubernetes
Tests de smoke après déploiement


Gestion des environnements (dev/staging/prod) avec promotion manuelle

# Phase 3 (Jour 5-6) : Monitoring et Observabilité

Déploiement de la stack Prometheus/Grafana
Configuration des métriques custom dans les applications
Dashboards Grafana pour chaque service + vue globale
Alertes intelligentes (latence, erreurs, ressources)
Stack ELK pour la centralisation des logs
Tracing distribué avec Jaeger

# Phase 4 (Jour 7) : Sécurité et Service Mesh

Installation et configuration de Vault
Migration des secrets vers Vault
Déploiement d'Istio
Configuration du traffic management
Mise en place de politiques de sécurité (mTLS, RBAC)

Défis techniques spécifiques

Zero-downtime deployments avec rolling updates et health checks
Backup automatisé des données et configuration avec rotation
Disaster recovery : script de restauration complète en cas de panne
Auto-scaling : HPA sur les pods + monitoring des métriques custom
Multi-environment : même infrastructure déployable en dev/staging/prod
Documentation : playbook d'incident et runbooks

Contraintes "entreprise" à respecter

Tout doit être versionné et reproductible
Logs centralisés avec rétention de 30 jours
Alertes par email/Slack simulé
Respect des standards de sécurité (pas de secrets en dur)
Interface web pour les développeurs (GitLab + Grafana + Kibana)
