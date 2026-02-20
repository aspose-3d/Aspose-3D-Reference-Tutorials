---
date: 2026-01-27
description: Μάθετε μοντελοποίηση 3D σε Java δημιουργώντας κυλίνδρους με κεκλιμένη
  βάση χρησιμοποιώντας το Aspose.3D for Java. Αυτό το αρχάριο σεμινάριο 3D δείχνει
  πώς να εγκαταστήσετε το Aspose 3D, να εφαρμόσετε μετασχηματισμό κλίσης και να εξάγετε
  αρχείο OBJ σε Java.
linktitle: Java 3D Modeling – Sheared Bottom Cylinders with Aspose.3D
second_title: Aspose.3D Java API
title: Java 3D Μοντελοποίηση – Κύλινδροι με Κόψιμο στο Κάτω Μέρος με Aspose.3D
url: /el/java/cylinders/creating-cylinders-with-sheared-bottom/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Java 3D Modeling – Κυλίνδρομοι με Κεκλιμένη Βάση με Aspose.3D

## Εισαγωγή

Καλώς ήρθατε σε αυτό το **java 3d modeling** tutorial! Σε αυτόν τον οδηγό βήμα‑βήμα θα δημιουργήσουμε έναν κύλινδρο του οποίου η βάση είναι κεκλιμένη, χρησιμοποιώντας τη βιβλιοθήκη Aspose.3D για Java. Είτε ακολουθείτε ένα **beginner 3d tutorial** είτε θέλετε να προσθέσετε μια προσαρμοσμένη μετασχηματισμό shear σε ένα υπάρχον μοντέλο, θα δείτε ακριβώς πώς να ρυθμίσετε τη σκηνή, να εφαρμόσετε το shear, και τελικά να **export OBJ file java** για χρήση σε άλλα εργαλεία.

## Γρήγορες Απαντήσεις
- **Ποια βιβλιοθήκη χρησιμοποιείται;** Aspose.3D for Java  
- **Μπορώ να εγκαταστήσω το Aspose 3D μέσω Maven;** Ναι – προσθέστε την εξάρτηση Aspose.3D στο `pom.xml` σας  
- **Απαιτείται άδεια για ανάπτυξη;** Μια προσωρινή άδεια είναι επαρκής για δοκιμές· πλήρης άδεια απαιτείται για παραγωγή  
- **Ποια μορφή αρχείου παρουσιάζεται;** Wavefront OBJ (`.obj`)  
- **Πόσο χρόνο χρειάζεται το παράδειγμα για εκτέλεση;** Λιγότερο από ένα δευτερόλεπτο σε τυπικό workstation  

## Προαπαιτούμενα

Πριν ξεκινήσουμε, βεβαιωθείτε ότι έχετε τα εξής:

