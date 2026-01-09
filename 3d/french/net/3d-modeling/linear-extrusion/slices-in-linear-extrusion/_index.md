---
date: 2026-01-09
description: Apprenez à créer une scène 3D et à enregistrer un modèle 3D en utilisant
  Aspose.3D pour .NET, y compris l'exportation au format Wavefront OBJ et les découpes
  d'extrusion linéaire.
linktitle: Create 3D Scene with Linear Extrusion Slices
second_title: Aspose.3D .NET API
title: Créer une scène 3D avec des tranches d'extrusion linéaire
url: /fr/net/3d-modeling/linear-extrusion/slices-in-linear-extrusion/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Créer une scène 3D avec des tranches d'extrusion linéaire

## Introduction

Bienvenue dans le monde de la conception 3D avec Aspose.3D pour .NET ! Dans ce tutoriel, vous allez **créer une scène 3d**, appliquer une extrusion linéaire avec un nombre de tranches personnalisé, puis **enregistrer le modèle 3d** au format Wavefront OBJ. Que vous construisiez un prototype rapide ou une visualisation prête pour la production, les étapes ci‑dessous vous montreront **comment utiliser Aspose** pour générer une géométrie de haute qualité directement depuis C#.

## Réponses rapides
- **Que signifie « créer une scène 3d » ?** Cela consiste à créer un objet Scene qui contient toutes les entités 3D (maillages, lumières, caméras).  
- **Quel format est utilisé pour l’exportation ?** L’exemple exporte vers **Wavefront OBJ** (`export wavefront obj`).  
- **Combien de tranches puis‑je définir ?** Vous pouvez définir n’importe quel entier ; la démo montre 2 et 10 tranches.  
- **Ai‑je besoin d’une licence ?** Une licence temporaire ou complète est requise pour une utilisation en production.  
- **Puis‑je exécuter cela sur .NET Core ?** Oui, Aspose.3D prend en charge .NET Framework et .NET Core.

## Prérequis

Avant de plonger dans la conception 3D avec Aspose.3D, assurez‑vous de disposer des éléments suivants :

