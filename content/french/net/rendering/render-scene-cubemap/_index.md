---
title: Rendu de la scène dans Cubemap avec six faces
linktitle: Rendu de la scène dans Cubemap avec six faces
second_title: API Aspose.3D .NET
description: Créez de superbes cubesmaps avec Aspose.3D pour .NET. Suivez notre guide étape par étape pour restituer des scènes 3D en captivantes cubesmaps à six faces.
type: docs
weight: 14
url: /fr/net/rendering/render-scene-cubemap/
---
## Introduction
Bienvenue dans ce guide étape par étape sur le rendu d'une scène dans une carte cubique à six faces à l'aide d'Aspose.3D pour .NET. Dans ce didacticiel, nous vous guiderons tout au long du processus de création d'une superbe carte cubique en rendant une scène 3D. Aspose.3D est une puissante API .NET qui simplifie la manipulation graphique 3D, et avec ce guide, vous exploiterez ses capacités pour créer des cubemaps captivantes.
## Conditions préalables
Avant de plonger dans le didacticiel, assurez-vous que les conditions préalables suivantes sont remplies :
- Une connaissance pratique du développement C# et .NET.
-  Aspose.3D pour .NET installé. Vous pouvez le télécharger[ici](https://releases.aspose.com/3d/net/).
- Un fichier de scène 3D au format GLB (par exemple, "VirtualCity.glb") pour le rendu.
## Importer des espaces de noms
Commencez par importer les espaces de noms nécessaires pour Aspose.3D dans votre code C# :
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
## Étape 1 : Charger la scène
Chargez le fichier de scène 3D à l'aide du code suivant :
```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("VirtualCity.glb"));
```
## Étape 2 : Créer une caméra et des lumières
Créez une caméra et deux lumières pour éclairer la scène :
```csharp
Camera cam = new Camera(ProjectionType.Perspective)
{
    NearPlane = 0.1,
    FarPlane = 200,
    RotationMode = RotationMode.FixedDirection
};
scene.RootNode.CreateChildNode(cam).Transform.Translation = new Vector3(5, 6, 0);
scene.RootNode.CreateChildNode(new Light() { LightType = LightType.Point }).Transform.Translation = new Vector3(-10, 7, -10);
scene.RootNode.CreateChildNode(new Light()
{
    Color = new Vector3(Color.CadetBlue)
}).Transform.Translation = new Vector3(49, 0, 49);
```
## Étape 3 : Créer un moteur de rendu et une cible de rendu
Créez un moteur de rendu et une cible de rendu de carte cubique avec une texture de profondeur :
```csharp
using (var renderer = Renderer.CreateRenderer())
{
    IRenderTexture rt = renderer.RenderFactory.CreateCubeRenderTexture(new RenderParameters(false), 512, 512);
    rt.CreateViewport(cam, RelativeRectangle.FromScale(0, 0, 1, 1));
    renderer.Render(rt);
    ITextureCubemap cubemap = rt.Targets[0] as ITextureCubemap;
```
## Étape 4 : Enregistrer les faces du cubemap
Enregistrez chaque face du cubemap sur le disque avec les noms de fichiers spécifiés :
```csharp
CubeFaceData<string> fileNames = new CubeFaceData<string>()
{
    Right = "Your Output Directory" + "right.png",
    Left = "Your Output Directory" + "left.png",
    Back = "Your Output Directory" + "back.png",
    Front = "Your Output Directory" + "front.png",
    Bottom = "Your Output Directory" + "bottom.png",
    Top = "Your Output Directory" + "top.png"
};
cubemap.Save(fileNames, ImageFormat.Png);
```
## Conclusion
Toutes nos félicitations! Vous avez réussi à restituer une scène 3D dans un cubemap à l'aide d'Aspose.3D pour .NET. Explorez d'autres options de personnalisation et améliorez vos projets graphiques 3D avec cette puissante API.
## Questions fréquemment posées
### Q : Puis-je utiliser Aspose.3D pour .NET avec d’autres formats de fichiers 3D ?
Oui, Aspose.3D prend en charge différents formats de fichiers 3D, offrant ainsi une flexibilité à vos projets.
### Q : Comment puis-je obtenir de l'aide pour Aspose.3D ?
 Visiter le[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) pour le soutien et les discussions de la communauté.
### Q : Existe-t-il un essai gratuit ?
 Oui, vous pouvez accéder à l'essai gratuit[ici](https://releases.aspose.com/).
### Q : Puis-je restituer des scènes avec des animations à l'aide d'Aspose.3D ?
Absolument! Aspose.3D prend en charge le rendu de scènes 3D animées.
### Q : Où puis-je trouver une documentation détaillée ?
 Se référer au[Documentation Aspose.3D](https://reference.aspose.com/3d/net/) pour des informations détaillées.