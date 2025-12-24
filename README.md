# Afterglam 💄💫
---
Afterglam est un serveur entièrement gratuit, pour recycler du maquillage expiré, qui permet aux clients de faire un don de leurs cosmétiques périmer pour les maisons de funérailles.
Les clients pourront soumettre des demandes de don, sur Afterglam, afin que les maisons de funérailles puissent récupérer les produits cosmétiques dont ceux-ci n’ont plus besoin. Cela permet d’éviter le gaspillage des cosmétiques non utilisés ou non terminés. 
Ainsi, les maisons funérailles n'ont pas non plus à dépenser de l'argent pour de nouveaux produits.

## Développement
---
Dans ce projet, nous développerons une base de données qui permet de récupérer, modifier ou supprimer des données. Pour cela, nous créerons le script de la création de la base de données ainsi que les tables et les données à insérer. Cette base de données sera créée et connectée sur le serveur Idéfix. De plus, nous déploierons cette base de données sur l’application Docker Desktop dans son propre conteneur. Lorsque le client fera une demande de don, l’application Afterglam envoie la requête à l’API (la couche contrôleurs), après au côté serveur dans la couche service et enfin, à la base de données. Pour retourner le résultat, la base de données envoie du code SQL à la couche service, ensuite à l’API, dont celui-ci interprètera le résultat sous JSON et affichera cela sur l’interface. Donc, nous devrons créer l’interface, la couche métier qui contient la couche service et l’accès aux données, qui est le côté serveur et la base de données.

## Authors
---
- Leen Al Harash
- Mariyam Hanfaoui 
---
---

# Diagrammes avec PlantUML
---
1. Diagramme entité-relation
![Diagram entité-relation](https://git.dti.crosemont.quebec/lal/afterglam/-/raw/main/Diagrammes/png/diagramme_entit%C3%A9-relation.png?ref_type=heads)
<br><br>

2. Diagramme model-relationnel
![Diagram model-relationnel](https://git.dti.crosemont.quebec/-/plantuml/png/~1U9oLazrgma0GXU_dAQPNjiNu02AY2A6bj1IHteQjZhYuEsjt9mKnldjfOarI0qakvsU_cSmvcGLHNb9hu4vsP0aFHcc6iDTyK5vPD9f9ZWT2vsNd08X5on4NHXCBdW3n4VKcMHVn69_VLZYPlBzCfu0OHO38pk8OF-RBnTDy2UShOhwncak2oiC-WDXvMxxV_aPDpvlsYujwm-1gnIeT7CSfarVQ6AetbOky_kyxjHAwVD_21KkYlz8AS5tc-g0yRJs5NI9kJnokk4P642Lfg6C6k5AVXWAg4DnQAz7V5F3Uar6Y7GVaqOWVgi8ahGuPOjnHvAJ5AZr8XLIT1Ef1xQnK2tE0ox-BmkL-MHP5xfIF0IZkK4lbFy7PvPboZKe-osxy2GtmYruDCuhh0zoulDfJ504gbwZ1AvlL1jID2JFYJMhD3vVOPPy0)
<br><br>

3. Diagramme séquence-systeme
![Diagram séquence-systeme](https://git.dti.crosemont.quebec/-/plantuml/png/~1U9n5ZyrEmp0GXEz-Yhcr72BkELIj2aWz09N22rZn1XdPky8_aQgAT-7OF8TV3BbfodLdlfcTRKmwfEoTMk79wi-WlISOGYpJToRk2V4KKxbuKYjqVPbO1ojeiNUME85u54l8N2clsLnf8wnkXcQ3tV605iVtxWEFWmIFin7cCb7yKLLhDdYfvnRxKAOQ1fOyaiweTdKLctjGb_k-NEA2xeotZ1PlaknWAS3f6NVk_wTr3NfGi_UUz4ef1KBvnPVa04U8IQUSwWId5tWfkWrgySoZdEQYNdYmmUjaXTMMs6Jl_W0iEdKP)
<br><br>

4. Diagramme classes du modèle
![Diagram classes du modèle](https://git.dti.crosemont.quebec/lal/afterglam/-/raw/main/Diagrammes/png/diagramme_classes_du_modele.png?ref_type=heads)
<br><br>

5. Diagramme composants de l'architecture
![Diagram composants de l'architecture](https://git.dti.crosemont.quebec/lal/afterglam/-/raw/main/Diagrammes/png/composant_de_l'architecture.png)
---
---

# Explications de nos utilisateurs : Admin & Client
---
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


### Récits et Critères de chaque Utilisateur
- Admin: https://git.dti.crosemont.quebec/lal/afterglam/-/work_items/13 , https://git.dti.crosemont.quebec/lal/afterglam/-/work_items/14
- Client: https://git.dti.crosemont.quebec/lal/afterglam/-/work_items/9 , https://git.dti.crosemont.quebec/lal/afterglam/-/work_items/10

### Un persona pour chaque Utilisateur
- Persona Admin: https://git.dti.crosemont.quebec/lal/afterglam/-/work_items/12
- Persona Client: https://git.dti.crosemont.quebec/lal/afterglam/-/work_items/8
---
---

# Des liens utiles
---
- [Simulateur Postman](https://mhanfaoui-9664884.postman.co/workspace/Afterglam's-Workspace~79ec3285-8dec-46d7-8ae7-1e95d3addfcd/collection/48024513-cdafdac3-6e39-4c2d-9596-3f8723a3294c?action=share&creator=48496166)
- [Idefix](http://idefix.dti.crosemont.quebec:10154/)
---
---

# Déploiement et tests
Pour plus d’informations sur la façon de déployer le serveur, veuillez vous référer au document "*Documentation_afterglam.docx*"