---
date: 2026-06-13
description: Apprenez un tutoriel de graphisme 3D Java sur le contrôle du centre dans
  l'extrusion linéaire avec Aspose.3D, y compris comment définir le rayon d'arrondi
  et enregistrer le fichier OBJ Java.
keywords:
- create 3d mesh java
- set rounding radius
- export 3d model obj
- save obj file java
- aspose 3d export obj
linktitle: Contrôle du centre dans l'extrusion linéaire avec Aspose.3D pour Java
schemas:
- author: Aspose
  dateModified: '2026-06-13'
  description: Learn a java 3d graphics tutorial on controlling the center in linear
    extrusion with Aspose.3D, including how to set rounding radius and save OBJ file
    java.
  headline: Create 3D Mesh Java – Center in Linear Extrusion
  type: TechArticle
- description: Learn a java 3d graphics tutorial on controlling the center in linear
    extrusion with Aspose.3D, including how to set rounding radius and save OBJ file
    java.
  name: Create 3D Mesh Java – Center in Linear Extrusion
  steps:
  - name: Set Up the Base Profile
    text: First, create the 2‑D shape that will be extruded. Here we use a rectangle
      and **set rounding radius** to 0.3, which smooths the corners and demonstrates
      how to **round extrusion corners**.
  - name: Create a 3D Scene
    text: '**Scene** is the top‑level container that holds all 3‑D objects, lights,
      and cameras.'
  - name: Add Left and Right Nodes
    text: A **Node** represents a transformable object in the scene graph, allowing
      positioning and hierarchy.
  - name: Linear Extrusion – No Center (Left Node)
    text: '**LinearExtrusion** converts a 2‑D profile into a 3‑D mesh by sweeping
      it along a straight line. **setCenter(boolean)** toggles whether the extrusion
      is centered around the profile origin.'
  - name: Add a Ground Plane for Reference (Left Node)
    text: A thin box acts as a visual floor, helping you see the extrusion’s orientation.
  - name: Linear Extrusion – Centered (Right Node)
    text: Now repeat the extrusion, this time enabling `center`. The geometry will
      be symmetric around the profile’s origin, giving you a perfectly balanced **create
      3d mesh java** result.
  - name: Add a Ground Plane for Reference (Right Node)
    text: Same ground plane for the right side, making the comparison clear.
  - name: Save the 3D Scene
    text: Finally, export the entire scene to a Wavefront OBJ file – a format readily
      usable in most 3‑D editors. The `save` method automatically converts the mesh
      to the OBJ specification, allowing you to **save obj file java** without additional
      post‑processing.
  type: HowTo
- questions:
  - answer: It determines whether the extrusion is symmetric around the profile's
      origin.
    question: What does the center property do?
  - answer: A temporary license works for testing; a full license is required for
      production.
    question: Do I need a license to run the code?
  - answer: The scene is saved as a Wavefront OBJ file.
    question: Which file format is used for the result?
  - answer: Yes, use `setSlices(int)` on the `LinearExtrusion` object.
    question: Can I change the number of slices?
  - answer: Absolutely – it supports all modern Java versions.
    question: Is Aspose.3D compatible with Java 8+?
  type: FAQPage
second_title: Aspose.3D Java API
title: Créer un maillage 3D Java – Centre dans l'extrusion linéaire
url: /fr/java/linear-extrusion/controlling-center/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Créer un maillage 3D Java – Centre dans l'extrusion linéaire

## Introduction

Si vous créez des visualisations 3D en Java, maîtriser les techniques d'extrusion est essentiel. Ce **java 3d graphics tutorial** vous montre comment **create 3d mesh java** des objets en contrôlant le centre d'une extrusion linéaire avec Aspose.3D for Java. À la fin de ce guide, vous comprendrez pourquoi la propriété `center` est importante, comment **set rounding radius**, et comment **save obj file java**‑compatible. Vous verrez également comment **export 3d model obj** pour une utilisation dans n'importe quel éditeur 3D majeur.

## Réponses rapides

- **Que fait la propriété center ?** Elle détermine si l'extrusion est symétrique par rapport à l'origine du profil.  
- **Ai‑je besoin d'une licence pour exécuter le code ?** Une licence temporaire fonctionne pour les tests ; une licence complète est requise pour la production.  
- **Quel format de fichier est utilisé pour le résultat ?** La scène est enregistrée au format Wavefront OBJ.  
- **Puis‑je changer le nombre de tranches ?** Oui, utilisez `setSlices(int)` sur l'objet `LinearExtrusion`.  
- **Aspose.3D est‑il compatible avec Java 8+ ?** Absolument – il prend en charge toutes les versions modernes de Java.  

## Qu'est‑ce qu'un java 3d graphics tutorial ?

Un **java 3d graphics tutorial** est un guide étape par étape qui vous apprend à utiliser les bibliothèques Java pour créer, manipuler et rendre des objets tridimensionnels. Dans ce tutoriel, vous apprendrez à **create 3d mesh java** en convertissant un profil 2D en un modèle 3D complet, à contrôler son alignement central, à arrondir les coins de l'extrusion, et enfin à exporter le résultat sous forme de fichier OBJ lisible par n'importe quel programme 3D.

## Pourquoi utiliser Aspose.3D pour Java ?

Aspose.3D for Java fournit une API de haut niveau qui élimine le besoin de calculs manuels de maillage, vous permettant de vous concentrer sur la conception plutôt que sur la géométrie de bas niveau. Il prend en charge **50+ input and output formats** — y compris OBJ, FBX, STL et GLTF — vous permettant de **export 3d model obj** ou tout autre format avec un appel de méthode unique. La bibliothèque traite des scènes de plusieurs centaines de pages sans charger le fichier complet en mémoire, offrant **up to 3× faster performance** comparé aux pipelines OpenGL bruts sur du matériel serveur typique.

