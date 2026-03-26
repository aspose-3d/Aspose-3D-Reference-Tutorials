---
date: 2026-03-26
description: Apprenez comment ajouter des informations sur le fournisseur à une scène
  3D et comment enregistrer des fichiers FBX en utilisant Aspose.3D pour .NET. Suivez
  ce guide étape par étape avec du code prêt à l'exécution.
linktitle: Extracting Information to Scene Assets
second_title: Aspose.3D .NET API
title: Comment ajouter les informations du fournisseur et enregistrer la scène FBX
  avec Aspose.3D
url: /fr/net/3d-scene/information-to-scene/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Comment ajouter des informations de fournisseur et enregistrer une scène FBX avec Aspose.3D

## Introduction

Bienvenue dans ce tutoriel complet qui montre **how to add vendor** aux détails d’une scène 3D puis **how to save FBX** avec Aspose.3D pour .NET. Que vous créiez des visualisations architecturales, des actifs de jeu ou des modèles d’ingénierie, intégrer les métadonnées du fournisseur et de l’application rend vos scènes plus informatives et plus faciles à gérer en aval. Parcourons le processus étape par étape.

## Quick Answers
- **What does “add vendor” mean?** Il stocke les noms de l'application et du fournisseur dans le bloc AssetInfo de la scène.  
- **Which format supports vendor info?** FBX (ASCII ou binary) conserve les métadonnées lors de l'enregistrement.  
- **How to save FBX?** Utilisez `scene.Save(path, FileFormat.FBX7500ASCII)` ou l'équivalent binaire.  
- **Do I need a license?** Un essai gratuit fonctionne pour le développement ; une licence commerciale est requise pour la production.  
- **Can I change measurement units?** Oui, définissez `AssetInfo.UnitName` et `AssetInfo.UnitScaleFactor`.

## Qu’est‑ce que “how to add vendor” dans une scène 3D ?

Ajouter des informations de fournisseur signifie remplir les propriétés `AssetInfo` d’un objet `Scene`. Ces propriétés voyagent avec le fichier, permettant à tout consommateur du fichier FBX de voir quelle application l’a créé et qui est le fournisseur.

## Why add vendor information?

- **Traceability:** Identifier rapidement la source d’un modèle dans de grands pipelines.  
- **Compliance:** Certaines industries exigent un marquage explicite du fournisseur pour la gestion des actifs.  
- **Automation:** Les scripts peuvent filtrer ou traiter les fichiers en fonction des métadonnées du fournisseur.

## Prerequisites

- Aspose.3D pour .NET installé. Vous pouvez le télécharger depuis la [page Aspose.3D for .NET](https://releases.aspose.com/3d/net/).

## Import Namespaces

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
```

## How to Add Vendor Information

### Étape 1 : Initialiser une scène 3D

```csharp
Scene scene = new Scene();
```

Créer une nouvelle `Scene` vous offre une toile vierge avec laquelle travailler.

### Étape 2 : Définir les informations d’application et de fournisseur

```csharp
scene.AssetInfo.ApplicationName = "Egypt";
scene.AssetInfo.ApplicationVendor = "Manualdesk";
```

Ici nous démontrons **how to add vendor** en assignant des chaînes significatives à `ApplicationName` et `ApplicationVendor`.

### Étape 3 : Définir les unités de mesure

```csharp
scene.AssetInfo.UnitName = "pole";
scene.AssetInfo.UnitScaleFactor = 0.6;
```

Spécifier le système d’unités garantit que toute personne ouvrant le fichier FBX interprète correctement les dimensions. Dans cet exemple, un « pole » équivaut à 60 cm.

## Comment enregistrer une scène FBX

### Étape 4 : Enregistrer la scène (how to save fbx)

```csharp
var output = "Your Output Directory" + "InformationToScene.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

Cette ligne montre **how to save fbx** en utilisant la version ASCII de FBX 7.5.0. Si vous préférez le binaire, remplacez `FBX7500ASCII` par `FBX7500Binary`.

> **Conseil pro :** Conservez l’extension de fichier `.fbx` cohérente avec le format que vous choisissez ; sinon certains visionneurs peuvent mal interpréter le contenu.

### Étape 5 : Afficher le message de succès

```csharp
Console.WriteLine("\nAsset information added successfully to Scene.\nFile saved at " + output);
```

Un message convivial dans la console confirme que la scène, complète avec les métadonnées du fournisseur, a été écrite sur le disque.

## Common Issues and Solutions

| Problème | Solution |
|----------|----------|
| **Vendor info not appearing in viewer** | Assurez‑vous d’avoir enregistré le fichier en **FBX ASCII** ou **Binary** ; certains visionneurs plus anciens ne lisent qu’un seul format. |
| **Path contains spaces** | Entourez le chemin de guillemets ou utilisez `Path.Combine` pour construire un chemin de fichier sûr. |
| **Unit scale looks wrong** | Vérifiez à nouveau `UnitScaleFactor` ; c’est un multiplicateur relatif aux mètres. |
| **License exception** | Utilisez l’essai gratuit pour les tests ; obtenez une licence complète pour les versions de production. |

## Frequently Asked Questions

**Q : Puis‑je utiliser Aspose.3D pour .NET avec d’autres langages de programmation ?**  
A : Aspose.3D prend principalement en charge les langages .NET, mais vous pouvez explorer les options d’interopérabilité pour d’autres langages.

**Q : Existe‑t‑il un essai gratuit disponible pour Aspose.3D pour .NET ?**  
A : Oui, vous pouvez accéder à l’essai gratuit [ici](https://releases.aspose.com/).

**Q : Comment obtenir du support pour les questions liées à Aspose.3D ?**  
A : Visitez le [forum Aspose.3D](https://forum.aspose.com/c/3d/18) pour la communauté et le support.

**Q : Puis‑je acheter une licence temporaire pour Aspose.3D pour .NET ?**  
A : Oui, vous pouvez obtenir une licence temporaire [ici](https://purchase.aspose.com/temporary-license/).

**Q : Où puis‑je trouver la documentation détaillée pour Aspose.3D pour .NET ?**  
A : Consultez la [documentation](https://reference.aspose.com/3d/net/) pour des informations approfondies.

---

**Dernière mise à jour :** 2026-03-26  
**Testé avec :** Aspose.3D 24.11 pour .NET  
**Auteur :** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}