---
date: 2026-01-07
description: Apprenez à extruder linéairement un profil 2D et à exporter un modèle
  3D au format OBJ en utilisant Aspose.3D pour .NET. Ce tutoriel d'extrusion linéaire
  vous guide étape par étape.
linktitle: Performing Linear Extrusion
second_title: Aspose.3D .NET API
title: Comment réaliser une extrusion linéaire avec Aspose.3D pour .NET
url: /fr/net/3d-modeling/linear-extrusion/performing-linear-extrusion/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# how to linear extrude with Aspose.3D for .NET

## Introduction

Bienvenue dans notre **tutoriel d'extrusion linéaire** ! Dans ce guide, vous découvrirez **comment réaliser une extrusion linéaire** d’un profil 2 D et le transformer en un objet 3 D complet à l’aide d’Aspose.3D pour .NET. Que vous construisiez une application de type CAD ou que vous ayez simplement besoin d’**export 3d model obj** pour un traitement en aval, ce pas‑à‑pas vous donnera la confiance nécessaire pour ajouter une création de géométrie puissante à vos projets.

## Réponses rapides
- **Qu’est‑ce que l’extrusion linéaire ?** Extension d’une forme 2 D le long d’un chemin droit pour créer un solide 3 D.  
- **Quelle bibliothèque utilisons‑nous ?** Aspose.3D pour .NET.  
- **Ai‑je besoin d’une licence ?** Une licence temporaire suffit pour les tests ; une licence complète est requise en production.  
- **Puis‑je exporter en OBJ ?** Oui – la scène finale est enregistrée au format Wavefront OBJ.  
- **Combien de lignes de code ?** Moins de 30 lignes de C# plus des commentaires explicatifs.

## Qu’est‑ce que l’extrusion linéaire ?

L’extrusion linéaire prend un profil plat (comme un rectangle ou un cercle) et le balaye le long d’une ligne droite, avec la possibilité d’ajouter des torsions, des mises à l’échelle ou des décalages. Le résultat est un solide qui peut être rendu, édité ou exporté pour être utilisé dans d’autres outils 3 D.

## Pourquoi utiliser Aspose.3D pour l’extrusion linéaire ?

* **Zero‑dependency :** Aucun besoin de noyaux CAD externes.  
* **Support complet .NET :** Fonctionne avec .NET Framework, .NET Core et .NET 5/6+.  
* **Flexibilité d’export :** Enregistrement direct en OBJ, STL, FBX et bien d’autres formats.  
* **API riche :** Contrôlez les tranches, la torsion et les décalages avec quelques propriétés seulement.

## Prérequis

Avant de commencer, assurez‑vous d’avoir :

1. **Aspose.3D installé** – téléchargez‑le depuis [here](https://releases.aspose.com/3d/net/).  
2. **Accès à la documentation** – suivez le guide d’installation [here](https://reference.aspose.com/3d/net/).  
3. Un environnement de développement .NET (Visual Studio, VS Code ou Rider) avec les espaces de noms requis référencés.

## Importer les espaces de noms

Incluez les espaces de noms essentiels pour débloquer les fonctionnalités d’Aspose.3D :

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

Ces espaces de noms vous donnent accès à `Scene`, `LinearExtrusion`, `RectangleShape` et aux classes utilitaires comme `Vector3`.

## Réaliser l’extrusion linéaire

Voici le flux de travail complet. Chaque étape est expliquée en langage clair avant le bloc de code correspondant, afin que vous puissiez suivre sans deviner ce que fait le code.

### Étape 1 : Initialiser le profil de base

Tout d’abord, créez la forme 2 D qui sera extrudée. Dans cet exemple, nous utilisons un rectangle avec un petit rayon d’arrondi.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

*Pourquoi c’est important :* Le profil définit la section transversale de l’objet 3 D final. Modifiez `RoundingRadius`, la largeur ou la hauteur pour obtenir des silhouettes différentes.

### Étape 2 : Appliquer l’extrusion linéaire

Nous balayons maintenant le profil de 10 unités le long de l’axe Z, en ajoutant 100 tranches pour la fluidité, en centrant la géométrie et en appliquant une torsion complète de 360° avec un décalage.

```csharp
var extrusion = new LinearExtrusion(profile, 10) { Slices = 100, Center = true, Twist = 360, TwistOffset = new Vector3(10, 0, 0) };
```

*Astuce :* Ajustez `Slices` pour équilibrer performance et qualité visuelle, et expérimentez `Twist` pour des effets en spirale.

### Étape 3 : Créer une scène

Une `Scene` agit comme le conteneur de toutes les entités 3 D — pensez‑y comme à la toile.

```csharp
Scene scene = new Scene();
```

### Étape 4 : Ajouter l’extrusion à la scène

Attachez la géométrie extrudée au nœud racine de la scène afin qu’elle devienne partie de la hiérarchie rendable.

```csharp
scene.RootNode.CreateChildNode(extrusion);
```

### Étape 5 : Enregistrer le modèle 3 D

Enfin, exportez la scène vers un fichier OBJ largement supporté. Cela démontre la capacité **export 3d model obj** d’Aspose.3D.

```csharp
scene.Save(RunExamples.GetOutputFilePath("LinearExtrusion.obj"), FileFormat.WavefrontOBJ);
```

Lorsque vous ouvrirez le `LinearExtrusion.obj` résultant dans n’importe quel visualiseur 3 D, vous verrez un prisme rectangulaire torsadé — exactement ce que le code décrit.

## Pièges courants & conseils

| Problème | Pourquoi cela se produit | Comment corriger |
|----------|--------------------------|------------------|
| **Profil invisible** | Oubli d’ajouter l’extrusion à la scène. | Vérifiez que `CreateChildNode` est appelé. |
| **Torsion plate** | `Slices` trop faible, géométrie grossière. | Augmentez `Slices` (par ex., 200) pour une torsion plus lisse. |
| **Échec d’export** | Le dossier de sortie n’existe pas ou permissions manquantes. | Utilisez `RunExamples.GetOutputFilePath` ou créez le répertoire manuellement. |
| **Mise à l’échelle inattendue** | `Center` à `false` décale la géométrie. | Mettez `Center = true` sauf si vous avez besoin d’un offset. |

## Questions fréquentes

### Q1 : Aspose.3D convient‑il aux débutants ?

R1 : Absolument ! Aspose.3D propose une API conviviale, et ce tutoriel vous guide pas à pas à travers les bases de l’extrusion linéaire.

### Q2 : Puis‑je utiliser Aspose.3D pour des projets commerciaux ?

R2 : Oui, Aspose.3D propose des options de licence pour un usage personnel et commercial. Consultez les détails [here](https://purchase.aspose.com/buy).

### Q3 : Comment obtenir des licences temporaires pour les tests ?

R3 : Rendez‑vous sur [this link](https://purchase.aspose.com/temporary-license/) pour obtenir des licences temporaires à des fins de test.

### Q4 : Où trouver du support communautaire ?

R4 : Rejoignez le [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) pour échanger avec une communauté dynamique et obtenir de l’aide.

### Q5 : Existe‑t‑il une version d’essai gratuite ?

R5 : Bien sûr ! Téléchargez la version d’essai gratuite [here](https://releases.aspose.com/) pour découvrir les capacités d’Aspose.3D.

---

**Dernière mise à jour :** 2026-01-07  
**Testé avec :** Aspose.3D 24.11 pour .NET  
**Auteur :** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}