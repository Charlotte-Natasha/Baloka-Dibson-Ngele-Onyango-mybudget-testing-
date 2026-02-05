# Budget Personnel

Application en ligne de commande pour la gestion du budget personnel. Suivi des dépenses, gestion des budgets et surveillance des dépenses avec une interface CLI intuitive.

## Fonctionnalités

- 💰 **Gestion des Budgets** - Créer et gérer les budgets personnels
- 📊 **Suivi des Transactions** - Enregistrer et catégoriser les dépenses
- 📈 **État du Budget** - Voir l'état des dépenses et les pourcentages de consommation
- ⚠️ **Alertes Budget** - Être averti lors de l'approche des limites budgétaires
- 📋 **Export CSV** - Exporter les transactions en CSV pour analyse
- 🧪 **Tests Complets** - Tests unitaires et d'intégration avec fonctionnalités BDD

## Structure du Projet

```
budgetapp/
├── cli/              # Interface en ligne de commande
├── services/         # Couche de logique métier
├── storage/          # Persistance des données
├── utils/            # Utilitaires (dates, validateurs)
└── __init__.py

tests/
├── unit/             # Tests unitaires
└── integrations/     # Tests d'intégration

docs/
├── architecture.md   # Documentation architecture
└── bdd/              # Fichiers fonctionnalités BDD
```

## Architecture

L'application suit une **architecture en couches** :

- **Couche CLI** (`cli/`) - Gère l'interaction utilisateur via des commandes en ligne de commande
- **Couche Service** (`services/`) - Contient toute la logique métier (calculs budgétaires, pourcentages, alertes)
- **Couche Stockage** (`storage/`) - Gère la persistance des données et les opérations de base de données

Cette séparation assure que la logique métier est découplée de l'accès aux données, facilitant les tests et la maintenance du code.

## Installation

### Prérequis

- Python 3.x
- pip

### Configuration

1. Cloner ou télécharger le référentiel
2. Installer les dépendances :

```bash
pip install -r requirements.txt
```

## Utilisation

### Commandes Disponibles

#### Ajouter un Budget

```bash
python -m budgetapp.cli.app add-budget --name "Épicerie" --amount 500
```

#### Enregistrer une Transaction

```bash
python -m budgetapp.cli.app add-transaction --budget-id 1 --amount 50.00 --description "Courses hebdomadaires"
```

#### Afficher l'État du Budget

```bash
python -m budgetapp.cli.app budget-status --budget-id 1
```

## Dépendances

- **click** - Framework interface en ligne de commande
- **pytest** - Framework de test

Voir [requirements.txt] pour la liste complète.

## Tests

### Exécuter Tous les Tests

```bash
pytest
```

### Exécuter les Tests Unitaires

```bash
pytest tests/unit/
```

### Exécuter les Tests d'Intégration

```bash
pytest tests/integrations/
```

### Exécuter les Tests avec Couverture

```bash
pytest --cov=budgetapp
```

## Fonctionnalités en Développement

Les fonctionnalités suivantes sont définies au format BDD :

- **Alerte Budget** - Alertes de limite budgétaire
- **Modifier Transaction** - Modifier les transactions existantes
- **Export CSV** - Exporter les données budgétaires au format CSV

Voir [docs/bdd/] pour les spécifications des fonctionnalités.

## Configuration

Les paramètres de configuration se trouvent dans [budgetapp/config.py].

## Documentation

- [Architecture] - Architecture système détaillée
- [Fonctionnalités BDD] - Spécifications des fonctionnalités

## Contribution

Lors de la contribution à ce projet :

1. Écrire des tests pour les nouvelles fonctionnalités
2. S'assurer que tous les tests réussissent
3. Suivre la structure et le style du code existant
4. Mettre à jour la documentation si nécessaire

