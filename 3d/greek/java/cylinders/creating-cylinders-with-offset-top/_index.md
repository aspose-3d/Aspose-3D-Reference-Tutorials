---
date: 2026-04-08
description: Μάθετε πώς να δημιουργήσετε έναν κύλινδρο με μετατόπιση στην κορυφή στο
  Aspose.3D για Java, προσθέστε παιδικό κόμβο Java, ορίστε τη μετατόπιση στην κορυφή,
  δημιουργήστε 3D μοντέλο και εξάγετε OBJ χρησιμοποιώντας προσωρινή άδεια Aspose.
keywords:
- aspose temporary license
- generate 3d model
- add child node java
- java export obj
- set offset top
linktitle: Προσωρινή Άδεια Aspose – Δημιουργία Κυλίνδρου με Μετατόπιση στην Κορυφή
  (Java)
second_title: Aspose.3D Java API
title: Προσωρινή Άδεια Aspose – Δημιουργία Κυλίνδρου με Μετατόπιση στην Κορυφή (Java)
url: /el/java/cylinders/creating-cylinders-with-offset-top/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose Temporary License – Δημιουργία Κυλίνδρου με Μετατόπιση στην Κορυφή (Java)

## Εισαγωγή

Αν θέλετε να **create cylinder** αντικείμενα με προσαρμοσμένη μετατόπιση στην κορυφή σε μια 3D σκηνή βασισμένη σε Java, το Aspose.3D κάνει τη διαδικασία απλή. Σε αυτό το tutorial θα περάσουμε βήμα προς βήμα—από τη ρύθμιση της σκηνής μέχρι την εξαγωγή του τελικού μοντέλου ως αρχείο OBJ—ώστε να ενσωματώσετε κυλίνδρους με μετατόπιση στην κορυφή στις εφαρμογές σας με σιγουριά. Στο τέλος του οδηγού θα καταλάβετε επίσης πώς μια **aspose temporary license** σας επιτρέπει να αξιολογήσετε αυτές τις δυνατότητες χωρίς πλήρη αγορά.

## Γρήγορες Απαντήσεις
- **Ποια βιβλιοθήκη χρησιμοποιείται;** Aspose.3D for Java  
- **Μπορώ να μετατοπίσω την κορυφή ενός κυλίνδρου;** Ναι, χρησιμοποιώντας `setOffsetTop`  
- **Πώς προσθέτω ένα παιδικό κόμβο σε Java;** Καλέστε `createChildNode` στον ριζικό κόμβο  
- **Σε ποια μορφή μπορώ να εξάγω;** Wavefront OBJ (`java export obj`)  
- **Χρειάζομαι άδεια για δοκιμή;** Μια **aspose temporary license** είναι διαθέσιμη για αξιολόγηση  

## Τι είναι η Aspose Temporary License;

Μια **aspose temporary license** είναι ένα βραχυπρόθεσμο, δωρεάν κλειδί αξιολόγησης που ξεκλειδώνει το πλήρες σύνολο λειτουργιών του Aspose.3D for Java κατά τη διάρκεια της ανάπτυξης και των δοκιμών. Αφαιρεί τα υδατογράμματα αξιολόγησης και σας επιτρέπει να δημιουργήσετε αρχεία 3D μοντέλων, όπως OBJ, STL ή FBX, ακριβώς όπως θα έκανε μια επί πληρωμή άδεια.

## Γιατί να Χρησιμοποιήσετε το Aspose.3D για Java;

- **High‑level API:** Δεν χρειάζεται να διαχειρίζεστε δεδομένα πλέγματος χαμηλού επιπέδου.  
- **Cross‑platform:** Λειτουργεί σε οποιοδήποτε περιβάλλον συμβατό με JVM.  
- **Built‑in exporters:** Αποθηκεύει απευθείας σε OBJ, STL, FBX και άλλα.  
- **Extensible:** Προσθέτετε εύκολα παιδικούς κόμβους, εφαρμόζετε μετασχηματισμούς και ενσωματώνετε άλλες βιβλιοθήκες Java.  

## Προαπαιτούμενα

Πριν ξεκινήσουμε, βεβαιωθείτε ότι έχετε:

