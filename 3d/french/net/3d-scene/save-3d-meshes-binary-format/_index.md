---
title: Enregistrement de maillages 3D au format binaire personnalisé
linktitle: Enregistrement de maillages 3D au format binaire personnalisé
second_title: API Aspose.3D .NET
description: Explorez le monde de la 3D avec Aspose.3D pour .NET. Apprenez à enregistrer des maillages au format binaire personnalisé.
weight: 13
url: /fr/net/3d-scene/save-3d-meshes-binary-format/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Enregistrement de maillages 3D au format binaire personnalisé

## Introduction

Bienvenue dans le monde d'Aspose.3D pour .NET, une bibliothèque puissante qui permet aux développeurs de travailler sans effort avec des fichiers 3D. Dans ce didacticiel, nous aborderons le processus d'enregistrement des maillages 3D dans un format binaire personnalisé à l'aide d'Aspose.3D pour .NET. Ce guide suppose que vous avez une compréhension de base de C# et que vous êtes familier avec la bibliothèque Aspose.3D.

## Conditions préalables

Avant de passer au didacticiel, assurez-vous d'avoir les éléments suivants en place :

-  Aspose.3D pour .NET : assurez-vous que la bibliothèque Aspose.3D est installée. Vous pouvez le télécharger depuis[ici](https://releases.aspose.com/3d/net/).

- Environnement de développement : configurez votre environnement de développement C# préféré, tel que Visual Studio.

- Fichier 3D d'entrée : disposez d'un fichier 3D (par exemple, test.fbx) que vous souhaitez convertir dans un format binaire personnalisé.

## Importer des espaces de noms

Dans votre code C#, incluez les espaces de noms nécessaires pour accéder aux fonctionnalités Aspose.3D :

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
```

## Étape 1 : Charger un fichier 3D

Chargez votre fichier 3D à l'aide d'Aspose.3D. Dans cet exemple, nous chargeons un fichier nommé "test.fbx" :

```csharp
Scene scene = Scene.FromFile("test.fbx");
```

## Étape 2 : Définir un format binaire personnalisé

Définissez la structure du format binaire personnalisé dans lequel vous souhaitez enregistrer vos maillages 3D. L'exemple utilise une structure avec MeshBlock, Vertex et Triangle comme composants.

```csharp
// La disposition de la mémoire d'un sommet est
// position flottante[3] ;
// flotteur[3] normal ;
// flotteur[3] uv;
var vertexDeclaration = new VertexDeclaration();
vertexDeclaration.AddField(VertexFieldDataType.FVector3, VertexFieldSemantic.Position);
vertexDeclaration.AddField(VertexFieldDataType.FVector3, VertexFieldSemantic.Normal);
vertexDeclaration.AddField(VertexFieldDataType.FVector3, VertexFieldSemantic.UV);

```

## Étape 3 : Ouvrir le fichier pour l'écriture

Ouvrez un fichier binaire en écriture, où les maillages 3D convertis seront enregistrés :

```csharp
using (var writer = new BinaryWriter(new FileStream("Your Output Directory" + "Save3DMeshesInCustomBinaryFormat_out", FileMode.Create, FileAccess.Write)))
```

## Étape 4 : Parcourir les nœuds et les entités

Visitez chaque nœud de la scène 3D et convertissez les entités de maillage au format binaire personnalisé. Ignorez les lumières, les caméras et autres entités non maillées :

```csharp
scene.RootNode.Accept(delegate(Node node)
{
    foreach (Entity entity in node.Entities)
    {
        if (!(entity is IMeshConvertible))
            continue;
        // ... (continuer le traitement)
    }
    return true;
});
```

## Étape 5 : Convertir et écrire des points de contrôle et des triangles

Pour chaque entité maillée, convertissez les points de contrôle en espace mondial et écrivez-les dans le fichier binaire avec les indices triangulaires :

```csharp
Mesh m = ((IMeshConvertible)entity).ToMesh();

var triMesh = TriMesh.FromMesh(vertexDeclaration, m);


//La disposition de la mémoire du maillage est :
// float[16] transform_matrix;
// int nombre_nombre de sommets ;
// int indices_count;
// sommet[vertices_count] sommets ;
// indices ushort[indices_count] ;


//écrire une transformation
var transform = node.GlobalTransform.TransformMatrix.ToArray();
for(int i = 0; i < transform.Length; i++)
    writer.Write((float)transform[i]);
//écrire le nombre de sommets/indices
writer.Write(triMesh.VerticesCount);
writer.Write(triMesh.IndicesCount);
//écrire des sommets et des indices
writer.Flush();
triMesh.WriteVerticesTo(writer.BaseStream);
triMesh.Write16bIndicesTo(writer.BaseStream);

```

## Conclusion

Dans ce didacticiel, nous avons couvert le processus d'enregistrement des maillages 3D dans un format binaire personnalisé à l'aide d'Aspose.3D pour .NET. Cette puissante bibliothèque fournit aux développeurs les outils nécessaires pour manipuler les fichiers 3D de manière transparente. Expérimentez avec différents formats et paramètres pour libérer tout le potentiel d'Aspose.3D dans vos projets.

## FAQ

### Q1 : Puis-je utiliser Aspose.3D pour .NET avec d’autres langages de programmation ?

A1 : Aspose.3D prend principalement en charge les langages .NET, mais vous pouvez explorer les options de compatibilité pour d'autres langages.

### Q2 : Où puis-je trouver des exemples et des ressources supplémentaires ?

 A2 : Le[Forum Aspose.3D](https://forum.aspose.com/c/3d/18)est un excellent endroit pour trouver du soutien, des exemples et interagir avec la communauté.

### Q3 : Existe-t-il une version d’essai disponible pour Aspose.3D ?

 A3 : Oui, vous pouvez bénéficier d'un essai gratuit auprès de[ici](https://releases.aspose.com/).

### Q4 : Comment puis-je obtenir une licence temporaire pour Aspose.3D ?

 A4 : Visite[ce lien](https://purchase.aspose.com/temporary-license/) pour obtenir une licence temporaire à des fins de test.

### Q5 : Puis-je acheter Aspose.3D pour .NET ?

 A5 : Oui, vous pouvez acheter Aspose.3D sur le site[page d'achat](https://purchase.aspose.com/buy).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
