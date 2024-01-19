---
title: Exportation d'une scène 3D au format AMF compressé
linktitle: Exportation d'une scène 3D au format AMF compressé
second_title: API Aspose.3D .NET
description: Découvrez comment exporter des scènes 3D au format AMF compressé à l'aide d'Aspose.3D pour .NET. Améliorez vos compétences de développement avec ce guide étape par étape.
type: docs
weight: 11
url: /fr/net/3d-scene/export-scene-compressed-amf/
---
## Introduction

Dans le monde dynamique de la modélisation et du rendu 3D, l’efficacité et la flexibilité sont primordiales. Aspose.3D pour .NET permet aux développeurs d'exporter de manière transparente des scènes 3D au format compressé AMF (Additive Manufacturing File), garantissant une taille de fichier optimale sans compromettre la qualité. Ce didacticiel vous guidera tout au long du processus étape par étape, permettant ainsi aux développeurs débutants et expérimentés d'exploiter facilement les capacités d'Aspose.3D pour .NET.

## Conditions préalables

Avant de plonger dans le didacticiel, assurez-vous d'avoir les prérequis suivants :

- Compréhension de base des concepts de modélisation 3D
- Visual Studio installé sur votre machine
-  Aspose.3D pour la bibliothèque .NET. Vous pouvez le télécharger[ici](https://releases.aspose.com/3d/net/)
- Une envie de valoriser vos compétences en développement 3D !

## Importer des espaces de noms

Dans votre projet, assurez-vous d'importer les espaces de noms nécessaires pour exploiter les fonctionnalités d'Aspose.3D pour .NET :

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```

## Étape 1 : Charger une scène 3D

Commencez par charger une scène 3D à l’aide d’Aspose.3D pour .NET. Créez un objet de scène et ajoutez-y des entités telles que des boîtes :

```csharp
Scene scene = new Scene();
var box = new Box();
var tr = scene.RootNode.CreateChildNode(box).Transform;
tr.Scale = new Vector3(12, 12, 12);
tr.Translation = new Vector3(10, 0, 0);
```

## Étape 2 : Transformation à l'échelle

Ensuite, appliquez une transformation d'échelle à une autre case de la scène :

```csharp
tr = scene.RootNode.CreateChildNode(box).Transform;
tr.Scale = new Vector3(5, 5, 5);
```

## Étape 3 : Définir les angles d'Euler

Définissez les angles d'Euler pour la transformation :

```csharp
tr.EulerAngles = new Vector3(50, 10, 0);
```

## Étape 4 : Créer des nœuds enfants

Continuez à construire la scène en créant des nœuds enfants :

```csharp
scene.RootNode.CreateChildNode();
scene.RootNode.CreateChildNode().CreateChildNode(box);
scene.RootNode.CreateChildNode().CreateChildNode(box);
```

## Étape 5 : Enregistrer le fichier AMF compressé

Enfin, enregistrez la scène 3D dans un fichier AMF compressé dans le répertoire de sortie souhaité :

```csharp
scene.Save("Your Output Directory" + "Aspose.amf", new AmfSaveOptions() { EnableCompression = false });
```

## Conclusion

Toutes nos félicitations! Vous avez exporté avec succès une scène 3D au format AMF compressé à l'aide d'Aspose.3D pour .NET. Cette puissante bibliothèque ouvre un monde de possibilités aux développeurs 3D, leur permettant de créer des modèles efficaces et visuellement époustouflants.

## FAQ

### Q1 : Aspose.3D est-il compatible avec les logiciels de modélisation 3D populaires ?

A1 : Aspose.3D prend en charge différents formats de fichiers, ce qui le rend compatible avec les outils de modélisation 3D populaires.

### Q2 : Puis-je activer la compression pour d’autres formats de fichiers que l’AMF ?

A2 : Oui, Aspose.3D fournit des options pour activer la compression pour différents formats de fichiers.

### Q3 : Aspose.3D convient-il aussi bien aux développeurs débutants qu’avancés ?

A3 : Absolument ! Aspose.3D offre de la simplicité pour les débutants et des fonctionnalités avancées pour les développeurs chevronnés.

### Q4 : Existe-t-il des limitations sur la taille des scènes 3D pouvant être exportées ?

A4 : Aspose.3D est conçu pour gérer des scènes de complexité variable et il n'y a pas de limitations de taille strictes.

### Q5 : Où puis-je trouver du soutien supplémentaire et des discussions communautaires ?

A5 : Visitez le[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) pour du soutien et des discussions.