---
date: 2025-12-18
description: Apprenez comment ajouter un plan de sol et définir la propriété centre
  lors d’une extrusion linéaire avec Aspose.3D pour Java, avec des exemples de code
  étape par étape.
linktitle: Controlling Center in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Comment ajouter un plan de sol et un centre de contrôle dans une extrusion
  linéaire avec Aspose.3D pour Java
url: /fr/java/linear-extrusion/controlling-center/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Contrôle du centre dans l'extrusion linéaire avec Aspose.3D pour Java

## Introduction

Lorsque vous créez des scènes 3D en Java, la capacité d'**ajouter un plan de sol** tout en définissant précisément la **propriété centre** sur une extrusion linéaire peut faire la différence entre un prototype plat et un rendu poli. Dans ce tutoriel, nous parcourrons le processus complet de contrôle du centre d'extrusion et d'ajout d'un plan de sol à l'aide d'Aspose.3D pour Java. Vous verrez pourquoi cela importe, comment le configurer, et obtenir un exemple de code prêt à l'exécution que vous pourrez adapter à vos propres projets.

## Quick Answers
- **Que fait « ajouter un plan de sol » ?** Il crée une géométrie de référence fine qui vous aide à voir la position de l'extrusion par rapport aux axes du monde.  
- **Comment définir le centre d'une extrusion linéaire ?** Utilisez la méthode `setCenter(boolean)` sur l'objet `LinearExtrusion`.  
- **Ai‑je besoin d'une licence pour exécuter l'exemple ?** Une licence temporaire suffit pour les tests ; une licence complète est requise pour la production.  
- **Quel format de fichier est utilisé pour l'enregistrement ?** L'exemple enregistre au format Wavefront OBJ (`.obj`).  
- **Quelle version de Java est requise ?** Java 8 ou ultérieure suffit.

## Qu'est-ce que « ajouter un plan de sol » dans une scène 3D ?

Ajouter un plan de sol consiste à insérer une géométrie rectangulaire fine (souvent une boîte à épaisseur minimale) qui repose sur le plan X‑Z. Il sert de sol visuel, facilitant l'évaluation de la hauteur et de l'alignement des autres objets, surtout lorsque vous expérimentez les centres d'extrusion.

## Pourquoi définir la propriété centre sur une extrusion linéaire ?

Par défaut, une extrusion linéaire démarre à l'origine du profil. Définir la propriété centre (`setCenter(true)`) décale le profil de façon que l'extrusion soit centrée autour de l'origine, ce qui est utile pour les conceptions symétriques ou lorsque vous avez besoin d'un alignement cohérent entre plusieurs objets.

## Prérequis

Avant de commencer ce tutoriel, assurez‑vous d'avoir les prérequis suivants :

