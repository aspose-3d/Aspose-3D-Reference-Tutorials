---
date: 2026-08-12
description: Πώς να δημιουργήσετε 3D χρησιμοποιώντας Aspose.3D – δημιουργήστε cylinder
  με offset top σε Java, προσθέστε child node, ορίστε offset top, δημιουργήστε 3D
  model, εξάγετε OBJ, και αξιολογήστε με temporary license.
keywords:
- how to generate 3d
- aspose temporary license
- export obj file
- set offset top
- java 3d cylinder
lastmod: 2026-08-12
linktitle: Πώς να δημιουργήσετε 3D – δημιουργήστε cylinder με offset top (Java)
og_description: Πώς να δημιουργήσετε 3D με Aspose.3D για Java. Μάθετε πώς να offset
  cylinder tops, να προσθέσετε child nodes, και να εξάγετε OBJ χρησιμοποιώντας temporary
  license.
og_image_alt: Guide showing Java code to create a cylinder with offset top and export
  OBJ using Aspose.3D
og_title: Πώς να δημιουργήσετε 3D – δημιουργήστε cylinder με offset top (Java)
schemas:
- author: Aspose
  dateModified: '2026-08-12'
  description: How to generate 3d using Aspose.3D – create a cylinder with offset
    top in Java, add child node, set offset top, generate 3D model, export OBJ, and
    evaluate with a temporary license.
  headline: How to generate 3d – create cylinder with offset top (Java)
  type: TechArticle
- description: How to generate 3d using Aspose.3D – create a cylinder with offset
    top in Java, add child node, set offset top, generate 3D model, export OBJ, and
    evaluate with a temporary license.
  name: How to generate 3d – create cylinder with offset top (Java)
  steps:
  - name: Create a Java 3D scene
    text: '`Scene` is the top‑level container that holds all nodes, meshes, lights,
      and cameras in a 3‑D environment.'
  - name: Initialize cylinder with offset top
    text: '`Cylinder` represents a cylindrical mesh and provides properties such as
      radius, height, and offset.'
  - name: Add child node Java – attach the first cylinder
    text: '`Node` is an element in the scene graph that can hold geometry and transformations.'
  - name: Java export OBJ – save the scene as OBJ
    text: '`FileFormat` enumerates the supported export formats such as OBJ, STL,
      and FBX.'
  type: HowTo
