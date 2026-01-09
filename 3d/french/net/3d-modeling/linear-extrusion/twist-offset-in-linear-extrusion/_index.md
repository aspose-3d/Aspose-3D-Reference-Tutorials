---
date: 2026-01-09
description: Apprenez à créer une scène 3D en utilisant Aspose.3D pour .NET, y compris
  l'exportation au format Wavefront OBJ et la façon de tordre le décalage dans une
  extrusion linéaire.
linktitle: Twist Offset in Linear Extrusion
second_title: Aspose.3D .NET API
title: Comment créer une scène 3D avec un décalage de torsion en extrusion linéaire
url: /fr/net/3d-modeling/linear-extrusion/twist-offset-in-linear-extrusion/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Créer une scène 3D : Décalage de torsion dans une extrusion linéaire

## Introduction

Si vous devez **créer une scène 3d** rapidement et ajouter de la géométrie dynamique, Aspose.3D for .NET vous fournit exactement les outils nécessaires. Dans ce **tutoriel Aspose 3D** nous passerons en revue la technique du *comment appliquer un décalage de torsion* lors d’une **extrusion linéaire avec torsion** et enfin **exporter des fichiers Wavefront OBJ**. À la fin, vous disposerez d’un modèle 3‑D complet, prêt pour le rendu ou un traitement ultérieur.

## Réponses rapides
- **Que fait le “twist offset” ?** Il décale le point de départ de la torsion le long de l’axe d’extrusion.  
- **Quelle méthode exporte Wavefront OBJ ?** `scene.Save(..., FileFormat.WavefrontOBJ)`.  
- **Ai‑je besoin d’une licence pour exécuter l’exemple ?** Une licence temporaire suffit pour les tests ; une licence complète est requise en production.  
- **Quelles versions .NET sont prises en charge ?** .NET Framework 4.5+, .NET Core 3.1+, .NET 5/6+.  
- **Combien de tranches sont recommandées pour des torsions fluides ?** Environ 100 tranches offrent un bon compromis entre qualité et performances.

## Qu’est‑ce que **create 3d scene** ?

Créer une scène 3‑D signifie construire une structure hiérarchique qui contient la géométrie, les lumières, les caméras et les transformations. Aspose.3D fournit une classe `Scene` qui agit comme le conteneur racine pour tous les nœuds que vous ajoutez.

## Pourquoi utiliser **linear extrusion twist** ?

Une extrusion linéaire avec torsion vous permet de transformer un profil 2‑D en un objet 3‑D en spirale — idéal pour des vis, des ressorts ou des colonnes décoratives. Ajouter un décalage de torsion vous donne encore plus de contrôle sur le point de départ de la rotation, permettant des conceptions asymétriques.

## Prérequis

Avant de commencer, assurez‑vous d’avoir :

- Bibliothèque Aspose.3D for .NET : téléchargez et installez la bibliothèque depuis la [page de diffusion](https://releases.aspose.com/3d/net/).  
- Votre environnement de développement : Visual Studio 2022 (ou tout IDE C#) prêt pour le développement .NET.

## Importer les espaces de noms

Commencez par importer les espaces de noms nécessaires pour accéder aux fonctionnalités d’Aspose.3D.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Guide étape par étape

### Étape 1 : Initialiser le profil de base  

Nous utiliserons un rectangle avec un petit rayon d’arrondi comme profil à extruder.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

### Étape 2 : Créer une scène  

C’est le conteneur où nous allons **create 3d scene** des nœuds.

```csharp
Scene scene = new Scene();
```

### Étape 3 : Créer des nœuds  

Deux nœuds frères sont ajoutés à la racine — un pour l’extrusion classique et un pour la version avec décalage.

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(18, 0, 0);
```

### Étape 4 : Extrusion linéaire sur le nœud de gauche (torsion de base)  

Ici nous démontrons une **linear extrusion twist** classique sans aucun décalage.

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100 });
```

### Étape 5 : Extrusion linéaire sur le nœud de droite avec **Twist Offset**  

Nous appliquons maintenant la technique du **how to twist offset** en fournissant un vecteur `TwistOffset`.

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100, TwistOffset = new Vector3(3, 0, 0) });
```

### Étape 6 : **Export Wavefront OBJ**  

Enfin, enregistrez la scène assemblée dans un fichier OBJ afin de pouvoir la visualiser avec n’importe quel visualiseur 3‑D standard.

```csharp
scene.Save("Your Output Directory" + "TwistOffsetInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## Problèmes courants & astuces

- **La torsion paraît plate ?** Augmentez la valeur `Slices` pour obtenir une géométrie plus lisse.  
- **Le décalage n’est pas visible ?** Vérifiez que le vecteur `TwistOffset` n’est pas nul et qu’il est aligné avec la direction d’extrusion.  
- **Le fichier OBJ ne contient pas de textures ?** OBJ ne stocke que la géométrie ; utilisez des fichiers MTL pour les définitions de matériaux si nécessaire.

## Questions fréquentes

**Q : Puis‑je utiliser Aspose.3D for .NET avec d’autres langages de programmation ?**  
R : Aspose.3D cible principalement les langages .NET, mais des bibliothèques équivalentes existent pour Java et d’autres plateformes.

**Q : Comment obtenir une licence temporaire pour Aspose.3D for .NET ?**  
R : Consultez [ce lien](https://purchase.aspose.com/temporary-license/) pour obtenir une licence temporaire à des fins de test.

**Q : Existe‑t‑il un forum communautaire pour Aspose.3D for .NET ?**  
R : Bien sûr ! Rejoignez la communauté sur le [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) pour échanger avec d’autres développeurs et obtenir de l’aide.

**Q : Y a‑t‑il des exemples supplémentaires et de la documentation disponible ?**  
R : Explorez la [documentation](https://reference.aspose.com/3d/net/) pour des guides détaillés et de nombreux exemples.

**Q : Où puis‑je acheter Aspose.3D for .NET ?**  
R : Rendez‑vous sur [ce lien](https://purchase.aspose.com/buy) pour effectuer un achat et débloquer tout le potentiel d’Aspose.3D.

## Conclusion

Dans ce **tutoriel aspose 3d** vous avez appris à **create 3d scene**, appliquer une **linear extrusion twist**, contrôler le **twist offset**, et **export Wavefront OBJ**. Ces techniques vous permettent d’ajouter une géométrie torsadée sophistiquée à n’importe quel projet 3‑D en quelques lignes de code seulement.

---

**Dernière mise à jour :** 2026-01-09  
**Testé avec :** Aspose.3D 24.11 for .NET  
**Auteur :** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}