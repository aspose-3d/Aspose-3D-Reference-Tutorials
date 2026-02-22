---
date: 2026-02-22
description: Apprenez à créer une extrusion 3D avec des tranches en utilisant Aspose.3D
  pour Java. Ce guide étape par étape couvre l'extrusion linéaire, la définition du
  rayon d'arrondi et l'exportation OBJ.
linktitle: Create 3D Extrusion with Slices – Aspose.3D for Java
second_title: Aspose.3D Java API
title: Créer une extrusion 3D avec des tranches – Aspose.3D pour Java
url: /fr/java/linear-extrusion/specifying-slices/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Créer une extrusion 3D avec des tranches – Aspose.3D for Java

## Introduction

Si vous devez **créer des objets d'extrusion 3D** qui soient lisses et précis, le contrôle du nombre de tranches est essentiel. Dans ce tutoriel, nous verrons comment spécifier les tranches lors d’une extrusion linéaire avec Aspose.3D for Java. Vous comprendrez pourquoi le nombre de tranches compte, comment définir un rayon d’arrondi, et comment exporter le résultat au format OBJ pouvant être utilisé dans n’importe quel pipeline 3D.

## Réponses rapides
- **Que contrôle le paramètre “tranches” ?** Le nombre de sections transversales intermédiaires utilisées pour approximer la surface d’extrusion.  
- **Quelle méthode définit le nombre de tranches ?** `LinearExtrusion.setSlices(int)`  
- **Puis‑je modifier le rayon d’arrondi du profil ?** Oui, via `RectangleShape.setRoundingRadius(double)`  
- **Quel format de fichier est utilisé dans cet exemple ?** Wavefront OBJ (`FileFormat.WAVEFRONTOBJ`)  
- **Ai‑je besoin d’une licence pour exécuter le code ?** Une version d’essai gratuite suffit pour l’évaluation ; une licence commerciale est requise pour la production.

## Qu’est‑ce qu’une extrusion linéaire avec des tranches ?

L’extrusion linéaire prend un profil 2‑D (comme un rectangle) et l’étire le long d’une ligne droite pour former un solide 3‑D. En spécifiant des **tranches**, vous indiquez à Aspose.3D combien d’étapes intermédiaires générer, ce qui influence directement la fluidité des arêtes courbes, comme un rectangle arrondi.

## Pourquoi utiliser Aspose.3D for Java pour créer une extrusion 3D ?

* **Contrôle total** – Vous pouvez ajuster le nombre de tranches, le rayon d’arrondi et le format d’exportation par programmation.  
* **Multi‑plateforme** – Fonctionne dans tout environnement Java sans dépendances natives.  
* **Flexibilité d’exportation** – Enregistrement direct en OBJ, FBX, STL et bien d’autres formats.

## Prérequis

1. **Java Development Kit** – JDK 8 ou supérieur installé.  
2. **Aspose.3D for Java** – Téléchargez la bibliothèque depuis le site officiel [ici](https://releases.aspose.com/3d/java/).  
3. Un IDE ou un éditeur de texte de votre choix.

## Importer les packages

Ajoutez l’espace de noms Aspose.3D à votre projet afin de pouvoir accéder aux classes de modélisation 3‑D.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## Guide étape par étape

### Étape 1 : Configurer la scène et définir le profil

Nous créons d’abord un `RectangleShape` et lui attribuons un **rayon d’arrondi** afin que les coins soient lisses. Puis nous initialisons une nouvelle `Scene` qui contiendra toute la géométrie.

```java
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
Scene scene = new Scene();
```

### Étape 2 : **Créer des nœuds enfants** pour chaque extrusion

Chaque élément de géométrie vit sous un `Node`. Ici nous générons deux nœuds frères – un pour une extrusion à faible nombre de tranches et un autre pour une extrusion à nombre élevé de tranches – et nous décalons légèrement le nœud de gauche afin de faciliter la comparaison des résultats.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### Étape 3 : Effectuer l’extrusion linéaire et **définir les tranches**

Nous créons maintenant les objets **d’extrusion 3D**. Le constructeur `LinearExtrusion` prend le profil et la profondeur d’extrusion. À l’aide d’une **classe interne anonyme** nous appelons `setSlices` pour contrôler la fluidité. Le nœud de gauche reçoit seulement 2 tranches (grossier), tandis que le nœud de droite en reçoit 10 (lisse).

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(2);}});
right.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(10);}});
```

### Étape 4 : **Exporter OBJ** – enregistrer la scène

Enfin, nous écrivons la scène dans un fichier Wavefront OBJ, un format largement supporté par les éditeurs 3‑D et les moteurs de jeu. Cela montre la capacité **export obj java** d’Aspose.3D.

```java
scene.save(MyDir + "SlicesInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Problèmes courants et solutions

| Problème | Pourquoi cela se produit | Solution |
|----------|--------------------------|----------|
| **L'extrusion apparaît plate** | Le nombre de tranches est réglé à 1 ou 0 | Assurez‑vous que `setSlices` est appelé avec une valeur ≥ 2. |
| **Les coins arrondis semblent dentelés** | Le rayon d’arrondi est trop petit par rapport au nombre de tranches | Augmentez soit le rayon, soit le nombre de tranches pour des courbes plus lisses. |
| **Fichier introuvable lors de l'enregistrement** | `MyDir` pointe vers un dossier inexistant | Créez le répertoire au préalable ou utilisez un chemin absolu. |

## Questions fréquentes

**Q : Comment télécharger Aspose.3D for Java ?**  
R : Vous pouvez télécharger la bibliothèque [ici](https://releases.aspose.com/3d/java/).

**Q : Où trouver la documentation d’Aspose.3D ?**  
R : Consultez la documentation [ici](https://reference.aspose.com/3d/java/).

**Q : Une version d’essai gratuite est‑elle disponible ?**  
R : Oui, vous pouvez explorer une version d’essai gratuite [ici](https://releases.aspose.com/).

**Q : Comment obtenir du support pour Aspose.3D ?**  
R : Visitez le forum de support [ici](https://forum.aspose.com/c/3d/18).

**Q : Puis‑je acheter une licence temporaire ?**  
R : Oui, une licence temporaire peut être obtenue [ici](https://purchase.aspose.com/temporary-license/).

---

**Dernière mise à jour :** 2026-02-22  
**Testé avec :** Aspose.3D for Java 24.11 (dernière version au moment de la rédaction)  
**Auteur :** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}