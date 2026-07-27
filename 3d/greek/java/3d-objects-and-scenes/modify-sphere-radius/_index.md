---
date: 2026-07-27
description: Μάθετε πώς να τροποποιήσετε την ακτίνα της σφαίρας σε Java και να εξάγετε
  αρχείο OBJ χρησιμοποιώντας το Aspose.3D, τη κορυφαία βιβλιοθήκη Java 3D για μετατροπή
  3D σε OBJ.
keywords:
- modify sphere radius java
- export obj file java
- aspose 3d java
lastmod: 2026-07-27
linktitle: 'Τροποποίηση Ακτίνας Σφαίρας Java: Μετατροπή 3D σε OBJ με το Aspose.3D'
og_description: Τροποποίηση ακτίνας σφαίρας Java και εξαγωγή αρχείου OBJ χρησιμοποιώντας
  το Aspose.3D. Αυτό το εκπαιδευτικό υλικό δείχνει βήμα‑βήμα πώς να προσθέσετε μια
  σφαίρα, να αλλάξετε το μέγεθός της και να αποθηκεύσετε ως OBJ.
og_image_alt: 'Guide: modify sphere radius Java and export OBJ using Aspose.3D'
og_title: Τροποποίηση Ακτίνας Σφαίρας Java – Μετατροπή 3D σε OBJ με το Aspose.3D
schemas:
- author: Aspose
  dateModified: '2026-07-27'
  description: Learn how to modify sphere radius Java and export OBJ file Java using
    Aspose.3D, the leading Java 3D library for converting 3D to OBJ.
  headline: 'Modify Sphere Radius Java: Convert 3D to OBJ with Aspose.3D'
  type: TechArticle
- description: Learn how to modify sphere radius Java and export OBJ file Java using
    Aspose.3D, the leading Java 3D library for converting 3D to OBJ.
  name: 'Modify Sphere Radius Java: Convert 3D to OBJ with Aspose.3D'
  steps:
  - name: Initialize a Scene
    text: '**Definition anchor:** The `Scene` class is Aspose.3D''s top‑level container
      that holds geometry, lights, and cameras for a 3D model. Creating a `Scene`
      gives you a workspace where you can add and manipulate objects. Creating a `Scene`
      gives you a container for all geometry, lights, and cameras. This'
  - name: Initialize a Sphere
    text: '**Definition anchor:** The `Sphere` class represents a geometric sphere
      primitive with a configurable radius, center, and material. By default it starts
      with a radius of 1.0. A `Sphere` object starts with a default radius of 1.0.
      Think of it as a blank canvas for the shape you want to export.'
  - name: Set the Desired Radius
    text: The `setRadius(double)` method updates the sphere’s size by assigning a
      new radius value in the same units used by the scene. Here we **write obj file
      java**‑style code that sets the exact radius. Replace `10` with any `double`
      value that matches your design requirements.
  - name: Add Sphere to the Scene
    text: This line **adds sphere to scene** by creating a child node under the root
      node. It’s the moment the geometry becomes part of the scene graph.
  - name: Export the Model as OBJ
    text: The `save(String, FileFormat)` method writes the entire scene to the specified
      file using the chosen format, such as OBJ. Calling `scene.save` **exports obj
      file java**‑style, effectively **save scene as obj**. The generated `sphere.obj`
      can be opened in any standard 3D viewer.
  type: HowTo
