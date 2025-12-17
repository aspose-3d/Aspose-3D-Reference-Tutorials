---
date: 2025-12-17
description: Learn how to create twisted 3D model using Aspose.3D for Java with linear
  extrusion twist and export OBJ file Java. Follow our step‑by‑step guide.
linktitle: Applying Twist in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Créer un modèle 3D torsadé – Appliquer la torsion dans l'extrusion linéaire
  avec Aspose.3D pour Java
url: /fr/java/linear-extrusion/applying-twist/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Appliquer une torsion lors de l'extrusion linéaire avec Aspose.3D pour Java

## Introduction

Bienvenue dans ce tutoriel pas à pas sur **comment créer un modèle 3D tordu** en appliquant une torsion lors de l'extrusion linéaire à l'aide d'Aspose.3D pour Java. Que vous réalisiez des visualisations architecturales, des actifs de jeu ou des prototypes d'ingénierie, ajouter une torsion peut donner à votre géométrie un aspect dynamique et en spirale avec seulement quelques lignes de code.

## Réponses rapides
- **Que signifie « torsion » dans l'extrusion ?** Elle fait pivoter le profil autour de l'axe d'extrusion pendant que la forme est allongée.  
- **Quelle classe API gère la torsion ?** `LinearExtrusion` fournit la méthode `setTwist`.  
- **Ai-je besoin d'une licence pour exécuter l'exemple ?** Un essai gratuit suffit pour l'évaluation ; une licence commerciale est requise pour la production.  
- **Puis-je exporter le résultat au format OBJ ?** Oui, utilisez `scene.save(..., FileFormat.WAVEFRONTOBJ)`.  
- **Quelle version de Java est requise ?** Java 8 ou ultérieure est entièrement prise en charge.

## Prérequis

Avant de plonger dans le tutoriel, assurez‑vous d'avoir les prérequis suivants :

- Environnement de développement Java : assurez‑vous que Java est installé sur votre système.  
- Bibliothèque Aspose.3D : téléchargez et installez la bibliothèque Aspose.3D pour Java depuis le [lien de téléchargement](https://releases.aspose.com/3d/java/).  
- Documentation : consultez la [documentation Aspose.3D](https://reference.aspose.com/3d/java/) pour des instructions complètes.

## Importer les packages

Avant de commencer le processus de codage, importez les packages nécessaires dans votre projet Java. Voici un exemple :

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Définir le répertoire du document

Tout d'abord, définissez où le fichier 3D généré sera enregistré.

```java
// ExStart:SetDocumentDirectory
String MyDir = "Your Document Directory";
// ExEnd:SetDocumentDirectory
```

## Initialiser le profil de base

Ensuite, créez la forme qui sera extrudée. Dans cet exemple, nous utilisons un rectangle avec un petit rayon d'arrondi.

```java
// ExStart:InitializeBaseProfile
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
// ExEnd:InitializeBaseProfile
```

## Créer une scène

Un objet `Scene` agit comme conteneur pour tous les nœuds 3D.

```java
// ExStart:CreateScene
Scene scene = new Scene();
// ExEnd:CreateScene
```

## Créer des nœuds

Ajoutez deux nœuds enfants à la scène – l'un restera droit, l'autre recevra la torsion.

```java
// ExStart:CreateNodes
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
// ExEnd:CreateNodes
```

## Torsion d'extrusion linéaire

Nous effectuons maintenant la **torsion d'extrusion linéaire** sur les deux nœuds. Le nœud de gauche reçoit une torsion de 0° (droit), tandis que le nœud de droite reçoit une torsion de 90°, créant une forme en spirale. Nous définissons également le nombre de tranches pour garantir une géométrie lisse.

```java
// ExStart:LinearExtrusionWithTwist
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(0); setSlices(100); }});
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(90); setSlices(100); }});
// ExEnd:LinearExtrusionWithTwist
```

## Exporter le fichier OBJ en Java

Enfin, enregistrez la scène au format OBJ largement supporté. Cela démontre la capacité **export OBJ file Java** d'Aspose.3D.

```java
// ExStart:Save3DScene
scene.save(MyDir + "TwistInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:Save3DScene
```

## Pourquoi c'est important

Créer un modèle 3D tordu vous offre un effet visuel puissant sans nécessiter d'outils de modélisation externes. C’est particulièrement utile pour :

- **Pièces mécaniques** nécessitant des caractéristiques hélicoïdales (par ex., ressorts, vis).  
- **Designs artistiques** où une spirale subtile ajoute de l'intérêt visuel.  
- **Actifs de jeu** qui bénéficient d'une géométrie low‑poly générée procéduralement.

## Problèmes courants & astuces

| Problème | Solution |
|----------|----------|
| La torsion apparaît plate ou manquante | Assurez‑vous que `setSlices` est suffisamment élevé (par ex., 100) pour une rotation fluide. |
| Le fichier OBJ ne s'ouvre pas dans le visualiseur | Vérifiez que le chemin de sortie (`MyDir`) est correct et que le fichier possède les permissions d'écriture. |
| Mise à l'échelle inattendue | Vérifiez le système d'unités de votre profil source ; Aspose.3D fonctionne en mètres par défaut. |

## Questions fréquemment posées

**Q : Puis‑je utiliser Aspose.3D pour Java avec d'autres formats de fichiers 3D ?**  
R : Oui, Aspose.3D prend en charge un large éventail de formats tels que FBX, STL, 3MF, et plus encore.

**Q : Où puis‑je trouver du support pour Aspose.3D pour Java ?**  
R : Consultez le [forum Aspose.3D](https://forum.aspose.com/c/3d/18) pour l'aide de la communauté et l'assistance officielle.

**Q : Une version d'essai gratuite est‑elle disponible ?**  
R : Oui, vous pouvez télécharger une version d'essai depuis [ici](https://releases.aspose.com/).

**Q : Comment obtenir une licence temporaire pour les tests ?**  
R : Obtenez une licence temporaire sur la [page de licence temporaire](https://purchase.aspose.com/temporary-license/).

**Q : Où puis‑je acheter une licence complète ?**  
R : Achetez Aspose.3D pour Java depuis la [page d'achat](https://purchase.aspose.com/buy).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Dernière mise à jour :** 2025-12-17  
**Testé avec :** Aspose.3D 24.11 pour Java  
**Auteur :** Aspose  

---