- Bibliothèque Aspose.3D pour .NET : assurez‑vous que la bibliothèque Aspose.3D est installée. Vous pouvez la télécharger [ici](https://releases.aspose.com/3d/net/).

- Environnement de développement intégré (IDE) : utilisez l’IDE de votre choix compatible avec le développement .NET.

- Connaissances de base en C# : familiarisez‑vous avec les fondamentaux du langage de programmation C#.

- Envie d’explorer la conception 3D : une passion pour la création de modèles 3D visuellement époustouflants !

## Importer les espaces de noms

Pour commencer votre aventure de conception 3D avec Aspose.3D, vous devez importer les espaces de noms nécessaires. Cela permet à votre code d’accéder aux classes et fonctionnalités requises.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Comment créer une scène 3d avec une extrusion linéaire

Ci‑dessous, nous parcourons chaque étape nécessaire pour construire la scène, appliquer l’extrusion et **enregistrer le modèle 3d** au format OBJ. Les explications sont rédigées de façon conversationnelle afin que vous puissiez suivre facilement.

### Étape 1 : Initialiser le profil de base

Tout d’abord, nous définissons la forme 2‑D qui sera extrudée. Dans ce cas, un rectangle aux coins arrondis.

```csharp
// ExStart:InitializeBaseProfile
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
// ExEnd:InitializeBaseProfile
```

### Étape 2 : Créer une scène 3D

Un objet `Scene` est le conteneur de toute la géométrie, des lumières et des caméras — le cœur de **la création d’une scène 3d**.

```csharp
// ExStart:Create3DScene
Scene scene = new Scene();
// ExEnd:Create3DScene
```

### Étape 3 : Créer les nœuds gauche et droit

Nous ajoutons deux nœuds enfants à la racine de la scène. L’un utilisera un faible nombre de tranches, l’autre un nombre plus élevé, afin que vous puissiez voir la différence visuelle.

```csharp
// ExStart:CreateLeftRightNodes
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(15, 0, 0);
// ExEnd:CreateLeftRightNodes
```

### Étape 4 : Effectuer l’extrusion linéaire sur le nœud gauche

Ici, nous extrudons le rectangle avec **2 tranches**. Un nombre réduit de tranches donne un aspect plus grossier.

```csharp
// ExStart:LinearExtrusionLeftNode
left.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 2 });
// ExEnd:LinearExtrusionLeftNode
```

### Étape 5 : Effectuer l’extrusion linéaire sur le nœud droit

Maintenant, nous extrudons le même profil mais avec **10 tranches**, produisant une surface plus lisse.

```csharp
// ExStart:LinearExtrusionRightNode
right.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 10 });
// ExEnd:LinearExtrusionRightNode
```

### Étape 6 : Enregistrer la scène 3D

Enfin, nous exportons la scène vers un fichier Wavefront OBJ. Cela montre **comment enregistrer un obj** et **exporter wavefront obj** à l’aide d’Aspose.3D.

```csharp
// ExStart:Save3DScene
scene.Save("Your Output Directory" + "SlicesInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
// ExEnd:Save3DScene
```

## Problèmes courants et solutions

| Problème | Pourquoi cela se produit | Solution |
|----------|--------------------------|----------|
| Le fichier OBJ apparaît vide | Le chemin de sortie est incorrect ou les permissions d’écriture sont manquantes. | Vérifiez que le répertoire existe et que l’application dispose des droits d’écriture. |
| Les tranches n’influencent pas la douceur | La valeur `Slices` est trop basse pour la taille de la géométrie. | Augmentez le nombre de tranches ou ajustez les dimensions du profil. |
| Exception de licence | Exécution sans licence valide dans une version non‑d’évaluation. | Appliquez une licence temporaire ou permanente avec `License license = new License(); license.SetLicense("Aspose.3D.lic");` |

## Questions fréquemment posées

**Q : Puis‑je utiliser Aspose.3D pour .NET avec d’autres langages de programmation ?**  
R : Aspose.3D est principalement conçu pour .NET, mais vous pouvez explorer des options d’interopérabilité avec des langages comme Python via des liaisons .NET.

**Q : Où puis‑je trouver la documentation détaillée d’Aspose.3D pour .NET ?**  
R : Consultez la documentation [ici](https://reference.aspose.com/3d/net/) pour des informations approfondies sur les capacités et l’utilisation d’Aspose.3D.

**Q : Existe‑t‑il un essai gratuit d’Aspose.3D pour .NET ?**  
R : Oui, vous pouvez obtenir votre essai gratuit [ici](https://releases.aspose.com/) pour explorer les fonctionnalités de la bibliothèque avant d’effectuer un achat.

**Q : Comment obtenir le support technique pour Aspose.3D pour .NET ?**  
R : Visitez le forum Aspose.3D [ici](https://forum.aspose.com/c/3d/18) pour demander de l’aide et interagir avec la communauté.

**Q : Puis‑je utiliser une licence temporaire pour Aspose.3D pour .NET ?**  
R : Oui, obtenez une licence temporaire [ici](https://purchase.aspose.com/temporary-license/) à des fins d’évaluation.

## Conclusion

Félicitations ! Vous avez appris à **créer une scène 3d**, appliquer une extrusion linéaire avec un nombre de tranches personnalisé, et **enregistrer le modèle 3d** au format Wavefront OBJ en utilisant Aspose.3D pour .NET. Ce n’est que le début de votre aventure de conception 3D — n’hésitez pas à expérimenter avec différents profils, valeurs de tranches et formats d’exportation pour exploiter tout le potentiel du **modélisation 3d c#**.

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Last Updated:** 2026-01-09  
**Tested With:** Aspose.3D 24.11 for .NET  
**Author:** Aspose