---
date: 2026-04-08
description: Apprenez à créer un cylindre avec un sommet décalé dans Aspose.3D pour
  Java, ajoutez un nœud enfant Java, définissez le décalage du sommet, générez le
  modèle 3D et exportez‑le au format OBJ à l’aide d’une licence temporaire Aspose.
keywords:
- aspose temporary license
- generate 3d model
- add child node java
- java export obj
- set offset top
linktitle: Licence temporaire Aspose – Créer un cylindre avec un haut décalé (Java)
second_title: Aspose.3D Java API
title: Licence temporaire Aspose – Créer un cylindre avec un sommet décalé (Java)
url: /fr/java/cylinders/creating-cylinders-with-offset-top/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Licence temporaire Aspose – Créer un cylindre avec un sommet décalé (Java)

## Introduction

Si vous cherchez à **create cylinder** des objets avec un sommet décalé personnalisé dans une scène 3D basée sur Java, Aspose.3D rend le processus simple. Dans ce tutoriel, nous parcourrons chaque étape — de la configuration de la scène à l’exportation du modèle final au format OBJ — afin que vous puissiez intégrer des cylindres à sommet décalé dans vos applications en toute confiance. À la fin du guide, vous comprendrez également comment une **aspose temporary license** vous permet d’évaluer ces fonctionnalités sans achat complet.

## Quick Answers
- **Quelle bibliothèque est utilisée ?** Aspose.3D for Java  
- **Puis-je décaler le sommet d’un cylindre ?** Oui, en utilisant `setOffsetTop`  
- **Comment ajouter un nœud enfant en Java ?** Appelez `createChildNode` sur le nœud racine  
- **Quel format puis‑je exporter ?** Wavefront OBJ (`java export obj`)  
- **Ai‑je besoin d’une licence pour les tests ?** Une **aspose temporary license** est disponible pour l’évaluation  

## Qu’est‑ce qu’une licence temporaire Aspose ?

Une **aspose temporary license** est une clé d’évaluation gratuite et de courte durée qui débloque l’ensemble complet des fonctionnalités d’Aspose.3D for Java pendant le développement et les tests. Elle supprime les filigranes d’évaluation et vous permet de générer des fichiers de modèles 3D, tels que OBJ, STL ou FBX, exactement comme le ferait une licence payante.

## Pourquoi utiliser Aspose.3D pour Java ?

- **API de haut niveau :** Pas besoin de gérer les données de maillage de bas niveau.  
- **Multi‑plateforme :** Fonctionne sur tout environnement compatible JVM.  
- **Exportateurs intégrés :** Enregistrez directement en OBJ, STL, FBX, et plus.  
- **Extensible :** Ajoutez facilement des nœuds enfants, appliquez des transformations et intégrez d’autres bibliothèques Java.  

## Prerequisites

