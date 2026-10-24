---
date: 2026-10-24
description: Apprenez à exporter des fichiers OBJ et à modifier l'orientation du plan
  en Java avec Aspose.3D. Ce guide étape par étape montre comment créer un plan incliné
  et exporter un modèle 3D OBJ.
keywords:
- how to export obj
- create sloped plane
- export 3d model obj
- adjust plane orientation
lastmod: 2026-10-24
linktitle: Comment exporter OBJ et modifier l'orientation du plan en Java
og_description: Apprenez à exporter OBJ et à modifier l'orientation du plan en Java
  avec Aspose.3D. Suivez ce guide pour créer un plan incliné et exporter efficacement
  un modèle 3D OBJ.
og_image_alt: 'Tutorial: export OBJ and adjust plane orientation in Java with Aspose.3D'
og_title: Comment exporter OBJ et modifier l'orientation du plan en Java
schemas:
- author: Aspose
  dateModified: '2026-10-24'
  description: Learn how to export OBJ files and change plane orientation in Java
    using Aspose.3D. This step‑by‑step guide shows creating a sloped plane and exporting
    a 3D model OBJ.
  headline: How to export OBJ and change plane orientation in Java
  type: TechArticle
- description: Learn how to export OBJ files and change plane orientation in Java
    using Aspose.3D. This step‑by‑step guide shows creating a sloped plane and exporting
    a 3D model OBJ.
  name: How to export OBJ and change plane orientation in Java
  steps:
  - name: set document directory path
    text: Define where the exported OBJ file will be saved. ` Replace `"Your Document
      Directory"` with the absolute path on your machine (e.g., `C:/3DOutputs/`).
  - name: initialize the scene – create 3D scene
    text: Create a fresh `Scene` object that will hold all geometry. `
  - name: initialize the plane – how to modify plane
    text: Instantiate a `Plane` object that we will later orient. `
  - name: set vector – how to set plane up
    text: Define a custom up‑vector for the plane. This is the core of **change plane
      orientation**. The vector `(1, 1, 3)` tilts the plane away from the default
      XY‑plane, giving you a sloped surface you can later **export OBJ**.
  - name: complete the plane orientation and export
    text: After this call, you’ll find `ChangePlaneOrientation.obj` in the directory
      you specified, ready for any **Aspose.3D export OBJ** workflow. Aspose.3D supports
      over 30 output formats—including OBJ, FBX, STL, and more—so you can switch formats
      with a single enum change.
  type: HowTo
