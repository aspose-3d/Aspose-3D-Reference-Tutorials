---
date: 2026-05-24
description: Apprenez à extruder une forme en utilisant Aspose.3D for Java. Ce tutoriel
  de modélisation 3D Java couvre l'extrusion linéaire, le contrôle du centre, la direction,
  les tranches, la torsion et plus encore !
keywords:
- how to extrude shape
- java 3d geometry
- create 3d model java
- create solid from 2d
linktitle: Créer des modèles 3D avec extrusion linéaire en Java
schemas:
- author: Aspose
  dateModified: '2026-05-24'
  description: Learn how to extrude shape using Aspose.3D for Java. This java 3d modeling
    tutorial covers linear extrusion, center control, direction, slices, twist and
    more!
  headline: How to Extrude Shape - Creating 3D Models with Linear Extrusion in Java
  type: TechArticle
- description: Learn how to extrude shape using Aspose.3D for Java. This java 3d modeling
    tutorial covers linear extrusion, center control, direction, slices, twist and
    more!
  name: How to Extrude Shape - Creating 3D Models with Linear Extrusion in Java
  steps:
  - name: Define the 2‑D profile
    text: Create a `Polygon` or `Polyline` that represents the shape you want to extrude.
      *A `Polygon` represents a closed shape defined by vertices, while a `Polyline`
      is an open series of line segments.* Ready to get started? [Perform Linear Extrusion
      Now](./performing-linear-extrusion/) For a detailed tuto
  - name: Configure extrusion options
    text: 'Set the center, direction, slices, twist, and twist offset on an `Extrusion`
      object. *The `Extrusion` class encapsulates all parameters needed to generate
      a 3‑D mesh from a 2‑D profile.* Get hands‑on with center control: [Control Center
      in Linear Extrusion](./controlling-center/) Read more about cen'
  - name: Add the extrusion to the scene
    text: 'Instantiate a `Scene`, attach the extrusion mesh, and export to your desired
      format. *`Scene` is the container that holds all 3‑D objects and handles exporting
      to various file formats.* Ready to set the direction? [Explore Now](./setting-direction/)
      Learn more about direction: [Setting Direction in '
  - name: Export or render
    text: 'Use `Scene.save()` to write the model to OBJ, STL, or any supported format.
      *`Scene.save()` writes the entire scene to the specified file format, applying
      any necessary post‑processing.* Start specifying slices: [Learn More](./specifying-slices/)
      Detailed guide: [Specifying Slices in Linear Extrusio'
  type: HowTo
- questions:
  - answer: Yes, a valid Aspose license is required for production use, but a free
      trial is available for evaluation.
    question: Can I use Aspose.3D for Java in a commercial project?
  - answer: The library works with Java 8 and newer runtimes, including Java 11, 17,
      and 21.
    question: Which Java versions are supported?
  - answer: Aspose.3D handles mesh generation efficiently, but you can call `scene.dispose()`
      when you’re done with large scenes to free native resources.
    question: Do I need to manage memory for large extrusions?
  - answer: Absolutely – you can create several extrusion objects, position them independently,
      and add them to the same scene.
    question: Can I combine multiple extrusion operations in one model?
  - answer: Yes, the “Applying Twist” and “Using Twist Offset” tutorials demonstrate
      how to set both properties on the same extrusion object.
    question: Is there sample code for applying twist and twist offset together?
  type: FAQPage
second_title: Aspose.3D Java API
title: Comment extruder une forme - Créer des modèles 3D avec extrusion linéaire en
  Java
url: /fr/java/linear-extrusion/
weight: 23
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Comment extruder une forme – Créer des modèles 3D avec l'extrusion linéaire en Java

Si vous vous êtes déjà demandé **how to extrude shape** dans une application Java, vous êtes au bon endroit. Dans ce tutoriel, nous parcourrons les fonctionnalités d'extrusion linéaire d'Aspose.3D for Java, en vous montrant comment transformer de simples profils 2‑D en modèles 3‑D complets. Que vous construisiez un visualiseur de type CAD, une chaîne d'outils pour les actifs de jeu, ou que vous expérimentiez simplement avec la géométrie, maîtriser l'extrusion linéaire vous donnera la confiance nécessaire pour créer des formes complexes avec seulement quelques lignes de code.

## Réponses rapides
- **Qu'est-ce que l'extrusion linéaire ?** Transformer un croquis 2‑D en un solide 3‑D en l'étendant le long d'une direction.  
- **Quelle bibliothèque vous aide ?** Aspose.3D for Java fournit une API fluide pour les tâches d'extrusion.  
- **Ai-je besoin d'une licence ?** Un essai gratuit suffit pour l'apprentissage ; une licence commerciale est requise pour la production.  
- **Quelle version de Java est requise ?** Java 8 ou supérieur.  
- **Puis-je appliquer des torsions ou des décalages ?** Oui – l'API prend en charge l'angle de torsion et le décalage de torsion dès le départ.  

## Qu'est-ce que “how to extrude shape” en Java ?
L'opération `Extrusion` est la fonctionnalité principale d'Aspose.3D qui convertit un contour plat en un maillage volumétrique. En termes simples, vous fournissez un profil 2‑D (par exemple, un rectangle ou un polygone personnalisé), indiquez au moteur jusqu'où l'étirer, et la bibliothèque génère la géométrie 3‑D pour vous.

## Pourquoi utiliser Aspose.3D pour Java ?
Aspose.3D prend en charge **plus de 50 formats d'entrée et de sortie** – y compris OBJ, STL, FBX et GLTF – et peut générer des maillages avec jusqu'à **10 000 sommets par extrusion** sans charger la scène entière en mémoire. Son moteur multiplateforme fonctionne sous Windows, Linux et macOS, offrant des résultats cohérents que vous soyez sur une station de travail de bureau ou sur un serveur CI sans interface.

## Prérequis
- Java 8 ou version plus récente installé sur votre machine de développement.  
- Maven ou Gradle pour la gestion des dépendances.  
- Un fichier de licence Aspose.3D for Java (optionnel pour l'essai).  

## Comment fonctionne l'extrusion linéaire ?
L'extrusion linéaire crée un solide 3‑D en balayant un profil 2‑D le long d'une ligne droite. Le moteur triangule d'abord le profil, puis le reproduit à chaque tranche le long de l'axe d'extrusion, pour enfin assembler les tranches afin de former un maillage étanche. Ce processus calcule automatiquement les normales et les coordonnées UV, vous permettant de rendre le résultat sans traitement géométrique supplémentaire.

## Quels sont les paramètres clés d'une extrusion linéaire ?
L'extrusion linéaire peut être personnalisée avec plusieurs paramètres. Le **center** définit le point de pivot du profil avant l'extrusion. Le vecteur **direction** définit l'axe d'extrusion, par défaut l'axe Z positif. Les **Slices** contrôlent le nombre de sections transversales intermédiaires générées, influençant la fluidité des formes torsadées ou coniques. L'**angle de torsion** fait pivoter le profil progressivement du début à la fin, tandis que le **décalage de torsion** ajoute un déplacement linéaire le long de l'axe, permettant des formes en spirale.

- **Center** – Le point de pivot autour duquel le profil est positionné avant l'extrusion.  
- **Direction** – Un vecteur qui définit l'axe d'extrusion ; la valeur par défaut est l'axe Z positif.  
- **Slices** – Le nombre de sections transversales intermédiaires ; davantage de tranches offrent des transitions plus fluides pour les extrusions torsadées ou coniques.  
- **Twist Angle** – La rotation totale appliquée au profil du début à la fin, exprimée en degrés.  
- **Twist Offset** – Un décalage linéaire qui déplace le profil le long de l'axe d'extrusion tout en le tordant, permettant des formes en spirale.  

## Réaliser une extrusion linéaire avec Aspose.3D pour Java
Chargez votre profil, configurez les paramètres, et laissez l'API générer le maillage. Les étapes suivantes décrivent le flux de travail typique.

### Étape 1 : Définir le profil 2‑D
Créez un `Polygon` ou un `Polyline` qui représente la forme que vous souhaitez extruder.  
*Un `Polygon` représente une forme fermée définie par des sommets, tandis qu'un `Polyline` est une série ouverte de segments de ligne.*  
Ready to get started? [Perform Linear Extrusion Now](./performing-linear-extrusion/)  
For a detailed tutorial, see [Performing Linear Extrusion in Aspose.3D for Java](./performing-linear-extrusion/).

### Étape 2 : Configurer les options d'extrusion
Définissez le centre, la direction, les tranches, la torsion et le décalage de torsion sur un objet `Extrusion`.  
*La classe `Extrusion` encapsule tous les paramètres nécessaires pour générer un maillage 3‑D à partir d'un profil 2‑D.*  
Get hands‑on with center control: [Control Center in Linear Extrusion](./controlling-center/)  
Read more about center control: [Controlling Center in Linear Extrusion with Aspose.3D for Java](./controlling-center/)

### Étape 3 : Ajouter l'extrusion à la scène
Instanciez un `Scene`, attachez le maillage d'extrusion et exportez-le dans le format souhaité.  
*`Scene` est le conteneur qui regroupe tous les objets 3‑D et gère l'exportation vers divers formats de fichier.*  
Ready to set the direction? [Explore Now](./setting-direction/)  
Learn more about direction: [Setting Direction in Linear Extrusion with Aspose.3D for Java](./setting-direction/)

### Étape 4 : Exporter ou rendre
Utilisez `Scene.save()` pour écrire le modèle en OBJ, STL ou tout autre format supporté.  
*`Scene.save()` écrit l'ensemble de la scène dans le format de fichier spécifié, en appliquant tout post‑traitement nécessaire.*  
Start specifying slices: [Learn More](./specifying-slices/)  
Detailed guide: [Specifying Slices in Linear Extrusion with Aspose.3D for Java](./specifying-slices/)

## Comment appliquer une torsion à une extrusion ?
Appliquez une torsion en définissant la propriété `twistAngle` dans les options d'extrusion. Le moteur fait pivoter chaque tranche proportionnellement, créant un effet hélicoïdal. En ajustant l'angle, vous pouvez obtenir tout, d'une torsion subtile à des spirales complètes de 360°, utiles pour des éléments décoratifs ou des ressorts fonctionnels.  
Ready to twist it up? [Apply Twist Now](./applying-twist/)  
Full example: [Applying Twist in Linear Extrusion with Aspose.3D for Java](./applying-twist/)

## Comment utiliser le décalage de torsion pour des formes en spirale ?
Le décalage de torsion déplace chaque tranche le long de l'axe d'extrusion tout en la faisant pivoter, formant un escalier en spirale ou une géométrie de tire-bouchon. Combiner l'angle de torsion avec un décalage positif donne une rampe hélicoïdale lisse, tandis qu'un décalage négatif peut créer des spirales descendantes. Cette technique est idéale pour modéliser des filetages, des ressorts ou des rubans artistiques.  
Enhance your skills: [Learn Twist Offset](./using-twist-offset/)  
Comprehensive guide: [Using Twist Offset in Linear Extrusion with Aspose.3D for Java](./using-twist-offset/)

## Cas d'utilisation courants de l'extrusion linéaire
- **Mechanical parts** – Générer rapidement des boulons, arbres et supports à partir de croquis simples.  
- **Architectural elements** – Extruder des plans d'étage en murs ou colonnes pour des prototypes BIM.  
- **Game assets** – Créer des objets low‑poly tels que des clôtures, tuyaux ou rails décoratifs directement à partir d'art 2‑D.  
- **Educational tools** – Visualiser des surfaces mathématiques en extrudant des courbes paramétriques.  

## Résolution des problèmes courants
- **Missing faces** – Assurez-vous que le profil forme une boucle fermée ; les contours ouverts créent des lacunes.  
- **Excessive memory usage** – Réduisez le nombre de `slices` ou activez `scene.setMemoryOptimization(true)`.  
- **Incorrect twist direction** – Les angles positifs tournent dans le sens horaire lorsqu'on regarde le long de la direction d'extrusion ; utilisez des valeurs négatives pour inverser.  

## Questions fréquentes

**Q : Puis-je utiliser Aspose.3D pour Java dans un projet commercial ?**  
R : Oui, une licence Aspose valide est requise pour une utilisation en production, mais un essai gratuit est disponible pour l'évaluation.

**Q : Quelles versions de Java sont prises en charge ?**  
R : La bibliothèque fonctionne avec Java 8 et les environnements d'exécution plus récents, y compris Java 11, 17 et 21.

**Q : Dois-je gérer la mémoire pour les grandes extrusions ?**  
R : Aspose.3D gère efficacement la génération de maillages, mais vous pouvez appeler `scene.dispose()` lorsque vous avez terminé avec de grandes scènes pour libérer les ressources natives.

**Q : Puis-je combiner plusieurs opérations d'extrusion dans un même modèle ?**  
R : Absolument – vous pouvez créer plusieurs objets d'extrusion, les positionner indépendamment et les ajouter à la même scène.

**Q : Existe-t-il un exemple de code pour appliquer la torsion et le décalage de torsion ensemble ?**  
R : Oui, les tutoriels “Applying Twist” et “Using Twist Offset” montrent comment définir les deux propriétés sur le même objet d'extrusion.

---

**Dernière mise à jour :** 2026-05-24  
**Testé avec :** Aspose.3D for Java 24.11  
**Auteur :** Aspose  

{{< blocks/products/products-backtop-button >}}

## Tutoriels associés

- [Tutoriel Java 3D Graphics – Centre dans l'extrusion linéaire](/3d/java/linear-extrusion/controlling-center/)
- [Comment définir la direction dans l'extrusion linéaire avec Aspose.3D pour Java](/3d/java/linear-extrusion/setting-direction/)
- [Créer une extrusion 3D avec des tranches – Aspose.3D pour Java](/3d/java/linear-extrusion/specifying-slices/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}