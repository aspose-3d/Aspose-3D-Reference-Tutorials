---
date: 2026-08-02
description: Apprenez comment modifier la direction d'extrusion dans linear extrusion
  et exporter des fichiers OBJ à l'aide d'Aspose.3D pour Java. Suivez notre guide
  step‑by‑step.
keywords:
- change extrusion direction
- export obj file java
- Aspose.3D Java
lastmod: 2026-08-02
linktitle: Modifier la direction d'extrusion – Aspose.3D Java
og_description: Modifiez la direction d'extrusion dans linear extrusion avec Aspose.3D
  pour Java et exportez des fichiers OBJ. Ce guide présente du code step‑by‑step et
  des astuces pour les développeurs.
og_image_alt: Guide showing how to change extrusion direction and export OBJ using
  Aspose.3D Java
og_title: Modifier la direction d'extrusion – Tutoriel Aspose.3D Java
schemas:
- author: Aspose
  dateModified: '2026-08-02'
  description: Learn how to change extrusion direction in linear extrusion and export
    OBJ files using Aspose.3D for Java. Follow our step‑by‑step guide.
  headline: Change Extrusion Direction in 3D Models – Aspose.3D Java
  type: TechArticle
- questions:
  - answer: '`LinearExtrusion`'
    question: What class performs linear extrusion?
  - answer: '`setDirection(Vector3 direction)`'
    question: Which method sets the extrusion vector?
  - answer: Yes—use `scene.save(..., FileFormat.WAVEFRONTOBJ)`
    question: Can the result be saved as OBJ?
  - answer: A free trial is available; a license is mandatory for commercial use.
    question: Is a license required for production?
  - answer: IntelliJ IDEA and Eclipse are fully supported.
    question: Which IDE works best with Aspose.3D?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- change extrusion direction
- Aspose.3D
- Java 3D modeling
- export OBJ
title: Modifier la direction d'extrusion dans les modèles 3D – Aspose.3D Java
url: /fr/java/linear-extrusion/setting-direction/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Modifier la direction d'extrusion dans les modèles 3D – Aspose.3D Java

## Introduction

Dans ce tutoriel complet, vous découvrirez **comment changer la direction d'extrusion** lors d’une extrusion linéaire avec Aspose.3D pour Java. Que vous construisiez un outil de type CAO, prépariez des actifs pour un moteur de jeu ou génériez des pièces pour l’impression 3 D, contrôler la direction d'extrusion vous permet de créer exactement la forme dont vous avez besoin. Nous parcourrons chaque étape, de l'initialisation d'un profil à l'enregistrement du résultat sous forme de fichier OBJ, afin que vous puissiez également **exporter des fichiers OBJ de modèle 3D** directement depuis Java.

## Réponses rapides
- **Quelle classe effectue l'extrusion linéaire ?** `LinearExtrusion`
- **Quelle méthode définit le vecteur d'extrusion ?** `setDirection(Vector3 direction)`
- **Le résultat peut‑il être enregistré au format OBJ ?** Oui—utilisez `scene.save(..., FileFormat.WAVEFRONTOBJ)`
- **Une licence est‑elle requise pour la production ?** Un essai gratuit est disponible ; une licence est obligatoire pour une utilisation commerciale.
- **Quel IDE fonctionne le mieux avec Aspose.3D ?** IntelliJ IDEA et Eclipse sont entièrement pris en charge.

## Qu'est‑ce que l'extrusion linéaire ?
L'extrusion linéaire est le processus qui consiste à étendre un croquis 2‑D (comme un rectangle ou un cercle) le long d'une ligne droite pour générer un solide 3‑D. Par défaut, l'extrusion suit l'axe Z positif, mais Aspose.3D vous permet de modifier ce chemin avec la propriété `setDirection`, vous offrant un contrôle total sur la géométrie finale.

## Pourquoi changer la direction d'extrusion dans l'extrusion linéaire ?
Changer la direction d'extrusion vous permet d'aligner la nouvelle géométrie avec des objets existants, de créer des composants inclinés sans transformations supplémentaires et de générer des modèles qui correspondent au système de coordonnées requis par les pipelines en aval (par ex., imprimantes 3‑D ou moteurs de jeu). Cela élimine le besoin d'étapes de post‑traitement et réduit la surcharge de taille de fichier jusqu'à 15 % lorsqu'on utilise des vecteurs directionnels qui évitent les rotations inutiles.