- questions:
  - answer: Yes, Aspose.3D provides APIs for Java, .NET, and other platforms, each
      offering the same feature set.
    question: Can I use Aspose.3D for Java with other programming languages?
  - answer: Certainly! You can explore the features of Aspose.3D by accessing the
      free trial [here](https://releases.aspose.com/).
    question: Is a free trial available for Aspose.3D?
  - answer: For any queries or assistance, visit our [support forum](https://forum.aspose.com/c/3d/18).
    question: Where can I find support for Aspose.3D?
  - answer: To purchase Aspose.3D, visit our [buy page](https://purchase.aspose.com/buy).
    question: How can I purchase Aspose.3D?
  - answer: Yes, if you need a temporary license, you can obtain one [here](https://purchase.aspose.com/temporary-license/).
    question: Is there a temporary license option?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- export obj
- Aspose.3D
- Java 3D
- plane orientation
- 3D modeling
title: Comment exporter OBJ et modifier l'orientation du plan en Java
url: /fr/java/3d-scenes-and-models/change-plane-orientation/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Comment exporter OBJ et modifier l'orientation du plan en Java

## Introduction

Dans ce tutoriel, vous apprendrez **comment exporter OBJ** et modifier l'orientation du plan en Java en utilisant l'API Aspose.3D. Ajuster le vecteur up d'un plan vous donne un contrôle précis sur le placement des objets dans un flux de travail **création de scène 3D** — parfait pour les jeux, les simulations et les visualisations architecturales où le positionnement exact est crucial. L'API Aspose.3D pour Java est disponible sur la page de téléchargement principale d'Aspose [ici](https://releases.aspose.com/).

## Réponses rapides
- **Que signifie « exporter OBJ » ?** Cela signifie convertir une scène 3D au format Wavefront OBJ, un type de fichier maillage universellement supporté.  
- **Pourquoi ajuster l'orientation du plan ?** Modifier le vecteur up du plan vous permet d'aligner la géométrie exactement où vous le souhaitez dans la scène.  
- **Ai-je besoin d'une licence pour exécuter le code ?** Un essai gratuit suffit pour le développement ; une licence commerciale est requise pour la production.  
- **Quelle version de Java est prise en charge ?** Aspose.3D fonctionne avec Java 8 et les versions ultérieures.  
- **Puis-je exporter d'autres formats ?** Oui — l'API prend également en charge FBX, STL, et plus encore.

## Qu’est‑ce que « modifier l'orientation du plan » ?

Modifier l'orientation du plan signifie ajuster le vecteur up du plan afin que le plan s'incline par rapport au plan XY par défaut, vous permettant de créer des surfaces inclinées telles que des rampes, des toits ou des plans de référence personnalisés. Cette opération influence directement la façon dont la géométrie est positionnée avant que vous **exportiez OBJ**.

## Pourquoi modifier l'orientation du plan ?

Modifier l'orientation du plan vous permet d'aligner les objets avec des axes personnalisés, de simuler des surfaces inclinées et de garantir que le maillage OBJ exporté reflète l'intention visuelle de votre conception. Utiliser un vecteur up personnalisé améliore la précision du placement et réduit considérablement le temps de post‑édition après l'exportation pour les développeurs.

## Prérequis

Avant de commencer, assurez‑vous d'avoir :

- Une compréhension de base de la programmation Java.  
- Aspose.3D pour Java installé — téléchargez-le [ici](https://releases.aspose.com/3d/java/).  
- Un IDE Java ou un outil de construction (par ex., IntelliJ IDEA, Maven ou Gradle) prêt pour le codage.

## Importer les packages

Les importations suivantes vous donnent accès aux classes principales d'Aspose.3D.

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Plane;
import com.aspose.threed.Scene;
import com.aspose.threed.Vector3;

import java.io.IOException;
```

La classe `Plane` représente un plan géométrique qui peut être positionné et orienté dans l'espace 3D.  
La classe `Vector3` définit un vecteur tridimensionnel utilisé pour les directions et les positions.  
La classe `Scene` est un conteneur qui contient tous les objets 3D, lumières et caméras d'un modèle.  
L'énumération `FileFormat` spécifie le format de fichier de sortie pour enregistrer une scène.

## Guide étape par étape

### Étape 1 : définir le chemin du répertoire du document
Définissez où le fichier OBJ exporté sera enregistré.

````java
String MyDir = "Your Document Directory";
````

Remplacez `"Your Document Directory"` par le chemin absolu sur votre machine (par ex., `C:/3DOutputs/`).

### Étape 2 : initialiser la scène – créer une scène 3D
Créez un nouvel objet `Scene` qui contiendra toute la géométrie.

````java
Scene scene = new Scene();
````

### Étape 3 : initialiser le plan – comment modifier le plan
Instanciez un objet `Plane` que nous orienterons plus tard.

````java
Plane plane = new Plane();
````

### Étape 4 : définir le vecteur – comment définir l'up du plan
Définissez un vecteur up personnalisé pour le plan. C’est le cœur de **modifier l'orientation du plan**.  
Le vecteur `(1, 1, 3)` incline le plan par rapport au plan XY par défaut, vous offrant une surface inclinée que vous pourrez ensuite **exporter OBJ**.

### Étape 5 : finaliser l'orientation du plan et exporter  

```java
// ExStart:ChangePlaneOrientation
try {
    plane.setUp(new Vector3(1, 1, 3));
    
    scene.getRootNode().createChildNode(plane);
    
    scene.save(MyDir + "ChangePlaneOrientation.obj", FileFormat.WAVEFRONTOBJ);
} catch (IOException e) {
    e.printStackTrace();
}
// ExEnd:ChangePlaneOrientation
```

Après cet appel, vous trouverez `ChangePlaneOrientation.obj` dans le répertoire que vous avez spécifié, prêt pour tout flux de travail **Aspose.3D export OBJ**. Aspose.3D prend en charge plus de 30 formats de sortie — y compris OBJ, FBX, STL, et plus — vous pouvez donc changer de format avec un simple changement d'énumération.

## Problèmes courants et solutions

| Problème | Pourquoi cela se produit | Solution |
|----------|--------------------------|----------|
| **Erreur « Fichier non trouvé » lors de l'enregistrement** | `MyDir` n'existe pas ou n'a pas les permissions d'écriture | Créez le dossier au préalable ou utilisez un chemin absolu avec les permissions appropriées. |
| Le plan apparaît plat dans le visualiseur | Le vecteur est colinéaire avec le vecteur up par défaut | Choisissez un vecteur non parallèle (par ex., `(1, 0, 1)`) pour voir une inclinaison visible. |
| Le fichier OBJ se charge avec des textures manquantes | Les textures n'ont jamais été ajoutées à la scène | Attachez le matériau/la texture à la géométrie avant l'exportation si nécessaire. |

## Questions fréquentes

**Q : Puis-je utiliser Aspose.3D pour Java avec d'autres langages de programmation ?**  
R : Oui, Aspose.3D fournit des API pour Java, .NET et d'autres plateformes, chacune offrant le même ensemble de fonctionnalités.

**Q : Une version d'essai gratuite est‑elle disponible pour Aspose.3D ?**  
R : Bien sûr ! Vous pouvez explorer les fonctionnalités d'Aspose.3D en accédant à l'essai gratuit [ici](https://releases.aspose.com/).

**Q : Où puis‑je trouver du support pour Aspose.3D ?**  
R : Pour toute question ou assistance, visitez notre [forum de support](https://forum.aspose.com/c/3d/18).

**Q : Comment puis‑je acheter Aspose.3D ?**  
R : Pour acheter Aspose.3D, visitez notre [page d'achat](https://purchase.aspose.com/buy).

**Q : Existe‑t‑il une option de licence temporaire ?**  
R : Oui, si vous avez besoin d'une licence temporaire, vous pouvez en obtenir une [ici](https://purchase.aspose.com/temporary-license/).

**Q : Puis‑je exporter la scène vers d'autres formats que OBJ ?**  
R : Absolument. La méthode `Scene.save` prend en charge FBX, STL et plusieurs autres formats — il suffit de changer l'énumération `FileFormat`.

## Conclusion

En définissant un vecteur up personnalisé, vous pouvez modifier l'orientation du plan pour créer une géométrie inclinée puis exporter le résultat en fichier OBJ en quelques lignes de code. Cette approche garantit que vos modèles 3D conservent l'inclinaison prévue et sont prêts pour les pipelines en aval tels que les moteurs de jeu, les outils CAO ou les visualiseurs web.

---

**Last Updated:** 2026-10-24  
**Tested With:** Aspose.3D for Java 24.11  
**Author:** Aspose

## Tutoriels associés

- [Exporter le modèle en FBX avec des quaternions en Java utilisant Aspose.3D](/3d/java/geometry/transform-3d-nodes-with-quaternions/)
- [Apprendre à exporter des fichiers PLY en Java avec Aspose.3D – comment exporter ply](/3d/java/point-clouds/ply-export-point-clouds-java/)
- [Enregistrer des scènes 3D en Java avec Aspose.3D – Convertir les fichiers 3D efficacement](/3d/java/load-and-save/save-3d-scenes/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}