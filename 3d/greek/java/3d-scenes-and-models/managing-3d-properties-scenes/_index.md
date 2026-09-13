---
date: 2026-09-13
description: Μάθετε πώς να ορίσετε το διασκορπιστικό χρώμα, να τροποποιήσετε το χρώμα
  του υλικού και να διαχειριστείτε τις 3D ιδιότητες σε σκηνές Java με το Aspose.3D.
  Αυτός ο οδηγός βήμα‑βήμα καλύπτει τη χρήση του Vector3, την ανάκτηση του υλικού
  και τη διαχείριση προσαρμοσμένων δεδομένων.
keywords:
- set diffuse color
- Aspose 3D Java
- modify material color
lastmod: 2026-09-13
linktitle: Πώς να ορίσετε το διασκορπιστικό χρώμα σε σκηνές Java χρησιμοποιώντας το
  Aspose.3D
og_description: Μάθετε πώς να ορίσετε το διασκορπιστικό χρώμα, να τροποποιήσετε το
  χρώμα του υλικού και να διαχειριστείτε τις 3D ιδιότητες σε σκηνές Java με το Aspose.3D.
  Ακολουθήστε ένα σύντομο βήμα‑βήμα tutorial για προγραμματιστές.
og_image_alt: Screenshot of Java code changing diffuse color with Aspose.3D
og_title: Πώς να ορίσετε το διασκορπιστικό χρώμα σε σκηνές Java χρησιμοποιώντας το
  Aspose.3D
schemas:
- author: Aspose
  dateModified: '2026-09-13'
  description: Learn how to set diffuse color, modify material color, and manage 3D
    properties in Java scenes with Aspose.3D. This step‑by‑step guide covers Vector3
    usage, material retrieval, and custom data handling.
  headline: How to set diffuse color in Java scenes using Aspose.3D
  type: TechArticle
