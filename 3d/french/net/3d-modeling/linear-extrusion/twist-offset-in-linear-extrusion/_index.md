---
date: 2026-03-23
description: Apprenez comment ajouter une torsion à l'extrusion linéaire avec Aspose.3D
  pour .NET et découvrez comment utiliser l'extrusion pour les projets de modélisation
  3D ASP.NET.
linktitle: Twist Offset in Linear Extrusion
second_title: Aspose.3D .NET API
title: Comment ajouter une torsion à une extrusion linéaire avec Aspose.3D pour .NET
url: /fr/net/3d-modeling/linear-extrusion/twist-offset-in-linear-extrusion/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Comment ajouter une torsion à une extrusion linéaire avec Aspose.3D pour .NET

## Introduction

Si vous recherchez un guide clair, étape par étape sur **comment ajouter une torsion** à une extrusion linéaire, vous êtes au bon endroit. Dans ce tutoriel, nous parcourrons le processus complet avec Aspose.3D pour .NET, en vous montrant **comment utiliser l'extrusion** pour créer des formes 3D dynamiques parfaites pour les scénarios de *asp.net 3d modeling*. À la fin, vous disposerez d'un exemple prêt à l'exécution qui démontre le décalage de torsion, les tranches, et l'enregistrement du résultat sous forme de fichier OBJ.

## Réponses rapides
- **Que fait le « twist offset » ?** Il décale le point de départ de la torsion le long de l'axe d'extrusion.  
- **Ai-je besoin d'une licence pour exécuter l'exemple ?** Une licence temporaire suffit pour les tests ; une licence complète est requise en production.  
- **Quelles versions de .NET sont prises en charge ?** .NET Framework 4.5+, .NET Core 3.1+, .NET 5/6+.  
- **Puis-je modifier le nombre de tranches ?** Oui—ajustez la propriété `Slices` pour contrôler la fluidité du maillage.  
- **Le format de sortie est‑il limité à OBJ ?** Non, Aspose.3D prend en charge de nombreux formats ; OBJ est utilisé ici pour la simplicité.

## Qu'est‑ce que le Twist Offset dans une extrusion linéaire ?

Un twist offset définit un déplacement translationnel appliqué à l'opération de torsion. Au lieu de pivoter autour du point de départ exact de l'extrusion, la géométrie commence à tourner à partir du vecteur d'offset spécifié, vous offrant un contrôle artistique supplémentaire sur la forme finale.

## Pourquoi utiliser Aspose.3D pour .NET ?

- **API complète** – Gère les profils, les transformations et une large gamme de formats de fichiers.  
- **Cross‑platform** – Fonctionne sous Windows, Linux et macOS avec .NET Core.  
- **Optimisé pour la performance** – Génère des maillages propres sans calculs manuels.  
- **Documentation excellente** – De nombreux exemples pour accélérer le développement.

## Prérequis

Avant de commencer, assurez‑vous d'avoir :

