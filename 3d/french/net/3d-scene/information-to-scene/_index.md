---
date: 2026-01-12
description: Apprenez à ajouter des métadonnées aux scènes 3D à l'aide d'Aspose.3D
  pour .NET, y compris comment ajouter des informations sur le fournisseur et exporter
  des fichiers de modèles 3D.
linktitle: 'How to Add Metadata: Extracting Information to Scene Assets'
second_title: Aspose.3D .NET API
title: 'Comment ajouter des métadonnées : extraction d''informations vers les actifs
  de scène'
url: /fr/net/3d-scene/information-to-scene/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Comment ajouter des métadonnées : extraire des informations vers les actifs de scène

## Introduction

Dans ce tutoriel complet, vous découvrirez **comment ajouter des métadonnées** à vos scènes 3D avec Aspose.3D for .NET. L’ajout de métadonnées telles que les détails du vendeur, des unités de mesure personnalisées et d’autres informations d’actif rend vos modèles plus informatifs, recherchables et prêts pour les pipelines en aval comme les moteurs de jeu ou les plateformes AR/VR.

## Réponses rapides
- **Quel est le but principal ?** Intégrer des métadonnées (infos vendeur, unités, balises personnalisées) directement dans une scène 3D.  
- **Quelle bibliothèque est utilisée ?** Aspose.3D for .NET.  
- **Puis‑je exporter le modèle après avoir ajouté les métadonnées ?** Oui – vous pouvez **exporter le modèle 3D**, par ex. enregistrer au format FBX.  
- **Ai‑je besoin d’une licence ?** Un essai gratuit est disponible ; une licence commerciale est requise pour la production.  
- **Quelles versions de .NET sont prises en charge ?** .NET Framework 4.5+, .NET Core 3.1+, .NET 5/6.

## Qu’est‑ce que « comment ajouter des métadonnées » dans une scène 3D ?

Ajouter des métadonnées signifie attacher des informations descriptives – comme le nom de l’application, le vendeur, les unités de mesure ou des balises personnalisées – au fichier de scène lui‑même. Ces données voyagent avec le modèle lorsque vous **enregistrez la scène au format FBX** ou d’autres formats pris en charge, permettant aux outils en aval de comprendre le contexte sans fichiers externes.

## Pourquoi intégrer des métadonnées personnalisées et des informations sur le vendeur ?

- **Recherchabilité :** Les systèmes de gestion d’actifs peuvent filtrer les modèles par vendeur ou type d’unité.  
- **Interopérabilité :** Les moteurs qui lisent le FBX peuvent appliquer automatiquement l’échelle correcte si vous **définissez les unités de mesure**.  
- **Branding :** Inclure le nom de l’application et le vendeur renforce la propriété et la conformité de licence.  

## Prérequis

Avant de commencer, assurez‑vous d’avoir :

- Aspose.3D for .NET installé. Vous pouvez le télécharger depuis la [page Aspose.3D for .NET](https://releases.aspose.com/3d/net/).

## Importer les espaces de noms

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
```

## Étape 1 : initialiser une scène 3D

```csharp
Scene scene = new Scene();
```

Créez un nouvel objet `Scene` qui contiendra toute la géométrie et les informations d’actif.

## Étape 2 : définir l’application et **ajouter les informations du vendeur**

```csharp
scene.AssetInfo.ApplicationName = "Egypt";
scene.AssetInfo.ApplicationVendor = "Manualdesk";
```

Ici nous intégrons le **nom de l’application** et les **informations du vendeur**. C’est une partie essentielle de **comment ajouter des métadonnées** qui identifie la source du modèle.

## Étape 3 : **définir les unités de mesure** pour un redimensionnement précis

```csharp
scene.AssetInfo.UnitName = "pole";
scene.AssetInfo.UnitScaleFactor = 0.6;
```

En spécifiant `UnitName` et `UnitScaleFactor`, vous indiquez aux outils en aval qu’un « pôle » équivaut à 0,6 mètre (60 cm). Cette étape est indispensable lorsque vous **exportez le modèle 3D** afin de garantir des dimensions réelles correctes.

## Étape 4 : **enregistrer la scène au format FBX** – **exporter le modèle 3D** avec métadonnées

```csharp
var output = "Your Output Directory" + "InformationToScene.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

L’appel `Save` écrit la scène dans un fichier FBX, en intégrant toutes les métadonnées que nous avons ajoutées. Cela montre **comment ajouter des métadonnées** puis **enregistrer la scène au format FBX**, réalisant ainsi **l’export du modèle 3D** avec l’ensemble des informations d’actif.

## Étape 5 : afficher le message de succès

```csharp
Console.WriteLine("\nAsset information added successfully to Scene.\nFile saved at " + output);
```

Un message convivial dans la console confirme que les métadonnées ont été écrites et indique l’emplacement du fichier.

## Problèmes courants et conseils

- **Échelle d’unité incorrecte :** Vérifiez que `UnitScaleFactor` correspond bien à la conversion réelle ; sinon les modèles exportés peuvent apparaître trop grands ou trop petits.  
- **Informations du vendeur manquantes :** Si `ApplicationVendor` est vide, certains visionneurs afficheront « Inconnu ». Définissez‑les toujours quand c’est possible.  
- **Erreurs de chemin de fichier :** Assurez‑vous que le répertoire de sortie existe ; sinon `scene.Save` lèvera une exception.

## Questions fréquentes

### Q1 : Puis‑je utiliser Aspose.3D for .NET avec d’autres langages de programmation ?

R1 : Aspose.3D prend principalement en charge les langages .NET, mais vous pouvez explorer des options d’interopérabilité pour d’autres langages.

### Q2 : Existe‑t‑il un essai gratuit pour Aspose.3D for .NET ?

R2 : Oui, vous pouvez accéder à l’essai gratuit [ici](https://releases.aspose.com/).

### Q3 : Comment obtenir du support pour les requêtes liées à Aspose.3D ?

R3 : Visitez le [forum Aspose.3D](https://forum.aspose.com/c/3d/18) pour la communauté et le support.

### Q4 : Puis‑je acheter une licence temporaire pour Aspose.3D for .NET ?

R4 : Oui, vous pouvez acquérir une licence temporaire [ici](https://purchase.aspose.com/temporary-license/).

### Q5 : Où trouver la documentation détaillée pour Aspose.3D for .NET ?

R5 : Consultez la [documentation](https://reference.aspose.com/3d/net/) pour des informations approfondies.

## Conclusion

Vous avez maintenant maîtrisé **comment ajouter des métadonnées** à une scène 3D avec Aspose.3D for .NET — en définissant les détails de l’application et du vendeur, **définissant les unités de mesure**, puis **enregistrant la scène au format FBX** pour **exporter le modèle 3D** contenant toutes ces précieuses informations. Utilisez ces techniques pour rendre vos actifs plus riches, plus recherchables et prêts pour tout workflow en aval.

---

**Dernière mise à jour :** 2026-01-12  
**Testé avec :** Aspose.3D 24.11 for .NET  
**Auteur :** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}