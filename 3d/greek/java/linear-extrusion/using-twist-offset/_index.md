---
date: 2025-12-19
description: Μάθετε πώς να δημιουργήσετε σκηνή 3D και να εξάγετε αρχείο 3D obj χρησιμοποιώντας
  το Twist Offset στην Γραμμική Εξώθηση με το Aspose.3D για Java.
linktitle: Create 3d scene with Twist Offset – Aspose.3D Java
second_title: Aspose.3D Java API
title: Δημιουργία 3Δ σκηνής με Twist Offset – Aspose.3D Java
url: /el/java/linear-extrusion/using-twist-offset/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Δημιουργία 3d σκηνής με Twist Offset – Aspose.3D για Java

## Εισαγωγή

Στον δυναμικό κόσμο των 3D γραφικών, η εκμάθηση του **δημιουργία 3d σκηνής** με γραμμική εξώθηση αποτελεί πραγματικό σημείο καμπής. Με το Aspose.3D για Java, μπορείτε να ανεβάσετε τις ικανότητές σας στη 3D μοντελοποίηση ενσωματώνοντας τη λειτουργία Twist Offset στη διαδικασία γραμμικής εξώθησης. Αυτό το tutorial θα σας καθοδηγήσει βήμα‑βήμα στη χρήση του Twist Offset στη Linear Extrusion με το Aspose.3D για Java, παρέχοντάς σας τα εργαλεία για τη δημιουργία εντυπωσιακών 3D σκηνών.

## Γρήγορες Απαντήσεις
- **Τι κάνει το Twist Offset;** Μετατοπίζει την αρχή της στρέψης κατά μήκος της διαδρομής εξώθησης, δίνοντάς σας μεγαλύτερο έλεγχο στη γεωμετρία.  
- **Ποια μορφή αρχείου χρησιμοποιείται για εξαγωγή;** Το παράδειγμα αποθηκεύει το μοντέλο ως Wavefront OBJ (`.obj`).  
- **Χρειάζεται άδεια για ανάπτυξη;** Μια δωρεάν δοκιμή λειτουργεί για δοκιμές· απαιτείται εμπορική άδεια για παραγωγή.  
- **Ποια έκδοση της Java απαιτείται;** Java 8 ή νεότερη.  
- **Μπορώ να αλλάξω τον αριθμό των φετών;** Ναι – η μέθοδος `setSlices` ορίζει την ομαλότητα της στρέψης.

## Προαπαιτούμενα

Πριν ξεκινήσετε το tutorial, βεβαιωθείτε ότι έχετε τα παρακάτω προαπαιτούμενα:

- Περιβάλλον Java: Βεβαιωθείτε ότι έχετε εγκαταστήσει ένα περιβάλλον ανάπτυξης Java στο σύστημά σας.  
- Aspose.3D για Java: Κατεβάστε και εγκαταστήστε τη βιβλιοθήκη Aspose.3D από τον [σύνδεσμο λήψης](https://releases.aspose.com/3d/java/).  
- Τεκμηρίωση: Εξοικειωθείτε με την [τεκμηρίωση του Aspose.3D για Java](https://reference.aspose.com/3d/java/).  

## Εισαγωγή Πακέτων

Στο έργο Java σας, εισάγετε τα απαραίτητα πακέτα για να αρχίσετε να χρησιμοποιείτε το Aspose.3D για Java. Βεβαιωθείτε ότι συμπεριλαμβάνετε τις απαιτούμενες βιβλιοθήκες για αδιάλειπτη ενσωμάτωση.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## Βήμα 1: Ρύθμιση του Περιβάλλοντος

Ξεκινήστε ρυθμίζοντας το περιβάλλον ανάπτυξης Java και βεβαιωθείτε ότι το Aspose.3D για Java είναι εγκατεστημένο σωστά.

## Βήμα 2: Αρχικοποίηση της Βασικής Προφίλ

Δημιουργήστε μια βασική προφίλ για εξώθηση, σε αυτήν την περίπτωση ένα `RectangleShape` με ακτίνα στρογγυλοποίησης 0.3.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
// Initialize the base profile to be extruded
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Βήμα 3: Δημιουργία 3D Σκηνής

Κατασκευάστε μια 3D σκηνή για να φιλοξενήσει τα εξωθημένα αντικείμενα.

```java
// Create a scene
Scene scene = new Scene();
```

## Βήμα 4: Δημιουργία Κόμβων

Δημιουργήστε κόμβους μέσα στη σκηνή για να αντιπροσωπεύουν διαφορετικές οντότητες.

```java
// Create left node
Node left = scene.getRootNode().createChildNode();
// Create right node
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Βήμα 5: Εκτέλεση Γραμμικής Εξώθησης

Εφαρμόστε γραμμική εξώθηση σε αριστερούς και δεξιούς κόμβους με διάφορες ιδιότητες.

```java
// Perform linear extrusion on left node using twist and slices property
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});

