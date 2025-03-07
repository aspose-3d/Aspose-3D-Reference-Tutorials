---
title: Application de l'effet d'objectif Fisheye avec Aspose.3D pour .NET
linktitle: Application de l'effet d'objectif Fisheye à une scène 3D
second_title: API Aspose.3D .NET
description: Améliorez vos scènes 3D avec Aspose.3D pour .NET ! Apprenez à appliquer un effet d'objectif fisheye captivant, étape par étape. Télécharger maintenant!
weight: 12
url: /fr/net/rendering/fisheye-lens-effect-3d-scene/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Application de l'effet d'objectif Fisheye avec Aspose.3D pour .NET

## Introduction
Cherchez-vous à améliorer l’attrait visuel de vos scènes 3D ? Plongez dans le monde fascinant des effets d'objectif fisheye avec Aspose.3D pour .NET. Ce tutoriel vous guidera étape par étape sur la façon d'appliquer un effet d'objectif fisheye à vos scènes 3D, leur donnant une perspective unique et captivante.
## Conditions préalables
Avant de commencer, assurez-vous que les conditions préalables suivantes sont remplies :
-  Aspose.3D pour .NET : assurez-vous que la bibliothèque Aspose.3D pour .NET est installée. Sinon, vous pouvez le télécharger[ici](https://releases.aspose.com/3d/net/).
-  Exemple de scène 3D : nous travaillerons avec un exemple de fichier de scène 3D (VirtualCity.glb). Vous pouvez utiliser votre propre scène ou télécharger l'échantillon depuis le[Documentation Aspose.3D](https://reference.aspose.com/3d/net/).
## Importer des espaces de noms
Dans votre projet .NET, incluez les espaces de noms nécessaires pour accéder aux fonctionnalités Aspose.3D. Ajoutez les espaces de noms suivants au début de votre code :
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Render;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Drawing.Imaging;
using System.Linq;
using System.Text;
```
## Étape 1 : Charger la scène 3D
Chargez le fichier de scène 3D dans votre projet à l'aide du code suivant :
```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("VirtualCity.glb"));
```
## Étape 2 : configurer la caméra et les lumières
Créez une caméra et des lumières pour améliorer les aspects visuels de votre scène. Ajustez les paramètres tels que NearPlane, FarPlane et RotationMode selon vos besoins :
```csharp
Camera cam = new Camera(ProjectionType.Perspective)
{
    NearPlane = 0.1,
    FarPlane = 200,
    RotationMode = RotationMode.FixedDirection
};
scene.RootNode.CreateChildNode(cam).Transform.Translation = new Vector3(5, 6, 0);
scene.RootNode.CreateChildNode(new Light() { LightType = LightType.Point }).Transform.Translation = new Vector3(-10, 7, -10);
scene.RootNode.CreateChildNode(new Light() { Color = new Vector3(Color.CadetBlue) }).Transform.Translation = new Vector3(49, 0, 49);
```
## Étape 3 : Créer un moteur de rendu et des cibles de rendu
Configurez le moteur de rendu et créez des cibles de rendu pour la carte cubique et la texture 2D :
```csharp
using (var renderer = Renderer.CreateRenderer())
{
    IRenderTexture rt = renderer.RenderFactory.CreateCubeRenderTexture(new RenderParameters(false), 512, 512);
    IRenderTexture final = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(false, 32, 0, 0), 1024, 1024);
    rt.CreateViewport(cam, RelativeRectangle.FromScale(0, 0, 1, 1));
    renderer.Render(rt);
```
## Étape 4 : Appliquer l'effet d'objectif Fisheye
Exécutez le post-traitement de l'effet de lentille fisheye sur la carte cubique rendue :
```csharp
PostProcessing fisheye = renderer.GetPostProcessing("fisheye");
fisheye.FindProperty("fov").Value = 360.0;
fisheye.Input = rt.Targets[0];
renderer.Execute(fisheye, final);
((ITexture2D)final.Targets[0]).Save("Your Output Directory" + "fisheye.png", ImageFormat.Png);
```
## Conclusion
Toutes nos félicitations! Vous avez appliqué avec succès un effet d'objectif fisheye à votre scène 3D à l'aide d'Aspose.3D pour .NET. Expérimentez avec différentes scènes et paramètres pour libérer votre créativité.
## Questions fréquemment posées
### Puis-je appliquer l’effet fisheye à n’importe quelle scène 3D ?
Oui, vous pouvez appliquer l'effet fisheye à n'importe quelle scène 3D. Assurez-vous que la scène est correctement chargée et éclairée pour des résultats optimaux.
### Quelle est l’importance d’ajuster le champ de vision (fov) à 360 degrés ?
Un champ de vision de 360 degrés assure une projection sphérique complète, créant un superbe effet fisheye.
### Comment puis-je personnaliser l’éclairage de ma scène 3D ?
Vous pouvez ajuster les propriétés des lumières, telles que la position, le type et la couleur, pour obtenir les effets d'éclairage souhaités.
### a-t-il une limite à la taille de la scène 3D pouvant être traitée ?
La taille de la scène 3D est principalement limitée par les ressources système. Assurez-vous que votre matériel peut gérer la taille de votre scène.
### Puis-je utiliser un format de sortie différent du format PNG pour le résultat de l'effet fisheye ?
Oui, vous pouvez modifier le code pour enregistrer la sortie dans différents formats d'image en fonction de vos besoins.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
