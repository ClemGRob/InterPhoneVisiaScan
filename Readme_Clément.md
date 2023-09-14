Je vais faire appel à la fonction en interne de ces fichiers pour le cas correspondant à la demande, lors-  d'un appuis sur l'interface pour l'interphone.
Dans les fichiers, suivant :
- mangager_call -> il manque les noms des utilisateurs
- manager_reco_facial -> cédric
- manager_search_next
- manager_search_previous
- manager_search_refresh_name

Dans le cas plus exeptionnel : Mode Admin
Il y a 2 fonctions à modifier dans 2 fichiers :
- Fonction "delete" dans ui_win_deletionpage
- Fonction "registre" dans ui_win_registrationpage

Pour l'execution du projet ces : src_main\Show_app_window.py