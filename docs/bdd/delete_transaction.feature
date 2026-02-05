Fonctionnalité: Supprimer une transaction
  En tant qu'utilisateur
  Je veux supprimer une transaction
  Afin que mes totaux budgétaires soient mis à jour correctement

  Scénario: Supprimer une transaction de dépense
    Soit un budget "Alimentation" pour "2025-01" d'un montant de 300
    Et les transactions suivantes existent:
      | montant | catégorie | date       | type    |
      | 50      | Alimentation | 2025-01-05 | dépense |
      | 20      | Alimentation | 2025-01-10 | dépense |
    Quand je supprime la transaction de montant 50 le "2025-01-05"
    Alors le total dépensé pour "Alimentation" en "2025-01" devrait être 20
    Et le budget restant devrait être 280
