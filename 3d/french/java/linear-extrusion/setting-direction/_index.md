---
date: 2025-12-18
description: Apprenez à créer une scène 3D et à enregistrer un fichier OBJ en utilisant
  Aspose.3D pour Java. Suivez notre guide étape par étape pour la direction d'extrusion
  linéaire.
linktitle: Setting Direction in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Créer une scène 3D – Définir la direction d'extrusion Aspose.3D Java
url: /fr/java/linear-extrusion/setting-direction/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Créer une scène 3D – Définir la direction d'extrusion Aspose.3D Java

## Introduction

Dans ce tutoriel, vous apprendrez **comment créer une scène 3d** d'objets et contrôler la direction d'extrusion avec Aspose.3D pour Java. Que vous créiez des visualisations architecturales, des prototypes de produits ou des actifs de jeu, maîtriser l'extrusion linéaire vous offre la flexibilité de modéliser rapidement des formes complexes. Nous parcourrons chaque étape, de l'ajout de nœuds en Java à l'**exportation de modèles 3d au format obj**, afin que vous puissiez voir le résultat immédiatement.

## Réponses rapides
- **Que signifie « créer une scène 3d » ?** Cela signifie initialiser un objet Aspose.3D `Scene` qui contiendra toute la géométrie, les lumières et les caméras.  
- **Comment définir la direction d'extrusion ?** Utilisez la méthode `setDirection(Vector3)` sur une instance `LinearExtrusion`.  
- **Quel format dois‑je utiliser pour l'exportation ?** Le format OBJ (`FileFormat.WAVEFRONTOBJ`) est largement supporté pour les flux de travail 3‑D.  
- **Ai‑je besoin d’une licence pour Aspose.3D ?** Un essai gratuit suffit pour le développement ; une licence commerciale est requise pour la production.  
- **Puis‑je ajouter davantage de nœuds en Java ?** Oui — utilisez `scene.getRootNode().createChildNode()` pour ajouter autant d'objets que nécessaire.

## Qu’est‑ce qu’un flux de travail « créer une scène 3d » ?

Un flux de travail **créer une scène 3d** commence avec un objet `Scene` vide, ajoute de la géométrie (comme des profils extrudés), la positionne à l'aide de transformations, puis enregistre finalement la scène dans un format de fichier tel que OBJ. Ce modèle constitue la colonne vertébrale de la plupart des applications 3‑D développées avec Aspose.3D.

## Pourquoi définir la direction d'extrusion ?

Définir la direction d'extrusion vous permet d’incliner, de faire pivoter ou de déformer la forme pendant l'extrusion, vous offrant ainsi un contrôle sur la géométrie finale sans post‑traitement supplémentaire. C’est particulièrement utile pour :

- Créer des colonnes coniques ou des tuyaux à forme personnalisée.  
- Aligner les extrusions avec des axes non standard dans des pièces mécaniques.  
- Générer des formes artistiques pour des effets visuels.

## Prérequis

- Connaissances de base en Java.  
- Bibliothèque Aspose.3D installée – téléchargez‑la depuis [here](https://releases.aspose.com/3d/java/).  
- Un IDE tel qu’Eclipse ou IntelliJ IDEA.

## Import Packages

Tout d'abord, importez les classes Aspose.3D requises :

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Étape 1 : Initialiser le profil de base

Créez le profil 2‑D qui sera extrudé. Dans cet exemple, nous utilisons un rectangle arrondi :

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

> **Astuce :** Ajustez le rayon d’arrondi pour contrôler la netteté ou la douceur des coins du rectangle avant l’extrusion.

## Étape 2 : Créer une scène

Maintenant, nous **créons une scène 3d** qui hébergera nos objets :

```java
Scene scene = new Scene();
```

## Étape 3 : Ajouter des nœuds Java – Positionnement des objets

Nous ajouterons deux nœuds enfants (gauche et droite) au nœud racine de la scène et déplacerons légèrement le nœud gauche sur le côté :

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Étape 4 : Comment extruder – Nœud gauche (direction par défaut)

Extrudez le profil sur le nœud gauche en utilisant la direction Z‑axe par défaut. Nous définissons également une torsion complète de 360° et augmentons le nombre de tranches pour plus de fluidité :

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## Étape 5 : Comment définir la direction – Nœud droit

Ici nous **définissons la direction** en fournissant un `Vector3` personnalisé. Cela incline l’extrusion vers le vecteur (0.3, 0.2, 1) :

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## Étape 6 : Enregistrer le fichier OBJ – Exporter le modèle 3D

Enfin, nous **enregistrons le fichier obj** pour voir le résultat dans n’importe quel visualiseur 3‑D :

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

Lorsque vous ouvrez le fichier OBJ généré, vous verrez deux rectangles extrudés : un avec la direction par défaut et un incliné selon le vecteur que nous avons défini.

## Problèmes courants et solutions

| Problème | Raison | Solution |
|----------|--------|----------|
| Le fichier OBJ apparaît vide | Scène non enregistrée ou chemin incorrect | Vérifiez que `MyDir` pointe vers un dossier accessible en écriture et que le nom du fichier se termine par `.obj`. |
| L'extrusion semble plate | `setSlices` trop faible | Augmentez `setSlices` (par ex., 200) pour une géométrie plus lisse. |
| La direction semble inchangée | Vecteur non normalisé | Utilisez un `Vector3` normalisé ou ajustez les valeurs pour refléter l’inclinaison souhaitée. |

## Questions fréquemment posées

### Q1 : Puis‑je utiliser Aspose.3D avec d’autres langages de programmation ?
A1 : Aspose.3D prend en charge plusieurs langages, dont .NET et Java.

### Q2 : Existe‑t‑il un essai gratuit disponible pour Aspose.3D ?
A2 : Oui, vous pouvez explorer les fonctionnalités d’Aspose.3D avec un essai gratuit [here](https://releases.aspose.com/).

### Q3 : Où puis‑je trouver une documentation détaillée pour Aspose.3D pour Java ?
A3 : La documentation complète est disponible [here](https://reference.aspose.com/3d/java/).

### Q4 : Comment puis‑je obtenir du support pour Aspose.3D ?
A4 : Consultez le [Aspose.3D forum](https://forum.aspose.com/c/3d/18) pour toute assistance ou question.

### Q5 : Des licences temporaires sont‑elles disponibles pour Aspose.3D ?
A5 : Oui, vous pouvez obtenir une licence temporaire [here](https://purchase.aspose.com/temporary-license/).

---

**Dernière mise à jour :** 2025-12-18  
**Testé avec :** Aspose.3D 24.11 for Java  
**Auteur :** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}