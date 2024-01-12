---
title: Chargement et sauvegarde - Conversion de matériaux non PBR en PBR
linktitle: Chargement et sauvegarde - Conversion de matériaux non PBR en PBR
second_title: API Aspose.3D .NET
description: Explorez Aspose.3D pour .NET - Convertissez sans effort des matériaux non-PBR en PBR. Tutoriel complet et API puissante.
type: docs
weight: 16
url: /fr/net/loading-and-saving/non-pbr-to-pbr-material-conversion/
---
## Introduction

Bienvenue dans ce guide étape par étape sur l'utilisation d'Aspose.3D pour .NET pour convertir des matériaux non PBR (rendu physique) en matériaux PBR. Aspose.3D est une API puissante qui permet aux développeurs de travailler de manière transparente avec les formats de fichiers 3D dans leurs applications .NET.

## Conditions préalables

Avant de plonger dans le didacticiel, assurez-vous de disposer des prérequis suivants :

- Aspose.3D pour .NET : assurez-vous que la bibliothèque Aspose.3D pour .NET est installée. Vous pouvez trouver le lien de téléchargement[ici](https://releases.aspose.com/3d/net/).

- Compréhension de base de C# : ce didacticiel suppose que vous possédez une compréhension fondamentale de la programmation C#.

- IDE (Integrated Development Environment) : choisissez votre IDE préféré pour le développement .NET, tel que Visual Studio.

## Importer des espaces de noms

Dans votre code C#, commencez par importer les espaces de noms nécessaires :

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
```

## Étape 1 : initialiser une nouvelle scène 3D

Commencez par créer une nouvelle scène 3D en utilisant le code suivant :

```csharp
// ExStart : Non_PBRtoPBRMaterial
// initialiser une nouvelle scène 3D
var scene = new Scene();
```

## Étape 2 : Créer un objet 3D

Créez ensuite un objet 3D, par exemple une boîte :

```csharp
var box = new Box();
scene.RootNode.CreateChildNode("box1", box).Material = new PhongMaterial() { DiffuseColor = new Vector3(1, 0, 1) };
```

## Étape 3 : Configurer la conversion des matériaux

Configurez les options de conversion de matériaux pour la conversion non-PBR en PBR :

```csharp
GltfSaveOptions options = new GltfSaveOptions(FileFormat.GLTF2);
options.MaterialConverter = delegate (Material material)
{
    PhongMaterial phongMaterial = (PhongMaterial)material;
    return new PbrMaterial() { Albedo = new Vector3(phongMaterial.DiffuseColor.x, phongMaterial.DiffuseColor.y, phongMaterial.DiffuseColor.z) };
};
```

## Étape 4 : Enregistrer au format GLTF 2.0

Enregistrez la scène convertie au format GLTF 2.0 :

```csharp
scene.Save("Your Output Directory" + "Non_PBRtoPBRMaterial_Out.gltf", options);
// ExEnd : Non_PBRtoPBRMaterial
```

Répétez ces étapes si nécessaire pour votre cas d'utilisation spécifique, en vous assurant que chaque détail est correctement configuré.

## Conclusion

Toutes nos félicitations! Vous avez appris avec succès comment convertir des matériaux non-PBR en PBR à l'aide d'Aspose.3D pour .NET. Cet outil puissant ouvre des possibilités infinies pour la manipulation graphique 3D dans vos applications .NET.

## FAQ

### Q1 : Aspose.3D est-il compatible avec tous les formats de fichiers 3D ?

A1 : Oui, Aspose.3D prend en charge une large gamme de formats de fichiers 3D, offrant ainsi une flexibilité à vos projets.

### Q2 : Puis-je utiliser Aspose.3D pour des applications commerciales ?

 A2 : Absolument ! Aspose.3D est un produit commercial et vous pouvez l'acheter[ici](https://purchase.aspose.com/buy).

### Q3 : Ai-je besoin d’une licence temporaire pour tester ?

 A3 : Oui, vous pouvez obtenir une licence temporaire à des fins de test[ici](https://purchase.aspose.com/temporary-license/).

### Q4 : Où puis-je trouver de l'assistance pour Aspose.3D ?

 A4 : Visitez le[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) pour le soutien et les discussions de la communauté.

### Q5 : Existe-t-il un essai gratuit ?

 A5 : Oui, vous pouvez explorer une version d'essai gratuite[ici](https://releases.aspose.com/).