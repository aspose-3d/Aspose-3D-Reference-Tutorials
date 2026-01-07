---
date: 2026-01-07
description: Apprenez à ajouter un plan de sol lors de l'extrusion linéaire avec Aspose.3D
  pour .NET et à exporter des fichiers Wavefront OBJ. Maîtrisez les techniques de
  centrage et d’ancrage dans la modélisation 3‑D.
linktitle: Add Ground Plane and Center in Linear Extrusion
second_title: Aspose.3D .NET API
title: Ajouter le plan de sol et le centre dans l'extrusion linéaire
url: /fr/net/3d-modeling/linear-extrusion/center-in-linear-extrusion/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Ajouter un plancher et centrer dans une extrusion linéaire

## Introduction

Bienvenue dans ce guide complet pour maîtriser l’extrusion linéaire avec Aspose.3D for .NET. Si vous souhaitez **ajouter un plancher** à vos modèles et **exporter des fichiers Wavefront OBJ** tout en gardant l’extrusion centrée, vous êtes au bon endroit. Dans ce tutoriel, nous explorerons la technique d’extrusion linéaire, en nous concentrant particulièrement sur l’aspect du centrage et sur la façon dont un plancher vous aide à visualiser le résultat plus clairement.

## Réponses rapides
- **Que réalise « ajouter un plancher » ?** Il fournit une référence visuelle qui facilite la visualisation de la position de l’extrusion sur le plan X‑Z.  
- **Quel format est utilisé pour exporter le modèle ?** La scène est enregistrée au format Wavefront OBJ (`FileFormat.WavefrontOBJ`).  
- **Ai‑je besoin d’une licence pour exécuter le code ?** Une version d’essai gratuite suffit pour le développement ; une licence permanente est requise pour la production.  
- **Puis‑je modifier la longueur de l’extrusion ?** Oui – modifiez le deuxième paramètre de `LinearExtrusion`.  
- **Le centrage est‑il optionnel ?** `Center = true` centre l’extrusion autour du profil ; `false` l’aligne sur un côté.

## Prérequis

Avant de commencer cette aventure passionnante, assurez‑vous d’avoir les prérequis suivants :

- Connaissances de base du langage de programmation C#.  
- Visual Studio installé sur votre machine.  
- Bibliothèque Aspose.3D for .NET, que vous pouvez télécharger depuis la [Documentation Aspose.3D .NET](https://reference.aspose.com/3d/net/).  
- Assurez‑vous d’avoir accès à la [Documentation Aspose.3D .NET](https://reference.aspose.com/3d/net/) pour vous y référer tout au long du tutoriel.

## Importer les espaces de noms

Pour démarrer, importons les espaces de noms nécessaires. Ils constitueront la base de notre chef‑d’œuvre de modélisation 3D.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Étape 1 : Initialiser le profil de base

Nous commençons par définir un profil rectangulaire qui sera extrudé. Le `RoundingRadius` ajoute un léger congé aux coins.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## Étape 2 : Créer une scène 3D

Un objet `Scene` agit comme conteneur pour toute la géométrie, les lumières et les caméras.

```csharp
Scene scene = new Scene();
```

## Étape 3 : Créer les nœuds gauche et droit

Deux nœuds frères sont créés sous la racine. L’un démontrera l’extrusion **sans** centrage, l’autre **avec** centrage. Nous déplaçons également le nœud gauche afin que les deux exemples ne se chevauchent pas.

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(5, 0, 0);
```

## Étape 4 : Effectuer l’extrusion linéaire sur le nœud gauche (Pas de centrage)

Ici nous extrudons le profil sans centrage. Remarquez le drapeau `Center = false`.

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 2) { Center = false, Slices = 3 });
```

## Étape 5 : Ajouter un plancher de référence (Nœud gauche)

L’ajout d’une boîte fine sert de **plancher** afin que vous puissiez clairement voir comment l’extrusion repose sur la base.

```csharp
left.CreateChildNode(new Box(0.01, 3, 3));
```

## Étape 6 : Effectuer l’extrusion linéaire sur le nœud droit (Avec centrage)

Maintenant nous extrudons le même profil mais en activant le centrage. La géométrie sera placée symétriquement autour de l’origine du profil.

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 2) { Center = true, Slices = 3 });
```

## Étape 7 : Ajouter un plancher de référence (Nœud droit)

Un deuxième plancher est ajouté au nœud droit pour garder la comparaison visuelle cohérente.

```csharp
right.CreateChildNode(new Box(0.01, 3, 3));
```

## Étape 8 : Exporter le fichier Wavefront OBJ

Enfin, nous **exportons le Wavefront OBJ** afin que le résultat puisse être ouvert dans n’importe quel visualiseur 3‑D standard.

```csharp
scene.Save("Your Output Directory" + "CenterInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## Pourquoi ajouter un plancher ?

Ajouter un plancher vous donne immédiatement un repère visuel sur la hauteur et l’alignement de l’extrusion. C’est particulièrement utile lorsque vous devez comparer les résultats centrés et non centrés, comme le montre ce tutoriel.

## Problèmes courants & conseils

- **Plan de référence invisible :** Assurez‑vous que l’épaisseur du plan (`0.01` dans le constructeur `Box`) est suffisamment petite pour ne pas masquer l’extrusion, mais assez grande pour être rendue.  
- **Échec de l’exportation :** Vérifiez que le répertoire de sortie existe et que vous avez les permissions d’écriture.  
- **L’extrusion centrée apparaît décalée :** Revérifiez la propriété `Center` ; `true` centre le profil, `false` l’aligne sur un côté.

## Foire aux questions

### Q1 : Puis‑je utiliser Aspose.3D for .NET avec d’autres langages de programmation ?

R1 : Aspose.3D prend principalement en charge les langages .NET tels que C# et VB.NET.

### Q2 : Où puis‑je trouver du support pour les questions relatives à Aspose.3D ?

R2 : Visitez le [Forum Aspose.3D](https://forum.aspose.com/c/3d/18) pour un support dédié et des discussions.

### Q3 : Existe‑t‑il un essai gratuit pour Aspose.3D for .NET ?

R3 : Oui, vous pouvez accéder à l’essai gratuit [ici](https://releases.aspose.com/).

### Q4 : Comment obtenir une licence temporaire pour Aspose.3D for .NET ?

R4 : Vous pouvez acquérir une licence temporaire [ici](https://purchase.aspose.com/temporary-license/).

### Q5 : Où puis‑je acheter la licence Aspose.3D for .NET ?

R5 : Achetez votre licence [ici](https://purchase.aspose.com/buy).

### Q6 : Puis‑je exporter la scène vers d’autres formats que OBJ ?

R6 : Oui, Aspose.3D prend en charge de nombreux formats tels que STL, FBX et GLTF. Il suffit de changer la valeur de l’énumération `FileFormat` dans la méthode `Save`.

### Q7 : Comment modifier le nombre de tranches de l’extrusion ?

R7 : Ajustez la propriété `Slices` dans le constructeur `LinearExtrusion` pour contrôler la densité du maillage.

---

**Dernière mise à jour :** 2026-01-07  
**Testé avec :** Aspose.3D for .NET dernière version  
**Auteur :** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}