- Aspose.3D for .NET Library : téléchargez et installez la bibliothèque depuis la [page de diffusion](https://releases.aspose.com/3d/net/).  
- Votre environnement de développement : Visual Studio, Rider ou tout IDE supportant C#.

## Importer les espaces de noms

Tout d'abord, importez les espaces de noms qui vous donnent accès aux classes 3D de base.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

Ces instructions rendent les types `Scene`, `LinearExtrusion`, `Vector3` et d'autres types essentiels disponibles dans votre code.

## Guide étape par étape

### Étape 1 : Initialiser le profil de base

Nous commençons avec un profil rectangulaire simple et lui appliquons un petit rayon d'arrondi afin que les arêtes ne soient pas parfaitement nettes.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

### Étape 2 : Créer une scène

Une `Scene` agit comme un conteneur pour tous les nœuds, lumières, caméras et géométries.

```csharp
Scene scene = new Scene();
```

### Étape 3 : Créer des nœuds

Deux nœuds enfants sont ajoutés à la racine de la scène — l'un pour l'extrusion simple et l'autre pour la version torsadée. Le nœud de gauche est déplacé sur l'axe X pour une séparation visuelle.

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(18, 0, 0);
```

### Étape 4 : Extrusion linéaire sur le nœud de gauche (sans twist offset)

Ici nous démontrons une extrusion de base avec une torsion complète de 360° et 100 tranches pour la fluidité.

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100 });
```

### Étape 5 : Extrusion linéaire sur le nœud de droite avec twist offset

Nous appliquons maintenant un twist offset de `(3, 0, 0)`. Cela déplace le point de départ de la torsion de trois unités le long de l'axe X, créant une hélice visiblement décalée.

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100, TwistOffset = new Vector3(3, 0, 0) });
```

### Étape 6 : Enregistrer la scène 3D

Enfin, nous écrivons la scène dans un fichier OBJ. Modifiez le chemin de sortie selon vos besoins.

```csharp
scene.Save("Your Output Directory" + "TwistOffsetInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## Problèmes courants et solutions

| Problème | Pourquoi cela se produit | Solution |
|----------|--------------------------|----------|
| **La torsion apparaît plate** | `Slices` est réglé trop bas, ce qui produit un maillage grossier. | Augmentez `Slices` (par ex., 200) pour une rotation plus fluide. |
| **L'objet est décentré** | `TwistOffset` utilise les coordonnées mondiales ; le nœud peut déjà être translaté. | Appliquez l'offset par rapport à la transformation locale du nœud ou ajustez la translation du nœud en conséquence. |
| **Fichier non enregistré** | Chemin de sortie incorrect ou permissions d'écriture manquantes. | Vérifiez que le répertoire existe et que l'application dispose des droits d'écriture. |
| **Exception de licence** | Exécution sans licence valide dans une version non‑d'essai. | Chargez une licence temporaire ou permanente avant de créer la scène. |

## Questions fréquentes

### Q1 : Puis‑je utiliser Aspose.3D pour .NET avec d'autres langages de programmation ?

**R1 :** Aspose.3D prend principalement en charge les langages .NET, mais Aspose propose des bibliothèques similaires pour Java et d'autres plateformes.

### Q2 : Comment obtenir une licence temporaire pour Aspose.3D pour .NET ?

**R2 :** Visitez [ce lien](https://purchase.aspose.com/temporary-license/) pour obtenir une licence temporaire à des fins de test.

### Q3 : Existe‑t‑il un forum communautaire pour Aspose.3D pour .NET ?

**R3 :** Absolument ! Rejoignez la communauté sur le [forum Aspose.3D](https://forum.aspose.com/c/3d/18) pour échanger avec d'autres développeurs et demander de l'aide.

### Q4 : Existe‑t‑il des exemples et de la documentation supplémentaires ?

**R4 :** Explorez la [documentation](https://reference.aspose.com/3d/net/) pour des guides et exemples détaillés.

### Q5 : Où puis‑je acheter Aspose.3D pour .NET ?

**R5 :** Rendez‑vous sur [ce lien](https://purchase.aspose.com/buy) pour effectuer un achat et débloquer tout le potentiel d'Aspose.3D.

### Q6 : Puis‑je exporter le modèle vers d'autres formats que OBJ ?

**R6 :** Oui—Aspose.3D prend en charge FBX, STL, 3MF et bien d'autres. Il suffit de changer la valeur de l'énumération `FileFormat` dans l'appel `Save`.

### Q7 : En quoi « comment ajouter une torsion » diffère‑t‑il d’une rotation ordinaire ?

**R7 :** Une torsion fait pivoter progressivement le profil le long de la longueur de l'extrusion, tandis qu'une rotation ordinaire applique un angle statique unique. L'offset ajoute un déplacement translationnel avant que la rotation ne commence.

---

**Last Updated:** 2026-03-23  
**Tested With:** Aspose.3D for .NET (latest release)  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}