## Prérequis

Avant de commencer, assurez‑vous d'avoir :

1. **Java Development Environment** – JDK 8 ou version plus récente installée.  
2. **Aspose.3D for Java** – Téléchargez la bibliothèque et la documentation [here](https://reference.aspose.com/3d/java/).  
3. **Document Directory** – Créez un dossier sur votre machine pour stocker les fichiers générés ; nous l'appellerons **« Your Document Directory ».**

## Importer les packages

Dans votre IDE Java, importez les classes Aspose.3D dont vous avez besoin. Cela donne au compilateur l'accès aux fonctionnalités d'extrusion et de construction de scène.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Guide étape par étape

### Étape 1 : Configurer le profil de base

Tout d'abord, créez la forme 2D qui sera extrudée. Ici, nous utilisons un rectangle et **set rounding radius** à 0,3, ce qui adoucit les coins et montre comment **round extrusion corners**.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

### Étape 2 : Créer une scène 3D

**Scene** est le conteneur de niveau supérieur qui contient tous les objets 3D, les lumières et les caméras.

```java
Scene scene = new Scene();
```

### Étape 3 : Ajouter les nœuds gauche et droit

Un **Node** représente un objet transformable dans le graphe de scène, permettant le positionnement et la hiérarchie.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### Étape 4 : Extrusion linéaire – Sans centre (nœud gauche)

**LinearExtrusion** convertit un profil 2D en un maillage 3D en le balayant le long d'une ligne droite.  
**setCenter(boolean)** bascule si l'extrusion est centrée autour de l'origine du profil.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

### Étape 5 : Ajouter un plan de sol de référence (nœud gauche)

Une boîte fine sert de sol visuel, vous aidant à voir l'orientation de l'extrusion.

```java
left.createChildNode(new Box(0.01, 3, 3));
```

### Étape 6 : Extrusion linéaire – Centrée (nœud droit)

Répétez maintenant l'extrusion, cette fois en activant `center`. La géométrie sera symétrique autour de l'origine du profil, vous offrant un résultat **create 3d mesh java** parfaitement équilibré.

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

### Étape 7 : Ajouter un plan de sol de référence (nœud droit)

Même plan de sol pour le côté droit, rendant la comparaison claire.

```java
right.createChildNode(new Box(0.01, 3, 3));
```

### Étape 8 : Enregistrer la scène 3D

Enfin, exportez la scène complète vers un fichier Wavefront OBJ – un format facilement utilisable dans la plupart des éditeurs 3D. La méthode `save` convertit automatiquement le maillage selon la spécification OBJ, vous permettant de **save obj file java** sans post‑traitement supplémentaire.

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Problèmes courants et solutions

| Problème | Pourquoi cela se produit | Solution |
|----------|--------------------------|----------|
| **L'extrusion apparaît décalée** | `setCenter(false)` laisse le profil ancré à son coin. | Utilisez `setCenter(true)` pour des résultats symétriques. |
| **Le fichier OBJ est vide** | Le chemin du répertoire de sortie est incorrect ou les permissions d'écriture sont manquantes. | Vérifiez que `MyDir` pointe vers un dossier existant et que l'application a les droits d'écriture. |
| **Les coins arrondis semblent nets** | Le rayon d'arrondissement est trop petit par rapport à la taille du rectangle. | Augmentez la valeur du rayon (par ex., `setRoundingRadius(0.5)`). |

## Questions fréquentes

### Q1 : Puis-je utiliser Aspose.3D pour Java dans des projets commerciaux ?

R1 : Oui, Aspose.3D for Java est disponible pour une utilisation commerciale. Pour les détails de licence, consultez [here](https://purchase.aspose.com/buy).

### Q2 : Une version d'essai gratuite est‑elle disponible ?

R2 : Oui, vous pouvez explorer une version d'essai gratuite d'Aspose.3D pour Java [here](https://releases.aspose.com/).

### Q3 : Où puis‑je trouver du support pour Aspose.3D pour Java ?

R3 : Le forum communautaire d'Aspose.3D est un excellent endroit pour obtenir du support et partager vos expériences. Visitez le forum [here](https://forum.aspose.com/c/3d/18).

### Q4 : Ai‑je besoin d'une licence temporaire pour les tests ?

R4 : Oui, si vous avez besoin d'une licence temporaire à des fins de test, vous pouvez en obtenir une [here](https://purchase.aspose.com/temporary-license/).

### Q5 : Où puis‑je trouver la documentation ?

R5 : La documentation d'Aspose.3D pour Java est disponible [here](https://reference.aspose.com/3d/java/).

## Conclusion

En terminant ce **java 3d graphics tutorial**, vous savez maintenant comment **create 3d mesh java** des objets, contrôler le centre d'une extrusion linéaire, ajuster le rayon d'arrondissement, et **save obj file java** en sortie en utilisant Aspose.3D. Ces techniques vous offrent un contrôle précis de la symétrie du maillage, ce qui est essentiel pour les actifs de jeux, les prototypes CAO et les visualisations scientifiques. N'hésitez pas à expérimenter avec différents profils, nombres de tranches et formats d'exportation pour élargir votre boîte à outils 3D.

---

**Dernière mise à jour :** 2026-06-13  
**Testé avec :** Aspose.3D for Java 24.11  
**Auteur :** Aspose

## Tutoriels associés

- [Créer une extrusion 3D Java avec Aspose.3D](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [Comment définir la direction dans l'extrusion linéaire avec Aspose.3D pour Java](/3d/java/linear-extrusion/setting-direction/)
- [Créer une scène 3D avec torsion dans l'extrusion linéaire – Aspose.3D pour Java](/3d/java/linear-extrusion/applying-twist/)

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}