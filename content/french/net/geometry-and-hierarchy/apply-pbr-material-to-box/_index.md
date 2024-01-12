---
title: Application d'un matériau PBR à une boîte dans des scènes 3D
linktitle: Application d'un matériau PBR à une boîte dans des scènes 3D
second_title: API Aspose.3D .NET
description: Explorez le monde des graphiques 3D avec Aspose.3D pour .NET. Créez des scènes immersives sans effort à l’aide de matériaux de rendu physique.
type: docs
weight: 10
url: /fr/net/geometry-and-hierarchy/apply-pbr-material-to-box/
---
## Introduction

Bienvenue dans le monde fascinant du graphisme 3D ! Dans ce guide étape par étape, nous explorerons la puissante bibliothèque Aspose.3D pour .NET et apprendrons comment créer de superbes scènes 3D à l'aide de matériaux de rendu physique (PBR). Aspose.3D simplifie le processus complexe de graphisme 3D et ouvre un champ de possibilités aux développeurs.

## Conditions préalables

Avant de plonger dans le monde passionnant des graphiques 3D, assurons-nous que tout est configuré :

### Téléchargez et installez Aspose.3D pour .NET

 Visiter le[Aspose.3D pour la documentation .NET](https://reference.aspose.com/3d/net/) pour des instructions détaillées sur le téléchargement et l’installation de la bibliothèque.

### Acquérir une licence

 Pour libérer tout le potentiel d’Aspose.3D, obtenez une licence valide. Vous pouvez obtenir une licence temporaire[ici](https://purchase.aspose.com/temporary-license/) ou achetez une licence complète[ici](https://purchase.aspose.com/buy).

## Importer des espaces de noms

Tout d'abord, assurez-vous d'importer les espaces de noms nécessaires pour exploiter les capacités d'Aspose.3D pour .NET :

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Shading;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
```

## Étape 1 : initialiser une scène

Commencez par initialiser une scène 3D à l'aide de l'extrait de code suivant :

```csharp
Scene scene = new Scene();
```

## Étape 2 : initialiser le matériel PBR

Créez un objet matériel PBR pour obtenir un rendu réaliste :

```csharp
PbrMaterial mat = new PbrMaterial();
```

## Étape 3 : Définir les propriétés du matériau

Affiner les propriétés du matériau, le rendant presque métallique et très rugueux :

```csharp
mat.MetallicFactor = 0.9;
mat.RoughnessFactor = 0.9;
```

## Étape 4 : Créer une boîte

Générez une boîte sur laquelle le matériau PBR sera appliqué :

```csharp
var boxNode = scene.RootNode.CreateChildNode("box", new Box());
```

## Étape 5 : Appliquer le matériau à la boîte

Affectez le matériau PBR au nœud de boîte créé :

```csharp
boxNode.Material = mat;
```

## Étape 6 : Enregistrez la scène 3D

Enregistrez la scène 3D au format STL avec le répertoire de sortie souhaité :

```csharp
scene.Save("Your Output Directory" + "PBR_Material_Box_Out.stl", FileFormat.STLASCII);
```

Toutes nos félicitations! Vous avez appliqué avec succès un matériau PBR à une boîte dans une scène 3D à l'aide d'Aspose.3D pour .NET.

## Conclusion

S'aventurer dans les graphiques 3D avec Aspose.3D pour .NET ouvre les portes à des possibilités créatives infinies. Grâce à son API intuitive et à ses fonctionnalités robustes, créer des scènes visuellement époustouflantes devient une expérience agréable pour les développeurs.

## FAQ

### Q1 : Aspose.3D est-il compatible avec d'autres formats de fichiers 3D ?

A1 : Oui, Aspose.3D prend en charge différents formats de fichiers 3D, garantissant ainsi la flexibilité de vos projets.

### Q2 : Puis-je utiliser Aspose.3D pour des applications commerciales ?

A2 : Absolument ! Aspose.3D fournit des licences commerciales pour une intégration transparente dans vos applications.

### Q3 : Existe-t-il une version d'essai disponible ?

 A3 : Oui, vous pouvez explorer les capacités d'Aspose.3D en téléchargeant la version d'essai gratuite[ici](https://releases.aspose.com/).

### Q4 : Où puis-je trouver le soutien et les discussions de la communauté ?

 A4 : Rejoignez la communauté Aspose.3D sur[Forums Aspose.3D](https://forum.aspose.com/c/3d/18) pour du soutien et des discussions.

### Q5 : Comment puis-je obtenir une licence temporaire pour Aspose.3D ?

 A5 : Vous pouvez obtenir une licence temporaire[ici](https://purchase.aspose.com/temporary-license/) à des fins d’évaluation.