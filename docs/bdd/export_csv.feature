Fonctionnalité: Exporter les transactions

  En tant qu'utilisateur, je veux exporter mes transactions afin de conserver un enregistrement en dehors de l'application.

  Scénario: Exporter toutes les transactions vers un fichier CSV

    Soit les transactions suivantes existent:

      | montant | description | catégorie | type    | date        |
      | 50      | Courses     | Alimentation| dépense | 2025-01-10  |
      | 20      | Ticket bus  | Transport | dépense | 2025-01-12  |

    Quand l'utilisateur exporte toutes les transactions vers un fichier CSV alors un fichier CSV devrait être généré et le fichier CSV devrait contenir les lignes suivantes:
    
      | montant | description | catégorie | type    | date        |
      | 50      | Courses     | Alimentation| dépense | 2025-01-10  |
      | 20      | Ticket bus  | Transport | dépense | 2025-01-12  |