---
date: 2026-08-12
description: Comment générer du 3D avec Aspose.3D – créer un cylindre avec un sommet
  décalé en Java, ajouter un nœud enfant, définir le sommet décalé, générer le modèle
  3D, exporter en OBJ et évaluer avec une temporary license.
keywords:
- how to generate 3d
- aspose temporary license
- export obj file
- set offset top
- java 3d cylinder
lastmod: 2026-08-12
linktitle: Comment générer du 3D – créer un cylindre avec un sommet décalé (Java)
og_description: Comment générer du 3D avec Aspose.3D pour Java. Apprenez à décaler
  les sommets des cylindres, ajouter des nœuds enfants et exporter en OBJ en utilisant
  une temporary license.
og_image_alt: Guide showing Java code to create a cylinder with offset top and export
  OBJ using Aspose.3D
og_title: Comment générer du 3D – créer un cylindre avec un sommet décalé (Java)
schemas:
- author: Aspose
  dateModified: '2026-08-12'
  description: How to generate 3d using Aspose.3D – create a cylinder with offset
    top in Java, add child node, set offset top, generate 3D model, export OBJ, and
    evaluate with a temporary license.
  headline: How to generate 3d – create cylinder with offset top (Java)
  type: TechArticle
- description: How to generate 3d using Aspose.3D – create a cylinder with offset
    top in Java, add child node, set offset top, generate 3D model, export OBJ, and
    evaluate with a temporary license.
  name: How to generate 3d – create cylinder with offset top (Java)
  steps:
  - name: Create a Java 3D scene
    text: '`Scene` is the top‑level container that holds all nodes, meshes, lights,
      and cameras in a 3‑D environment.'
  - name: Initialize cylinder with offset top
    text: '`Cylinder` represents a cylindrical mesh and provides properties such as
      radius, height, and offset.'
  - name: Add child node Java – attach the first cylinder
    text: '`Node` is an element in the scene graph that can hold geometry and transformations.'
  - name: Java export OBJ – save the scene as OBJ
    text: '`FileFormat` enumerates the supported export formats such as OBJ, STL,
      and FBX.'
  type: HowTo
