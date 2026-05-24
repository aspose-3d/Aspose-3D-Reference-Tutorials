---
date: 2026-05-24
description: Apprenez à créer une extrusion 3D avec des slices en utilisant Aspose.3D
  for Java. Ce guide étape par étape couvre linear extrusion, set rounding radius
  et exporting OBJ.
keywords:
- create 3d extrusion java
- Aspose 3D slices
- linear extrusion Java
linktitle: Créer une extrusion 3D avec des slices – Aspose.3D for Java
schemas:
- author: Aspose
  dateModified: '2026-05-24'
  description: Learn how to create 3d extrusion with slices using Aspose.3D for Java.
    This step‑by‑step guide covers linear extrusion, set rounding radius, and exporting
    OBJ.
  headline: Create 3D Extrusion with Slices – Aspose.3D for Java
  type: TechArticle
- description: Learn how to create 3d extrusion with slices using Aspose.3D for Java.
    This step‑by‑step guide covers linear extrusion, set rounding radius, and exporting
    OBJ.
  name: Create 3D Extrusion with Slices – Aspose.3D for Java
  steps:
  - name: Set up the scene and define the profile
    text: '`RectangleShape` is a class that defines a 2‑D rectangle profile. First
      we create a `RectangleShape` and give it a **rounding radius** so the corners
      are smooth. `Scene` is the root container for all nodes and geometry. Then we
      initialise a new `Scene` that will hold all geometry.'
  - name: Create child node objects for each extrusion
    text: '`Node` represents an element in the scene graph that can hold geometry
      and transformations. Every piece of geometry lives under a `Node`. Here we generate
      two sibling nodes – one for a low‑slice extrusion and another for a high‑slice
      extrusion – and move the left node a little to the side so the res'
  - name: Perform linear extrusion and set slices
    text: '`LinearExtrusion` is the class that creates a solid by sweeping a profile
      linearly. `LinearExtrusion` is Aspose.3D''s class that generates a solid by
      extruding a 2‑D profile along a straight line. Using an **anonymous inner class**
      we call `setSlices` to control the smoothness. The left node gets onl'
  - name: Export OBJ – save the scene
    text: Finally we write the scene to a Wavefront OBJ file, a format widely supported
      by 3‑D editors and game engines. This demonstrates the **export OBJ Java** capability
      of Aspose.3D.
  type: HowTo
