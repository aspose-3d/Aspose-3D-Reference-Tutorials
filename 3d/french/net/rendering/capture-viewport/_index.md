---
title: Capturer des fenêtres dans des scènes 3D
linktitle: Capturer des fenêtres dans des scènes 3D
second_title: API Aspose.3D .NET
description: Apprenez à capturer de superbes fenêtres 3D à l'aide d'Aspose.3D pour .NET. Guide étape par étape pour rendre des scènes avec flexibilité.
weight: 11
url: /fr/net/rendering/capture-viewport/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Capturer des fenêtres dans des scènes 3D

## Introduction

Dans le domaine des graphiques et de la visualisation 3D, la capture de fenêtres est une compétence essentielle qui améliore la profondeur et les détails de vos scènes. Aspose.3D pour .NET fournit une solution robuste pour le rendu et la manipulation de scènes 3D. Ce didacticiel vous guidera tout au long du processus de capture de fenêtres dans des scènes 3D à l'aide d'Aspose.3D, vous permettant de créer facilement des visualisations époustouflantes.

## Conditions préalables

Avant de plonger dans le didacticiel, assurez-vous que les conditions préalables suivantes sont remplies :

-  Aspose.3D pour la bibliothèque .NET : assurez-vous que la bibliothèque Aspose.3D est installée. Vous pouvez le télécharger depuis[ici](https://releases.aspose.com/3d/net/).

## Importer des espaces de noms

Pour commencer, importez les espaces de noms nécessaires dans votre projet .NET :

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using System.Drawing;
using System.Drawing.Imaging;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Render;
using Aspose.ThreeD.Utilities;
```

## Étape 1 : Charger une scène 3D existante

Commencez par charger une scène 3D existante dans votre projet. L'extrait de code suivant le démontre :

```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("scene.obj"));
```

## Étape 2 : Créer une caméra

Ensuite, créez une instance de la caméra et définissez sa position et sa cible :

```csharp
Camera camera = new Camera();
scene.RootNode.CreateChildNode("camera", camera).Transform.Translation = new Vector3(2, 44, 66);
camera.LookAt = new Vector3(50, 12, 0);
```

## Étape 3 : ajouter de l'éclairage à la scène

Améliorez votre scène en ajoutant une source de lumière. L'extrait de code ci-dessous montre comment créer un point lumineux :

```csharp
scene.RootNode.CreateChildNode("light", new Light() { Color = new Vector3(Color.White), LightType = LightType.Point }).Transform.Translation = new Vector3(26, 57, 43);
```

## Étape 4 : Configurer le moteur de rendu et la cible de rendu

Configurez le moteur de rendu et créez une cible de rendu pour capturer la scène :

```csharp
using (var renderer = Renderer.CreateRenderer())
{
    renderer.EnableShadows = false;

    using (IRenderTexture rt = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(), 1, 1024, 1024))
    {
        // ... (suite dans les prochaines étapes)
    }
}
```

## Étape 5 : Définir les fenêtres et le rendu

Définissez les fenêtres et effectuez le rendu de la scène pour générer des images de sortie :

```csharp
Viewport vp = rt.CreateViewport(camera, new RelativeRectangle() { ScaleWidth = 1, ScaleHeight = 1 });
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "file-1viewports_out.png", ImageFormat.Png);
```

## Étape 6 : modifier les fenêtres et effectuer à nouveau le rendu

Modifiez les fenêtres et restituez la scène une fois de plus, démontrant la flexibilité d'Aspose.3D :

```csharp
vp.Area = new RelativeRectangle() { ScaleWidth = 0.5f, ScaleHeight = 1 };
rt.CreateViewport(camera, new RelativeRectangle() { ScaleX = 0.5f, ScaleWidth = 0.5f, ScaleHeight = 1 });
camera.FieldOfView = 90;
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "file-2viewports_out.png", ImageFormat.Png);
```

Continuez à expérimenter différentes configurations pour obtenir les effets visuels souhaités.

## Conclusion

Dans ce didacticiel, nous avons exploré le processus de capture de fenêtres dans des scènes 3D à l'aide d'Aspose.3D pour .NET. En tirant parti de ses puissantes fonctionnalités, vous pouvez élever vos projets graphiques 3D vers de nouveaux sommets, en offrant des expériences visuelles captivantes.

## FAQ

### Q1 : Aspose.3D est-il compatible avec d'autres formats de fichiers 3D ?

A1 : Oui, Aspose.3D prend en charge différents formats de fichiers 3D, garantissant ainsi la compatibilité avec une large gamme d'outils de conception.

### Q2 : Puis-je utiliser Aspose.3D pour le développement de jeux ?

A2 : Bien qu'Aspose.3D soit principalement conçu pour le graphisme et la visualisation, ses fonctionnalités peuvent compléter certains aspects du développement de jeux.

### Q3 : Où puis-je trouver des exemples et de la documentation supplémentaires ?

 A3 : Explorer l'ensemble[Documentation Aspose.3D](https://reference.aspose.com/3d/net/) pour plus d’exemples et d’informations détaillées.

### Q4 : Existe-t-il un essai gratuit ?

 A4 : Oui, vous pouvez accéder à un essai gratuit[ici](https://releases.aspose.com/).

### Q5 : Comment puis-je demander de l'aide ou participer à la communauté ?

 A5 : Rejoignez la communauté Aspose.3D sur le[forum d'entraide](https://forum.aspose.com/c/3d/18) pour votre aide et votre collaboration.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
