---
title: Chargement et sauvegarde - Utilisation de CancellationToken
linktitle: Chargement et sauvegarde - Utilisation de CancellationToken
second_title: API Aspose.3D .NET
description: Explorez le monde transparent de la modélisation 3D avec Aspose.3D pour .NET. Apprenez à charger et enregistrer efficacement des documents 3D à l'aide de CancellationToken.
type: docs
weight: 10
url: /fr/net/loading-and-saving/cancellation-token/
---
## Introduction

Bienvenue dans notre guide complet sur l'utilisation d'Aspose.3D pour .NET pour améliorer vos projets de modélisation et de rendu 3D. Aspose.3D est une bibliothèque puissante qui permet aux développeurs .NET de travailler de manière transparente avec des fichiers 3D. Dans ce didacticiel, nous approfondirons les aspects de chargement et de sauvegarde, en nous concentrant spécifiquement sur l'utilisation de CancellationToken pour une gestion efficace des tâches asynchrones.

## Conditions préalables

Avant de nous lancer dans cette aventure, assurez-vous d’avoir les conditions préalables suivantes en place :

-  Aspose.3D pour .NET : téléchargez et installez la bibliothèque à partir de[ici](https://releases.aspose.com/3d/net/).
- Environnement .NET : assurez-vous d'avoir configuré un environnement de développement .NET compatible.
- Compréhension de base de C# : Une connaissance du langage de programmation C# est recommandée.

## Importer des espaces de noms

Pour commencer, assurez-vous d'inclure les espaces de noms nécessaires dans votre projet. Ces espaces de noms donneront accès aux fonctionnalités nécessaires à la manipulation de fichiers 3D.

```csharp
using Aspose.ThreeD;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
```

## Chargement et sauvegarde - Utilisation de CancellationToken

### Étape 1 : Créer CancellationTokenSource

```csharp
// ExStart : CancellationTokenSource

CancellationTokenSource cts = new CancellationTokenSource();
```

Ici, nous instancions un CancellationTokenSource, un composant crucial pour gérer l'annulation dans les opérations asynchrones.

### Étape 2 : initialiser la scène 3D

```csharp
Scene scene = new Scene();
```

Créez une instance de la classe Scene. Ce sera la toile de fond de vos activités de modélisation 3D.

### Étape 3 : définir le délai d'expiration du jeton d'annulation

```csharp
cts.CancelAfter(1000);
```

 Réglez le délai d'annulation à l'aide du`CancelAfter` méthode. Dans cet exemple, le délai d'attente est défini sur 1 000 millisecondes (1 seconde).

### Étape 4 : ouvrir le document 3D

```csharp
try
{
    scene.Open("Your Output Directory" + "document.fbx", cts.Token);
    Console.WriteLine("Import is done within 1000ms");
}
catch (ImportException e)
{
    if (e.InnerException is OperationCanceledException)
    {
        Console.WriteLine("It takes too long time to import, import has been canceled.");
    }
}
```

 Essayez d'ouvrir le document 3D dans le délai spécifié. Le`cts.Token`Le paramètre garantit que l’opération peut être annulée si elle dépasse le délai d’attente défini.

### Étape 5 : Gérer l'exception d'importation

En cas d'ImportException, gérez-la gracieusement en vérifiant si elle a été causée par une OperationCanceledException.

```csharp
catch (ImportException e)
{
    if (e.InnerException is OperationCanceledException)
    {
        Console.WriteLine("It takes too long time to import, import has been canceled.");
    }
}
// ExEnd : CancellationTokenSource
```

## Conclusion

Toutes nos félicitations! Vous avez réussi à parcourir le processus d'utilisation d'Aspose.3D pour .NET avec CancellationToken pour gérer le chargement des documents 3D. Cette technique garantit des opérations d'importation efficaces et rapides, améliorant ainsi les performances globales de vos applications 3D.

## FAQ

### Q1 : Aspose.3D est-il compatible avec tous les formats de fichiers 3D ?

 A1 : Aspose.3D prend en charge une large gamme de formats de fichiers 3D, notamment FBX, STL, OBJ, etc. Se référer au[Documentation](https://reference.aspose.com/3d/net/) pour la liste complète.

### Q2 : Comment puis-je obtenir une licence temporaire pour Aspose.3D ?

 A2 : Obtenez un permis temporaire en visitant[ce lien](https://purchase.aspose.com/temporary-license/).

### Q3 : Où puis-je trouver de l'assistance pour Aspose.3D ?

 A3 : Rejoignez la discussion de la communauté au[Forum Aspose.3D](https://forum.aspose.com/c/3d/18).

### Q4 : Puis-je essayer Aspose.3D gratuitement avant d’acheter ?

 A4 : Oui, explorez les fonctionnalités avec un essai gratuit disponible[ici](https://releases.aspose.com/).

### Q5 : Quelle est la dernière version d’Aspose.3D pour .NET ?

 A5 : Restez à jour en consultant le[page de téléchargement](https://releases.aspose.com/3d/net/) pour la dernière version.