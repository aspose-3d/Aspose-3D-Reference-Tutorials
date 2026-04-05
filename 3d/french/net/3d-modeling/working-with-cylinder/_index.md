---
date: 2026-03-26
description: Apprenez à créer un cylindre et à exporter un fichier OBJ en utilisant
  Aspose.3D pour .NET. Ce guide convivial pour les débutants couvre la configuration
  de la scène 3D et l'exportation OBJ.
linktitle: Customized Shear Bottom Cylinder
second_title: Aspose.3D .NET API
title: Comment créer un cylindre avec une base en cisaillement – Aspose.3D pour .NET
url: /fr/net/3d-modeling/working-with-cylinder/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Comment créer un cylindre avec une base en cisaillement – Aspose.3D pour .NET

## Introduction
Si vous vous demandez **comment créer un cylindre** avec une base en cisaillement personnalisée dans un environnement .NET, vous êtes au bon endroit. Dans ce tutoriel, nous parcourrons chaque étape — de la configuration d’une scène 3 D à l’exportation du modèle final au format OBJ — afin que vous puissiez améliorer vos compétences en *modélisation 3D pour débutants* en utilisant **Aspose.3D for .NET**.

## Quick Answers
- **Quelle est la classe principale pour démarrer un modèle 3D ?** `Scene` crée le conteneur racine pour toute la géométrie.  
- **Quelle méthode exporte le modèle au format OBJ ?** `scene.Save(..., FileFormat.WavefrontOBJ)`.  
- **Ai‑je besoin d’une licence pour les tests ?** Un essai gratuit est disponible — voir le lien d’essai dans la FAQ.  
- **Puis‑je modifier l’angle de cisaillement ?** Oui, modifiez `ShearBottom` avec une valeur `Vector2`.  
- **Ce tutoriel convient‑il aux débutants ?** Absolument ; l’API abstrait la gestion de maillage de bas niveau.

## What is a 3D Scene?
Une *scène 3D* est un conteneur hiérarchique qui regroupe toutes les entités géométriques, lumières, caméras et transformations. Dans Aspose.3D, la classe `Scene` offre un moyen propre d’organiser puis d’exporter vos modèles.

## Why Export OBJ?
OBJ est un format texte largement supporté que de nombreuses applications 3‑D (Blender, Maya, Unity) peuvent importer. Exporter en OBJ vous permet de partager ou de modifier davantage vos modèles de cylindre en dehors de .NET.

## Prerequisites
Avant de commencer, assurez‑vous d’avoir :

- Connaissances de base en C# et développement .NET.  
- **Aspose.3D for .NET** installé – vous pouvez le télécharger **[ici](https://releases.aspose.com/3d/net/)**.  
- Un IDE .NET (Visual Studio, Rider ou VS Code) prêt pour le codage.

## Import Namespaces
Tout d’abord, importez les espaces de noms requis afin que les types de l’API soient reconnus.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```

## Step 1: Create a 3D Scene
L’objet `Scene` agit comme la racine de la hiérarchie de votre modèle.

```csharp
Scene scene = new Scene();
```

## Step 2: Create Cylinder 1
Nous générons le premier cylindre avec un rayon de 2, une hauteur de 10 et 20 segments radiaux.

```csharp
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```

## Step 3: Customize Shear Bottom for Cylinder 1
Appliquez une transformation de cisaillement, activez la génération de cylindre en éventail, et ajustez d’autres propriétés pour obtenir la forme souhaitée.

```csharp
// Shear 47.5deg in the xy plane (z-axis)
cylinder1.ShearBottom = new Vector2(0, 0.83); 

// Set GenerateFanCylinder to true
cylinder1.GenerateFanCylinder = true;
// Set ThetaLength
cylinder1.ThetaLength = MathUtils.ToRadian(270);

// Set OffsetTop
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```

## Step 4: Add Cylinder 1 to the Scene
Placez le premier cylindre à un emplacement pratique en utilisant une transformation de translation.

```csharp
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```

## Step 5: Create Cylinder 2
Un second cylindre est créé avec les mêmes dimensions de base mais sans cisaillement personnalisé — parfait pour une comparaison côte à côte.

```csharp
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```

## Step 6: Add Cylinder 2 to the Scene
Nous attachons simplement le second cylindre au graphe de la scène.

```csharp
scene.RootNode.CreateChildNode(cylinder2);
```

## Step 7: Export the Scene as an OBJ File
Enfin, nous enregistrons la scène entière dans un fichier OBJ afin qu’il puisse être ouvert dans n’importe quel visualiseur 3‑D standard.

```csharp
scene.Save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WavefrontOBJ);
```

## Common Issues and Solutions
| Problème | Pourquoi cela se produit | Solution |
|----------|--------------------------|----------|
| **Le fichier OBJ est vide** | La scène n’a aucune géométrie attachée. | Assurez‑vous que les deux cylindres sont ajoutés à `scene.RootNode`. |
| **Le cisaillement est incorrect** | `ShearBottom` attend la tangente de l’angle. | Utilisez `Math.Tan(angleInRadians)` ou la valeur fournie `0.83` pour ≈ 47,5°. |
| **Erreurs de chemin de fichier** | Répertoire invalide ou manquant. | Utilisez `Path.Combine(Environment.CurrentDirectory, "CustomizedShearBottomCylinder.obj")`. |

## Frequently Asked Questions
### Aspose.3D for .NET convient‑il aux débutants ?
Absolument ! Aspose.3D for .NET propose une API de haut niveau qui abstrait les parties mathématiques lourdes de la modélisation 3‑D, la rendant accessible aux développeurs de tout niveau.

### Puis‑je appliquer différents angles de cisaillement aux cylindres ?
Oui, chaque instance `Cylinder` possède sa propre propriété `ShearBottom`, vous pouvez donc attribuer un angle unique à chaque objet.

### Une version d’essai est‑elle disponible ?
Oui, vous pouvez explorer la version d’essai gratuite **[ici](https://releases.aspose.com/)**.

### Où puis‑je trouver un support supplémentaire ?
Visitez le **[forum Aspose.3D](https://forum.aspose.com/c/3d/18)** pour obtenir de l’aide communautaire, des exemples de code et des discussions.

### Comment obtenir une licence temporaire ?
Obtenez votre licence temporaire **[ici](https://purchase.aspose.com/temporary-license/)**.

**Additional Q&A**

**Q : Comment exporter le modèle dans un autre format, comme STL ?**  
R : Remplacez `FileFormat.WavefrontOBJ` par `FileFormat.STL` dans l’appel `scene.Save`.

**Q : Puis‑je animer les cylindres après leur création ?**  
R : Oui, vous pouvez ajouter des animations image‑par‑image aux transformations des nœuds en utilisant les classes `Animation` fournies par Aspose.3D.

**Q : L’API prend‑elle en charge .NET Core ?**  
R : La bibliothèque est entièrement compatible avec .NET Core, .NET 5+ et .NET 6+.

---

**Last Updated:** 2026-03-26  
**Tested With:** Aspose.3D for .NET (latest release)  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}