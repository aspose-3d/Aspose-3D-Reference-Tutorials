---
date: 2026-10-03
description: Apprenez comment **sélectionner des objets par nom** en utilisant des
  requêtes de type XPath dans Aspose.3D pour Java et créer une scène 3D programmatiquement.
keywords:
- select objects by name
- how to query scene
- Aspose.3D Java
lastmod: 2026-10-03
linktitle: Sélectionner des objets par nom dans une scène Java 3D – requêtes de type
  XPath avec Aspose.3D
og_description: Sélectionnez des objets par nom dans une scène Java 3D en utilisant
  les requêtes de type XPath d'Aspose.3D. Ce guide vous montre comment interroger
  le graphe de scène efficacement et récupérer les caméras, lumières ou toute entité
  par nom.
og_image_alt: 'Developer guide: select objects by name in Java 3D scene using Aspose.3D'
og_title: Sélectionner des objets par nom dans une scène Java 3D – guide Aspose.3D
schemas:
- author: Aspose
  dateModified: '2026-10-03'
  description: Learn how to **select objects by name** using XPath‑like queries in
    Aspose.3D for Java and build a 3D scene programmatically.
  headline: Select objects by name in Java 3D scene – XPath‑like queries with Aspose.3D
  type: TechArticle
- description: Learn how to **select objects by name** using XPath‑like queries in
    Aspose.3D for Java and build a 3D scene programmatically.
  name: Select objects by name in Java 3D scene – XPath‑like queries with Aspose.3D
  steps:
  - name: create a scene for testing
    text: We start with an empty scene that will host our hierarchy. `
  - name: build a hierarchy of nodes
    text: Next, we add a few child nodes under the root node. Some nodes contain a
      **Camera** or a **Light** entity, which we'll later query. `
  - name: query objects by traversing the scene graph
    text: Now the fun part—iterating through the scene to **select objects by name**
      or type using the `NodeVisitor` pattern. `NodeVisitor` is a built‑in Aspose.3D
      class that walks the scene graph node‑by‑node, calling your callback for each
      visited node. It lets you inspect each node’s `Entity` and `Name` wi
  type: HowTo
