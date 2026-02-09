#!/bin/bash
# Script complet de préparation du dépôt CFD Solar Panel Dust

# 1️⃣ Créer les dossiers
mkdir -p figures
mkdir -p results/postProcessing
mkdir -p docs

# 2️⃣ Déplacer les figures PNG dans figures/
if ls *.png 1> /dev/null 2>&1; then
    mv *.png figures/
    echo "Figures déplacées dans le dossier figures/"
else
    echo "Aucune figure PNG trouvée."
fi

# 3️⃣ Copier le log dans results/
if [ -f log ]; then
    cp log results/
    echo "Log copié dans results/"
else
    echo "Fichier log introuvable."
fi

# 4️⃣ Créer README.md
cat > README.md << 'EOF'
# Simulation CFD: Dépôt de Poussière sur Panneaux Solaires

## Description
Simulation RANS (k-epsilon) de l'écoulement d'air autour d'un panneau solaire photovoltaïque pour étudier le dépôt de poussière.

## Logiciels
- OpenFOAM 2312
- ParaView pour visualisation
- Python 3 + matplotlib pour post-traitement

## Structure
- `0/` : Conditions initiales et aux limites
- `constant/` : Propriétés physiques et maillage
- `system/` : Paramètres de simulation
- `figures/` : Résultats visualisés
- `results/` : Logs et données numériques
- `docs/` : Documentation complémentaire

## Exécution
```bash
blockMesh
simpleFoam
python3 post_traitement.py

EOF