## Prérequis
- Connaissances de base en Java.
- Bibliothèque Aspose.3D installée. Vous pouvez la télécharger [ici](https://releases.aspose.com/3d/java/). Vous pouvez également parcourir toutes les versions d'Aspose sur la page principale [ici](https://releases.aspose.com/).
- Un IDE tel qu'Eclipse ou IntelliJ IDEA.

## Importer les packages
L'espace de noms `com.aspose.threed` fournit les classes 3‑D de base ainsi que les types utilitaires.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Étape 1 : Initialiser le profil de base
La classe `RectangleShape` crée le profil 2‑D qui sera extrudé. Un petit rayon d'arrondi donne aux arêtes un aspect lisse.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Étape 2 : Créer une scène
La classe `Scene` est le conteneur de haut niveau d'Aspose.3D qui regroupe tous les nœuds 3‑D, lumières, caméras et matériaux.

```java
Scene scene = new Scene();
```

## Étape 3 : Créer des nœuds
Un `Node` représente un objet dans le graphe de la scène, vous permettant d'attacher géométrie, transformations et autres propriétés.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Étape 4 : Effectuer une extrusion linéaire sur le nœud gauche
`LinearExtrusion` réalise l'opération d'extrusion, convertissant un profil 2‑D en un maillage 3‑D.

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## Étape 5 : Effectuer une extrusion linéaire sur le nœud droit avec direction
Ici nous **changeons la direction d'extrusion**. En passant un `Vector3` personnalisé à `setDirection`, l'extrusion suit le vecteur (0.3, 0.2, 1), produisant une forme inclinée qui s'aligne avec le système de coordonnées de la scène.

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## Étape 6 : Enregistrer la scène 3D
La méthode `save` écrit la scène dans un fichier au format spécifié.

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Problèmes courants et solutions

| Problème | Pourquoi cela se produit | Solution |
|----------|--------------------------|----------|
| Le fichier OBJ apparaît vide | Le profil n'a pas été ajouté à un nœud | Assurez‑vous que `createChildNode` est appelé sur un nœud valide |
| La direction semble inchangée | `setDirection` a été appelé après que l'extrusion était déjà construite | Définissez la direction à l'intérieur de l'initialiseur `LinearExtrusion` comme indiqué |
| Maillage à basse résolution | La valeur de `setSlices` est trop basse | Augmentez le nombre de tranches (par ex., 100 ou plus) |

## Conclusion
Vous savez maintenant **comment changer la direction d'extrusion** dans une extrusion linéaire, comment ajuster les paramètres de torsion et de tranches, et comment **exporter des fichiers OBJ de modèle 3D** à l'aide d'Aspose.3D pour Java. Ces techniques vous offrent un contrôle fin sur la création de géométrie et facilitent l'intégration d'actifs 3‑D dans des pipelines plus larges.

## Questions fréquentes

**Q:** Puis‑je utiliser Aspose.3D avec d'autres langages de programmation ?  
**A:** Oui—Aspose.3D fournit des API pour .NET et Java, permettant le développement multiplateforme.

**Q:** Existe‑t‑il un essai gratuit disponible pour Aspose.3D ?  
**A:** Absolument. Vous pouvez explorer l'ensemble des fonctionnalités avec un essai gratuit [ici](https://releases.aspose.com/).

**Q:** Où puis‑je trouver la documentation détaillée d'Aspose.3D pour Java ?  
**A:** La référence complète est disponible [ici](https://reference.aspose.com/3d/java/).

**Q:** Comment obtenir du support pour Aspose.3D ?  
**A:** Consultez le [forum officiel d'Aspose.3D](https://forum.aspose.com/c/3d/18) pour obtenir de l'aide de la communauté et de l'équipe produit.

**Q:** Des licences temporaires sont‑elles disponibles pour les tests ?  
**A:** Oui—les licences temporaires peuvent être obtenues [ici](https://purchase.aspose.com/temporary-license/).

---

**Dernière mise à jour:** 2026-08-02  
**Testé avec:** Aspose.3D for Java (latest release)  
**Auteur:** Aspose

{{< blocks/products/products-backtop-button >}}

## Tutoriels associés

- [Comment extruder une forme - Créer des modèles 3D avec extrusion linéaire en Java](/3d/java/linear-extrusion/)
- [Créer une extrusion 3D Java avec Aspose.3D](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [Tutoriel Java 3D Graphics – Centre dans l'extrusion linéaire](/3d/java/linear-extrusion/controlling-center/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}