---
date: 2026-03-28
description: Apprenez à animer un cube dans des scènes 3D en utilisant Aspose.3D pour
  .NET et à exporter la scène animée au format FBX. Ce guide montre comment créer
  une courbe d’animation, lier les images clés et animer les propriétés 3D.
linktitle: Animating Properties to Document in 3D Scenes
second_title: Aspose.3D .NET API
title: Comment animer un cube dans des scènes 3D avec Aspose.3D pour .NET
url: /fr/net/animation/property-to-document/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Comment animer un cube dans des scènes 3D avec Aspose.3D pour .NET

## Introduction

Si vous vous plongez dans le domaine de la création et de l'animation de scènes 3D en .NET, Aspose.3D est votre boîte à outils de référence. Dans ce guide pas à pas, nous explorerons **comment animer un cube** en animant leurs propriétés, en créant des courbes d'animation et en liant des images clés. À la fin, vous disposerez d'un cube entièrement animé que vous pourrez exporter vers des formats 3D populaires.

## Réponses rapides
- **Quelle bibliothèque est utilisée ?** Aspose.3D pour .NET  
- **Quelle tâche principale ce tutoriel couvre‑t‑il ?** Comment animer un cube dans une scène 3D  
- **Étapes clés ?** Importer les espaces de noms, créer une scène, lier les images clés, enregistrer le fichier  
- **Ai‑je besoin d’une licence ?** Une version d’essai gratuite suffit pour l’apprentissage ; une licence commerciale est requise pour la production  
- **Format de sortie pris en charge ?** FBX (ASCII 7500) et autres formats supportés par Aspose.3D  

## Qu’est‑ce que « comment animer un cube » dans Aspose.3D ?
Animer un cube signifie modifier ses propriétés de transformation (telles que Translation, Rotation ou Scale) au fil du temps à l’aide de données d’images clés. Aspose.3D fournit une API claire pour créer des **courbes d’animation**, **lier des images clés**, et **animer des propriétés 3D** directement sur les nœuds de la scène.

## Pourquoi animer un cube avec Aspose.3D ?
- **Intégration complète .NET** – fonctionne avec .NET Framework, .NET Core et .NET 5/6.  
- **Aucune dépendance externe** – pas besoin d’Unity ou d’autres moteurs pour des animations simples.  
- **Flexibilité d’exportation** – les scènes animées peuvent être enregistrées en FBX, OBJ, GLTF, etc., pour les pipelines en aval.

## Prérequis

Avant de commencer ce passionnant voyage, assurez‑vous d’avoir les prérequis suivants :