- questions:
  - answer: The documentation is available **[Aspose.3D Java API reference](https://reference.aspose.com/3d/java/)**.
    question: Where can I find the Aspose.3D for Java documentation?
  - answer: You can download it **[Aspose.3D for Java download page](https://releases.aspose.com/3d/java/)**.
    question: How can I download Aspose.3D for Java?
  - answer: Yes, you can get a free trial **[Aspose free trial page](https://releases.aspose.com/)**.
    question: Is there a free trial available?
  - answer: Visit the support forum **[Aspose 3D support forum](https://forum.aspose.com/c/3d/18)**.
    question: Where can I get support for Aspose.3D for Java?
  - answer: Obtain a temporary license **[temporary license request page](https://purchase.aspose.com/temporary-license/)**.
    question: Need a temporary license?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- select objects by name
- Aspose.3D
- Java 3D scene
- XPath queries
- 3D programming
title: Sélectionner des objets par nom dans une scène Java 3D – requêtes de type XPath
  avec Aspose.3D
url: /fr/java/3d-objects-and-scenes/xpath-like-object-queries/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Sélectionner des objets par nom dans une scène Java 3D – requêtes de type XPath avec Aspose.3D

## Introduction  

Si vous devez **create 3d scene java** des applications qui manipulent des hiérarchies complexes d'objets, Aspose.3D for Java vous offre une méthode propre, de style XPath, pour localiser exactement ce dont vous avez besoin. Dans ce tutoriel, nous allons parcourir la création d'une scène simple, ajouter une hiérarchie de nœuds, puis utiliser des requêtes de type XPath pour **select objects by name** (par exemple, des caméras ou des lumières) quel que soit leur emplacement dans l'arbre. À la fin, vous serez à l'aise pour interroger, filtrer et récupérer des entités 3‑D avec une seule expression.

## Réponses rapides
- **Que puis‑je interroger ?** Tout nœud ou entité (Camera, Light, Mesh, etc.) dans une scène.  
- **Comment sélectionner des objets par type ?** Utilisez une expression de type XPath telle que `//*[(@Type='Camera')]`.  
- **Ai‑je besoin d’une licence pour le développement ?** Un essai gratuit suffit pour les tests ; une licence est requise pour la production.  
- **Quelle version de Java est prise en charge ?** Java 8 ou ultérieure.  
- **Où puis‑je télécharger Aspose.3D ?** Depuis la page officielle de téléchargement liée dans les prérequis.

## Qu’est‑ce qu’une requête de type XPath dans Aspose.3D ?

Une requête de type XPath dans Aspose.3D est une expression concise qui filtre les instances **A3DObject** (nœuds, caméras, lumières, maillages, etc.) directement sur le graphe de la scène. **A3DObject représente tout objet du graphe de la scène, tel que des nœuds, des caméras, des lumières ou des maillages.** Elle fonctionne comme XPath XML mais cible le modèle d'objets 3‑D, vous permettant de localiser « toutes les caméras » ou « les objets dont le nom est ‘light’ » sans écrire de code de traversée manuel.

## Pourquoi c’est important

Lorsque vous travaillez avec du contenu 3‑D, parcourir manuellement le graphe de la scène devient rapidement source d’erreurs et difficile à maintenir. Les requêtes de type XPath vous offrent une méthode déclarative et lisible pour localiser exactement les objets dont vous avez besoin, ce qui accélère le développement et réduit les bugs — en particulier dans les grandes scènes contenant des dizaines ou des centaines de nœuds. Aspose.3D prend en charge **plus de 50 formats d’entrée et de sortie** et peut traiter des scènes de plusieurs centaines de pages sans charger le fichier complet en mémoire, vous offrant à la fois flexibilité et performances.

## Comment sélectionner des objets par nom à l’aide de requêtes de type XPath

Chargez les objets par nom avec une seule expression qui correspond à l’attribut `@Name`. Voici trois modèles courants :

1. **Sélectionner toutes les caméras** – `//*[(@Type='Camera')]`  
2. **Sélectionner les nœuds nommés « light »** – `//*[(@Name='light')]`  
3. **Combiner type et nom** – `//*[(@Type='Camera') or (@Name='light')]`

Ces expressions renvoient les entités sous‑jacentes, vous permettant de les manipuler directement en Java.

## Prérequis

Avant de commencer, assurez-vous d'avoir :

- Java Development Kit (JDK) installé sur votre machine.  
- Bibliothèque Aspose.3D for Java téléchargée et configurée. Vous pouvez trouver le lien de téléchargement **[Aspose.3D for Java download page](https://releases.aspose.com/3d/java/)**.  
- Connaissances de base en programmation Java.  

## Importer les packages

Tout d'abord, importez les classes Aspose.3D dont vous avez besoin. Cette étape rend la bibliothèque disponible pour votre projet.

```java
import com.aspose.threed.*;
import com.aspose.threed.scene.*;
import java.util.ArrayList;
import java.util.List;
```

## Guide étape par étape

### Étape 1 : créer une scène pour les tests  

Nous commençons avec une scène vide qui accueillera notre hiérarchie.

````java
// ExStart:CreateScene
Scene scene = new Scene();
// ExEnd:CreateScene
````

### Étape 2 : construire une hiérarchie de nœuds  

Ensuite, nous ajoutons quelques nœuds enfants sous le nœud racine. Certains nœuds contiennent une entité **Camera** ou **Light**, que nous interrogerons plus tard.

````java
// ExStart:CreateHierarchy
Node a = scene.getRootNode().createChildNode("a");
a.createChildNode("a1");
a.createChildNode("a2");
scene.getRootNode().createChildNode("b");
Node c = scene.getRootNode().createChildNode("c");
c.createChildNode("c1").addEntity(new Camera("cam"));
c.createChildNode("c2").addEntity(new Light("light"));
// ExEnd:CreateHierarchy
````

### Étape 3 : interroger les objets en parcourant le graphe de la scène  

Passons maintenant à la partie amusante — parcourir la scène pour **select objects by name** ou le type en utilisant le modèle `NodeVisitor`.

`NodeVisitor` est une classe intégrée d’Aspose.3D qui parcourt le graphe de la scène nœud par nœud, appelant votre fonction de rappel pour chaque nœud visité. Elle vous permet d’inspecter l’`Entity` et le `Name` de chaque nœud sans écrire de boucles récursives.

```
\u0060\u0060\u0060\u0060java
// The scene from Step 1

// Create a list to store the found objects
List<Object> objects = new ArrayList<>();

// Use a NodeVisitor to traverse the scene graph
scene.getRootNode().accept(new NodeVisitor() {
    @Override
    public boolean call(Node node) {
        Entity entity = node.getEntity();
        // Check if the node has a Camera or if the node's name is 'light'
        if (entity instanceof Camera || "light".equals(node.getName())) {
            objects.add(entity);
        }
        return true;
    }
});

// Print the found objects
for (Object obj : objects) {
    System.out.println("Found: " + obj);
}
// ExEnd:XPathLikeObjectQueries
\u0060\u0060\u0060
```

**Explication des expressions clés**

- `//*[(@Type = 'Camera') or (@Name = 'light')]` – Trouve chaque objet dans la scène dont l’attribut **type** vaut `Camera` **ou** dont l’attribut **name** vaut `light`. C’est un exemple classique de **select objects by name** (et par type).  
- `/c/*/<Camera>` – Commence à la racine, va au nœud `c`, puis à n’importe quel enfant (`*`), et enfin sélectionne l’entité `<Camera>`.  
- `a1` – Un raccourci qui recherche dans tout l’arbre un nœud nommé `a1`.  
- `/` – Retourne le nœud racine lui‑-même.

### Pièges courants et conseils  

- **Sensibilité à la casse :** Les noms d’attributs (`@Type`, `@Name`) sont sensibles à la casse.  
- **Entité vs. nœud :** Utilisez la syntaxe `<Camera>` uniquement lorsque vous avez besoin de l’entité sous‑jacente, pas seulement du nœud.  
- **Performance :** Pour les scènes très volumineuses, restreignez le chemin de recherche (par ex., commencez à partir d’un sous‑arbre spécifique) pour améliorer la vitesse.  

## Problèmes courants et solutions  

| Problème | Raison | Solution |
|----------|--------|----------|
| Aucun résultat retourné | Erreur de saisie de la chaîne de requête ou mauvaise casse d’attribut | Vérifiez l’orthographe et la casse de `@Name` ; utilisez les noms de nœuds exacts. |
| Nœuds inattendus inclus | L’utilisation de `//*` parcourt tout l’arbre | Restreignez le chemin, par ex., `/c/*` pour limiter la portée. |
| Performance lente sur de très grandes scènes | La requête s’exécute sur l’ensemble du graphe | Commencez la requête à partir d’un sous‑nœud connu au lieu de la racine. |

## Questions fréquentes  

**Q : Où puis‑je trouver la documentation Aspose.3D pour Java ?**  
A : La documentation est disponible **[Aspose.3D Java API reference](https://reference.aspose.com/3d/java/)**.

**Q : Comment puis‑je télécharger Aspose.3D pour Java ?**  
A : Vous pouvez le télécharger **[Aspose.3D for Java download page](https://releases.aspose.com/3d/java/)**.

**Q : Une version d’essai gratuite est‑elle disponible ?**  
A : Oui, vous pouvez obtenir une version d’essai gratuite **[Aspose free trial page](https://releases.aspose.com/)**.

**Q : Où puis‑je obtenir du support pour Aspose.3D pour Java ?**  
A : Visitez le forum de support **[Aspose 3D support forum](https://forum.aspose.com/c/3d/18)**.

**Q : Besoin d’une licence temporaire ?**  
A : Obtenez une licence temporaire **[temporary license request page](https://purchase.aspose.com/temporary-license/)**.

**Q : Puis‑je interroger des propriétés personnalisées définies par l’utilisateur ?**  
A : Oui, vous pouvez étendre l’expression XPath avec des attributs `@` supplémentaires que vous ajoutez aux nœuds.

**Q : Le moteur de requête fonctionne‑t‑il avec des scènes animées ?**  
A : Absolument — les requêtes opèrent sur la hiérarchie statique ; les animations sont attachées aux mêmes nœuds et sont donc incluses dans les résultats.

## Conclusion  

Vous savez maintenant comment **select objects by name** dans des scènes Java 3D en utilisant des requêtes de type XPath. Cette approche passe des démonstrations simples aux applications 3‑D de niveau production, vous offrant un contrôle fin sur le parcours de la scène sans code verbeux.

---

**Dernière mise à jour :** 2026-10-03  
**Testé avec :** Aspose.3D for Java 24.11  
**Auteur :** Aspose  








```java
import com.aspose.threed.*;

import java.util.ArrayList;
import java.util.List;
```

## Tutoriels associés

- [Comment utiliser XPath pour modifier le rayon d’une sphère en Java avec Aspose.3D](/3d/java/3d-objects-and-scenes/)
- [Lire des scènes 3D en Java avec Aspose.3D](/3d/java/load-and-save/read-existing-3d-scenes/)
- [Appliquer des transformations géométriques à un nœud en utilisant l’API Java d’Aspose.3D](/3d/java/geometry/expose-geometric-transformations/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}