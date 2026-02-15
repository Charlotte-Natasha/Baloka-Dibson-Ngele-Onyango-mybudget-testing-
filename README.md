# Budget Personnel

Application en ligne de commande pour la gestion du budget personnel.  
Suivi des dépenses, gestion des budgets et analyse des consommations via une interface CLI simple et efficace.

---

##  Fonctionnalités

- 💰 **Gestion des Budgets** — création, consultation et suppression  
- 📊 **Suivi des Transactions** — enregistrement et catégorisation des dépenses  
- 📈 **État du Budget** — calcul du total dépensé, restant, pourcentage consommé  
- ⚠️ **Alertes Budget** — avertissements lorsque les limites sont proches  
- 📋 **Export CSV** — export des transactions  
- 🧪 **Tests Complets** — tests unitaires, intégration et scénarios BDD  

---

## 📁 Structure du Projet

```
budgetapp/
├── cli/              # Interface en ligne de commande
├── services/         # Logique métier
├── storage/          # Accès aux données (SQLite)
├── utils/            # Outils (dates, validateurs)
└── __init__.py

tests/
├── unit/             # Tests unitaires
└── integrations/     # Tests d'intégration

docs/
├── architecture.md
└── bdd/
```

---

## 🏗️ Architecture

L’application suit une architecture en couches :

- **CLI** — interaction utilisateur  
- **Services** — logique métier (calculs, règles)  
- **Storage** — persistance SQLite  

Cette séparation facilite les tests, la maintenance et l’évolution du projet.

---

## 🚀 Installation

### Prérequis
- Python 3.10+  
- pip  

### Installation

```bash
git clone <votre-repo>
cd budgetapp
pip install -r requirements.txt
```

### Initialisation de la base de données

```bash
python -m budgetapp.cli.app init-db
```

ou automatiquement lors de la première commande.

---

## 🧑‍💻 Utilisation

### Créer un budget

```bash
python -m budgetapp.cli.app budget create --category "Food" --period "2025-01" --amount 300
```

### Ajouter une transaction

```bash
python -m budgetapp.cli.app transaction add --category "Food" --amount 45 --date "2025-01-10"
```

### Voir l’état du budget

```bash
python -m budgetapp.cli.app budget status --category "Food" --period "2025-01"
```

---

## 🧪 Tests

### Lancer tous les tests

```bash
pytest
```

### Tests avec couverture

```bash
pytest --cov=budgetapp --cov-report=term-missing
```

Couverture actuelle : **89%**

---

## 🧩 Scénarios BDD

Exemple :

```
Feature: Suivi du budget
  Scenario: Voir l'état d'un budget existant
    Given un budget "Food" pour "2025-01" de 300€
    And une dépense de 50€ dans "Food"
    When je consulte l'état du budget
    Then le total dépensé doit être 50€
    And le montant restant doit être 250€
```

Tous les scénarios sont disponibles dans `docs/bdd/`.

---

## 🌿 Branches Git

- `main` — version stable  
- `feature-xxx` — une branche par fonctionnalité  
- Commits fréquents et descriptifs  

---

## ⚙️ Configuration

Variable d’environnement :

```
BUDGET_DB_PATH=/chemin/vers/budget.db
```

---

## 🎥 Vidéo Démonstration

Durée : 3–5 minutes  
Lien : [https://drive.google.com/file/d/1vmNx-_JqzhY6uNejzR2syIGkTCUZOKhK/view?usp=sharing](https://drive.google.com/file/d/1vmNx-_JqzhY6uNejzR2syIGkTCUZOKhK/view?usp=sharing)

---

## 🤝 Contribution

1. Créer une branche `feature-nom`  
2. Ajouter des tests  
3. Vérifier que tous les tests passent  
4. Mettre à jour la documentation  