- questions:
  - answer: Yes, it works seamlessly with Eclipse, IntelliJ IDEA, NetBeans, and other
      IDEs.
    question: Is Aspose.3D compatible with different Java IDEs?
  - answer: Absolutely! Use the `Material` class to assign textures and surface properties.
    question: Can I apply textures to the created 3D objects?
  - answer: Various licensing models are available; you can explore them **[Aspose
      purchase page](https://purchase.aspose.com/buy)**.
    question: Are there licensing options for Aspose.3D?
  - answer: Join the **[Aspose.3D community forum](https://forum.aspose.com/c/3d/18)**
      for support and discussion.
    question: How can I get help or share experiences?
  - answer: Yes, an **aspose temporary license** can be obtained for evaluation **[temporary
      license request page](https://purchase.aspose.com/temporary-license/)**.
    question: Is a temporary license available for testing?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- generate 3d
- aspose.3d
- java cylinder offset
title: Πώς να δημιουργήσετε 3D – δημιουργήστε cylinder με offset top (Java)
url: /el/java/cylinders/creating-cylinders-with-offset-top/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Πώς να δημιουργήσετε 3δ – δημιουργία κυλίνδρου με μετατόπιση στην κορυφή (Java)

## Εισαγωγή

Αν θέλετε να **δημιουργήσετε κυλίνδρους** με προσαρμοσμένη μετατόπιση στην κορυφή σε μια σκηνή 3D βασισμένη σε Java, το Aspose.3D κάνει τη διαδικασία απλή. Σε αυτό το tutorial θα περάσουμε από κάθε βήμα — από τη ρύθμιση της σκηνής μέχρι την εξαγωγή του τελικού μοντέλου ως αρχείο OBJ — ώστε να μπορείτε να ενσωματώσετε κυλίνδρους με μετατόπιση στην κορυφή στις εφαρμογές σας με σιγουριά. Στο τέλος του οδηγού θα καταλάβετε επίσης πώς μια **aspose temporary license** σας επιτρέπει να αξιολογήσετε αυτές τις λειτουργίες χωρίς πλήρη αγορά.

## Γρήγορες απαντήσεις
- **Ποια βιβλιοθήκη χρησιμοποιείται;** Aspose.3D for Java  
- **Μπορώ να μετατοπίσω την κορυφή ενός κυλίνδρου;** Ναι, μέσω του `setOffsetTop`  
- **Πώς προσθέτω ένα παιδικό κόμβο σε Java;** Καλέστε το `createChildNode` στον ριζικό κόμβο  
- **Σε ποια μορφή μπορώ να εξάγω;** Wavefront OBJ (`export obj file`)  
- **Χρειάζομαι άδεια για δοκιμή;** Μια **aspose temporary license** είναι διαθέσιμη για αξιολόγηση  

## Τι είναι η άδεια Aspose temporary license;

Μια **aspose temporary license** είναι ένα βραχυπρόθεσμο, δωρεάν κλειδί αξιολόγησης που ξεκλειδώνει το πλήρες σύνολο λειτουργιών του Aspose.3D for Java κατά τη διάρκεια ανάπτυξης και δοκιμών. Αφαιρεί τα υδατογραφήματα αξιολόγησης και σας επιτρέπει να δημιουργήσετε αρχεία 3D μοντέλων, όπως OBJ, STL ή FBX, ακριβώς όπως θα έκανε μια πλήρης άδεια.

## Γιατί να χρησιμοποιήσετε το Aspose.3D για Java;

Aspose.3D παρέχει ένα υψηλού επιπέδου,跨平台 API που απλοποιεί τη δημιουργία και εξαγωγή 3D. Περιλαμβάνει ενσωματωμένους εξαγωγείς για πάνω από 30 μορφές, υποστηρίζει ιεραρχίες σκηνικού και σας επιτρέπει να εστιάσετε στη γεωμετρία αντί για τη διαχείριση mesh χαμηλού επιπέδου.

- **High‑level API:** Δεν χρειάζεται να διαχειρίζεστε δεδομένα mesh χαμηλού επιπέδου.  
- **Cross‑platform:** Λειτουργεί σε οποιοδήποτε περιβάλλον συμβατό με JVM.  
- **Built‑in exporters:** Αποθηκεύει απευθείας σε OBJ, STL, FBX και άλλα — το Aspose.3D υποστηρίζει **30+** μορφές εξαγωγής.  
- **Extensible:** Προσθέστε εύκολα παιδικούς κόμβους, εφαρμόστε μετασχηματισμούς και ενσωματώστε με άλλες βιβλιοθήκες Java.  

## Προαπαιτούμενα

- **Java Development Kit (JDK)** – εγκατεστημένη συμβατή έκδοση.  
- **Aspose.3D for Java library** – κατεβάστε το τελευταίο JAR από την επίσημη ιστοσελίδα **[Aspose.3D for Java download page](https://releases.aspose.com/3d/java/)**.  
- Ένα IDE της επιλογής σας (Eclipse, IntelliJ IDEA, NetBeans, κλ.).  

## Εισαγωγή πακέτων

Οι παρακάτω εισαγωγές φέρνουν τις απαραίτητες κλάσεις του Aspose.3D για τη δημιουργία και εξαγωγή ενός κυλίνδρου.

```java
import com.aspose.threed.Cylinder;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Vector3;


import java.io.IOException;
```

## Οδηγός βήμα‑βήμα

### Βήμα 1: Δημιουργία σκηνής Java 3D

`Scene` είναι το κοντέινερ υψηλότερου επιπέδου που κρατά όλους τους κόμβους, meshes, φώτα και κάμερες σε ένα περιβάλλον 3‑D.

```java
// ExStart:1
// Create a scene
Scene scene = new Scene();
// ExEnd:1
```

### Βήμα 2: Αρχικοποίηση κυλίνδρου με μετατόπιση στην κορυφή

`Cylinder` αντιπροσωπεύει ένα κυλινδρικό mesh και παρέχει ιδιότητες όπως ακτίνα, ύψος και μετατόπιση.

```java
// ExStart:2
// Initialize cylinder
Cylinder cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
// Set OffsetTop
cylinder1.setOffsetTop(new Vector3(5, 3, 0));
// ExEnd:2
```

### Βήμα 3: Προσθήκη παιδικού κόμβου Java – επισύναψη του πρώτου κυλίνδρου

`Node` είναι ένα στοιχείο στο γράφημα σκηνής που μπορεί να κρατήσει γεωμετρία και μετασχηματισμούς.

```java
// ExStart:3
// Create ChildNode
scene.getRootNode().createChildNode(cylinder1).getTransform().setTranslation(10, 0, 0);
// ExEnd:3
```

### Βήμα 4: Αρχικοποίηση δεύτερου κυλίνδρου (χωρίς μετατόπιση)

```java
// ExStart:4
// Initialize second cylinder without customized OffsetTop
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// ExEnd:4
```

### Βήμα 5: Προσθήκη παιδικού κόμβου Java – επισύναψη του δεύτερου κυλίνδρου

```java
// ExStart:5
// Create ChildNode
scene.getRootNode().createChildNode(cylinder2);
// ExEnd:5
```

### Βήμα 6: Εξαγωγή OBJ σε Java – αποθήκευση της σκηνής ως OBJ

`FileFormat` απαριθμεί τις υποστηριζόμενες μορφές εξαγωγής όπως OBJ, STL και FBX.

```java
// ExStart:6
// Save
scene.save("Your Document Directory" + "CustomizedOffsetTopCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

## Πώς να δημιουργήσετε 3δ μοντέλο και να εξάγετε OBJ σε Java

Για να δημιουργήσετε ένα 3D μοντέλο, φορτώστε τη σκηνή, εφαρμόστε τυχόν απαιτούμενους μετασχηματισμούς και, στη συνέχεια, καλέστε `scene.save("path/CustomizedOffsetTopCylinder.obj", FileFormat.WAVEFRONTOBJ)`. Η **aspose temporary license** αφαιρεί το υδατογράφημα αξιολόγησης, επιτρέποντάς σας να παράγετε έτοιμα για παραγωγή αρχεία OBJ χωρίς την αγορά πλήρους άδειας.

## Πραγματικές περιπτώσεις χρήσης

- **Architectural visualisation:** Οι κυλίνδροι με μετατόπιση στην κορυφή μοντελοποιούν κολώνες που στενεύουν προς την οροφή.  
- **Mechanical parts:** Δημιουργήστε πίσσες ή θήκες γραναζιών όπου η επάνω επιφάνεια είναι σκόπιμα μετατοπισμένη.  
- **Game assets:** Παραγάγετε ποικίλα σχήματα στηλών άμεσα, μειώνοντας την ανάγκη για χειροποίητα mesh.  

## Συνηθισμένα προβλήματα και λύσεις

| Πρόβλημα | Αιτία | Διόρθωση |
|----------|-------|----------|
| **Το αρχείο OBJ είναι κενό** | Η σκηνή δεν αποθηκεύτηκε σωστά ή το μονοπάτι είναι λανθασμένο. | Επαληθεύστε ότι ο φάκελος εξόδου υπάρχει και έχετε δικαιώματα εγγραφής. |
| **Η μετατόπιση δεν εφαρμόστηκε** | Χρήση παλαιότερης έκδοσης του Aspose.3D. | Αναβαθμίστε στην πιο πρόσφατη βιβλιοθήκη όπου υποστηρίζεται το `setOffsetTop`. |
| **Ο παιδικός κόμβος δεν είναι ορατός** | Ο μετασχηματισμός δεν εφαρμόστηκε. | Βεβαιωθείτε ότι καλείτε το `getTransform().setTranslation` μετά τη δημιουργία του παιδικού κόμβου. |

## Συχνές ερωτήσεις

**Ε: Είναι το Aspose.3D συμβατό με διαφορετικά Java IDEs;**  
Α: Ναι, λειτουργεί άψογα με Eclipse, IntelliJ IDEA, NetBeans και άλλα IDEs.

**Ε: Μπορώ να εφαρμόσω υφές στα δημιουργημένα 3D αντικείμενα;**  
Α: Απολύτως! Χρησιμοποιήστε την κλάση `Material` για να αναθέσετε υφές και ιδιότητες επιφάνειας.

**Ε: Υπάρχουν επιλογές αδειοδότησης για το Aspose.3D;**  
Α: Διατίθενται διάφορα μοντέλα αδειοδότησης· μπορείτε να τα εξερευνήσετε **[Aspose purchase page](https://purchase.aspose.com/buy)**.

**Ε: Πώς μπορώ να λάβω βοήθεια ή να μοιραστώ εμπειρίες;**  
Α: Εγγραφείτε στο **[Aspose.3D community forum](https://forum.aspose.com/c/3d/18)** για υποστήριξη και συζήτηση.

**Ε: Υπάρχει προσωρινή άδεια διαθέσιμη για δοκιμές;**  
Α: Ναι, μια **aspose temporary license** μπορεί να ληφθεί για αξιολόγηση **[temporary license request page](https://purchase.aspose.com/temporary-license/)**.

---

**Last updated:** 2026-08-12  
**Tested with:** Aspose.3D for Java 24.12 (latest)  
**Author:** Aspose

{{< blocks/products/products-backtop-button >}}

## Σχετικοί Οδηγοί

- [Πώς να δημιουργήσετε μοντέλα κυλίνδρων με Aspose.3D για Java](/3d/java/cylinders/)
- [Πώς να δημιουργήσετε σχήμα κυλίνδρου-ανεμιστήρα χρησιμοποιώντας Aspose.3D για Java](/3d/java/cylinders/creating-fan-cylinders/)
- [Δημιουργία παιδικών κόμβων και εξαγωγή FBX σε Java με Aspose.3D](/3d/java/geometry/build-node-hierarchies/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}