- questions:
  - answer: You can download the library [here](https://releases.aspose.com/3d/java/).
    question: How can I download Aspose.3D for Java?
  - answer: Refer to the documentation [here](https://reference.aspose.com/3d/java/).
    question: Where can I find the documentation for Aspose.3D?
  - answer: Yes, you can explore a free trial [here](https://releases.aspose.com/).
    question: Is there a free trial available?
  - answer: Visit the support forum [here](https://forum.aspose.com/c/3d/18).
    question: How can I get support for Aspose.3D?
  - answer: Yes, a temporary license can be obtained [here](https://purchase.aspose.com/temporary-license/).
    question: Can I purchase a temporary license?
  type: FAQPage
second_title: Aspose.3D Java API
title: Créer une extrusion 3D avec des slices – Aspose.3D for Java
url: /fr/java/linear-extrusion/specifying-slices/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Créer une extrusion 3D avec des tranches – Aspose.3D for Java

## Introduction

Si vous devez **créer une extrusion 3d** d'objets qui semblent lisses et précis, contrôler le nombre de tranches est essentiel. Dans ce tutoriel, nous expliquerons comment spécifier les tranches lors d'une extrusion linéaire avec Aspose.3D for Java. Vous verrez pourquoi le nombre de tranches est important, comment définir un rayon d'arrondi, et comment exporter le résultat sous forme de fichier OBJ pouvant être utilisé dans n'importe quel pipeline 3‑D.

## Réponses rapides
- **Que contrôle « slices » ?** Le nombre de sections transversales intermédiaires utilisées pour approximer la surface de l'extrusion.  
- **Quelle méthode définit le nombre de tranches ?** `LinearExtrusion.setSlices(int)`  
- **Puis-je modifier le rayon d’arrondi du profil ?** Oui, via `RectangleShape.setRoundingRadius(double)`  
- **Quel format de fichier est utilisé dans cet exemple ?** Wavefront OBJ (`FileFormat.WAVEFRONTOBJ`)  
- **Ai-je besoin d’une licence pour exécuter le code ?** Un essai gratuit suffit pour l'évaluation ; une licence commerciale est requise pour la production.

`LinearExtrusion.setSlices(int)` définit le nombre de tranches intermédiaires que l'extrusion générera.  
`RectangleShape.setRoundingRadius(double)` définit le rayon des coins d'un profil rectangulaire.

## Comment créer une extrusion 3d Java avec des tranches ?

Chargez votre profil 2‑D, choisissez un nombre de tranches, définissez le rayon d’arrondi, et appelez `save` – l’ensemble du flux de travail tient en quelques lignes. Aspose.3D for Java gère la création de la géométrie, l’interpolation des tranches et l’exportation OBJ automatiquement, vous permettant de vous concentrer sur la qualité visuelle plutôt que sur les calculs de maillage de bas niveau.

## Qu’est‑ce qu’une extrusion linéaire avec des tranches ?

Une extrusion linéaire avec des tranches transforme une forme 2‑D plane en un solide 3‑D en la balayant le long d’une ligne droite tout en générant un nombre configurable de sections transversales intermédiaires. Le nombre de tranches influence directement la fluidité des arêtes courbées, comme les coins arrondis, lors du rendu.

## Pourquoi utiliser Aspose.3D pour Java pour créer une extrusion 3d ?

Aspose.3D offre **un contrôle programmatique complet** sur chaque paramètre d'extrusion, prend en charge **plus de 50 formats d'entrée et de sortie** (y compris OBJ, FBX, STL et GLTF), et peut traiter **des modèles de plusieurs centaines de pages** sans charger le fichier complet en mémoire. Il fonctionne sur toute plateforme compatible Java, ne nécessite aucune DLL native, et garantit des résultats déterministes sous Windows, Linux et macOS.

## Prérequis

1. **Java Development Kit** – JDK 8 ou supérieur installé.  
2. **Aspose.3D for Java** – Téléchargez la bibliothèque depuis le site officiel [ici](https://releases.aspose.com/3d/java/).  
3. Un IDE ou éditeur de texte de votre choix.

## Importer les packages

Ajoutez l’espace de noms Aspose.3D à votre projet afin de pouvoir accéder aux classes de modélisation 3‑D.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## Guide étape par étape

### Étape 1 : Configurer la scène et définir le profil

`RectangleShape` est une classe qui définit un profil de rectangle 2‑D.  
Tout d'abord, nous créons un `RectangleShape` et lui attribuons un **rayon d’arrondi** afin que les coins soient lisses.  
`Scene` est le conteneur racine pour tous les nœuds et la géométrie.  
Ensuite, nous initialisons une nouvelle `Scene` qui contiendra toute la géométrie.

```java
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
Scene scene = new Scene();
```

### Étape 2 : Créer des objets nœuds enfants pour chaque extrusion

`Node` représente un élément du graphe de scène pouvant contenir de la géométrie et des transformations.  
Chaque morceau de géométrie vit sous un `Node`. Ici, nous générons deux nœuds frères — un pour une extrusion à faible nombre de tranches et un autre pour une extrusion à nombre élevé de tranches — et déplaçons légèrement le nœud de gauche sur le côté afin que les résultats soient faciles à comparer.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### Étape 3 : Effectuer l'extrusion linéaire et définir les tranches

`LinearExtrusion` est la classe qui crée un solide en balayant un profil linéairement.  
`LinearExtrusion` est la classe d’Aspose.3D qui génère un solide en extrudant un profil 2‑D le long d’une ligne droite. En utilisant une **classe interne anonyme**, nous appelons `setSlices` pour contrôler la fluidité. Le nœud de gauche reçoit seulement 2 tranches (grossières), tandis que le nœud de droite reçoit 10 tranches (lisses).

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(2);}});
right.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(10);}});
```

### Étape 4 : Exporter OBJ – enregistrer la scène

Enfin, nous écrivons la scène dans un fichier Wavefront OBJ, un format largement supporté par les éditeurs 3‑D et les moteurs de jeu. Cela démontre la capacité **export OBJ Java** d’Aspose.3D.

```java
scene.save(MyDir + "SlicesInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Problèmes courants et solutions

| Problème | Pourquoi cela se produit | Solution |
|----------|--------------------------|----------|
| **L'extrusion apparaît plate** | Le nombre de tranches est fixé à 1 ou 0 | Assurez‑vous que `setSlices` est appelé avec une valeur ≥ 2. |
| **Les coins arrondis semblent dentelés** | Le rayon d’arrondi est trop petit par rapport au nombre de tranches | Augmentez soit le rayon, soit le nombre de tranches pour des courbes plus lisses. |
| **Fichier introuvable lors de l'enregistrement** | `MyDir` pointe vers un dossier inexistant | Créez le répertoire au préalable ou utilisez un chemin absolu. |

## Questions fréquemment posées

**Q : Comment puis‑je télécharger Aspose.3D pour Java ?**  
R : Vous pouvez télécharger la bibliothèque [ici](https://releases.aspose.com/3d/java/).

**Q : Où puis‑je trouver la documentation d’Aspose.3D ?**  
R : Consultez la documentation [ici](https://reference.aspose.com/3d/java/).

**Q : Une version d’essai gratuite est‑elle disponible ?**  
R : Oui, vous pouvez explorer une version d’essai gratuite [ici](https://releases.aspose.com/).

**Q : Comment puis‑je obtenir du support pour Aspose.3D ?**  
R : Visitez le forum de support [ici](https://forum.aspose.com/c/3d/18).

**Q : Puis‑je acheter une licence temporaire ?**  
R : Oui, une licence temporaire peut être obtenue [ici](https://purchase.aspose.com/temporary-license/).

---

**Dernière mise à jour :** 2026-05-24  
**Testé avec :** Aspose.3D for Java 24.11 (le plus récent au moment de la rédaction)  
**Auteur :** Aspose

## Tutoriels associés

- [Créer une extrusion 3D Java avec Aspose.3D](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [Comment définir la direction dans l'extrusion linéaire avec Aspose.3D for Java](/3d/java/linear-extrusion/setting-direction/)
- [Créer une scène 3D avec torsion dans l'extrusion linéaire – Aspose.3D for Java](/3d/java/linear-extrusion/applying-twist/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}