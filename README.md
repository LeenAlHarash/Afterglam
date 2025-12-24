# Afterglam 💄💫

Afterglam est un serveur entièrement gratuit, pour recycler du maquillage expiré, qui permet aux clients de faire un don de leurs cosmétiques périmer pour les maisons de funérailles.
Les clients pourront soumettre des demandes de don, sur Afterglam, afin que les maisons de funérailles puissent récupérer les produits cosmétiques dont ceux-ci n’ont plus besoin. Cela permet d’éviter le gaspillage des cosmétiques non utilisés ou non terminés. 
Ainsi, les maisons funérailles n'ont pas non plus à dépenser de l'argent pour de nouveaux produits.

## Développement

Dans ce projet, nous développerons une base de données qui permet de récupérer, modifier ou supprimer des données. Pour cela, nous créerons le script de la création de la base de données ainsi que les tables et les données à insérer. Cette base de données sera créée et connectée sur le serveur Idéfix. De plus, nous déploierons cette base de données sur l’application Docker Desktop dans son propre conteneur. Lorsque le client fera une demande de don, l’application Afterglam envoie la requête à l’API (la couche contrôleurs), après au côté serveur dans la couche service et enfin, à la base de données. Pour retourner le résultat, la base de données envoie du code SQL à la couche service, ensuite à l’API, dont celui-ci interprètera le résultat sous JSON et affichera cela sur l’interface. Donc, nous devrons créer l’interface, la couche métier qui contient la couche service et l’accès aux données, qui est le côté serveur et la base de données.

## Authors

- Leen Al Harash
- Mariyam Hanfaoui 

---

# Explications de nos utilisateurs : Admin & Client

- **Les administrateurs ont la capacité de :**
    - Voir les informations des clients.
	- Voir les informations des admins.
	- Créer des cosmétiques
	- Voir les formulaires et ceux qui sont pris en charge par d'autres administrateurs.
	- Chercher des maisons funérailles, des clients, des formulaires et des cosmétiques par leurs ID.

- **Les clients ont la possibilité de :**
	- Créer un formulaire et le remplir avec leurs informations.
	- Voir les maisons Funérailles.
	- Trouver leurs formulaires en utilisant leurs courriels.
    - Voir la liste des cosmétiques.


# Des liens utiles

- [Simulateur Postman](https://mhanfaoui-9664884.postman.co/workspace/Afterglam's-Workspace~79ec3285-8dec-46d7-8ae7-1e95d3addfcd/collection/48024513-cdafdac3-6e39-4c2d-9596-3f8723a3294c?action=share&creator=48496166)
- [Idefix](http://idefix.dti.crosemont.quebec:10154/)


# Déploiement et tests
Pour plus d’informations sur la façon de déployer le serveur, veuillez vous référer au document "*Documentation_afterglam.docx*"
