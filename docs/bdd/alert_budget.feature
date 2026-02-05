Fonctionnalité: Alerte de dépassement budgétaire
  En tant qu'utilisateur,
  Je veux être alerté lorsque mes dépenses dépassent un budget,
  Afin que je puisse mieux contrôler mes dépenses.

  Scénario: Une alerte est déclenchée lorsque les dépenses dépassent le budget
    Soit un budget de 300€ existe pour la catégorie "Alimentation" pour la période "2025-01"
    Et les dépenses suivantes existent pour "Alimentation" en "2025-01":
      | montant | description |
      | 200     | Courses     |
      | 90      | Snacks      |
    Quand une nouvelle dépense de 20€ est ajoutée pour "Alimentation" le "2025-01-20"
    Alors le total dépensé devrait être 310€
    Et le budget restant devrait être -10€
    Et le pourcentage de consommation devrait être 103%
    Et un message d'alerte devrait s'afficher