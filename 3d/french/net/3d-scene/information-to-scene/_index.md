---
title: Extraction d'informations vers les ressources de scène
linktitle: Extraction d'informations vers les ressources de scène
second_title: API Aspose.3D .NET
description: Améliorez vos scènes 3D sans effort avec Aspose.3D pour .NET. Apprenez à ajouter des informations précieuses sur les actifs étape par étape. Téléchargez-le maintenant pour une expérience 3D dynamique.
type: docs
weight: 10
url: /fr/net/3d-scene/information-to-scene/
---
## Introduction

Bienvenue dans ce didacticiel complet sur l'utilisation d'Aspose.3D pour .NET pour extraire des informations précieuses et améliorer vos scènes 3D. Aspose.3D est une bibliothèque puissante qui permet aux développeurs de manipuler des scènes 3D de manière transparente dans les applications .NET. Dans ce didacticiel, nous nous concentrerons sur la tâche cruciale consistant à ajouter des informations sur les ressources à une scène.

## Conditions préalables

Avant de plonger dans le didacticiel, assurez-vous de disposer des prérequis suivants :

-  Aspose.3D pour .NET : assurez-vous que la bibliothèque est installée. Vous pouvez le télécharger depuis le[Page Aspose.3D pour .NET](https://releases.aspose.com/3d/net/).

## Importer des espaces de noms

Dans votre projet .NET, assurez-vous d'inclure les espaces de noms nécessaires pour accéder aux fonctionnalités Aspose.3D :

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
```

## Étape 1 : initialiser une scène 3D

```csharp
Scene scene = new Scene();
```

 Créez une nouvelle scène 3D à l'aide du`Scene` classe.

## Étape 2 : Définir les informations sur l'application et le fournisseur

```csharp
scene.AssetInfo.ApplicationName = "Egypt";
scene.AssetInfo.ApplicationVendor = "Manualdesk";
```

Définissez les noms d'application et de fournisseur associés à votre scène 3D.

## Étape 3 : Définir les unités de mesure

```csharp
scene.AssetInfo.UnitName = "pole";
scene.AssetInfo.UnitScaleFactor = 0.6;
```

Spécifiez les unités de mesure utilisées dans votre scène. Dans cet exemple, nous utilisons des unités égyptiennes anciennes appelées « pôle », avec 1 pôle égal à 60 cm.

## Étape 4 : Enregistrez la scène

```csharp
var output = "Your Output Directory" + "InformationToScene.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

Enregistrez la scène avec les informations sur les ressources ajoutées dans un format de fichier pris en charge par la 3D. Ajustez le répertoire de sortie selon vos besoins.

## Étape 5 : Afficher le message de réussite

```csharp
Console.WriteLine("\nAsset information added successfully to Scene.\nFile saved at " + output);
```

Informez l'utilisateur que les informations sur l'actif ont été ajoutées avec succès et que le fichier est enregistré.

## Conclusion

Toutes nos félicitations! Vous avez appris avec succès à utiliser Aspose.3D pour .NET pour extraire et ajouter des informations essentielles sur les ressources à vos scènes 3D. Ces connaissances ouvrent des possibilités infinies pour créer du contenu 3D plus informatif et engageant.

## FAQ

### Q1 : Puis-je utiliser Aspose.3D pour .NET avec d’autres langages de programmation ?

A1 : Aspose.3D prend principalement en charge les langages .NET, mais vous pouvez explorer les options d'interopérabilité pour d'autres langages.

### Q2 : Existe-t-il un essai gratuit disponible pour Aspose.3D pour .NET ?

 A2 : Oui, vous pouvez accéder à l'essai gratuit[ici](https://releases.aspose.com/).

### Q3 : Comment puis-je obtenir de l'aide pour les requêtes liées à Aspose.3D ?

 A3 : Visitez le[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) pour la communauté et le soutien.

### Q4 : Puis-je acheter une licence temporaire pour Aspose.3D pour .NET ?

 A4 : Oui, vous pouvez acquérir une licence temporaire[ici](https://purchase.aspose.com/temporary-license/).

### Q5 : Où puis-je trouver une documentation détaillée pour Aspose.3D pour .NET ?

 A5 : Reportez-vous au[Documentation](https://reference.aspose.com/3d/net/) pour des informations détaillées.