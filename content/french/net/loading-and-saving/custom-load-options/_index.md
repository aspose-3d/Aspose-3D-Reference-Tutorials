---
title: Chargement et sauvegarde - Options de chargement personnalisées
linktitle: Chargement et sauvegarde - Options de chargement personnalisées
second_title: API Aspose.3D .NET
description: Explorez Aspose.3D pour .NET, la solution ultime pour un chargement et une sauvegarde transparents de modèles 3D.
type: docs
weight: 15
url: /fr/net/loading-and-saving/custom-load-options/
---
## Introduction

Bienvenue dans le monde d'Aspose.3D pour .NET – une bibliothèque puissante qui permet aux développeurs de travailler de manière transparente avec des fichiers 3D. Dans ce didacticiel, nous aborderons les subtilités du chargement et de l'enregistrement de modèles 3D, en nous concentrant sur les options de chargement personnalisées. Que vous soyez un développeur chevronné ou un nouveau venu, ce guide vous guidera étape par étape tout au long du processus, vous garantissant ainsi d'exploiter tout le potentiel d'Aspose.3D pour .NET.

## Conditions préalables

Avant de nous lancer dans ce voyage, assurez-vous d’avoir les conditions préalables suivantes en place :

-  Aspose.3D pour .NET : assurez-vous que la bibliothèque est installée. Vous pouvez le télécharger[ici](https://releases.aspose.com/3d/net/).

- Répertoire de documents : créez un répertoire pour stocker vos fichiers de modèle 3D.

Maintenant que vous avez l’essentiel, plongeons dans le monde passionnant de la manipulation de modèles 3D !

## Importer des espaces de noms

Tout d’abord, importons les espaces de noms nécessaires. Cela préparera le terrain pour notre voyage dans le domaine Aspose.3D.

```csharp
using System;
using System.IO;
using System.Collections.Generic;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Formats;
```

## Chargement et sauvegarde - Options de chargement personnalisées

### Étape 1 : Chargement des fichiers Discreet3DS

```csharp
private static void Discreet3DSLoadOption()
{
    // Le chemin d'accès au répertoire des documents.
    string dataDir = "Your Document Directory";
    Discreet3dsLoadOptions loadOpts = new Discreet3dsLoadOptions();

    //Définir des options personnalisées
    loadOpts.ApplyAnimationTransform = true;
    loadOpts.FlipCoordinateSystem = true;
    loadOpts.GammaCorrectedColor = true;
    loadOpts.LookupPaths = new List<string>(new string[] { dataDir });
}
```

### Étape 2 : Chargement des fichiers OBJ

```csharp
private static void ObjLoadOption()
{
    // Le chemin d'accès au répertoire des documents.
    string dataDir = "Your Document Directory";
    ObjLoadOptions loadObjOpts = new ObjLoadOptions();

    //Définir des options personnalisées
    loadObjOpts.EnableMaterials = true;
    loadObjOpts.FlipCoordinateSystem = true;
    loadObjOpts.LookupPaths = new List<string>(new string[] { dataDir });
}
```

### Étape 3 : Chargement des fichiers STL

```csharp
private static void STLLoadOption()
{
    // Le chemin d'accès au répertoire des documents.
    string dataDir = "Your Document Directory";
    StlLoadOptions loadSTLOpts = new StlLoadOptions();

    //Définir des options personnalisées
    loadSTLOpts.FlipCoordinateSystem = true;
    loadSTLOpts.LookupPaths = new List<string>(new string[] { dataDir });
}
```

### Étape 4 : Chargement des fichiers U3D

```csharp
private static void U3DLoadOption()
{
    // Le chemin d'accès au répertoire des documents.
    string dataDir = "Your Document Directory";
    U3dLoadOptions loadU3DOpts = new U3dLoadOptions();

    //Définir des options personnalisées
    loadU3DOpts.FlipCoordinateSystem = true;
    loadU3DOpts.LookupPaths = new List<string>(new string[] { dataDir });
}
```

### Étape 5 : Chargement des fichiers glTF

```csharp
private static void glTFLoadOptions()
{
    // Le chemin d'accès au répertoire des documents.
    string dataDir = "Your Document Directory";
    Scene scene = new Scene();
    GltfLoadOptions loadOpt = new GltfLoadOptions();

    //Définir des options personnalisées
    loadOpt.FlipTexCoordV = true;
    scene.Open(dataDir + "Duck.gltf", loadOpt);
}
```

### Étape 6 : Chargement des fichiers PLY

```csharp
private static void PlyLoadOptions()
{
    // Le chemin d'accès au répertoire des documents.
    string dataDir = "Your Document Directory";
    Scene scene = new Scene();
    PlyLoadOptions loadPLYOpts = new PlyLoadOptions();

    //Définir des options personnalisées
    loadPLYOpts.FlipCoordinateSystem = true;
    scene.Open(RunExamples.GetDataFilePath("vase-v2.ply"), loadPLYOpts);
}
```

### Étape 7 : Chargement des fichiers FBX

```csharp
private static void FBXLoadOptions()
{
    // Le chemin d'accès au répertoire des documents.
    string dataDir = "Your Document Directory";
    Scene scene = new Scene();
    FbxLoadOptions opt = new FbxLoadOptions() { KeepBuiltinGlobalSettings = true };

    //Définir des options personnalisées
    scene.Open(dataDir + "test.FBX", opt);

    // Propriétés de sortie définies dans GlobalSettings dans le fichier FBX
    foreach (Property property in scene.RootNode.AssetInfo.Properties)
    {
        Console.WriteLine(property);
    }
}
```

## Conclusion

Toutes nos félicitations! Vous avez réussi à naviguer dans le monde complexe du chargement et de l'enregistrement de modèles 3D à l'aide d'Aspose.3D pour .NET. Ce didacticiel couvre différents formats de fichiers et leurs options de chargement personnalisées, vous permettant de manipuler facilement les ressources 3D.

## FAQ

### Q1 : Aspose.3D pour .NET convient-il aux débutants ?

A1 : Absolument ! Aspose.3D pour .NET fournit une interface conviviale, la rendant accessible aux développeurs de tous niveaux.

### Q2 : Puis-je utiliser Aspose.3D pour des projets commerciaux ?

A2 : Oui, Aspose.3D pour .NET est livré avec une licence commerciale, vous permettant de l'utiliser dans vos projets.

### Q3 : Existe-t-il des limitations sur les formats de fichiers pris en charge ?

 A3 : Aspose.3D pour .NET prend en charge un large éventail de formats de fichiers 3D populaires, notamment OBJ, STL, FBX, etc. Se référer au[Documentation](https://reference.aspose.com/3d/net/) pour une liste complète.

### Q4 : Existe-t-il une version d'essai disponible ?

A4 : Oui, vous pouvez explorer les capacités d'Aspose.3D pour .NET en téléchargeant le[essai gratuit](https://releases.aspose.com/).

### Q5 : Où puis-je demander de l'aide pour Aspose.3D pour .NET ?

 A5 : Visitez le[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) pour le soutien et l’assistance de la communauté.