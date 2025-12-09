---
date: 2025-12-09
description: Apprenez à ajouter un nœud enfant, à positionner des objets 3D et à enregistrer
  la scène au format OBJ tout en créant des cylindres ventilateurs personnalisés avec
  Aspose.3D pour Java.
language: fr
linktitle: Adding Child Node for Fan Cylinders with Aspose.3D Java
second_title: Aspose.3D Java API
title: Ajouter un nœud enfant pour créer des cylindres en éventail avec Aspose.3D
  pour Java
url: /java/cylinders/creating-fan-cylinders/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Ajouter un nœud enfant pour créer des cylindres ventilateurs avec Aspose.3D pour Java

## Introduction

Prêt à **add child node** à une scène 3‑D et à créer des cylindres ventilateurs accrocheurs ? Dans ce tutoriel, nous parcourrons chaque étape — de la configuration de la scène, du positionnement des objets 3D, jusqu’à **save scene as OBJ** — en utilisant Aspose.3D pour Java. Que vous peaufiniez un actif de jeu ou construisiez un prototype rapide, les concepts présentés vous offriront un contrôle solide sur vos modèles 3‑D.

## Réponses rapides
- **Que fait « add child node » ?** Il insère un nouvel objet dans le graphe de scène, héritant des transformations de son parent.  
- **Comment positionner un objet 3D ?** En appliquant une translation (ou rotation/échelle) à la transformation du nœud.  
- **Quel format de fichier est utilisé pour l’exportation ?** L’exemple enregistre le modèle au format Wavefront OBJ.  
- **Ai‑je besoin d’une licence pour exécuter le code ?** Un essai gratuit suffit pour l’évaluation ; une licence est requise pour la production.  
- **Quel IDE est le plus adapté ?** Tout IDE Java (IntelliJ IDEA, Eclipse, VS Code) supportant JDK 8+.

## Qu’est‑ce que « add child node » dans Aspose.3D ?
Ajouter un nœud enfant signifie créer un nouveau nœud sous un parent existant dans la hiérarchie de la scène. L’enfant hérite du système de coordonnées du parent, ce qui facilite le **position 3d object** relatif entre plusieurs instances.

## Pourquoi ajouter un nœud enfant lors de la création de cylindres ventilateurs ?
- **Conception modulaire :** chaque cylindre (ventilateur ou non) vit dans son propre nœud, simplifiant les modifications ultérieures.  
- **Héritage des transformations :** déplacer, faire pivoter ou mettre à l’échelle le parent entraîne automatiquement tous les enfants.  
- **Graphe de scène plus propre :** améliore la lisibilité et le débogage de modèles complexes.

## Prérequis

- **Java Development Kit (JDK)** – téléchargez‑le depuis le [official site](https://www.oracle.com/java/technologies/javase-downloads.html).  
- **Aspose.3D for Java** – obtenez la dernière bibliothèque via le [download link](https://releases.aspose.com/3d/java/).

## Import Packages

Commencez par importer les packages nécessaires dans votre projet Java. Cette étape est cruciale pour accéder aux fonctionnalités fournies par Aspose.3D.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Étape 1 : créer une scène

Tout d’abord, nous créons une scène 3‑D vide qui accueillera tous nos objets.

```java
// ExStart:2
// Create a Scene
Scene scene = new Scene();
// ExEnd:2
```

## Étape 2 : créer un cylindre ventilateur

Ensuite, nous construisons un cylindre qui sera rendu comme un ventilateur (balayage partiel).

```java
// ExStart:3
// Create a cylinder with fan
Cylinder fan = new Cylinder(2, 2, 10, 20, 1, false);
fan.setGenerateFanCylinder(true);
fan.setThetaLength(MathUtils.toRadian(270.0));
// ExEnd:3
```

## Étape 3 : ajouter un nœud enfant et positionner l’objet 3D

Nous **add child node** maintenant à la scène et **position the 3d object** en définissant sa translation. C’est à ce moment que le cylindre ventilateur devient partie du graphe de scène.

```java
// ExStart:4
// Create ChildNode and set translation
scene.getRootNode().createChildNode(fan).getTransform().setTranslation(10, 0, 0);
// ExEnd:4
```

## Étape 4 : créer un cylindre non‑ventilateur

Pour montrer la flexibilité d’Aspose.3D, nous créons également un cylindre standard sans ventilateur et l’ajoutons comme un autre nœud enfant.

```java
// ExStart:5
// Create a cylinder without a fan
Cylinder nonfan = new Cylinder(2, 2, 10, 20, 1, false);
// Create ChildNode
scene.getRootNode().createChildNode(nonfan);
// ExEnd:5
```

## Étape 5 : enregistrer la scène au format OBJ

Enfin, nous **save scene as OBJ** afin que vous puissiez visualiser le résultat dans n’importe quel visualiseur 3‑D standard.

```java
// ExStart:6
// Save scene
scene.save("Your Document Directory" + "CreateFanCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

Félicitations ! Vous avez **added child node** avec succès, positionné vos objets et exporté le modèle.

## Problèmes courants et astuces

| Problème | Solution |
|----------|----------|
| **File not found** when saving | Assurez‑vous que le répertoire cible existe et que vous disposez des permissions d’écriture. |
| **Cylinder appears flat** | Vérifiez les valeurs de rayon et de hauteur ; Aspose.3D attend des unités à la même échelle. |
| **Fan slice looks incomplete** | Ajustez `ThetaLength` (en radians) pour couvrir l’angle souhaité. |
| **Scene not visible in viewer** | Confirmez que le fichier OBJ a été enregistré avec le fichier `.mtl` (matériau) associé si nécessaire. |

## Questions fréquentes

**Q :** *Aspose.3D est‑il compatible avec d’autres bibliothèques Java pour la modélisation 3D ?*  
**R :** Oui, Aspose.3D fonctionne en parallèle avec d’autres bibliothèques Java 3‑D, vous permettant de combiner les fonctionnalités selon vos besoins.

**Q :** *Puis‑je personnaliser davantage l’apparence des cylindres ventilateurs générés ?*  
**R :** Absolument. Vous pouvez appliquer des matériaux, des textures et de l’éclairage à l’aide des classes `Material` et `Light`.

**Q :** *Où puis‑je trouver un support supplémentaire ou de l’aide pour Aspose.3D ?*  
**R :** Visitez le [Aspose.3D forum](https://forum.aspose.com/c/3d/18) pour l’aide de la communauté et les réponses officielles.

**Q :** *Existe‑t‑il un essai gratuit disponible pour Aspose.3D ?*  
**R :** Oui, vous pouvez explorer Aspose.3D avec un [free trial](https://releases.aspose.com/) avant d’acheter.

**Q :** *Comment obtenir une licence temporaire pour Aspose.3D ?*  
**R :** Obtenez une licence temporaire [ici](https://purchase.aspose.com/temporary-license/) pour les tests et le développement.

## Conclusion

Dans ce guide, nous avons démontré comment **add child node**, **position 3d object**, et **save scene as OBJ** tout en créant des cylindres ventilateurs personnalisés avec Aspose.3D pour Java. Ces blocs de construction vous offrent la flexibilité nécessaire pour construire des hiérarchies 3‑D complexes et les exporter vers n’importe quel flux de travail en aval.

---

**Last Updated:** 2025-12-09  
**Tested With:** Aspose.3D 24.12 for Java  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}