- **Java Development Kit (JDK)** – εγκατεστημένη συμβατή έκδοση.  
- **Aspose.3D for Java library** – κατεβάστε το τελευταίο JAR από την επίσημη ιστοσελίδα [here](https://releases.aspose.com/3d/java/).  
- Ένα IDE της επιλογής σας (Eclipse, IntelliJ IDEA, NetBeans, κλ.).  

## Εισαγωγή Πακέτων

Πρώτα, εισάγετε τις κλάσεις που θα χρειαστείτε. Τοποθετήστε αυτές τις δηλώσεις στην αρχή του αρχείου Java:

```java
import com.aspose.threed.Cylinder;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Vector3;


import java.io.IOException;
```

## Οδηγός βήμα προς βήμα

### Βήμα 1: Δημιουργία Σκηνής Java 3D

Μια **java 3d scene** λειτουργεί ως ο container για όλα τα 3D αντικείμενα.

```java
// ExStart:1
// Create a scene
Scene scene = new Scene();
// ExEnd:1
```

### Βήμα 2: Αρχικοποίηση Κυλίνδρου με Μετατόπιση στην Κορυφή

Εδώ απαντάμε στο **how to create cylinder** με προσαρμοσμένη μετατόπιση. Ο κατασκευαστής ορίζει την ακτίνα, το ύψος, τις φέτες, τα στρώματα και αν ο κύλινδρος είναι κλειστός. Στη συνέχεια, μετατοπίζουμε την κορυφή χρησιμοποιώντας `setOffsetTop`.

```java
// ExStart:2
// Initialize cylinder
Cylinder cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
// Set OffsetTop
cylinder1.setOffsetTop(new Vector3(5, 3, 0));
// ExEnd:2
```

### Βήμα 3: Προσθήκη Παιδικού Κόμβου Java – Επισύναψη του Πρώτου Κυλίνδρου

Δημιουργούμε έναν παιδικό κόμβο κάτω από τον ριζικό κόμβο της σκηνής και μετακινούμε τον κύλινδρο στην επιθυμητή θέση.

```java
// ExStart:3
// Create ChildNode
scene.getRootNode().createChildNode(cylinder1).getTransform().setTranslation(10, 0, 0);
// ExEnd:3
```

### Βήμα 4: Αρχικοποίηση Δεύτερου Κυλίνδρου (Χωρίς Μετατόπιση)

Για σύγκριση, προσθέτουμε έναν κανονικό κύλινδρο χωρίς μετατόπιση.

```java
// ExStart:4
// Initialize second cylinder without customized OffsetTop
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// ExEnd:4
```

### Βήμα 5: Προσθήκη Παιδικού Κόμβου Java – Επισύναψη του Δεύτερου Κυλίνδρου

```java
// ExStart:5
// Create ChildNode
scene.getRootNode().createChildNode(cylinder2);
// ExEnd:5
```

### Βήμα 6: Java Export OBJ – Αποθήκευση της Σκηνής ως OBJ

Τέλος, **java export obj** ολόκληρη τη σκηνή (και τους δύο κυλίνδρους) ως αρχείο Wavefront OBJ, το οποίο υποστηρίζεται ευρέως από εργαλεία 3D.

```java
// ExStart:6
// Save
scene.save("Your Document Directory" + "CustomizedOffsetTopCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

Όταν εκτελέσετε το πρόγραμμα, θα βρείτε το `CustomizedOffsetTopCylinder.obj` στον καθορισμένο φάκελο, έτοιμο να ανοιχτεί στο Blender, Maya ή οποιονδήποτε άλλο προβολέα συμβατό με OBJ.

## Πώς να Δημιουργήσετε 3D Μοντέλο και να Εξάγετε OBJ σε Java

Ο συνδυασμός του `Scene.save(..., FileFormat.WAVEFRONTOBJ)` και της **aspose temporary license** σας επιτρέπει να **generate 3d model** αρχεία γρήγορα, χωρίς την ανάγκη εξωτερικών μετατροπέων. Αυτό είναι ιδιαίτερα χρήσιμο κατά τη φάση του πρωτοτύπου ή όταν μοιράζεστε πόρους με σχεδιαστές.

## Πραγματικές Περιπτώσεις Χρήσης

- **Architectural visualisation:** Οι κυλίνδροι με μετατόπιση στην κορυφή μοντελοποιούν κολώνες που στενεύουν προς την οροφή.  
- **Mechanical parts:** Δημιουργήστε πίσσες ή θήκες γραναζιών όπου η άνω επιφάνεια είναι σκόπιμα μετατοπισμένη.  
- **Game assets:** Παραγάγετε ποικίλα σχήματα πυλώνων άμεσα, μειώνοντας την ανάγκη για χειροποίητα πλέγματα.

## Κοινά Προβλήματα και Λύσεις

| Πρόβλημα | Αιτία | Διόρθωση |
|----------|-------|----------|
| **Το αρχείο OBJ είναι κενό** | Η σκηνή δεν αποθηκεύτηκε σωστά ή το μονοπάτι είναι λάθος. | Επιβεβαιώστε ότι ο φάκελος εξόδου υπάρχει και έχετε δικαιώματα εγγραφής. |
| **Η μετατόπιση δεν εφαρμόστηκε** | Χρήση παλαιότερης έκδοσης του Aspose.3D. | Ενημερώστε στη νεότερη βιβλιοθήκη όπου υποστηρίζεται το `setOffsetTop`. |
| **Ο παιδικός κόμβος δεν είναι ορατός** | Ο μετασχηματισμός δεν εφαρμόστηκε. | Βεβαιωθείτε ότι καλείτε `getTransform().setTranslation` μετά τη δημιουργία του παιδικού κόμβου. |

## Συχνές Ερωτήσεις

**Ε: Είναι το Aspose.3D συμβατό με διαφορετικά Java IDEs;**  
Α: Ναι, λειτουργεί απρόσκοπτα με Eclipse, IntelliJ IDEA, NetBeans και άλλα IDEs.

**Ε: Μπορώ να εφαρμόσω υφές στα δημιουργημένα 3D αντικείμενα;**  
Α: Σίγουρα! Χρησιμοποιήστε την κλάση `Material` για να αναθέσετε υφές και ιδιότητες επιφάνειας.

**Ε: Υπάρχουν επιλογές αδειοδότησης για το Aspose.3D;**  
Α: Διατίθενται διάφορα μοντέλα αδειοδότησης· μπορείτε να τα εξερευνήσετε [here](https://purchase.aspose.com/buy).

**Ε: Πώς μπορώ να λάβω βοήθεια ή να μοιραστώ εμπειρίες;**  
Α: Συμμετέχετε στο φόρουμ της κοινότητας Aspose.3D [here](https://forum.aspose.com/c/3d/18) για υποστήριξη και συζήτηση.

**Ε: Διατίθεται προσωρινή άδεια για δοκιμές;**  
Α: Ναι, μια **aspose temporary license** μπορεί να ληφθεί για αξιολόγηση [here](https://purchase.aspose.com/temporary-license/).

---

**Τελευταία ενημέρωση:** 2026-04-08  
**Δοκιμάστηκε με:** Aspose.3D for Java 24.12 (latest)  
**Συγγραφέας:** Aspose

---

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}