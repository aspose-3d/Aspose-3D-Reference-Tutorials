---
date: 2026-02-20
description: Apprenez à créer une scène 3D et à appliquer une torsion d'extrusion
  linéaire avec Aspose.3D pour Java. Exportez des fichiers OBJ grâce à un guide étape
  par étape facile.
linktitle: Create 3D Scene with Twist in Linear Extrusion – Aspose.3D for Java
second_title: Aspose.3D Java API
title: Créer une scène 3D avec torsion dans l'extrusion linéaire – Aspose.3D pour
  Java
url: /fr/java/linear-extrusion/applying-twist/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Créer une scène 3D avec torsion dans l'extrusion linéaire – Aspose.3D pour Java

## Introduction

Dans ce tutoriel pratique **java 3d tutoriel**, vous apprendrez à **créer des objets de scène 3d**, appliquer une *torsion d'extrusion linéaire*, et enfin **exporter des fichiers obj java** à l'aide d'Aspose.3D pour Java. Que vous créiez un élément de jeu, un prototype CAO ou un effet visuel, ajoutez une torsion lors de l'extrusion donne à vos modèles une apparence dynamique, en forme de spirale, difficile à obtenir avec une extrusion simple.

## Réponses rapides
- **Qu'est-ce que signifie « twist » (torsion) dans l'extrusion ?** Elle fait pivoter le profil progressivement le long du chemin d'extrusion.
- **Quelle bibliothèque fournit la fonction de torsion ?** Aspose.3D pour Java.
- **Puis-je exporter le résultat au format OBJ ?** Oui – utilisez `FileFormat.WAVEFRONTOBJ`.
- **Ai-je besoin d'une licence pour ce tutoriel ?** Une licence temporaire ou complète est requise pour une utilisation en production.
- **Quelle version de Java est requise ?** Java8 ou supérieure.

## Qu'est-ce qu'une « torsion » dans l'extrusion linéaire ?

Une torsion est une transformation qui fait pivoter chaque tranche de la forme extrudée d'un angle spécifié. En contrôlant cet angle, vous pouvez créer des spirales, des vis sans fin ou des torsions subtiles qui ajoutent de l'intérêt visuel aux extrusions autrement des plaques.

## Pourquoi utiliser Aspose.3D pour Java ?

- **Support multi‑format :** Importez et exportez des dizaines de formats 3D, y compris OBJ, FBX et STL.
- **API Java pure :** Aucune dépendance native, ce qui facilite l'intégration dans n'importe quel projet Java.
- **Moteur géométrique haute performance :** Gère des opérations complexes comme la torsion sans sacrifier la vitesse.

## Prérequis

