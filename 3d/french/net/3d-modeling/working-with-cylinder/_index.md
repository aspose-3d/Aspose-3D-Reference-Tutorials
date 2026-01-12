---
date: 2026-01-12
description: Apprenez comment créer un cylindre de base de cisaillement et comment
  exporter un modèle 3D au format OBJ en utilisant Aspose.3D pour .NET. Suivez ce
  guide étape par étape pour maîtriser la modélisation 3D.
linktitle: Customized Shear Bottom Cylinder
second_title: Aspose.3D .NET API
title: Comment créer un cylindre à base cisaillée avec Aspose.3D pour .NET
url: /fr/net/3d-modeling/working-with-cylinder/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Cylindre à base cisaillée personnalisé

## Introduction
Bienvenue dans notre guide complet où **vous apprendrez à créer des modèles de cylindre à base cisaillée** avec Aspose.3D for .NET. Que vous créiez un asset de jeu, une pièce mécanique ou une démo visuelle, ce tutoriel vous montre exactement comment façonner la base d’un cylindre, appliquer une cisaille, et enfin **exporter le fichier modèle 3D OBJ** pour une utilisation dans n’importe quel pipeline en aval. Parcourons chaque étape ensemble, afin que vous puissiez commencer à produire des géométries personnalisées en quelques minutes.

## Quick Answers
- **Qu’est‑ce qu’un cylindre à base cisaillée ?** Un cylindre dont la face inférieure est inclinée (cisaillée) plutôt que plate.  
- **Quelle bibliothèque est utilisée ?** Aspose.3D for .NET.  
- **Comment exporter le modèle ?** Utilisez `scene.Save(..., FileFormat.WavefrontOBJ)`.  
- **Ai‑je besoin d’une licence ?** Une version d’essai est disponible ; une licence commerciale est requise pour la production.  
- **Quelles sont les prérequis ?** Un environnement de développement .NET et le package NuGet Aspose.3D.

## Qu’est‑ce qu’un cylindre à base cisaillée ?
Un cylindre à base cisaillée est un maillage cylindrique standard dont la face inférieure a été transformée par une opération de cisaille. Cela vous permet de créer des bases inclinées, des rampes ou des connecteurs personnalisés sans éditer manuellement les sommets.

## Pourquoi utiliser Aspose.3D pour cette tâche ?
- **Contrôle total** sur les paramètres de géométrie (rayon, hauteur, segments).  
- **Support de la cisaille intégré** via la propriété `ShearBottom`, vous évitant la manipulation de maillage de bas niveau.  
- **Export en un clic** vers des formats populaires comme OBJ, FBX et STL, rendant l’intégration avec d’autres outils fluide.

## Prérequis
Avant de commencer, assurez‑vous de disposer de :

- Connaissances de base en C# et .NET.  
- Aspose.3D for .NET installé. Vous pouvez le télécharger **[ici](https://releases.aspose.com/3d/net/)**.  
- Un IDE compatible .NET (Visual Studio, Rider ou VS Code).

## Import Namespaces
Dans votre fichier C#, commencez par importer les espaces de noms nécessaires :

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

## Step 1: Create a Scene
Tout d’abord, créez une nouvelle scène 3‑D qui contiendra tous nos objets.

```csharp
Scene scene = new Scene();
```

## Step 2: Create Cylinder 1
Créez le cylindre principal que nous personnaliserons avec une base cisaillée.

```csharp
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```

## Step 3: Customize Shear Bottom for Cylinder 1
Appliquez la cisaille, activez la génération de fan et ajustez les autres propriétés pour obtenir la forme souhaitée.

```csharp
// Shear 47.5deg in the xy plane (z‑axis)
cylinder1.ShearBottom = new Vector2(0, 0.83); 

// Set GenerateFanCylinder to true
cylinder1.GenerateFanCylinder = true;
// Set ThetaLength
cylinder1.ThetaLength = MathUtils.ToRadian(270);

// Set OffsetTop
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```

## Step 4: Add Cylinder 1 to the Scene
Placez le cylindre personnalisé dans la scène et déplacez‑le légèrement vers la droite afin de voir les deux objets côte à côte.

```csharp
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```

## Step 5: Create Cylinder 2
Créez un second cylindre simple pour la comparaison.

```csharp
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```

## Step 6: Add Cylinder 2 to the Scene
Ajoutez le second cylindre sans aucune cisaille personnalisée — cela permet d’illustrer l’effet des étapes précédentes.

```csharp
scene.RootNode.CreateChildNode(cylinder2);
```

## Step 7: Save the Scene
Enfin, exportez la scène entière au format OBJ afin de pouvoir l’ouvrir dans Blender, Maya ou tout autre visualiseur 3‑D.

```csharp
scene.Save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WavefrontOBJ);
```

## Common Issues & Tips
- **Valeurs de cisaille** : le `Vector2` prend les facteurs de cisaille X et Y. Une valeur de `0.83` correspond à environ 47,5°, mais vous pouvez l’ajuster pour d’autres angles.  
- **Chemin d’export** : assurez‑vous que le dossier spécifié existe et que vous avez les droits d’écriture ; sinon `scene.Save` lèvera une exception.  
- **Performance** : pour des cylindres à très haut nombre de segments, envisagez de réduire le nombre de segments (`20` dans l’exemple) afin de garder la taille du fichier OBJ raisonnable.

## Frequently Asked Questions

### Aspose.3D for .NET convient‑il aux débutants ?
Absolument ! Aspose.3D for .NET propose une API conviviale, accessible tant aux débutants qu’aux développeurs expérimentés.

### Puis‑je appliquer différents angles de cisaille aux cylindres ?
Oui, vous pouvez personnaliser la propriété `ShearBottom` pour chaque cylindre individuellement, ce qui vous permet d’obtenir des effets uniques.

### Une version d’essai est‑elle disponible ?
Oui, vous pouvez explorer la version d’essai gratuite **[ici](https://releases.aspose.com/)**.

### Où trouver un support supplémentaire ?
Visitez le **[forum Aspose.3D](https://forum.aspose.com/c/3d/18)** pour le support communautaire et les discussions.

### Comment obtenir une licence temporaire ?
Obtenez votre licence temporaire **[ici](https://purchase.aspose.com/temporary-license/)**.

**Additional Q&A**

**Q : Comment changer le format d’export en FBX ?**  
R : Remplacez `FileFormat.WavefrontOBJ` par `FileFormat.FBX` dans l’appel `scene.Save`.

**Q : Puis‑je animer le cylindre après l’export ?**  
R : OBJ ne supporte pas l’animation ; utilisez FBX ou GLTF si vous avez besoin de données animées.

**Q : Et si j’ai besoin d’un rayon de cylindre plus grand ?**  
R : Ajustez les deux premiers paramètres du constructeur `Cylinder` (par ex., `new Cylinder(4, 4, …)`).

## Conclusion
Vous avez maintenant maîtrisé comment **créer des modèles de cylindre à base cisaillée** et les exporter au format OBJ avec Aspose.3D for .NET. Expérimentez avec différentes valeurs de cisaille, nombres de segments et formats d’export pour répondre aux besoins de votre projet. Bon modélisation !

---

**Last Updated:** 2026-01-12  
**Tested With:** Aspose.3D for .NET 24.11 (latest at time of writing)  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}