// Perform linear extrusion on right node using twist, twist offset, and slices property
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setTwistOffset(new Vector3(3, 0, 0)); }});
```

## Βήμα 6: Αποθήκευση της 3D Σκηνής

Αποθηκεύστε τη νεοδημιουργημένη 3D σκηνή με τη συγκεκριμένη μορφή αρχείου.

```java
// Save 3D scene
scene.save(MyDir + "TwistOffsetInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Πώς να αποθηκεύσετε 3d μοντέλο και να εξάγετε 3d obj

Η κλήση `scene.save` στο προηγούμενο βήμα **αποθηκεύει το 3d μοντέλο** ως αρχείο OBJ, το οποίο είναι μια ευρέως υποστηριζόμενη **εξαγωγή 3d obj** μορφή. Μπορείτε να αλλάξετε το όνομα του αρχείου ή να επιλέξετε άλλη υποστηριζόμενη μορφή (π.χ., STL, FBX) προσαρμόζοντας το enum `FileFormat`.

## Συμπέρασμα

Συγχαρητήρια! Έχετε εφαρμόσει επιτυχώς το Twist Offset στη Linear Extrusion χρησιμοποιώντας το Aspose.3D για Java. Αυτή η ισχυρή δυνατότητα ανοίγει έναν κόσμο δυνατοτήτων για τις 3D μοντελοποιήσεις σας, επιτρέποντάς σας να **δημιουργήσετε 3d σκηνή** με πολύπλοκες στρεπές και μετατοπίσεις, και στη συνέχεια να **αποθηκεύσετε 3d μοντέλο** σε μορφή έτοιμη για downstream pipelines.

## Συχνές Ερωτήσεις

### Q1: Μπορώ να χρησιμοποιήσω το Aspose.3D για Java σε μη εμπορικά έργα;

A1: Ναι, το Aspose.3D για Java μπορεί να χρησιμοποιηθεί τόσο σε εμπορικά όσο και σε μη εμπορικά έργα. Ελέγξτε τις [επιλογές αδειοδότησης](https://purchase.aspose.com/buy) για περισσότερες λεπτομέρειες.

### Q2: Πού μπορώ να βρω υποστήριξη για το Aspose.3D για Java;

A2: Επισκεφθείτε το [φόρουμ του Aspose.3D για Java](https://forum.aspose.com/c/3d/18) για βοήθεια και σύνδεση με την κοινότητα.

### Q3: Υπάρχει δωρεάν δοκιμή για το Aspose.3D για Java;

A3: Ναι, μπορείτε να εξερευνήσετε μια δωρεάν δοκιμαστική έκδοση από τη [σελίδα releases](https://releases.aspose.com/).

### Q4: Πώς μπορώ να αποκτήσω προσωρινή άδεια για το Aspose.3D για Java;

A4: Λάβετε μια προσωρινή άδεια για το έργο σας επισκεπτόμενοι [αυτόν τον σύνδεσμο](https://purchase.aspose.com/temporary-license/).

### Q5: Υπάρχουν επιπλέον παραδείγματα και tutorials διαθέσιμα;

A5: Ναι, ανατρέξτε στην [τεκμηρίωση](https://reference.aspose.com/3d/java/) για περισσότερα παραδείγματα και εις βάθος tutorials.

## Συχνές Ερωτήσεις

**Ε: Είναι αυτό το tutorial μέρος μιας σειράς tutorials του Aspose 3d;**  
Α: Ναι – είναι ένα επίσημο **aspose 3d tutorial** που παρουσιάζει μια συγκεκριμένη λειτουργία της βιβλιοθήκης.

**Ε: Μπορώ να χρησιμοποιήσω διαφορετικό σχήμα αντί για ορθογώνιο;**  
Α: Απόλυτα. Οποιαδήποτε υλοποίηση του `IProfile` (π.χ., `CircleShape`, προσαρμοσμένο `PolygonShape`) μπορεί να εξωθηθεί.

**Ε: Τι συμβαίνει αν παραλείψω το `setTwistOffset`;**  
Α: Η εξώθηση θα αρχίσει να στρέφεται από το αρχικό σημείο του προφίλ, παράγοντας μια συμμετρική στρέψη.

**Ε: Πώς αυξάνω την ομαλότητα της στρέψης;**  
Α: Αυξήστε την τιμή που περνάτε στο `setSlices`; μεγαλύτερο πλήθος φετών παράγει πιο ομαλή γεωμετρία.

**Ε: Ποιες άλλες μορφές αρχείων μπορώ να εξάγω εκτός από OBJ;**  
Α: Το Aspose.3D υποστηρίζει STL, FBX, GLTF, 3MF και αρκετές άλλες μέσω του enum `FileFormat`.

---

**Τελευταία ενημέρωση:** 2025-12-19  
**Δοκιμή με:** Aspose.3D 24.11 για Java  
**Συγγραφέας:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}