- questions:
  - answer: You can refer to the [Aspose.3D for Java documentation](https://reference.aspose.com/3d/java/)
      for comprehensive guidance.
    question: Where can I find the documentation for Aspose.3D for Java?
  - answer: 'Download the library from the releases page: [Download Aspose.3D for
      Java](https://releases.aspose.com/3d/java/).'
    question: How do I download Aspose.3D for Java?
  - answer: Yes, explore the features with a free trial by visiting [Aspose.3D Free
      Trial](https://releases.aspose.com/).
    question: Is there a free trial available for Aspose.3D for Java?
  - answer: Join the Aspose community at [Aspose.3D Support Forum](https://forum.aspose.com/c/3d/18)
      for assistance and discussions.
    question: Where can I get support for Aspose.3D for Java?
  - answer: Get a temporary license by visiting [Temporary License](https://purchase.aspose.com/temporary-license/).
    question: How can I obtain a temporary license for Aspose.3D?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- modify sphere radius
- export OBJ
- aspose.3d
- java 3d
- 3d conversion
title: 'Τροποποίηση Ακτίνας Σφαίρας Java: Μετατροπή 3D σε OBJ με το Aspose.3D'
url: /el/java/3d-objects-and-scenes/modify-sphere-radius/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Μετατροπή 3D σε OBJ: Προσθήκη Σφαίρας & Τροποποίηση Ακτίνας σε Java

## Εισαγωγή

Αν χρειάζεστε **modify sphere radius java** γρήγορα και προγραμματιστικά, αυτός ο οδηγός σας δείχνει ακριβώς πώς να προσθέσετε μια σφαίρα σε μια σκηνή, να αλλάξετε την ακτίνα της και να γράψετε το αποτέλεσμα σε αρχείο OBJ χρησιμοποιώντας τη **Aspose.3D Java library**. Θα περάσουμε από κάθε γραμμή κώδικα, θα εξηγήσουμε γιατί κάθε βήμα είναι σημαντικό και θα σας δώσουμε συμβουλές για να αποφύγετε κοινά λάθη—ώστε να ενσωματώσετε τη ροή εργασίας σε παιχνίδια, εργαλεία CAD ή επιστημονικές απεικονίσεις με σιγουριά.

## Γρήγορες Απαντήσεις
- **Ποιος είναι ο κύριος στόχος αυτού του οδηγού;** Να δείξει πώς να μετατρέψετε 3D σε OBJ δημιουργώντας μια σφαίρα, ρυθμίζοντας την ακτίνα της και εξάγοντας το μοντέλο σε Java.  
- **Ποια βιβλιοθήκη παρέχει τη λειτουργικότητα 3D;** Aspose.3D, ένα πλήρες **java 3d library tutorial**.  
- **Πώς αλλάζω το μέγεθος της σφαίρας;** Καλείτε `sphere.setRadius(double)` στο αντικείμενο `Sphere`.  
- **Μπορώ να γράψω το αρχείο OBJ απευθείας από Java;** Ναι—χρησιμοποιήστε `scene.save("file.obj", FileFormat.WAVEFRONTOBJ)`.  
- **Χρειάζομαι άδεια για παραγωγή;** Μια δωρεάν δοκιμή είναι εντάξει για ανάπτυξη· απαιτείται μόνιμη άδεια για εμπορική χρήση.

## Τι είναι το Aspose.3D για Java;

Το Aspose.3D για Java είναι μια ολοκληρωμένη **java 3d library** που επιτρέπει στους προγραμματιστές να δημιουργούν, να επεξεργάζονται και να μετατρέπουν αρχεία 3D χωρίς εξωτερικές εξαρτήσεις. Υποστηρίζει περισσότερα από **50 μορφές εισόδου και εξόδου**—συμπεριλαμβανομένων των OBJ, FBX, STL και GLTF—επιτρέποντας αδιάλειπτη ενσωμάτωση σε οποιοδήποτε 3‑D pipeline.

## Γιατί να μετατρέψετε 3D σε OBJ;

Η μετατροπή σε OBJ παρέχει μια καθολικά αναγνώσιμη, κειμενική αναπαράσταση γεωμετρίας που μπορεί να επιθεωρηθεί, να επεξεργαστεί και να εισαχθεί από σχεδόν κάθε εφαρμογή 3D, καθιστώντας την ιδανική για γρήγορη πρωτοτυποποίηση και ανταλλαγή πόρων μεταξύ πλατφορμών.

- **Καθολική Συμβατότητα** – Το OBJ υποστηρίζεται από σχεδόν κάθε προβολέα 3D, μηχανή παιχνιδιών και λογισμικό μοντελοποίησης.  
- **Ελαφριά Εξαγωγή** – Το OBJ αποθηκεύει τη γεωμετρία σε μορφή απλού κειμένου, που είναι εύκολο να επιθεωρηθεί και να αποσφαλματωθεί.  
- **Ευελιξία Ροής Εργασίας** – Μπορείτε να δημιουργήσετε αρχεία OBJ εν κινήσει από κώδικα Java στο διακομιστή, επιτρέποντας αυτοματοποιημένες διαδικασίες δημιουργίας πόρων.

## Προαπαιτούμενα

- Βασικές γνώσεις προγραμματισμού Java.  
- Η βιβλιοθήκη Aspose.3D εγκατεστημένη – κατεβάστε την από την [Aspose.3D for Java documentation](https://reference.aspose.com/3d/java/).  
- JDK 8 ή νεότερο εγκατεστημένο στο μηχάνημά σας.

## Εισαγωγή Πακέτων

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Sphere;

import java.io.IOException;
```

## Πώς να τροποποιήσετε την ακτίνα σφαίρας java;

Φορτώστε το αντικείμενο `Sphere`, καλέστε `setRadius` με την επιθυμητή τιμή και, στη συνέχεια, αποθηκεύστε τη σκηνή ως OBJ—όλη αυτή η ροή εργασίας μπορεί να εκτελεστεί σε πέντε σύντομα βήματα. Η προσέγγιση λειτουργεί για οποιαδήποτε αριθμητική ακτίνα και εγγυάται ότι το εξαγόμενο OBJ αντικατοπτρίζει το ακριβές μέγεθος που καθορίζετε.

### Βήμα 1: Αρχικοποίηση Σκηνής

```java
// ExStart:WorkingWithSphereRadius

// initialize a scene
Scene scene = new Scene();
```

**Αγκύρωση ορισμού:** Η κλάση `Scene` είναι το κορυφαίο κοντέινερ του Aspose.3D που κρατά γεωμετρία, φωτισμούς και κάμερες για ένα 3D μοντέλο. Η δημιουργία ενός `Scene` σας παρέχει έναν χώρο εργασίας όπου μπορείτε να προσθέτετε και να χειρίζεστε αντικείμενα.

Η δημιουργία ενός `Scene` σας δίνει ένα κοντέινερ για όλη τη γεωμετρία, τα φώτα και τις κάμερες. Εδώ θα **add sphere to scene** αργότερα.

### Βήμα 2: Αρχικοποίηση Σφαίρας

```java
// initialize a Sphere
Sphere sphere = new Sphere();
```

**Αγκύρωση ορισμού:** Η κλάση `Sphere` αντιπροσωπεύει ένα γεωμετρικό πρωτότυπο σφαίρας με ρυθμιζόμενη ακτίνα, κέντρο και υλικό. Από προεπιλογή ξεκινά με ακτίνα 1.0.

Ένα αντικείμενο `Sphere` ξεκινά με προεπιλεγμένη ακτίνα 1.0. Σκεφτείτε το ως λευκό καμβά για το σχήμα που θέλετε να εξάγετε.

### Βήμα 3: Ορισμός Επιθυμητής Ακτίνας

Η μέθοδος `setRadius(double)` ενημερώνει το μέγεθος της σφαίρας αναθέτοντας μια νέα τιμή ακτίνας στις ίδιες μονάδες που χρησιμοποιεί η σκηνή.

```java
// set radius
sphere.setRadius(10);
```

Εδώ **write obj file java**‑style κώδικας ορίζει την ακριβή ακτίνα. Αντικαταστήστε το `10` με οποιαδήποτε τιμή `double` ταιριάζει στις απαιτήσεις του σχεδίου σας.

### Βήμα 4: Προσθήκη Σφαίρας στη Σκηνή

```java
// add sphere to the scene
scene.getRootNode().createChildNode(sphere);
```

Αυτή η γραμμή **adds sphere to scene** δημιουργώντας έναν παιδικό κόμβο κάτω από τον ριζικό κόμβο. Είναι η στιγμή που η γεωμετρία γίνεται μέρος του γραφήματος σκηνής.

### Βήμα 5: Εξαγωγή Μοντέλου ως OBJ

Η μέθοδος `save(String, FileFormat)` γράφει ολόκληρη τη σκηνή στο καθορισμένο αρχείο χρησιμοποιώντας την επιλεγμένη μορφή, όπως OBJ.

```java
// save scene
scene.save("sphere.obj", FileFormat.WAVEFRONTOBJ);
```

Καλώντας `scene.save` **exports obj file java**‑style, ουσιαστικά **save scene as obj**. Το παραγόμενο `sphere.obj` μπορεί να ανοιχτεί σε οποιονδήποτε τυπικό προβολέα 3D.

## Συχνά Προβλήματα και Λύσεις

| Πρόβλημα | Λύση |
|----------|------|
| **Η σφαίρα εμφανίζεται πολύ μικρή στον προβολέα** | Επαληθεύστε ότι η τιμή της ακτίνας έχει οριστεί σωστά· θυμηθείτε ότι οι μονάδες είναι αυθαίρετες εκτός αν εφαρμόσετε μετασχηματισμό κλιμάκωσης. |
| **Το εξαγόμενο OBJ δεν έχει υλικό** | Το Aspose.3D γράφει μόνο τη γεωμετρία· προσθέστε υλικό στη σφαίρα αν χρειάζεστε υφές (`sphere.setMaterial(...)`). |
| **Εξαίρεση άδειας κατά την εκτέλεση** | Βεβαιωθείτε ότι έχετε φορτώσει είτε προσωρινή είτε μόνιμη άδεια πριν δημιουργήσετε το `Scene`. |

## Συχνές Ερωτήσεις

**Ε: Πού μπορώ να βρω την τεκμηρίωση για το Aspose.3D για Java;**  
Α: Μπορείτε να ανατρέξετε στην [Aspose.3D for Java documentation](https://reference.aspose.com/3d/java/) για ολοκληρωμένη καθοδήγηση.

**Ε: Πώς κατεβάζω το Aspose.3D για Java;**  
Α: Κατεβάστε τη βιβλιοθήκη από τη σελίδα εκδόσεων: [Download Aspose.3D for Java](https://releases.aspose.com/3d/java/).

**Ε: Υπάρχει δωρεάν δοκιμή για το Aspose.3D για Java;**  
Α: Ναι, εξερευνήστε τις δυνατότητες με δωρεάν δοκιμή επισκεπτόμενοι το [Aspose.3D Free Trial](https://releases.aspose.com/).

**Ε: Πού μπορώ να λάβω υποστήριξη για το Aspose.3D για Java;**  
Α: Ενταχθείτε στην κοινότητα Aspose στο [Aspose.3D Support Forum](https://forum.aspose.com/c/3d/18) για βοήθεια και συζητήσεις.

**Ε: Πώς μπορώ να αποκτήσω προσωρινή άδεια για το Aspose.3D;**  
Α: Λάβετε προσωρινή άδεια επισκεπτόμενοι το [Temporary License](https://purchase.aspose.com/temporary-license/).

**Ε: Μπορώ να χρησιμοποιήσω αυτόν τον κώδικα με άλλες μορφές 3D όπως STL;**  
Α: Απόλυτα – απλώς αλλάξτε το enum `FileFormat` όταν καλείτε `scene.save`, π.χ., `FileFormat.STL`.

**Τελευταία Ενημέρωση:** 2026-07-27  
**Δοκιμή Με:** Aspose.3D for Java 24.11  
**Συγγραφέας:** Aspose

## Σχετικά Μαθήματα

- [Πώς να ορίσετε κανονικές σε 3D αντικείμενα σε Java χρησιμοποιώντας το Aspose.3D Java API](/3d/java/geometry/set-up-normals-on-3d-objects/)
- [Πώς να ενσωματώσετε υφή σε FBX με Java – Εφαρμογή Υλικών σε 3D Αντικείμενα χρησιμοποιώντας το Aspose.3D](/3d/java/geometry/apply-materials-to-3d-objects/)
- [Πώς να αλλάξετε τον προσανατολισμό του επιπέδου και να εξάγετε OBJ σε Java](/3d/java/3d-scenes-and-models/change-plane-orientation/)

{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< blocks/products/products-backtop-button >}}
{{< /blocks/products/pf/main-wrap-class >}}