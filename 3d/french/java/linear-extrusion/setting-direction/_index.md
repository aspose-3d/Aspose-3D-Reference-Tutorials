---
date: 2026-02-22
description: Apprenez à définir la direction dans l'extrusion linéaire et à exporter
  un modèle 3D au format OBJ à l'aide d'Aspose.3D pour Java. Suivez notre guide étape
  par étape.
linktitle: Setting Direction in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Comment définir la direction dans l'extrusion linéaire avec Aspose.3D pour
  Java
url: /fr/java/linear-extrusion/setting-direction/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Comment définir la direction dans une extrusion linéaire avec Aspose.3D pour Java

## Introduction

Dans ce tutoriel complet, vous découvrirez **comment définir la direction** lors d’une extrusion linéaire avec Aspose.3D pour Java. Que vous construisiez un outil de type CAD ou que vous génériez de la géométrie pour un moteur de jeu, contrôler la direction de l’extrusion vous permet de créer exactement la forme dont vous avez besoin. Nous parcourrons chaque étape, de l’initialisation d’un profil à l’enregistrement du résultat sous forme de fichier OBJ, afin que vous puissiez également **exporter des modèles 3d obj** directement depuis Java.

## Quick Answers
- **Quelle est la classe principale pour l'extrusion linéaire ?** `LinearExtrusion`
- **Quelle méthode définit la direction de l'extrusion ?** `setDirection(Vector3 direction)`
- **Puis-je exporter le résultat au format OBJ ?** Oui, en utilisant `scene.save(..., FileFormat.WAVEFRONTOBJ)`
- **Ai-je besoin d'une licence pour le développement ?** Un essai gratuit est disponible ; une licence est requise pour la production.
- **Quel IDE Java est le plus adapté ?** IntelliJ IDEA ou Eclipse sont tous deux entièrement pris en charge.

## What is Linear Extrusion?

L'extrusion linéaire prend un profil 2‑D (tel qu'un rectangle ou un cercle) et l'étend le long d'une ligne droite pour créer un solide 3‑D. Par défaut, l'extrusion suit l'axe Z positif, mais Aspose.3D vous permet de modifier ce chemin avec la propriété `setDirection`.

## Why Set Direction in Linear Extrusion?

Définir une direction personnalisée est utile lorsque :
- Aligner la géométrie avec des objets existants dans une scène.
- Créer des pièces inclinées ou angulaires sans étapes de transformation supplémentaires.
- Exporter des modèles qui doivent correspondre à un système de coordonnées spécifique (par ex., pour l'impression 3‑D ou les moteurs de jeu).

## Prerequisites

Avant de commencer, assurez-vous de disposer de :
- Connaissances de base en Java.
- Bibliothèque Aspose.3D installée. Vous pouvez la télécharger [ici](https://releases.aspose.com/3d/java/).
- Un IDE tel qu'Eclipse ou IntelliJ IDEA.

## Import Packages

Tout d'abord, importez les espaces de noms qui fournissent les classes 3‑D de base et les types utilitaires.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Step 1: Initialize Base Profile

Créez la forme qui sera extrudée. Dans cet exemple, nous utilisons un `RectangleShape` avec un petit rayon d'arrondi pour donner aux arêtes un aspect lisse.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Step 2: Create a Scene

Un objet `Scene` agit comme conteneur pour tous les nœuds 3‑D, lumières, caméras et matériaux.

```java
Scene scene = new Scene();
```

## Step 3: Create Nodes

Ajoutez deux nœuds enfants à la racine de la scène — un pour l'extrusion à gauche et un pour l'extrusion à droite. Le nœud de droite est translaté afin que les deux objets ne se chevauchent pas.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Step 4: Perform Linear Extrusion on the Left Node

Extrudez le profil sur le nœud de gauche en utilisant la direction par défaut de l'axe Z. Nous ajoutons également une torsion complète de 360° et augmentons le nombre de tranches pour un maillage plus lisse.

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## Step 5: Perform Linear Extrusion on the Right Node with Direction

C’est ici que nous **définissons la direction**. En passant un `Vector3` personnalisé à `setDirection`, l'extrusion suit le vecteur (0.3, 0.2, 1), produisant une forme inclinée.

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## Step 6: Save 3D Scene

Enfin, exportez la scène au format Wavefront OBJ. Cette étape montre comment **enregistrer des fichiers obj java** et facilite la visualisation du résultat dans n'importe quel visualiseur 3‑D.

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Common Issues and Solutions

| Problème | Pourquoi cela se produit | Solution |
|----------|--------------------------|----------|
| Le fichier OBJ apparaît vide | Le profil n'a pas été ajouté à un nœud | Assurez-vous que `createChildNode` est appelé sur un nœud valide |
| La direction semble inchangée | `setDirection` a été appelé après que l'extrusion ait déjà été construite | Définissez la direction à l'intérieur de l'initialiseur `LinearExtrusion` comme indiqué |
| Maillage à basse résolution | La valeur de `setSlices` est trop basse | Augmentez le nombre de tranches (par ex., 100 ou plus) |

## Conclusion

Vous savez maintenant **comment définir la direction** dans une extrusion linéaire, comment ajuster les paramètres de torsion et de tranches, et comment **exporter des modèles 3d obj** en utilisant Aspose.3D pour Java. Ces techniques vous offrent un contrôle fin sur la création de géométrie et facilitent l'intégration d'actifs 3‑D dans des pipelines plus larges.

## FAQ's

### Q1 : Puis-je utiliser Aspose.3D avec d'autres langages de programmation ?

A1 : Aspose.3D prend en charge divers langages de programmation, y compris .NET et Java.

### Q2 : Une version d'essai gratuite est‑elle disponible pour Aspose.3D ?

A2 : Oui, vous pouvez explorer les fonctionnalités d'Aspose.3D avec un essai gratuit [ici](https://releases.aspose.com/).

### Q3 : Où puis‑je trouver la documentation détaillée d'Aspose.3D pour Java ?

A3 : La documentation complète est disponible [ici](https://reference.aspose.com/3d/java/).

### Q4 : Comment puis‑je obtenir du support pour Aspose.3D ?

A4 : Visitez le [forum Aspose.3D](https://forum.aspose.com/c/3d/18) pour toute assistance ou question.

### Q5 : Des licences temporaires sont‑elles disponibles pour Aspose.3D ?

A5 : Oui, vous pouvez obtenir une licence temporaire [ici](https://purchase.aspose.com/temporary-license/).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Dernière mise à jour :** 2026-02-22  
**Testé avec :** Aspose.3D for Java (latest release)  
**Auteur :** Aspose