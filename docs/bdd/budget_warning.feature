Fonctionnalité: Avertissement budgétaire à 80%
  En tant qu'utilisateur
  Je veux recevoir un avertissement lorsque 80% de mon budget est consommé
  Afin que je puisse éviter de dépenser trop

  Scénario: Les dépenses atteignent 80% du budget
    Soit un budget "Divertissement" pour "2025-01" d'un montant de 200
    Et les transactions suivantes existent:
      | montant | catégorie      | date       | type    |
      | 50      | Divertissement | 2025-01-05 | dépense |
      | 110     | Divertissement | 2025-01-10 | dépense |
    Quand je vérifie l'état du budget
    Alors le total dépensé devrait être 160
    Et le budget restant devrait être 40
    Et un avertissement devrait être émis indiquant 80% consommé