- questions:
  - answer: Yes, it works seamlessly with Eclipse, IntelliJ IDEA, NetBeans, and other
      IDEs.
    question: Is Aspose.3D compatible with different Java IDEs?
  - answer: Absolutely! Use the `Material` class to assign textures and surface properties.
    question: Can I apply textures to the created 3D objects?
  - answer: Various licensing models are available; you can explore them **[Aspose
      purchase page](https://purchase.aspose.com/buy)**.
    question: Are there licensing options for Aspose.3D?
  - answer: Join the **[Aspose.3D community forum](https://forum.aspose.com/c/3d/18)**
      for support and discussion.
    question: How can I get help or share experiences?
  - answer: Yes, an **aspose temporary license** can be obtained for evaluation **[temporary
      license request page](https://purchase.aspose.com/temporary-license/)**.
    question: Is a temporary license available for testing?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- generate 3d
- aspose.3d
- java cylinder offset
title: Comment générer du 3D – créer un cylindre avec un sommet décalé (Java)
url: /fr/java/cylinders/creating-cylinders-with-offset-top/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Comment générer du 3D – créer un cylindre avec un sommet décalé (Java)

## Introduction

Si vous cherchez à **créer un cylindre** avec un sommet décalé personnalisé dans une scène 3D basée sur Java, Aspose.3D rend le processus simple. Dans ce tutoriel, nous parcourrons chaque étape — de la configuration de la scène à l'exportation du modèle final au format OBJ — afin que vous puissiez intégrer des cylindres à sommet décalé dans vos applications en toute confiance. À la fin du guide, vous comprendrez également comment une **aspose temporary license** vous permet d'évaluer ces fonctionnalités sans achat complet.

## Réponses rapides
- **Quelle bibliothèque est utilisée ?** Aspose.3D for Java  
- **Puis-je décaler le sommet d'un cylindre ?** Oui, via `setOffsetTop`  
- **Comment ajouter un nœud enfant en Java ?** Appelez `createChildNode` sur le nœud racine  
- **Quel format puis-je exporter ?** Wavefront OBJ (`export obj file`)  
- **Ai-je besoin d'une licence pour les tests ?** Une **aspose temporary license** est disponible pour l'évaluation  

## Qu'est-ce qu'une licence temporaire Aspose ?

Une **aspose temporary license** est une clé d'évaluation à court terme et gratuite qui débloque l'ensemble des fonctionnalités d'Aspose.3D for Java pendant le développement et les tests. Elle supprime les filigranes d'évaluation et vous permet de générer des fichiers de modèle 3D, tels que OBJ, STL ou FBX, exactement comme le ferait une licence payante.

## Pourquoi utiliser Aspose.3D for Java ?

Aspose.3D fournit une API de haut niveau, multiplateforme, qui simplifie la création et l'exportation 3D. Elle inclut des exportateurs intégrés pour plus de 30 formats, prend en charge les hiérarchies de graphes de scène, et vous permet de vous concentrer sur la géométrie plutôt que sur la gestion de maillage de bas niveau.

- **API de haut niveau :** Pas besoin de gérer les données de maillage de bas niveau.  
- **Multiplateforme :** Fonctionne sur tout environnement compatible JVM.  
- **Exportateurs intégrés :** Enregistrez directement en OBJ, STL, FBX, et plus — Aspose.3D prend en charge **30+** formats d'exportation.  
- **Extensible :** Ajoutez facilement des nœuds enfants, appliquez des transformations et intégrez d'autres bibliothèques Java.  

## Prérequis

Avant de commencer, assurez‑vous d'avoir :

- **Java Development Kit (JDK)** – une version compatible installée.  
- **Bibliothèque Aspose.3D for Java** – téléchargez le dernier JAR depuis le site officiel **[Aspose.3D for Java download page](https://releases.aspose.com/3d/java/)**.  
- Un IDE de votre choix (Eclipse, IntelliJ IDEA, NetBeans, etc.).  

## Import packages

Les importations suivantes apportent les classes essentielles d'Aspose.3D nécessaires pour créer et exporter un cylindre.

```java
import com.aspose.threed.Cylinder;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Vector3;


import java.io.IOException;
```

## Guide étape par étape

### Étape 1 : Créer une scène 3D Java

`Scene` est le conteneur de niveau supérieur qui contient tous les nœuds, maillages, lumières et caméras dans un environnement 3D.

```java
// ExStart:1
// Create a scene
Scene scene = new Scene();
// ExEnd:1
```

### Étape 2 : Initialiser le cylindre avec un sommet décalé

`Cylinder` représente un maillage cylindrique et fournit des propriétés telles que le rayon, la hauteur et le décalage.

```java
// ExStart:2
// Initialize cylinder
Cylinder cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
// Set OffsetTop
cylinder1.setOffsetTop(new Vector3(5, 3, 0));
// ExEnd:2
```

### Étape 3 : Ajouter un nœud enfant Java – attacher le premier cylindre

`Node` est un élément du graphe de scène qui peut contenir de la géométrie et des transformations.

```java
// ExStart:3
// Create ChildNode
scene.getRootNode().createChildNode(cylinder1).getTransform().setTranslation(10, 0, 0);
// ExEnd:3
```

### Étape 4 : Initialiser un deuxième cylindre (sans décalage)

```java
// ExStart:4
// Initialize second cylinder without customized OffsetTop
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// ExEnd:4
```

### Étape 5 : Ajouter un nœud enfant Java – attacher le deuxième cylindre

```java
// ExStart:5
// Create ChildNode
scene.getRootNode().createChildNode(cylinder2);
// ExEnd:5
```

### Étape 6 : Exporter OBJ en Java – enregistrer la scène au format OBJ

`FileFormat` énumère les formats d'exportation pris en charge tels que OBJ, STL et FBX.

```java
// ExStart:6
// Save
scene.save("Your Document Directory" + "CustomizedOffsetTopCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

## Comment générer un modèle 3D et exporter OBJ en Java

Pour générer un modèle 3D, chargez la scène, appliquez les transformations nécessaires, puis appelez `scene.save("path/CustomizedOffsetTopCylinder.obj", FileFormat.WAVEFRONTOBJ)`. La **aspose temporary license** supprime le filigrane d'évaluation, vous permettant de produire des fichiers OBJ prêts pour la production sans acheter de licence complète.

## Cas d'utilisation réels

- **Visualisation architecturale :** Les cylindres à sommet décalé modélisent des colonnes qui s'effilent vers le plafond.  
- **Pièces mécaniques :** Créez des pistons ou des carters d'engrenages où la surface supérieure est intentionnellement décalée.  
- **Assets de jeu :** Produisez des formes de piliers variées à la volée, réduisant le besoin de maillages faits à la main.  

## Problèmes courants et solutions

| Problème | Raison | Solution |
|----------|--------|----------|
| **Le fichier OBJ est vide** | Scène non enregistrée correctement ou chemin incorrect. | Vérifiez que le répertoire de sortie existe et que vous avez les permissions d'écriture. |
| **Le décalage n'est pas appliqué** | Utilisation d'une version plus ancienne d'Aspose.3D. | Mettez à jour vers la dernière bibliothèque où `setOffsetTop` est pris en charge. |
| **Le nœud enfant n'est pas visible** | Transformation non appliquée. | Assurez‑vous d'appeler `getTransform().setTranslation` après la création du nœud enfant. |

## Questions fréquemment posées

**Q : Aspose.3D est‑il compatible avec différents IDE Java ?**  
R : Oui, il fonctionne parfaitement avec Eclipse, IntelliJ IDEA, NetBeans et d'autres IDE.

**Q : Puis‑je appliquer des textures aux objets 3D créés ?**  
R : Absolument ! Utilisez la classe `Material` pour assigner des textures et des propriétés de surface.

**Q : Existe‑t‑il des options de licence pour Aspose.3D ?**  
R : Divers modèles de licence sont disponibles ; vous pouvez les explorer sur la **[Aspose purchase page](https://purchase.aspose.com/buy)**.

**Q : Comment puis‑je obtenir de l'aide ou partager des expériences ?**  
R : Rejoignez le **[Aspose.3D community forum](https://forum.aspose.com/c/3d/18)** pour le support et les discussions.

**Q : Une licence temporaire est‑elle disponible pour les tests ?**  
R : Oui, une **aspose temporary license** peut être obtenue pour l'évaluation sur la **[temporary license request page](https://purchase.aspose.com/temporary-license/)**.

**Dernière mise à jour :** 2026-08-12  
**Testé avec :** Aspose.3D for Java 24.12 (latest)  
**Auteur :** Aspose

---

{{< blocks/products/products-backtop-button >}}

## Tutoriels associés

- [Comment créer des modèles de cylindre avec Aspose.3D for Java](/3d/java/cylinders/)
- [Comment créer une forme d'éventail de cylindre avec Aspose.3D for Java](/3d/java/cylinders/creating-fan-cylinders/)
- [Créer des nœuds enfants et exporter FBX en Java avec Aspose.3D](/3d/java/geometry/build-node-hierarchies/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}