- **Java Development Kit (JDK)** – une version compatible installée.  
- **Bibliothèque Aspose.3D for Java** – téléchargez le dernier JAR depuis le site officiel [ici](https://releases.aspose.com/3d/java/).  
- Un IDE de votre choix (Eclipse, IntelliJ IDEA, NetBeans, etc.).  

## Import Packages

Tout d’abord, importez les classes dont nous aurons besoin. Placez ces instructions en haut de votre fichier Java :

```java
import com.aspose.threed.Cylinder;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Vector3;


import java.io.IOException;
```

## Step‑by‑Step Guide

### Étape 1 : Créer une scène Java 3D

Une **java 3d scene** sert de conteneur pour tous les objets 3D.

```java
// ExStart:1
// Create a scene
Scene scene = new Scene();
// ExEnd:1
```

### Étape 2 : Initialiser un cylindre avec un sommet décalé

Ici nous répondons à **how to create cylinder** avec un décalage personnalisé. Le constructeur définit le rayon, la hauteur, les tranches, les piles, et si le cylindre est fermé. Ensuite, nous décalons le sommet à l’aide de `setOffsetTop`.

```java
// ExStart:2
// Initialize cylinder
Cylinder cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
// Set OffsetTop
cylinder1.setOffsetTop(new Vector3(5, 3, 0));
// ExEnd:2
```

### Étape 3 : Ajouter un nœud enfant Java – Attacher le premier cylindre

Nous créons un nœud enfant sous le nœud racine de la scène et déplaçons le cylindre à l’emplacement souhaité.

```java
// ExStart:3
// Create ChildNode
scene.getRootNode().createChildNode(cylinder1).getTransform().setTranslation(10, 0, 0);
// ExEnd:3
```

### Étape 4 : Initialiser un deuxième cylindre (sans décalage)

À titre de comparaison, nous ajoutons un cylindre standard sans décalage.

```java
// ExStart:4
// Initialize second cylinder without customized OffsetTop
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// ExEnd:4
```

### Étape 5 : Ajouter un nœud enfant Java – Attacher le deuxième cylindre

```java
// ExStart:5
// Create ChildNode
scene.getRootNode().createChildNode(cylinder2);
// ExEnd:5
```

### Étape 6 : Exporter en OBJ Java – Enregistrer la scène au format OBJ

Enfin, nous **java export obj** toute la scène (les deux cylindres) en tant que fichier Wavefront OBJ, largement pris en charge par les outils 3D.

```java
// ExStart:6
// Save
scene.save("Your Document Directory" + "CustomizedOffsetTopCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

Lorsque vous exécutez le programme, vous trouverez `CustomizedOffsetTopCylinder.obj` dans le répertoire spécifié, prêt à être ouvert dans Blender, Maya ou tout autre visualiseur compatible OBJ.

## Comment générer un modèle 3D et l’exporter en OBJ en Java

La combinaison de `Scene.save(..., FileFormat.WAVEFRONTOBJ)` et de la **aspose temporary license** vous permet de **generate 3d model** rapidement, sans avoir besoin de convertisseurs externes. Cela est particulièrement pratique lors du prototypage ou du partage d’actifs avec des designers.

## Cas d’utilisation réels

- **Visualisation architecturale :** Les cylindres à sommet décalé modélisent des colonnes qui s’effilent vers le plafond.  
- **Pièces mécaniques :** Créez des pistons ou des carters d’engrenages où la surface supérieure est intentionnellement décalée.  
- **Actifs de jeu :** Produisez des formes de piliers variées à la volée, réduisant le besoin de maillages faits à la main.  

## Problèmes courants et solutions

| Problème | Raison | Solution |
|----------|--------|----------|
| **Le fichier OBJ est vide** | Scène non enregistrée correctement ou chemin incorrect. | Vérifiez que le répertoire de sortie existe et que vous avez les permissions d’écriture. |
| **Décalage non appliqué** | Utilisation d’une version plus ancienne d’Aspose.3D. | Mettez à jour vers la dernière bibliothèque où `setOffsetTop` est pris en charge. |
| **Nœud enfant non visible** | Transformation non appliquée. | Assurez‑vous d’appeler `getTransform().setTranslation` après la création du nœud enfant. |

## Questions fréquemment posées

**Q : Aspose.3D est‑il compatible avec différents IDE Java ?**  
R : Oui, il fonctionne parfaitement avec Eclipse, IntelliJ IDEA, NetBeans et d’autres IDE.

**Q : Puis‑je appliquer des textures aux objets 3D créés ?**  
R : Absolument ! Utilisez la classe `Material` pour assigner des textures et des propriétés de surface.

**Q : Existe‑t‑il des options de licence pour Aspose.3D ?**  
R : Divers modèles de licence sont disponibles ; vous pouvez les explorer [ici](https://purchase.aspose.com/buy).

**Q : Comment puis‑je obtenir de l’aide ou partager des expériences ?**  
R : Rejoignez le forum communautaire Aspose.3D [ici](https://forum.aspose.com/c/3d/18) pour le support et les discussions.

**Q : Une licence temporaire est‑elle disponible pour les tests ?**  
R : Oui, une **aspose temporary license** peut être obtenue pour l’évaluation [ici](https://purchase.aspose.com/temporary-license/).

---

**Dernière mise à jour :** 2026-04-08  
**Testé avec :** Aspose.3D for Java 24.12 (latest)  
**Auteur :** Aspose

---

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}