- questions:
  - answer: Download the JAR from the [Aspose website](https://releases.aspose.com/3d/java/)
      and add it to your project's classpath or Maven/Gradle dependencies.
    question: How can I install the Aspose.3D library in my Java project?
  - answer: Yes, a fully functional 30‑day trial is available from the [Aspose free
      trial page](https://releases.aspose.com/).
    question: Are there any free trial options for Aspose.3D?
  - answer: The official API reference is at [Aspose.3D documentation](https://reference.aspose.com/3d/java/).
    question: Where can I find detailed documentation for Aspose.3D in Java?
  - answer: Absolutely—visit the [Aspose.3D support forum](https://forum.aspose.com/c/3d/18)
      to connect with the community and experts.
    question: Is there a support forum for Aspose.3D where I can ask questions?
  - answer: Request one via the [temporary license page](https://purchase.aspose.com/temporary-license/)
      on the Aspose site.
    question: How can I obtain a temporary license for Aspose.3D?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- 3d rendering
- Aspose.3D
- java graphics
- material properties
title: Πώς να ορίσετε το διασκορπιστικό χρώμα σε σκηνές Java χρησιμοποιώντας το Aspose.3D
url: /el/java/3d-scenes-and-models/managing-3d-properties-scenes/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Πώς να ορίσετε το διασκορπιστικό χρώμα σε σκηνές Java χρησιμοποιώντας το Aspose.3D

## Εισαγωγή

Σε αυτό το **Aspose 3D tutorial** θα μάθετε **πώς να ορίσετε το διασκορπιστικό χρώμα** σε ένα υλικό και να διαχειριστείτε άλλες 3D ιδιότητες μέσα σε σκηνές Java. Είτε δημιουργείτε έναν διαμορφωτή προϊόντων, ένα παιχνίδι ή έναν επιστημονικό οπτικοποιητή, η αλλαγή του διασκορπιστικού χρώματος σε χρόνο εκτέλεσης σας δίνει πλήρη καλλιτεχνικό έλεγχο πάνω στην εμφάνιση των μοντέλων σας. Θα περάσουμε από τη φόρτωση μιας σκηνής, την ανάκτηση ενός υλικού και την ανάθεση μιας νέας τιμής χρώματος `Vector3` — όλα με σαφή, έτοιμο για παραγωγή κώδικα.

## Γρήγορες απαντήσεις
- **Τι μπορώ να τροποποιήσω;** Μπορείτε να αλλάξετε το χρώμα της υφής, τη διαφάνεια, τη λάμψη και οποιαδήποτε προσαρμοσμένη ιδιότητα συνδεδεμένη με ένα υλικό.  
- **Ποια κλάση κρατά τα δεδομένα;** `Material` και η `PropertyCollection`.  
- **Πώς ορίζω νέο χρώμα;** Χρησιμοποιήστε `props.set("Diffuse", new Vector3(r, g, b))`.  
- **Πώς ορίζω χρώμα vector3 java;** Καλέστε `props.set("Diffuse", new Vector3(r, g, b))` στη συλλογή ιδιοτήτων του υλικού.  
- **Χρειάζομαι άδεια;** Μια προσωρινή άδεια λειτουργεί για αξιολόγηση· απαιτείται πλήρης άδεια για παραγωγή.  
- **Υποστηριζόμενες μορφές;** FBX, OBJ, STL, GLTF, και πολλές άλλες.

## Τι είναι η ρύθμιση του διασκορπιστικού χρώματος;
`set diffuse color` είναι η διαδικασία ανάθεσης ενός νέου χρώματος RGB στο κανάλι διασκορπισμού ενός υλικού, το οποίο καθορίζει τη βασική απόχρωση που η επιφάνεια αντανακλά υπό άμεσο φωτισμό. Στο Aspose.3D αυτό γίνεται μέσω της `PropertyCollection` του υλικού. Χρησιμοποιείται συνήθως για την προσαρμογή της εμφάνισης των μοντέλων χωρίς τροποποίηση των αρχείων υφής, επιτρέποντας δυναμικές αλλαγές χρώματος σε χρόνο εκτέλεσης.

## Γιατί να τροποποιήσετε το χρώμα του υλικού;
Το Aspose.3D υποστηρίζει **30+ μορφές εισόδου και εξόδου** και μπορεί να επεξεργαστεί μοντέλα έως **500 MB** χωρίς να φορτώνει ολόκληρο το αρχείο στη μνήμη. Η ενημέρωση του διασκορπιστικού χρώματος σας επιτρέπει να δημιουργήσετε δυναμικά οπτικά εφέ όπως επιλογείς χρώματος από τον χρήστη, ρυθμίσεις φωτισμού σε πραγματικό χρόνο ή οπτική ανάδραση για καταστάσεις προσομοίωσης.

## Προαπαιτούμενα
- Java Development Kit (JDK) 8 ή νεότερο εγκατεστημένο.  
- Βιβλιοθήκη Aspose.3D for Java (κατεβάστε από το [Aspose website](https://releases.aspose.com/3d/java/)).  
- Βασική εξοικείωση με τη σύνταξη της Java και τις αντικειμενοστραφείς έννοιες.

## Εισαγωγή πακέτων
Πριν γράψετε οποιαδήποτε λογική, εισάγετε τις κλάσεις που σας δίνουν πρόσβαση στις ιδιότητες του υλικού και στη διαχείριση διανυσμάτων.

Η κλάση `Scene` φορτώνει και αντιπροσωπεύει το 3D αρχείο.  
Η κλάση `Material` ορίζει χαρακτηριστικά επιφάνειας όπως χρώματα και υφές.  
Η κλάση `PropertyCollection` λειτουργεί όπως ένα λεξικό, επιτρέποντάς σας να διαβάζετε ή να γράφετε ιδιότητες υλικού με όνομα.  
Η κλάση `Vector3` αποθηκεύει τιμές τριών συνιστωσών και χρησιμοποιείται για χρώματα, κανονικές και άλλα δεδομένα διανυσμάτων.

## Πώς να ορίσω το διασκορπιστικό χρώμα χρησιμοποιώντας Vector3 στη Java;
Φορτώστε τη σκηνή σας, εντοπίστε τον στόχο κόμβο, ανακτήστε το υλικό του και αναθέστε μια νέα τιμή `Vector3` στην ιδιότητα **Diffuse** — όλα σε λίγες γραμμές κώδικα. Αυτό το μοτίβο άμεσης απάντησης εξασφαλίζει ότι μπορείτε να εφαρμόσετε αλλαγές χρώματος γρήγορα και αξιόπιστα.

### Οδηγός βήμα‑βήμα – πρόσβαση και τροποποίηση ιδιοτήτων υλικού
Ακολουθεί το πλήρες λειτουργικό παράδειγμα που δείχνει όλα τα βήματα:

```java
import java.io.IOException;

import com.aspose.threed.Material;
import com.aspose.threed.Property;
import com.aspose.threed.PropertyCollection;
import com.aspose.threed.Scene;
import com.aspose.threed.Vector3;
```

## Κοινά προβλήματα & λύσεις

| Πρόβλημα | Γιατί συμβαίνει | Διόρθωση |
|----------|----------------|----------|
| **`NullPointerException` on `material`** | Ο κόμβος ενδέχεται να μην έχει εκχωρημένο υλικό. | Κλήση `node.setMaterial(new Material())` πριν την πρόσβαση στις ιδιότητες. |
| **Το χρώμα δεν αλλάζει** | Το μοντέλο χρησιμοποιεί μια υφή που παρακάμπτει το χρώμα *Diffuse*. | Απενεργοποιήστε την υφή ή τροποποιήστε απευθείας την εικόνα υφής. |
| **`ClassCastException` κατά την ανάκτηση** | Προσπάθεια μετατροπής μιας ιδιότητας που δεν είναι Vector3. | Επαληθεύστε τον τύπο της ιδιότητας με `pdiffuse.getValue().getClass()` πριν τη μετατροπή. |

## Συχνές ερωτήσεις

**Q: Πώς μπορώ να εγκαταστήσω τη βιβλιοθήκη Aspose.3D στο Java project μου;**  
A: Κατεβάστε το JAR από το [Aspose website](https://releases.aspose.com/3d/java/) και προσθέστε το στο classpath του έργου σας ή στις εξαρτήσεις Maven/Gradle.

**Q: Υπάρχουν δωρεάν δοκιμαστικές επιλογές για το Aspose.3D;**  
A: Ναι, μια πλήρως λειτουργική δοκιμή 30 ημερών είναι διαθέσιμη από τη [σελίδα δωρεάν δοκιμής του Aspose](https://releases.aspose.com/).

**Q: Πού μπορώ να βρω λεπτομερή τεκμηρίωση για το Aspose.3D σε Java;**  
A: Η επίσημη αναφορά API βρίσκεται στο [Aspose.3D documentation](https://reference.aspose.com/3d/java/).

**Q: Υπάρχει φόρουμ υποστήριξης για το Aspose.3D όπου μπορώ να θέσω ερωτήσεις;**  
A: Σίγουρα—επισκεφθείτε το [Aspose.3D support forum](https://forum.aspose.com/c/3d/18) για να συνδεθείτε με την κοινότητα και τους ειδικούς.

**Q: Πώς μπορώ να αποκτήσω προσωρινή άδεια για το Aspose.3D;**  
A: Ζητήστε την μέσω της [σελίδας προσωρινής άδειας](https://purchase.aspose.com/temporary-license/) στον ιστότοπο Aspose.

**Q: Μπορώ να αλλάξω άλλες ιδιότητες υλικού εκτός του διασκορπιστικού;**  
A: Ναι, ιδιότητες όπως `Specular`, `Opacity` και προσαρμοσμένα δεδομένα χρήστη μπορούν να τροποποιηθούν χρησιμοποιώντας το ίδιο μοτίβο `props.set`.

## Συμπέρασμα

Τώρα έχετε μάθει **πώς να ορίσετε το διασκορπιστικό χρώμα**, **να ανακτήσετε ιδιότητες υλικού**, και **να διαχειριστείτε 3D ιδιότητες** σε μια σκηνή Java χρησιμοποιώντας το Aspose.3D. Αυτές οι τεχνικές σας παρέχουν λεπτομερή έλεγχο σε οποιοδήποτε 3D αντικείμενο, επιτρέποντας δυναμικά οπτικά εφέ και προσαρμογή σε χρόνο εκτέλεσης στις εφαρμογές σας.

---

**Τελευταία ενημέρωση:** 2026-09-13  
**Δοκιμή με:** Aspose.3D for Java 24.11  
**Συγγραφέας:** Aspose  

```java
import java.io.IOException;
import com.aspose.threed.Material;
import com.aspose.threed.Property;
import com.aspose.threed.PropertyCollection;
import com.aspose.threed.Scene;
import com.aspose.threed.Vector3;

String dataDir = "Your Document Directory";
Scene scene = Scene.fromFile(dataDir + "EmbeddedTexture.fbx");

Material material = scene.getRootNode().getChildNodes().get(0).getMaterial();
PropertyCollection props = material.getProperties();

// List All Properties (Inspect Before Changing)
for (Property prop : props) {
    System.out.println("Name" + prop.getName() + " Value = " + prop.getValue());
}

// Set Vector3 Value to Change Diffuse Color
props.set("Diffuse", new Vector3(1, 0, 1));

// Retrieve Material Property by Name
Object diffuse = (Vector3) props.get("Diffuse");
System.out.println(diffuse);

// Access Property Instance Directly
Property pdiffuse = props.findProperty("Diffuse");
System.out.println(pdiffuse);

// Access property value directly
System.out.println("Property value: " + pdiffuse.getValue());
```

## Σχετικά μαθήματα

- [Μετατροπή Mesh σε FBX και Ορισμός Χρώματος Υλικού σε Java 3D χρησιμοποιώντας Aspose.3D](/3d/java/geometry/share-mesh-geometry-data/)
- [Πώς να ενσωματώσετε υφή σε FBX με Java – Εφαρμογή Υλικών σε 3D Αντικείμενα χρησιμοποιώντας Aspose.3D](/3d/java/geometry/apply-materials-to-3d-objects/)
- [Αποθήκευση Αποδομένων 3D Σκηνών σε Αρχεία Εικόνας με Aspose.3D για Java](/3d/java/rendering-3d-scenes/render-to-file/)

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}