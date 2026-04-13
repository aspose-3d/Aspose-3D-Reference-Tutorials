---
date: 2026-03-23
description: Apprenez comment réaliser une extrusion linéaire avec des tranches en
  utilisant Aspose.3D pour .NET. Créez des modèles 3D détaillés avec des exemples
  de code étape par étape.
linktitle: How to Linear Extrusion with Slices
second_title: Aspose.3D .NET API
title: Comment réaliser une extrusion linéaire avec des coupes en utilisant Aspose.3D
  pour .NET
url: /fr/net/3d-modeling/linear-extrusion/slices-in-linear-extrusion/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Comment réaliser une extrusion linéaire avec des tranches à l'aide d'Aspose.3D pour .NET

## Introduction

Bienvenue dans le monde de la conception 3D avec Aspose.3D pour .NET ! Dans ce tutoriel, vous découvrirez **comment réaliser une extrusion linéaire** avec des tranches, une technique qui vous permet de contrôler le niveau de détail de vos modèles. Que vous soyez un développeur chevronné ou que vous débutiez, nous vous guiderons pas à pas, expliquerons le pourquoi de chaque action et vous donnerons des astuces pratiques à appliquer immédiatement.

## Réponses rapides
- **Qu’est‑ce que l’extrusion linéaire avec des tranches ?** C’est une méthode qui étend un profil 2D en 3D tout en spécifiant le nombre de sections transversales intermédiaires (tranches) générées.  
- **Pourquoi utiliser des tranches ?** Plus de tranches donnent une courbure plus lisse ; moins de tranches allègent le maillage.  
- **Prérequis ?** Aspose.3D pour .NET, un IDE compatible .NET et des connaissances de base en C#.  
- **Temps d’exécution typique ?** L’exemple s’exécute en moins d’une seconde sur un PC moderne.  
- **Format de sortie ?** L’exemple enregistre au format Wavefront OBJ, mais Aspose.3D prend en charge de nombreux formats.

## Qu’est‑ce que l’extrusion linéaire avec des tranches ?

L’extrusion linéaire prend une forme 2‑D (un profil) et l’étire le long d’une ligne droite pour créer un solide 3‑D. La propriété **Slices** détermine combien de sections transversales intermédiaires sont insérées entre le début et la fin de l’extrusion, influençant la fluidité et le nombre de polygones.

## Pourquoi utiliser des tranches dans une extrusion linéaire ?

- **Contrôle de la densité du maillage :** Ajustez le compromis entre qualité visuelle et taille du fichier.  
- **Optimisation des performances :** Utilisez moins de tranches pour les applications en temps réel, plus pour les rendus haute résolution.  
- **Flexibilité créative :** Combinez différents nombres de tranches sur des objets séparés pour mettre en avant l’intention de conception.

## Prérequis

Avant de commencer, assurez‑vous d’avoir :

