---
date: 2026-02-22
description: Apprenez à créer une scène 3D et à l'exporter en utilisant Aspose.3D
  pour Java avec extrusion linéaire, torsion et décalage de torsion.
linktitle: Using Twist Offset in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Comment créer une scène 3D avec un décalage de torsion dans une extrusion linéaire
  en utilisant Aspose.3D pour Java
url: /fr/java/linear-extrusion/using-twist-offset/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Utilisation du Twist Offset dans l'extrusion linéaire avec Aspose.3D pour Java

## Introduction

Dans le monde dynamique des graphiques 3D, maîtriser l'art de **create 3d scene** est un facteur décisif pour tout projet de modélisation 3D Java. Avec Aspose.3D pour Java, vous pouvez non seulement extruder des formes linéairement mais aussi ajouter un twist offset pour produire une géométrie complexe et torsadée. Ce tutoriel vous guide à travers chaque étape nécessaire pour **create 3d scene**, appliquer une torsion d'extrusion linéaire, et enfin **export 3d scene** vers un fichier OBJ courant.

## Quick Answers
- **What does Twist Offset do?** Il décale le point de départ de la torsion, vous permettant de décaler la rotation le long du chemin d'extrusion.  
- **Which class performs linear extrusion?** `LinearExtrusion` – vous pouvez définir la torsion, les tranches et le twist offset dessus.  
- **Can I export the result?** Oui, appelez `scene.save(..., FileFormat.WAVEFRONTOBJ)` pour exporter la scène 3D.  
- **Do I need a license for development?** Une licence temporaire suffit pour les tests ; une licence complète est requise pour la production.  
- **What Java version is supported?** Tout runtime Java 8+ fonctionne avec la dernière bibliothèque Aspose.3D.

## What is “create 3d scene” in Aspose.3D?
Créer une scène 3D signifie instancier un objet `Scene`, ajouter des nœuds (objets) à sa hiérarchie, puis enregistrer la scène dans le format de fichier de votre choix. C’est la base de tout flux de travail de modélisation 3D en Java.

## Why use linear extrusion twist with a twist offset?
Ajouter une torsion lors de l'extrusion vous donne des formes en spirale comme des colonnes hélicoïdales ou des poignées décoratives. Le twist offset vous permet de commencer la torsion à une position personnalisée, offrant un contrôle plus fin sur la forme finale—parfait pour les pièces mécaniques, les modèles artistiques ou les détails architecturaux.

## Prerequisites

- **Environnement Java :** Assurez‑vous d’avoir un environnement de développement Java configuré sur votre système.  
- **Aspose.3D pour Java :** Téléchargez et installez la bibliothèque Aspose.3D depuis le [lien de téléchargement](https://releases.aspose.com/3d/java/).  
- **Documentation :** Familiarisez‑vous avec la [documentation Aspose.3D pour Java](https://reference.aspose.com/3d/java/).

## Import Packages

Dans votre projet Java, importez les packages nécessaires pour commencer à utiliser Aspose.3D pour Java. Assurez‑vous d’inclure les bibliothèques requises pour une intégration fluide.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## How to create 3d scene – Guide étape par étape

### Step 1: Set Up the Environment
Commencez par configurer votre environnement de développement Java et vous assurer qu’Aspose.3D pour Java est correctement installé. Cette étape est essentielle pour tout travail de **java 3d modeling**.

### Step 2: Initialize the Base Profile
Créez un profil de base pour l'extrusion, dans ce cas, un `RectangleShape` avec un rayon d’arrondi de 0,3. Le profil définit la section transversale qui sera balayée le long du chemin d'extrusion.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
// Initialize the base profile to be extruded
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

### Step 3: Create a 3D Scene
Construisez une scène 3D pour contenir vos objets extrudés. C’est ici que vous **create child node** des éléments qui représentent chaque pièce de géométrie.

```java
// Create a scene
Scene scene = new Scene();
```

### Step 4: Create Nodes
Générez des nœuds dans la scène pour représenter différentes entités. Ici nous créons deux nœuds frères—un pour une extrusion simple et un autre qui utilise un twist offset.

```java
// Create left node
Node left = scene.getRootNode().createChildNode();
// Create right node
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### Step 5: Perform Linear Extrusion with Twist and Twist Offset
Appliquez une extrusion linéaire sur les deux nœuds. Le nœud de gauche montre une torsion basique, tandis que le nœud de droite ajoute un twist offset pour illustrer le contrôle supplémentaire offert par cette fonctionnalité.

```java
// Perform linear extrusion on left node using twist and slices property
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});

// Perform linear extrusion on right node using twist, twist offset, and slices property
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setTwistOffset(new Vector3(3, 0, 0)); }});
```

> **Astuce :** Ajustez `setSlices()` pour augmenter la résolution du maillage lorsque vous avez besoin d’une courbure plus lisse.

### Step 6: Save the 3D Scene (Export 3d scene)
Enfin, exportez la scène assemblée vers un fichier OBJ afin de pouvoir la visualiser dans n’importe quel visualiseur 3D standard ou l’importer dans d’autres pipelines.

```java
// Save 3D scene
scene.save(MyDir + "TwistOffsetInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

Lorsque le code s’exécute avec succès, vous trouverez `TwistOffsetInLinearExtrusion.obj` dans le répertoire spécifié, prêt à être ouvert dans des outils tels que Blender, MeshLab ou tout logiciel de CAO.

## Common Issues and Solutions
| Problème | Pourquoi cela se produit | Solution |
|----------|--------------------------|----------|
| **La scène s’enregistre comme fichier vide** | Le chemin `MyDir` est incorrect ou les permissions d’écriture sont manquantes. | Vérifiez que le répertoire existe et est accessible en écriture, ou utilisez un chemin absolu. |
| **La torsion semble plate** | `setSlices()` est trop faible, ce qui produit un maillage grossier. | Augmentez le nombre de tranches (par ex., 200) pour des torsions plus lisses. |
| **Le twist offset n’a aucun effet** | Le vecteur d’offset est colinéaire à la direction d’extrusion. | Utilisez une composante X ou Y non nulle pour voir le décalage de l’offset. |

## Frequently Asked Questions

### Q1 : Puis‑je utiliser Aspose.3D pour Java dans des projets non commerciaux ?
A1 : Oui, Aspose.3D pour Java peut être utilisé dans des projets commerciaux et non commerciaux. Consultez les [options de licence](https://purchase.aspose.com/buy) pour plus de détails.

### Q2 : Où puis‑je trouver du support pour Aspose.3D pour Java ?
A2 : Visitez le [forum Aspose.3D pour Java](https://forum.aspose.com/c/3d/18) pour obtenir de l’aide et rejoindre la communauté.

### Q3 : Existe‑t‑il une version d’essai gratuite pour Aspose.3D pour Java ?
A3 : Oui, vous pouvez explorer une version d’essai gratuite depuis la [page des releases](https://releases.aspose.com/).

### Q4 : Comment obtenir une licence temporaire pour Aspose.3D pour Java ?
A4 : Obtenez une licence temporaire pour votre projet en visitant [ce lien](https://purchase.aspose.com/temporary-license/).

### Q5 : Existe‑t‑il des exemples et tutoriels supplémentaires ?
A5 : Oui, consultez la [documentation](https://reference.aspose.com/3d/java/) pour plus d’exemples et de tutoriels approfondis.

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Dernière mise à jour :** 2026-02-22  
**Testé avec :** Aspose.3D for Java 24.11 (latest)  
**Auteur :** Aspose