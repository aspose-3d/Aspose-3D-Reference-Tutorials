---
title: Rendu d'une image de modèle 3D à partir d'une caméra
linktitle: Rendu d'une image de modèle 3D à partir d'une caméra
second_title: API Aspose.3D .NET
description: Explorez le monde du rendu 3D avec Aspose.3D pour .NET. Apprenez à créer sans effort des visualisations captivantes à l’aide de notre guide étape par étape.
weight: 11
url: /fr/net/rendering/render-3d-model-image/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Rendu d'une image de modèle 3D à partir d'une caméra

## Introduction
La création de superbes visualisations 3D est un aspect passionnant du développement logiciel, et avec Aspose.3D pour .NET, vous pouvez donner vie à vos modèles 3D. Dans ce didacticiel, nous vous guiderons dans le rendu d'une image de modèle 3D à partir d'une caméra à l'aide d'Aspose.3D, en vous fournissant des instructions étape par étape et des informations précieuses.
## Conditions préalables
Avant de plonger dans le processus de rendu, assurez-vous que les conditions préalables suivantes sont remplies :
-  Aspose.3D pour la bibliothèque .NET : téléchargez et installez la bibliothèque à partir du[lien de téléchargement](https://releases.aspose.com/3d/net/).
- Modèle 3D : préparez un fichier de modèle 3D (par exemple, Aspose3D.obj) que vous souhaitez restituer.
- Environnement de développement .NET : assurez-vous de disposer d'un environnement de développement .NET fonctionnel.
## Importer des espaces de noms
Dans votre projet .NET, incluez les espaces de noms nécessaires pour Aspose.3D :
```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD.Utilities;
using System.Drawing;
using System.Drawing.Imaging;
```
## Étape 1 : Charger la scène 3D
```csharp
Scene scene = new Scene();
var path = RunExamples.GetDataFilePath("Aspose3D.obj");
scene.Open(path);
```
## Étape 2 : Créer une caméra
```csharp
Camera cam = new Camera(ProjectionType.Perspective);
cam.NearPlane = 1;
cam.FarPlane = 500;
scene.RootNode.CreateChildNode(cam).Transform.Translation = new Vector3(170, 16, 130);
cam.LookAt = new Vector3(28, 0, -30);
```
## Étape 3 : ajouter des lumières à la scène
```csharp
scene.RootNode.CreateChildNode(new Light()
{
    LightType = LightType.Point,
    ConstantAttenuation = 0.3,
    Color = new Vector3(Color.White)
}).Transform.Translation = new Vector3(30, 10, 10);
scene.RootNode.CreateChildNode(new Light()
{
    LightType = LightType.Directional,
    ConstantAttenuation = 0.3,
    Direction = new Vector3(-0.3, -0.4, 0.3),
    Color = new Vector3(Color.White)
});
scene.RootNode.CreateChildNode(new Light()
{
    LightType = LightType.Spot,
    CastShadows = true,
    LookAt = new Vector3(28, 10, -30),
    Color = new Vector3(Color.White)
}).Transform.Translation = new Vector3(40, 10, 50);
```
## Étape 4 : Spécifier les options de rendu d'image
```csharp
ImageRenderOptions opt = new ImageRenderOptions();
opt.BackgroundColor = Color.AliceBlue;
opt.AssetDirectories.Add("Your Document Directory" + "textures");
opt.EnableShadows = true;
```
## Étape 5 : rendre la scène
```csharp
scene.Render(cam, "Your Output Directory" + "Render3DModelImageFromCamera.png", new Size(1024, 1024), ImageFormat.Png, opt);
```
## Conclusion
Toutes nos félicitations! Vous avez réussi à restituer une image de modèle 3D à partir d'une caméra à l'aide d'Aspose.3D pour .NET. N'hésitez pas à expérimenter différents modèles, angles de caméra et configurations d'éclairage pour améliorer vos visualisations 3D.
## FAQ
### Q : Puis-je utiliser Aspose.3D pour .NET avec d’autres outils de modélisation 3D ?
R : Aspose.3D prend en charge différents formats de modèles 3D, ce qui le rend compatible avec de nombreux outils de modélisation populaires.
### Q : Comment puis-je résoudre les problèmes de rendu ?
 R : Vérifiez Aspose.3D[forum](https://forum.aspose.com/c/3d/18) pour obtenir de l'aide et des solutions aux problèmes de rendu courants.
### Q : Existe-t-il un essai gratuit ?
 : Oui, vous pouvez explorer les fonctionnalités d'Aspose.3D en obtenant un[essai gratuit](https://releases.aspose.com/).
### Q : Où puis-je trouver une documentation complète ?
 R : Reportez-vous au[Documentation](https://reference.aspose.com/3d/net/) pour des conseils approfondis sur Aspose.3D pour .NET.
### Q : Comment puis-je acheter Aspose.3D pour .NET ?
 R : Visitez le[page d'achat](https://purchase.aspose.com/buy) pour acquérir la licence la plus adaptée à vos besoins.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
