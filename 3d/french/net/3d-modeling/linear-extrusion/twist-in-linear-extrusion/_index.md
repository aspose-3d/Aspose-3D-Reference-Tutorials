---
date: 2026-03-23
description: Apprenez à créer une extrusion avec une torsion en utilisant Aspose.3D
  pour .NET. Ce guide étape par étape couvre les techniques d'extrusion linéaire avec
  torsion.
linktitle: Twist in Linear Extrusion
second_title: Aspose.3D .NET API
title: Comment créer une extrusion avec une torsion en extrusion linéaire
url: /fr/net/3d-modeling/linear-extrusion/twist-in-linear-extrusion/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Comment créer une extrusion avec une torsion en extrusion linéaire

## Introduction

Si vous développez des applications .NET qui nécessitent des visuels 3D saisissants, vous découvrirez rapidement que **comment créer une extrusion** est une compétence fondamentale. Aspose.3D for .NET vous offre une API propre et haute performance pour transformer de simples profils 2‑D en modèles 3‑D sophistiqués—surtout lorsque vous ajoutez une torsion. Dans ce tutoriel, nous parcourrons chaque étape, de la configuration de la scène à l’enregistrement du fichier OBJ final, afin que vous puissiez voir la puissance de la torsion d’extrusion linéaire en action.

## Réponses rapides
- **Quelle est la classe principale pour l'extrusion ?** `LinearExtrusion`
- **Quelle propriété ajoute la rotation ?** `Twist`
- **Combien de tranches donnent un rendu lisse ?** Environ 100 tranches (ajustez selon les besoins)
- **Puis‑je utiliser d'autres formes ?** Oui, tout `IProfile` tel que des cercles, des polygones ou des courbes personnalisées
- **Quel format de fichier est utilisé dans l'exemple ?** Wavefront OBJ (`.obj`)

## Prérequis

Avant de commencer, assurez‑vous de disposer de :

- Aspose.3D for .NET installé. Si vous ne l’avez pas encore téléchargé, obtenez‑le **[ici](https://releases.aspose.com/3d/net/)**.
- Un environnement de développement .NET fonctionnel (Visual Studio, VS Code ou tout autre IDE de votre choix).
- Une connaissance de base de la syntaxe C# et des concepts orientés objet.

## Importer les espaces de noms

Dans tout projet .NET, l’utilisation correcte des espaces de noms est cruciale. Commencez par importer les espaces de noms nécessaires afin de tirer parti des fonctionnalités d’Aspose.3D de manière efficace. Voici un extrait pour vous guider :

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Guide étape par étape

### Étape 1 : Initialiser le profil de base

Nous commençons par définir la forme qui sera extrudée. Dans cet exemple, nous utilisons un rectangle avec un petit rayon d’arrondi pour donner aux arêtes une courbe subtile.

```csharp
// Initialize the base profile to be extruded
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

### Étape 2 : Créer une scène 3D

Un objet `Scene` agit comme la toile où toutes les entités 3‑D résident. Pensez‑y comme à la scène pour votre extrusion.

```csharp
// Create a scene 
Scene scene = new Scene();
```

### Étape 3 : Ajouter les nœuds gauche et droit

Les nœuds vous permettent d’organiser les objets de façon hiérarchique. Nous créerons deux nœuds frères — l’un pour une extrusion droite et l’autre pour une version tordue.

```csharp
// Create left node
var left = scene.RootNode.CreateChildNode();
// Create right node
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(15, 0, 0);
```

### Étape 4 : Effectuer une extrusion linéaire avec torsion sur le nœud gauche

La propriété `Twist` contrôle la quantité de rotation du profil pendant l’extrusion. La régler à **0** donne une extrusion droite classique.

```csharp
// Twist property defines the degree of the rotation while extruding the profile
// Perform linear extrusion on the left node using twist and slices property
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 0, Slices = 100 });
```

### Étape 5 : Effectuer une extrusion linéaire avec torsion sur le nœud droit

Nous appliquons maintenant une torsion de 90 degrés au même profil. Cela montre clairement l’effet de **torsion d’extrusion linéaire**.

```csharp
// Perform linear extrusion on the right node using twist and slices property
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 90, Slices = 100 });
```

### Étape 6 : Enregistrer la scène 3D

Enfin, exportez la scène dans un format que vous pouvez visualiser avec n’importe quel visionneur 3‑D. L’exemple utilise Wavefront OBJ, mais Aspose.3D prend en charge de nombreux autres formats.

```csharp
// Save 3D scene
scene.Save("Your Output Directory" + "TwistInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## Pourquoi utiliser l’extrusion linéaire avec une torsion ?

- **Prototypage rapide** : Transformez des croquis 2‑D en pièces 3‑D sans modélisation manuelle.
- **Flexibilité de conception** : Ajustez la valeur `Twist` pour créer des spirales, des nervures hélicoïdales ou des éléments décoratifs.
- **Performance optimisée** : Le paramètre `Slices` vous permet d’équilibrer la fidélité visuelle et la vitesse d’exécution.

## Problèmes courants et astuces

- **Trop de tranches** : Bien que 100 tranches offrent une apparence lisse, des valeurs extrêmement élevées peuvent ralentir le rendu. Testez avec des comptes plus faibles si les performances deviennent un problème.
- **Valeurs de torsion négatives** : Un `Twist` négatif tourne dans le sens opposé—utile pour les conceptions miroir.
- **Chemins de fichiers** : Assurez‑vous que le répertoire de sortie existe et que vous disposez des droits d’écriture ; sinon, `scene.Save` lèvera une exception.

## Conclusion

Dans ce tutoriel, nous avons montré **comment créer une extrusion** avec une torsion en utilisant Aspose.3D for .NET. En ajustant les propriétés `Twist` et `Slices`, vous pouvez générer une grande variété de formes, des barres tordues simples aux structures hélicoïdales complexes, le tout avec quelques lignes de code seulement.

## Foire aux questions

**Q : Puis‑je appliquer une extrusion linéaire avec une torsion à d’autres formes ?**  
R : Absolument ! Toute classe implémentant `IProfile`—comme `CircleShape`, `PolygonShape` ou une spline personnalisée—peut être extrudée avec une torsion.

**Q : Que représente réellement la propriété `Twist` ?**  
R : Elle spécifie l’angle de rotation total (en degrés) appliqué au profil sur toute la longueur de l’extrusion.

**Q : L’augmentation du nombre de tranches affecte‑t‑elle l’utilisation de la mémoire ?**  
R : Oui, plus de tranches génèrent davantage de sommets et de faces, ce qui consomme plus de mémoire et peut impacter les performances sur des appareils peu puissants.

**Q : Puis‑je combiner l’extrusion linéaire avec d’autres fonctionnalités d’Aspose.3D ?**  
R : Définitivement. Vous pouvez appliquer des matériaux, des textures ou même des opérations booléennes après l’extrusion pour créer des modèles encore plus riches.

**Q : Où puis‑je obtenir de l’aide ou discuter d’idées avec d’autres développeurs ?**  
R : Rejoignez la communauté Aspose.3D sur **[Aspose Forum](https://forum.aspose.com/c/3d/18)** pour du support, des exemples et des discussions.

---

**Dernière mise à jour :** 2026-03-23  
**Testé avec :** Aspose.3D 24.11 for .NET  
**Auteur :** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}