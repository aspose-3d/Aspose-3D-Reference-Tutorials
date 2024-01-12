---
title: Conversion d'une primitive sphère en maillage
linktitle: Conversion d'une primitive sphère en maillage
second_title: API Aspose.3D .NET
description: Explorez Aspose.3D pour .NET et convertissez sans effort Sphere Mesh en Triangle Mesh avec une disposition de mémoire personnalisée. Suivez notre guide étape par étape pour une intégration transparente.
type: docs
weight: 16
url: /fr/net/objects/convert-sphere-primitive-to-mesh/
---
## Introduction
Cherchez-vous à exploiter la puissance d’Aspose.3D pour .NET pour convertir un maillage sphérique en maillage triangulaire avec une disposition de mémoire personnalisée ? Ce guide étape par étape vous guidera tout au long du processus, ce qui permettra même aux débutants de le suivre facilement. À la fin de ce didacticiel, vous comprendrez parfaitement comment y parvenir en utilisant Aspose.3D pour .NET.
## Conditions préalables
Avant de plonger dans le didacticiel, assurez-vous que les conditions préalables suivantes sont remplies :
- Connaissance de base de la programmation .NET.
- Aspose.3D pour la bibliothèque .NET installée. Vous pouvez le télécharger depuis le[Page de téléchargement d'Aspose.3D pour .NET](https://releases.aspose.com/3d/net/).
- Familiarité avec le langage de programmation C#.
## Importer des espaces de noms
Dans votre projet C#, assurez-vous d'importer les espaces de noms nécessaires pour exploiter la fonctionnalité Aspose.3D :
```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
```
## Étape 1 : initialiser l'objet de scène
```csharp
// Initialiser l'objet de scène
Scene scene = new Scene();
```
## Étape 2 : initialiser l'objet de classe de nœud
```csharp
// Initialiser l'objet de classe Node
Node cubeNode = new Node("sphere");
```
## Étape 3 : Convertir le maillage de sphère en TriMesh typé
```csharp
Mesh sphere = (new Sphere()).ToMesh();
var myMesh = TriMesh<MyVertex>.FromMesh(sphere);
```
## Étape 4 : Obtenez les données de sommet dans une structure personnalisée
```csharp
MyVertex[] vertex = myMesh.VerticesToTypedArray();
```
## Étape 5 : Obtenez des index 32 bits et 16 bits
```csharp
int[] indices32bit;
ushort[] indices16bit;
myMesh.IndicesToArray(out indices32bit);
myMesh.IndicesToArray(out indices16bit);
```
## Étape 6 : Écrire les données de sommet et d'index dans le flux de mémoire
```csharp
using (MemoryStream ms = new MemoryStream())
{
    myMesh.WriteVerticesTo(ms);
    myMesh.Write16bIndicesTo(ms);
    myMesh.Write32bIndicesTo(ms);
}
```
## Étape 7 : Pointer le nœud vers la géométrie du maillage
```csharp
cubeNode.Entity = sphere;
```
## Étape 8 : Ajouter un nœud à la scène
```csharp
scene.RootNode.ChildNodes.Add(cubeNode);
```
## Étape 9 : Enregistrer la scène 3D
```csharp
string output = "Your Output Directory" + "SphereToTriangleMeshCustomMemoryLayoutScene.fbx";
scene.Save(output, FileFormat.FBX7400ASCII);
```
## Étape 10 : Afficher les résultats
```csharp
Console.WriteLine("Indices = {0}, Actual vertices = {1}, vertices before merging = {2}", myMesh.IndicesCount, myMesh.VerticesCount, myMesh.UnmergedVerticesCount);
Console.WriteLine("Total bytes of vertices in memory {0}bytes", myMesh.VerticesSizeInBytes);
Console.WriteLine("\nConverted a Sphere mesh to a triangle mesh with a custom memory layout of the vertex successfully.\nFile saved at " + output);
```

## Exemple de code source MyVertex
```csharp
[StructLayout(LayoutKind.Sequential)]
struct MyVertex
{
	[Semantic(VertexFieldSemantic.Position)]
	FVector3 position;
	[Semantic(VertexFieldSemantic.Normal)]
	FVector3 normal;
}
```
## Conclusion
Toutes nos félicitations! Vous avez converti avec succès un maillage sphérique en maillage triangulaire avec une disposition de mémoire personnalisée à l'aide d'Aspose.3D pour .NET. Cette puissante bibliothèque offre un moyen transparent de manipuler des objets 3D dans vos applications .NET.
## FAQ
### Q : Puis-je utiliser Aspose.3D pour .NET avec d’autres frameworks .NET ?
R : Oui, Aspose.3D pour .NET est compatible avec divers frameworks .NET.
### Q : Où puis-je trouver une documentation détaillée pour Aspose.3D pour .NET ?
 R : Reportez-vous au[Aspose.3D pour la documentation .NET](https://reference.aspose.com/3d/net/) pour des informations détaillées.
### Q : Comment puis-je obtenir une licence temporaire pour Aspose.3D pour .NET ?
 Une visite[ce lien](https://purchase.aspose.com/temporary-license/) pour obtenir un permis temporaire.
### Q : Existe-t-il des exemples de projets disponibles pour Aspose.3D pour .NET ?
 R : Explorez la documentation Aspose.3D pour .NET et[Dépôt GitHub](https://github.com/aspose-3d/Aspose.3D-for-.NET) pour des exemples de projets.
### Q : Existe-t-il une communauté active pour la prise en charge d'Aspose.3D pour .NET ?
 R : Oui, rejoignez le[Forum Aspose.3D pour .NET](https://forum.aspose.com/c/3d/18) pour obtenir de l'aide de la communauté.