- **Java Development Kit (JDK) 8+** installé sur votre machine.
- **Aspose.3D for Java** – téléchargez depuis le [download link](https://releases.aspose.com/3d/java/).
- Familiarité avec la syntaxe Java de base et les concepts 3‑D.
- Accès à la documentation officielle [Documentation Aspose.3D](https://reference.aspose.com/3d/java/) pour référence.

## Importer des packages

Tout d’abord, intégrez les classes Aspose.3D requises dans votre projet.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Étape 1 : Définir le répertoire du document

Indiquez l’emplacement où le fichier OBJ généré sera enregistré. Remplacez l’espace réservé par un chemin d’accès réel sur votre système.

```java
// ExStart:SetDocumentDirectory
String MyDir = "Your Document Directory";
// ExEnd:SetDocumentDirectory
```

## Étape 2 : Initialiser le profil de base

Créez la forme à extruder. Ici, nous utilisons un rectangle avec un petit rayon d’arrondi pour adoucir les bords.

```java
// ExStart:InitializeBaseProfile
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
// ExEnd:InitializeBaseProfile
```

## Étape 3 : Créer une scène pour vos nœuds

Un objet `Scene` est le conteneur de toutes les entités 3D (maillages, lumières, caméras, etc.). 

```java
// ExStart:CreateScene
Scene scene = new Scene();
// ExEnd:CreateScene
```

## Étape 4 : Ajouter les nœuds gauche et droit

Nous allons créer deux nœuds frères : un sans torsion (pour comparaison) et un avec une torsion de 90 degrés.

```java
// ExStart:CreateNodes
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
// ExEnd:CreateNodes
```

## Étape 5 : Effectuer une extrusion linéaire avec torsion

Le constructeur `LinearExtrusion` prend en paramètres le profil et la longueur d’extrusion.

- `setTwist(0)` → aucune rotation (extrusion rectiligne).

- `setTwist(90)` → rotation complète de 90 degrés sur toute la longueur.

Les deux nœuds utilisent 100 tranches pour une géométrie lisse.

```java
// ExStart:LinearExtrusionWithTwist
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(0); setSlices(100); }});
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(90); setSlices(100); }});
// ExEnd:LinearExtrusionWithTwist
```

## Étape 6 : Enregistrer la scène 3D au format OBJ

Enfin, enregistrez la scène dans un fichier OBJ afin de pouvoir la visualiser dans n’importe quel visualiseur 3D standard.

```java
// ExStart:Save3DScene
scene.save(MyDir + "TwistInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:Save3DScene
```

## Problèmes courants et conseils

- **Erreurs de chemin de fichier :** Assurez-vous que `MyDir` se termine par un séparateur de chemin (`/` ou `\\`) adapté à votre OS.
- **Angle de torsion trop élevé :** Les angles supérieurs à 360° peuvent provoquer un chevauchement de la géométrie ; maintenir-le entre 0‑360° pour des résultats prévisibles.
- **Performance :** Augmenter `setSlices` améliore la fluidité mais peut impacter la mémoire ; 100 tranches constituant un bon compromis dans la plupart des cas.

## Foire aux questions (original)

### Q1 : Puis-je utiliser Aspose.3D pour Java avec d'autres formats de fichiers 3D ?

A1 : Oui, Aspose.3D prend en charge divers formats de fichiers 3D, vous permettant d'importer, d'exporter et de manipuler différents types de fichiers.

### Q2 : Où puis‑je trouver du support pour Aspose.3D pour Java ?

A2 : Visitez le [forum Aspose.3D](https://forum.aspose.com/c/3d/18) pour le support communautaire et les discussions.

### Q3 : Existe-t-il une version d'essai gratuite pour Aspose.3D pour Java ?

A3 : Oui, vous pouvez accéder à la version d'essai gratuite depuis [ici](https://releases.aspose.com/).

### Q4 : Comment obtenir une licence temporaire pour Aspose.3D pour Java ?

A4 : Obtenez une licence temporaire sur la [page de licence temporaire](https://purchase.aspose.com/temporary-license/).

### Q5 : Où puis-je acheter Aspose.3D pour Java ?

A5 : Achetez Aspose.3D pour Java sur la [page d'achat](https://purchase.aspose.com/buy).

## FAQ supplémentaire (optimisée par l'IA)

**Q : Puis‑je changer la direction de la torsion?**
R : Oui – utilisez un angle négatif dans `setTwist()` pour tourner dans la direction opposée.

**Q : Est‑il possible d'appliquer différentes valeurs de torsion le long de l'extrusion ?**
A : Aspose.3D applique actuellement une torsion uniforme ; pour une torsion variable, vous devez générer plusieurs segments manuellement.

**Q : Comment visualiser le fichier OBJ exporté ?**
R : Tout visualiseur 3‑D standard (par ex., Blender, MeshLab) peut ouvrir les fichiers OBJ.

**Q : La bibliothèque prend‑elle en charge le mappage de textures sur les extrusions tordues ?**
R : Oui – après l'extrusion, vous pouvez assigner des matériaux ou des coordonnées UV au maillage du nœud.

## Conclusion

Vous avez maintenant **créé une scène 3D**, appliqué une **torsion d'extrusion linéaire**, et exporté le résultat sous forme de fichier OBJ à l'aide d'Aspose.3D pour Java. Expérimentez avec différents profils, angles de torsion et nombres de tranches pour créer des géométries uniques pour les jeux, les simulations ou l'impression 3D.

---

**Dernière mise à jour :** 2026-02-20  
**Testé avec :** Aspose.3D for Java 24.11  
**Auteur :** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}