- La bibliothèque Aspose.3D pour .NET – téléchargez‑la depuis [ici](https://releases.aspose.com/3d/net/).  
- Un IDE qui supporte le C# (Visual Studio, Rider, VS Code, etc.).  
- Une familiarité de base avec la syntaxe C# et les concepts orientés objet.  
- Une curiosité d’expérimenter avec la géométrie 3‑D !

## Importer les espaces de noms

Tout d’abord, importez les espaces de noms qui vous donnent accès aux classes principales d’Aspose.3D.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Guide étape par étape

### Étape 1 : Initialiser le profil de base

Nous commençons avec une forme rectangulaire simple et lui appliquons un petit rayon d’arrondi afin que les arêtes ne soient pas parfaitement nettes.

```csharp
// ExStart:InitializeBaseProfile
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
// ExEnd:InitializeBaseProfile
```

### Étape 2 : Créer une scène 3D

Un `Scene` agit comme le conteneur pour tous les nœuds, maillages, lumières et caméras.

```csharp
// ExStart:Create3DScene
Scene scene = new Scene();
// ExEnd:Create3DScene
```

### Étape 3 : Ajouter les nœuds gauche et droit

Nous créerons deux nœuds frères sous la racine de la scène. Le nœud de gauche recevra un faible nombre de tranches, le nœud de droite un nombre élevé, afin que vous puissiez comparer la différence visuelle.

```csharp
// ExStart:CreateLeftRightNodes
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(15, 0, 0);
// ExEnd:CreateLeftRightNodes
```

### Étape 4 : Effectuer l’extrusion linéaire sur le nœud gauche (faible détail)

Ici nous extrudons le rectangle avec seulement **2 tranches**. Cela produit un maillage grossier—idéal pour des aperçus rapides.

```csharp
// ExStart:LinearExtrusionLeftNode
left.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 2 });
// ExEnd:LinearExtrusionLeftNode
```

### Étape 5 : Effectuer l’extrusion linéaire sur le nœud droit (haut détail)

Maintenant nous utilisons **10 tranches** pour un résultat beaucoup plus lisse. Remarquez comment la géométrie devient plus fine.

```csharp
// ExStart:LinearExtrusionRightNode
right.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 10 });
// ExEnd:LinearExtrusionRightNode
```

### Étape 6 : Enregistrer la scène 3D

Enfin, écrivez la scène dans un fichier OBJ. Remplacez `"Your Output Directory"` par un chemin valide sur votre machine.

```csharp
// ExStart:Save3DScene
scene.Save("Your Output Directory" + "SlicesInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
// ExEnd:Save3DScene
```

## Problèmes courants et solutions

| Problème | Pourquoi cela se produit | Solution |
|----------|--------------------------|----------|
| **Aucun fichier créé** | Le chemin de sortie est invalide ou les permissions d'écriture sont manquantes. | Utilisez un chemin absolu et assurez‑vous que le dossier existe. |
| **L'objet apparaît plat** | `Slices` réglé à 1 ou 0. | Réglez `Slices` à au moins 2 pour une extrusion visible. |
| **Géométrie inattendue** | Rayon d'arrondi trop grand pour la taille du rectangle. | Ajustez `RoundingRadius` à une valeur inférieure à la moitié du plus petit côté du rectangle. |

## Questions fréquentes

**Q : Puis‑je changer la direction de l’extrusion ?**  
R : Oui. Utilisez la propriété `Transform` du nœud pour faire pivoter ou translater la géométrie extrudée avant l’enregistrement.

**Q : Aspose.3D prend‑il en charge d’autres types d’extrusion ?**  
R : Absolument. En plus de `LinearExtrusion`, vous pouvez utiliser `RevolveExtrusion`, `SweepExtrusion`, et bien d’autres.

**Q : Quels formats de fichier puis‑je exporter ?**  
R : Aspose.3D supporte OBJ, STL, FBX, 3MF, Collada, et de nombreux autres. Il suffit de changer l’énumération `FileFormat`.

**Q : Existe‑t‑il un moyen de définir un matériau par programme ?**  
R : Oui. Après avoir créé le nœud, assignez un `Material` à sa collection `Entity`.

**Q : Comment le nombre de tranches affecte‑t‑il la consommation mémoire ?**  
R : Plus de tranches augmentent le nombre de sommets et de faces, ce qui élève proportionnellement la consommation de mémoire. Utilisez le profilage pour trouver le juste milieu pour votre plateforme cible.

## FAQ originales

### Q1 : Puis‑je utiliser Aspose.3D pour .NET avec d’autres langages de programmation ?

R1 : Aspose.3D est principalement conçu pour .NET, mais vous pouvez explorer des options d’interopérabilité avec des langages comme Python via les liaisons .NET.

### Q2 : Où puis‑je trouver la documentation détaillée d’Aspose.3D pour .NET ?

R2 : Consultez la documentation [ici](https://reference.aspose.com/3d/net/) pour des informations approfondies sur les capacités et l’utilisation d’Aspose.3D.

### Q3 : Existe‑t‑il une version d’essai gratuite d’Aspose.3D pour .NET ?

R3 : Oui, vous pouvez obtenir votre version d’essai gratuite [ici](https://releases.aspose.com/) pour explorer les fonctionnalités de la bibliothèque avant d’effectuer un achat.

### Q4 : Comment obtenir le support technique pour Aspose.3D pour .NET ?

R4 : Visitez le forum Aspose.3D [ici](https://forum.aspose.com/c/3d/18) pour demander de l’aide et interagir avec la communauté.

### Q5 : Puis‑je utiliser une licence temporaire pour Aspose.3D pour .NET ?

R5 : Oui, obtenez une licence temporaire [ici](https://purchase.aspose.com/temporary-license/) à des fins d’évaluation.

## Conclusion

Vous avez maintenant vu **comment réaliser une extrusion linéaire** avec des tranches en utilisant Aspose.3D pour .NET, exploré l’impact de différents nombres de tranches et appris à exporter votre travail. Expérimentez avec d’autres profils, jouez avec la valeur `Slices` et intégrez des matériaux ou des lumières pour créer des actifs 3D prêts pour la production.

---

**Dernière mise à jour :** 2026-03-23  
**Testé avec :** Aspose.3D 24.11 pour .NET (dernière version au moment de la rédaction)  
**Auteur :** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}