1. **Environnement de développement Java** – Assurez‑vous d'avoir un environnement de développement Java installé sur votre machine.  
2. **Aspose.3D pour Java** – Téléchargez et installez la bibliothèque Aspose.3D. Vous pouvez trouver la bibliothèque et sa documentation [ici](https://reference.aspose.com/3d/java/).  
3. **Répertoire de documents** – Créez un répertoire pour stocker vos documents Java. Appelons‑le « Your Document Directory ».

## Importer les packages

Dans votre environnement de développement Java, importez les packages nécessaires pour Aspose.3D. Cela garantit que votre code a accès aux fonctionnalités fournies par la bibliothèque.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Étape 1 : Configurer le profil de base

Initialisez le profil de base à extruder. Dans cet exemple, nous utiliserons une forme rectangulaire avec un rayon d'arrondi de 0,3.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Étape 2 : Créer une scène 3D

Construisez les fondations de votre monde 3D en créant une scène.

```java
Scene scene = new Scene();
```

## Étape 3 : Créer les nœuds gauche et droit

Établissez les nœuds gauche et droit dans votre scène. Ces nœuds servent de canevas pour vos objets 3D.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Étape 4 : Extrusion linéaire avec la propriété centre (nœud gauche)

Effectuez une extrusion linéaire sur le nœud gauche **sans centrage** et définissez le nombre de tranches à 3. Remarquez l'appel `setCenter(false)` – c'est ici que nous **définissons la propriété centre** à *false*.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

## Étape 5 : Ajouter un plan de sol pour référence (nœud gauche)

Améliorez la représentation visuelle en **ajoutant un plan de sol** au nœud gauche. La boîte fine agit comme un sol afin que vous puissiez clairement voir la hauteur de l'extrusion.

```java
left.createChildNode(new Box(0.01, 3, 3));
```

## Étape 6 : Extrusion linéaire avec la propriété centre (nœud droit)

Effectuez maintenant une extrusion linéaire sur le nœud droit, cette fois **en centrant l'extrusion**. L'appel `setCenter(true)` montre comment **définir la propriété centre** à *true*.

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

## Étape 7 : Ajouter un plan de sol pour référence (nœud droit)

Tout comme du côté gauche, ajoutez un plan de sol au nœud droit pour une base visuelle cohérente.

```java
right.createChildNode(new Box(0.01, 3, 3));
```

## Étape 8 : Enregistrer la scène 3D

Enregistrez votre scène 3D au format Wavefront OBJ afin de pouvoir la visualiser dans n'importe quel visualiseur 3D standard.

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Problèmes courants et solutions

| Problème | Pourquoi cela se produit | Solution |
|----------|--------------------------|----------|
| Le plan de sol n'est pas visible | L'épaisseur de la boîte est trop petite pour l'échelle du visualiseur. | Augmentez l'épaisseur (premier paramètre de `Box`) ou dézoomez dans le visualiseur. |
| L'extrusion apparaît décalée | La valeur de `setCenter` n'est pas définie comme prévu. | Vérifiez le booléen passé à `setCenter`. |
| Le fichier n'est pas enregistré | Chemin du répertoire incorrect ou permissions d'écriture manquantes. | Vérifiez que `MyDir` pointe vers un dossier existant avec accès en écriture. |

## Questions fréquentes

**Q1 : Puis‑je utiliser Aspose.3D pour Java dans des projets commerciaux ?**  
R1 : Oui, Aspose.3D pour Java est disponible pour une utilisation commerciale. Pour les détails de licence, visitez [ici](https://purchase.aspose.com/buy).

**Q2 : Existe‑t‑il un essai gratuit ?**  
R2 : Oui, vous pouvez explorer un essai gratuit d'Aspose.3D pour Java [ici](https://releases.aspose.com/).

**Q3 : Où puis‑je trouver du support pour Aspose.3D pour Java ?**  
R3 : Le forum communautaire Aspose.3D est un excellent endroit pour obtenir du support et partager vos expériences. Visitez le forum [ici](https://forum.aspose.com/c/3d/18).

**Q4 : Ai‑je besoin d'une licence temporaire pour les tests ?**  
R4 : Oui, si vous avez besoin d'une licence temporaire à des fins de test, vous pouvez en obtenir une [ici](https://purchase.aspose.com/temporary-license/).

**Q5 : Où puis‑je documentation ?**  
R5 : La documentation d'Aspose.3D pour Java est disponible [ici](https://reference.aspose.com/3d/java/).

## Conclusion

Contrôler le centre dans une extrusion linéaire **et** apprendre à **ajouter un plan de sol** avec Aspose.3D pour Java ouvre des possibilités passionnantes dans le développement graphique 3D. En suivant les étapes ci‑dessus, vous disposez désormais d'un modèle réutilisable pour créer des extrusions centrées, des plans de référence visuels, et exporter le résultat au format OBJ. N'hésitez pas à expérimenter avec différents profils, nombres de tranches et transformations pour répondre aux besoins de votre projet.

---

**Dernière mise à jour :** 2025-12-18  
**Testé avec :** Aspose.3D 24.11 for Java (latest at time of writing)  
**Auteur :** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}