- Java Development Kit (JDK) εγκατεστημένο στο σύστημά σας.  
- **Install Aspose 3D** – κατεβάστε τη βιβλιοθήκη από την επίσημη ιστοσελίδα [here](https://releases.aspose.com/3d/java/).  
- Ένα IDE ή εργαλείο κατασκευής (Maven/Gradle) για τη διαχείριση της εξάρτησης Aspose.3D.  

## Εισαγωγή Πακέτων

Πρώτα, εισάγετε τις κλάσεις που θα χρειαστούμε για τη σκηνή, τη γεωμετρία και τη διαχείριση αρχείων.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Βήμα 1: Δημιουργία Σκηνής

Μια σκηνή είναι το κοντέινερ για όλα τα 3‑D αντικείμενα. Θα ξεκινήσουμε δημιουργώντας μια κενή σκηνή.

```java
// ExStart:3
// Create a scene
Scene scene = new Scene();
// ExEnd:3
```

## Βήμα 2: Δημιουργία Cylinder 1 – Πώς να εφαρμόσετε shear σε Cylinder

Τώρα θα δημιουργήσουμε τον πρώτο κύλινδρο και **apply shear transformation** στη βάση του. Αυτό δείχνει **how to shear cylinder** γεωμετρία απευθείας μέσω του API.

```java
// ExStart:4
// Create cylinder 1
Cylinder cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
// Customized shear bottom for cylinder 1
cylinder1.setShearBottom(new Vector2(0, 0.83)); // Shear 47.5deg in the xy plane (z-axis)
// Add cylinder 1 to the scene
scene.getRootNode().createChildNode(cylinder1).getTransform().setTranslation(10, 0, 0);
// ExEnd:4
```

## Βήμα 3: Δημιουργία Cylinder 2 – Standard Cylinder (No Shear)

Για σύγκριση, θα προσθέσουμε έναν δεύτερο κύλινδρο που **δεν** έχει κεκλιμένη βάση.

```java
// ExStart:5
// Create cylinder 2
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// Add cylinder 2 without a ShearBottom to the scene
scene.getRootNode().createChildNode(cylinder2);
// ExEnd:5
```

## Βήμα 4: Αποθήκευση Σκηνής – Export OBJ File Java

Τέλος, εξάγουμε τη σκηνή σε αρχείο Wavefront OBJ, επιδεικνύοντας τη χρήση του **export obj file java**.

```java
// ExStart:6
// Save scene
scene.save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

## Γιατί Αυτό Είναι Σημαντικό για Java 3D Modeling

Η προσθήκη shear σε ένα primitive σας επιτρέπει να δημιουργήσετε πιο οργανικές μορφές χωρίς να χρειάζεται να χρησιμοποιήσετε εξωτερικά εργαλεία μοντελοποίησης. Αυτή η τεχνική είναι χρήσιμη για:

- Αρχιτεκτονικές απεικονίσεις όπου απαιτούνται κεκλιμένες βάσεις.  
- Παιχνίδια assets που χρειάζονται προσαρμοσμένα footprints ενώ διατηρούν το γεωμετρικό βάρος χαμηλό.  
- Γρήγορη πρωτοτυποποίηση όπου θέλετε να ρυθμίσετε διαστάσεις προγραμματιστικά.  

## Κοινά Προβλήματα & Λύσεις

| Issue | Solution |
|-------|----------|
| **Shear appears too extreme** | Προσαρμόστε τις τιμές του `Vector2`; αντιπροσωπεύουν τον shear factor (εύρος 0‑1). |
| **OBJ file not opening in viewer** | Επαληθεύστε ότι ο προορισμός υπάρχει και ότι έχετε δικαιώματα εγγραφής. |
| **License exception at runtime** | Εφαρμόστε προσωρινή ή μόνιμη άδεια πριν δημιουργήσετε τη σκηνή (`License license = new License(); license.setLicense("Aspose.3D.lic");`). |

## Συχνές Ερωτήσεις

**Q: Μπορώ να χρησιμοποιήσω το Aspose.3D for Java με άλλες βιβλιοθήκες Java 3D;**  
A: Το Aspose.3D σχεδιάστηκε ώστε να λειτουργεί ανεξάρτητα. Αν και μπορείτε να το ενσωματώσετε με άλλες βιβλιοθήκες, παρέχει ήδη ένα πλήρες API για τις περισσότερες εργασίες 3‑D.

**Q: Είναι το Aspose.3D κατάλληλο για αρχάριους στη 3D μοντελοποίηση;**  
A: Απόλυτα. Το API είναι απλό, και αυτό το **beginner 3d tutorial** δείχνει τις βασικές έννοιες με ελάχιστο κώδικα.

**Q: Πού μπορώ να βρω πρόσθετη υποστήριξη για το Aspose.3D for Java;**  
A: Επισκεφθείτε το [Aspose.3D forum](https://forum.aspose.com/c/3d/18) για βοήθεια από την κοινότητα και επίσημες απαντήσεις.

**Q: Πώς μπορώ να αποκτήσω προσωρινή άδεια για το Aspose.3D;**  
A: Μπορείτε να λάβετε μια προσωρινή άδεια [here](https://purchase.aspose.com/temporary-license/).

**Q: Πού μπορώ να αγοράσω πλήρη άδεια Aspose.3D for Java;**  
A: Οι επιλογές αγοράς είναι διαθέσιμες [here](https://purchase.aspose.com/buy).

---

**Τελευταία Ενημέρωση:** 2026-01-27  
**Δοκιμή με:** Aspose.3D 24.11 for Java  
**Συγγραφέας:** Aspose

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Τελευταία Ενημέρωση:** 2026-01-27  
**Δοκιμή με:** Aspose.3D 24.11 for Java  
**Συγγραφέας:** Aspose