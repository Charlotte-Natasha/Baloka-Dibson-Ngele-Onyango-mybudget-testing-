Fonctionnalité: Modifier une transaction

  En tant qu'utilisateur, je veux modifier une transaction existante afin de corriger les erreurs de montant ou de catégorie.

  Scénario: L'utilisateur modifie le montant d'une transaction existante

    Soit une transaction existante avec:
      | id | montant | catégorie  | type    | date        |
      | 1  | 50      | Transport  | dépense | 2025-01-10  |

    Et un budget de 200€ existe pour la catégorie "Transport" pour la période "2025-01". 

    Quand l'utilisateur met à jour la transaction avec l'id 1 pour avoir un montant de 30€, alors le montant de la transaction devrait être mis à jour à 30€
    et le total dépensé pour "Transport" en "2025-01" devrait être 30€. 