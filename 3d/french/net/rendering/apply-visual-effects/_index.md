---
title: Application d'effets visuels dans les fenêtres 3D
linktitle: Application d'effets visuels dans les fenêtres 3D
second_title: API Aspose.3D .NET
description: Explorez le monde de la visualisation 3D avec Aspose.3D pour .NET. Apprenez à appliquer des effets visuels captivants à vos scènes à l'aide de didacticiels étape par étape. Améliorez vos projets avec des effets de pixellisation, de niveaux de gris, de détection des contours et de flou.
weight: 10
url: /fr/net/rendering/apply-visual-effects/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Application d'effets visuels dans les fenêtres 3D

## Introduction

Améliorer l'attrait visuel des scènes 3D est un aspect crucial de la création d'expériences immersives. Aspose.3D pour .NET fournit un ensemble d'outils puissants pour appliquer des effets visuels aux fenêtres 3D. Dans ce didacticiel, nous expliquerons le processus d'application de divers effets à une scène 3D, notamment la pixellisation, les niveaux de gris, la détection des contours et le flou.

## Conditions préalables

Avant de plonger dans le didacticiel, assurez-vous d'avoir les éléments suivants :

- Une connaissance pratique du développement C# et .NET.
-  Aspose.3D pour la bibliothèque .NET installée. Vous pouvez le télécharger depuis[ici](https://releases.aspose.com/3d/net/).
- Un fichier de scène 3D (par exemple, "scene.obj") pour l'expérimentation.

## Importer des espaces de noms

Pour commencer, importez les espaces de noms nécessaires pour Aspose.3D et d'autres dépendances. Ajoutez les lignes suivantes à votre code :

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

```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("scene.obj"));
```

 Chargez votre scène 3D à l'aide du`Scene` classe.

## Étape 2 : Créer une caméra

```csharp
Camera camera = new Camera();
scene.RootNode.CreateChildNode("camera", camera).Transform.Translation = new Vector3(2, 44, 66);
camera.LookAt = new Vector3(50, 12, 0);
```

Créez une instance de caméra et définissez sa position et sa cible.

## Étape 3 : ajouter de la lumière à la scène

```csharp
scene.RootNode.CreateChildNode("light", new Light() { Color = new Vector3(Color.White), LightType = LightType.Point }).Transform.Translation = new Vector3(26, 57, 43);
```

Introduisez un éclairage pour améliorer les effets visuels.

## Étape 4 : Créer un moteur de rendu et une cible de rendu

```csharp
using (var renderer = Renderer.CreateRenderer())
{
    // Configurer les paramètres du moteur de rendu
    renderer.EnableShadows = false;

    // Créer une cible de rendu
    using (IRenderTexture rt = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(), 1, 1024, 1024))
    {
        // Configurer la fenêtre
        Viewport vp = rt.CreateViewport(camera, new RelativeRectangle() { ScaleWidth = 1, ScaleHeight = 1 });

        // Rendre la scène en texture
        renderer.Render(rt);

        // Enregistrer la texture rendue dans un fichier
        ((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "Original_viewport_out.png", ImageFormat.Png);

        // Continuez avec les effets de post-traitement...
    }
}
```

Créez un moteur de rendu et une cible de rendu pour capturer la scène.

## Étape 5 : appliquer des effets de post-traitement

### Étape 5.1 Effet de pixellisation

```csharp
// Créer un effet de pixellisation
PostProcessing pixelation = renderer.GetPostProcessing("pixelation");
renderer.PostProcessings.Add(pixelation);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_pixelation_out.png", ImageFormat.Png);
```

Appliquez un effet de pixellisation et enregistrez le résultat.

### Étape 5.2 Effet en niveaux de gris

```csharp
// Créer un effet de niveaux de gris
PostProcessing grayscale = renderer.GetPostProcessing("grayscale");
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(grayscale);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_grayscale_out.png", ImageFormat.Png);
```

Appliquez un effet de niveaux de gris et enregistrez le résultat.

### Étape 5.3 Combiner les effets

```csharp
// Combinez les effets de niveaux de gris et de pixellisation
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(grayscale);
renderer.PostProcessings.Add(pixelation);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_grayscale+pixelation_out.png", ImageFormat.Png);
```

Combinez plusieurs effets pour des résultats uniques.

### Étape 5.4 Effet de détection des bords

```csharp
// Créer un effet de détection de contour
PostProcessing edgedetection = renderer.GetPostProcessing("edge-detection");
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(edgedetection);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_edgedetection_out.png", ImageFormat.Png);
```

Appliquez l'effet de détection de bord et enregistrez le résultat.

### Étape 5.5 Effet de flou

```csharp
// Créer un effet de flou
PostProcessing blur = renderer.GetPostProcessing("blur");
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(blur);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_blur_out.png", ImageFormat.Png);
```

Appliquez un effet de flou et enregistrez le résultat.

## Conclusion

Expérimenter des effets visuels dans les fenêtres 3D ajoute de la profondeur et de la créativité à vos scènes. Aspose.3D pour .NET simplifie ce processus, offrant une gamme d'effets de post-traitement pour élever vos projets.

## FAQ

### Q1 : Puis-je appliquer plusieurs effets simultanément ?

A1 : Oui, vous pouvez combiner différents effets de post-traitement pour obtenir des résultats uniques et complexes.

### Q2 : Comment puis-je ajuster l’intensité des effets visuels ?

A2 : Chaque effet peut avoir des paramètres que vous pouvez modifier pour contrôler son intensité. Reportez-vous à la documentation pour plus de détails.

### Q3 : Aspose.3D est-il adapté au développement de jeux ?

R3 : Bien qu'Aspose.3D soit principalement conçu pour la modélisation et le rendu 3D, il peut être utilisé dans certains aspects du développement de jeux.

### Q4 : Des effets de post-traitement supplémentaires sont-ils disponibles ?

A4 : Aspose.3D fournit une variété d'effets de post-traitement intégrés et vous pouvez créer des effets personnalisés à l'aide de la bibliothèque.

### Q5 : Puis-je utiliser Aspose.3D pour des projets commerciaux ?

 A5 : Oui, vous pouvez utiliser Aspose.3D à des fins commerciales. Se référer au[page d'achat](https://purchase.aspose.com/buy) pour les détails de la licence.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
