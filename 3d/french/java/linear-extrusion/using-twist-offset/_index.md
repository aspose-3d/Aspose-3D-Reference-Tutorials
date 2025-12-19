---
date: 2025-12-19
description: Apprenez à créer une scène 3D et à exporter un objet 3D au format OBJ
  en utilisant le décalage de torsion dans l'extrusion linéaire avec Aspose.3D pour
  Java.
linktitle: Create 3d scene with Twist Offset – Aspose.3D Java
second_title: Aspose.3D Java API
title: Créer une scène 3D avec Twist Offset – Aspose.3D Java
url: /fr/java/linear-extrusion/using-twist-offset/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Créer une scène 3d avec Twist Offset – Aspose.3D pour Java

## Introduction

Dans le monde dynamique des graphiques 3D, apprendre à **créer une scène 3d** avec extrusion linéaire est un véritable changement de jeu. Avec Aspose.3D pour Java, vous pouvez élever vos compétences en modélisation 3D en incorporant la fonction Twist Offset dans votre processus d'extrusion linéaire. Ce tutoriel vous guidera à travers les étapes d'utilisation de Twist Offset dans l'extrusion linéaire avec Aspose.3D pour Java, vous fournissant les outils pour créer des scènes 3D époustouflantes.

## Quick Answers
- **Que fait Twist Offset ?** Il décale le début de la torsion le long du chemin d'extrusion, vous offrant plus de contrôle sur la géométrie.  
- **Quel format de fichier est utilisé pour l'exportation ?** L'exemple enregistre le modèle au format Wavefront OBJ (`.obj`).  
- **Ai-je besoin d'une licence pour le développement ?** Un essai gratuit suffit pour les tests ; une licence commerciale est requise pour la production.  
- **Quelle version de Java est requise ?** Java 8 ou ultérieure.  
- **Puis-je changer le nombre de tranches ?** Oui – la méthode `setSlices` définit la fluidité de la torsion.

## Prerequisites

Avant de plonger dans le tutoriel, assurez-vous d'avoir les prérequis suivants en place :

- Environnement Java : Assurez-vous d'avoir un environnement de développement Java configuré sur votre système.  
- Aspose.3D pour Java : Téléchargez et installez la bibliothèque Aspose.3D depuis le [lien de téléchargement](https://releases.aspose.com/3d/java/).  
- Documentation : Familiarisez‑vous avec la [documentation Aspose.3D pour Java](https://reference.aspose.com/3d/java/).  

## Import Packages

Dans votre projet Java, importez les packages nécessaires pour commencer à utiliser Aspose.3D pour Java. Assurez‑vous d'inclure les bibliothèques requises pour une intégration fluide.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## Step 1: Set Up the Environment

### Étape 1 : Configurer l'environnement

Commencez par configurer votre environnement de développement Java et assurez‑vous qu'Aspose.3D pour Java est correctement installé.

## Step 2: Initialize the Base Profile

### Étape 2 : Initialiser le profil de base

Créez un profil de base pour l'extrusion, dans ce cas, un `RectangleShape` avec un rayon d'arrondi de 0,3.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
// Initialize the base profile to be extruded
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Step 3: Create a 3D Scene

### Étape 3 : Créer une scène 3D

Construisez une scène 3D pour contenir vos objets extrudés.

```java
// Create a scene
Scene scene = new Scene();
```

## Step 4: Create Nodes

### Étape 4 : Créer des nœuds

Générez des nœuds au sein de la scène pour représenter différentes entités.

```java
// Create left node
Node left = scene.getRootNode().createChildNode();
// Create right node
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Step 5: Perform Linear Extrusion

### Étape 5 : Effectuer une extrusion linéaire

Utilisez l'extrusion linéaire sur les nœuds gauche et droit avec diverses propriétés.

```java
// Perform linear extrusion on left node using twist and slices property
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});