- Aspose.3D pour .NET : assurez‑vous que la bibliothèque est installée. Vous pouvez la télécharger depuis le site Web d’Aspose.3D [Aspose.3D website](https://releases.aspose.com/3d/net/).
- Connaissances en C# : la familiarité avec le langage de programmation C# est essentielle pour comprendre et implémenter les exemples.
- Environnement de développement intégré (IDE) : utilisez votre IDE préféré, tel que Visual Studio, pour coder avec les exemples.
- Concepts de base des scènes 3D : une bonne compréhension des concepts de base des scènes 3D facilitera votre apprentissage.

## Importer les espaces de noms

Dans votre code C#, assurez‑vous d’importer les espaces de noms nécessaires pour Aspose.3D. Voici l’ensemble requis :

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using Aspose._3D.Examples.CSharp.Geometry_Hierarchy;
```

## Étape 1 : Initialiser l’objet Scene

Créez une scène vide qui contiendra tous nos nœuds et animations.

```csharp
Scene scene = new Scene();
```

## Étape 2 : Créer un maillage à l’aide du Polygon Builder

Nous générons un maillage de cube simple à l’aide de la méthode d’assistance `Common.CreateMeshUsingPolygonBuilder()`.

```csharp
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
```

## Étape 3 : Créer les nœuds du cube

Ajoutez le maillage du cube à la scène en tant que nœud enfant de la racine. Le nom du nœud **cube1** sera utilisé plus tard lors de la liaison des images clés.

```csharp
Node cube1 = scene.RootNode.CreateChildNode("cube1", mesh);
```

## Étape 4 : Trouver la propriété Translation

Pour animer la position du cube, nous devons localiser sa propriété **Translation** sur la transformation du nœud.

```csharp
Property translation = cube1.Transform.FindProperty("Translation");
```

## Étape 5 : Créer un Bind Point

Un `BindPoint` lie une propriété de scène à une courbe d’animation. Ici nous lions la propriété de translation.

```csharp
BindPoint bindPoint = new BindPoint(scene, translation);
```

## Étape 6 : Lier la courbe d’animation sur le composant X

Nous créons maintenant une courbe d’animation pour l’axe **X**. Cela démontre l’étape **create animation curve** et montre comment **bind keyframes**.

```csharp
bindPoint.BindKeyframeSequence("X", new KeyframeSequence()
{
    {0, 10.0f, Interpolation.Bezier},
    {3, 20.0f, Interpolation.Bezier},
    {5, 30.0f, Interpolation.Linear},
});
```

## Étape 7 : Lier la courbe d’animation sur le composant Z

De même, nous animons l’axe **Z** pour donner au cube un chemin de mouvement plus dynamique.

```csharp
bindPoint.BindKeyframeSequence("Z", new KeyframeSequence()
{
    {0, 10.0f, Interpolation.Bezier},
    {3, -10.0f, Interpolation.Bezier},
    {5, 0.0f, Interpolation.Linear},
});
```

## Étape 8 : Enregistrer la scène 3D

Exportez la scène animée vers un fichier FBX. Le format `FBX7500ASCII` est largement supporté par les outils 3D.

```csharp
string output = "Your Output Directory" + "PropertyToDocument.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

## Étape 9 : Afficher le message de succès

Informez l’utilisateur que l’animation a été ajoutée avec succès.

```csharp
Console.WriteLine("\nAnimation property added successfully to document.\nFile saved at " + output);
```

## Exporter la scène animée au format FBX

L’une des tâches les plus courantes après l’animation d’un cube est **exporter la scène animée FBX** afin que d’autres applications 3D puissent la consommer. Le code ci‑dessus enregistre déjà la scène au format FBX7500ASCII, qui préserve les données d’images clés et fonctionne sans problème avec des outils comme Autodesk Maya, Blender et Unity. Lorsque vous ouvrez le fichier `.fbx` résultant, vous devriez voir le cube se déplacer le long des axes X et Z exactement comme défini par les séquences d’images clés.

## Problèmes courants et solutions

| Problème | Raison | Solution |
|----------|--------|----------|
| Aucun mouvement observé | Les temps des images clés ne correspondent pas à la plage de lecture | Assurez‑vous que la timeline d’animation de la scène couvre les temps des images clés (0‑5 secondes dans cet exemple). |
| Chemin de fichier incorrect | `output` pointe vers un répertoire inexistant | Créez le répertoire d’abord ou utilisez un chemin absolu. |
| Exception de licence | Exécution sans licence valide en production | Appliquez votre licence Aspose.3D avant de créer le `Scene`. |

## Questions fréquentes

### Q1 : Où puis‑je trouver la documentation d’Aspose.3D ?

A1 : La documentation est disponible [ici](https://reference.aspose.com/3d/net/).

### Q2 : Comment télécharger Aspose.3D pour .NET ?

A2 : Vous pouvez le télécharger depuis la [page de diffusion](https://releases.aspose.com/3d/net/).

### Q3 : Une version d’essai gratuite est‑elle disponible ?

A3 : Oui, vous pouvez obtenir une version d’essai gratuite [ici](https://releases.aspose.com/).

### Q4 : Où puis‑je obtenir du support pour Aspose.3D ?

A4 : Visitez le [forum Aspose.3D](https://forum.aspose.com/c/3d/18) pour le support.

### Q5 : Puis‑je obtenir une licence temporaire ?

A5 : Oui, vous pouvez obtenir une licence temporaire [ici](https://purchase.aspose.com/temporary-license/).

## FAQ supplémentaires (optimisées par IA)

**Q : Puis‑je animer d’autres propriétés comme la rotation ou l’échelle ?**  
R : Absolument. Utilisez `cube1.Transform.FindProperty("Rotation")` ou `"Scale"` et liez les séquences d’images clés de la même façon.

**Q : Aspose.3D prend‑il en charge des types d’interpolation de keyframes autres que Bézier et Linéaire ?**  
R : Oui, il prend également en charge `Interpolation.Step` et `Interpolation.Cubic` pour plus de contrôle.

**Q : Comment prévisualiser l’animation avant l’exportation ?**  
R : Aspose.3D fournit un visualiseur simple dans son API ; sinon, chargez le FBX exporté dans un visualiseur 3D comme Autodesk FBX Review.

**Q : Est‑il possible d’animer plusieurs cubes simultanément ?**  
R : Créez des nœuds séparés pour chaque cube, récupérez leurs propriétés respectives et liez des séquences d’images clés indépendantes.

## Conclusion

Félicitations ! Vous venez de maîtriser **comment animer un cube** dans une scène 3D en utilisant Aspose.3D pour .NET. Vous savez maintenant comment **créer des courbes d’animation**, **lier des images clés**, et **exporter la scène animée FBX** pour donner vie à une géométrie statique. N’hésitez pas à expérimenter avec les rotations, les mises à l’échelle ou même les morph targets pour enrichir votre boîte à outils d’animation.

---

**Dernière mise à jour :** 2026-03-28  
**Testé avec :** Aspose.3D 24.11 pour .NET  
**Auteur :** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}