// Perform linear extrusion on right node using twist, twist offset, and slices property
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setTwistOffset(new Vector3(3, 0, 0)); }});
```

## Step 6: Save the 3D Scene

### Étape 6 : Enregistrer la scène 3D

Enregistrez votre scène 3D nouvellement créée avec le format de fichier spécifié.

```java
// Save 3D scene
scene.save(MyDir + "TwistOffsetInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## How to save 3d model and export 3d obj

Comment enregistrer le modèle 3d et exporter le 3d obj

L'appel `scene.save` à l'étape précédente **enregistre le modèle 3d** sous forme de fichier OBJ, qui est un format **export 3d obj** largement pris en charge. Vous pouvez changer le nom du fichier ou choisir un autre format supporté (par ex., STL, FBX) en ajustant l'énumération `FileFormat`.

## Conclusion

Félicitations ! Vous avez implémenté avec succès Twist Offset dans l'extrusion linéaire en utilisant Aspose.3D pour Java. Cette fonctionnalité puissante ouvre un monde de possibilités pour vos projets de modélisation 3D, vous permettant de **créer une scène 3d** avec des torsions et décalages complexes, puis de **enregistrer le modèle 3d** dans un format prêt pour les pipelines en aval.

## FAQ's

### Q1 : Puis‑je utiliser Aspose.3D pour Java dans des projets non commerciaux ?

R1 : Oui, Aspose.3D pour Java peut être utilisé dans des projets commerciaux et non commerciaux. Consultez les [options de licence](https://purchase.aspose.com/buy) pour plus de détails.

### Q2 : Où puis‑je trouver du support pour Aspose.3D pour Java ?

R2 : Visitez le [forum Aspose.3D pour Java](https://forum.aspose.com/c/3d/18) pour obtenir de l'aide et rejoindre la communauté.

### Q3 : Existe‑t‑il une version d'essai gratuite pour Aspose.3D pour Java ?

R3 : Oui, vous pouvez explorer une version d'essai gratuite depuis la [page des releases](https://releases.aspose.com/).

### Q4 : Comment obtenir une licence temporaire pour Aspose.3D pour Java ?

R4 : Obtenez une licence temporaire pour votre projet en visitant [ce lien](https://purchase.aspose.com/temporary-license/).

### Q5 : Existe‑t‑il d'autres exemples et tutoriels disponibles ?

R5 : Oui, consultez la [documentation](https://reference.aspose.com/3d/java/) pour plus d'exemples et de tutoriels approfondis.

## Frequently Asked Questions

## Questions fréquemment posées

**Q : Ce tutoriel fait‑il partie d’une série de tutoriels Aspose 3d ?**  
R : Oui – il s'agit d'un **tutoriel aspose 3d** officiel qui démontre une fonctionnalité spécifique de la bibliothèque.

**Q : Puis‑je utiliser une forme différente au lieu d'un rectangle ?**  
R : Absolument. Toute implémentation de `IProfile` (par ex., `CircleShape`, `PolygonShape` personnalisé) peut être extrudée.

**Q : Que se passe‑t‑il si j'omets `setTwistOffset` ?**  
R : L'extrusion commencera à se tordre depuis l'origine du profil, ce qui entraîne une torsion symétrique.

**Q : Comment augmenter la fluidité de la torsion ?**  
R : Augmentez la valeur passée à `setSlices` ; un nombre de tranches plus élevé produit une géométrie plus lisse.

**Q : Quels autres formats de fichier puis‑je exporter en plus de OBJ ?**  
R : Aspose.3D prend en charge STL, FBX, GLTF, 3MF, et plusieurs autres via l'énumération `FileFormat`.

---

**Last Updated:** 2025-12-19  
**Tested With:** Aspose.3D 24.11 for Java  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

## MOTS‑CLÉS CIBLES:

**Mot‑clé principal (PRIORITÉ MAXIMALE) :**  
create 3d scene  

**Mots‑clés secondaires (SUPPORT) :**  
save 3d model, export 3d obj, aspose 3d tutorial