---
date: 2026-02-22
description: Μάθετε πώς να ορίζετε την κατεύθυνση στην γραμμική εξώθηση και να εξάγετε
  μοντέλο 3D obj χρησιμοποιώντας το Aspose.3D για Java. Ακολουθήστε τον βήμα‑βήμα
  οδηγό μας.
linktitle: Setting Direction in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Πώς να ορίσετε την κατεύθυνση στην γραμμική εξώθηση με το Aspose.3D για Java
url: /el/java/linear-extrusion/setting-direction/
weight: 12
---

Make sure to preserve bold formatting.

Now produce final answer.{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Πώς να ορίσετε την κατεύθυνση στην γραμμική εξώθηση με το Aspose.3D για Java

## Introduction

Σε αυτό το ολοκληρωμένο tutorial θα ανακαλύψετε **πώς να ορίσετε την κατεύθυνση** κατά την εκτέλεση μιας γραμμικής εξώθησης με το Aspose.3D για Java. Είτε δημιουργείτε ένα εργαλείο τύπου CAD είτε παράγετε γεωμετρία για κινητήρα παιχνιδιών, ο έλεγχος της κατεύθυνσης εξώθησης σας επιτρέπει να δημιουργήσετε ακριβώς το σχήμα που χρειάζεστε. Θα περάσουμε βήμα‑βήμα, από την αρχικοποίηση ενός προφίλ μέχρι την αποθήκευση του αποτελέσματος ως αρχείο OBJ, ώστε να μπορείτε επίσης **να εξάγετε αρχεία 3d model obj** απευθείας από τη Java.

## Quick Answers
- **Ποια είναι η κύρια κλάση για γραμμική εξώθηση;** `LinearExtrusion`
- **Ποια μέθοδος ορίζει την κατεύθυνση εξώθησης;** `setDirection(Vector3 direction)`
- **Μπορώ να εξάγω το αποτέλεσμα ως OBJ;** Ναι, χρησιμοποιώντας `scene.save(..., FileFormat.WAVEFRONTOBJ)`
- **Χρειάζομαι άδεια για ανάπτυξη;** Διατίθεται δωρεάν δοκιμή· απαιτείται άδεια για παραγωγή.
- **Ποιο Java IDE λειτουργεί καλύτερα;** IntelliJ IDEA ή Eclipse υποστηρίζονται πλήρως.

## What is Linear Extrusion?

Η γραμμική εξώθηση παίρνει ένα 2‑Δ προφίλ (όπως ένα ορθογώνιο ή κύκλο) και το επεκτείνει κατά μια ευθεία γραμμή για να δημιουργήσει ένα 3‑Δ στερεό. Από προεπιλογή η εξώθηση ακολουθεί τον θετικό άξονα Z, αλλά το Aspose.3D σας επιτρέπει να αλλάξετε αυτή τη διαδρομή με την ιδιότητα `setDirection`.

## Why Set Direction in Linear Extrusion?

Η ρύθμιση προσαρμοσμένης κατεύθυνσης είναι χρήσιμη όταν:
- Στοίχιση γεωμετρίας με υπάρχοντα αντικείμενα σε μια σκηνή.
- Δημιουργία κεκλιμένων ή γωνιακών εξαρτημάτων χωρίς πρόσθετα βήματα μετασχηματισμού.
- Εξαγωγή μοντέλων που πρέπει να ταιριάζουν με συγκεκριμένο σύστημα συντεταγμένων (π.χ., για 3‑D εκτύπωση ή κινητήρες παιχνιδιών).

## Prerequisites

Πριν προχωρήσουμε, βεβαιωθείτε ότι έχετε:

- Βασικές γνώσεις Java.
- Εγκατεστημένη βιβλιοθήκη Aspose.3D. Μπορείτε να τη κατεβάσετε από [εδώ](https://releases.aspose.com/3d/java/).
- Ένα IDE όπως Eclipse ή IntelliJ IDEA.

## Import Packages

Πρώτα, εισάγετε τα namespaces που παρέχουν τις βασικές κλάσεις 3‑D και τους τύπους βοηθητικών λειτουργιών.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Step 1: Initialize Base Profile

Δημιουργήστε το σχήμα που θα εξωθηθεί. Σε αυτό το παράδειγμα χρησιμοποιούμε ένα `RectangleShape` με μικρή ακτίνα στρογγυλοποίησης για να δώσουμε στα άκρα μια ομαλή εμφάνιση.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Step 2: Create a Scene

Ένα αντικείμενο `Scene` λειτουργεί ως δοχείο για όλους τους 3‑Δ κόμβους, φωτισμούς, κάμερες και υλικά.

```java
Scene scene = new Scene();
```

## Step 3: Create Nodes

Προσθέστε δύο θυγατρικούς κόμβους στη ρίζα της σκηνής — έναν για την αριστερή εξώθηση και έναν για τη δεξιά εξώθηση. Ο δεξιός κόμβος μετατοπίζεται ώστε τα δύο αντικείμενα να μην επικαλύπτονται.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Step 4: Perform Linear Extrusion on the Left Node

Εξάγετε το προφίλ στον αριστερό κόμβο χρησιμοποιώντας την προεπιλεγμένη κατεύθυνση του άξονα Z. Προσθέτουμε επίσης μια πλήρη περιστροφή 360° και αυξάνουμε τον αριθμό των φετών για ένα πιο ομαλό πλέγμα.

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## Step 5: Perform Linear Extrusion on the Right Node with Direction

Εδώ **ορίζουμε την κατεύθυνση**. Με τη μετάδοση ενός προσαρμοσμένου `Vector3` στο `setDirection`, η εξώθηση ακολουθεί το διάνυσμα (0.3, 0.2, 1), παράγοντας ένα κεκλιμένο σχήμα.

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## Step 6: Save 3D Scene

Τέλος, εξάγετε τη σκηνή στη μορφή Wavefront OBJ. Αυτό το βήμα δείχνει πώς να **αποθηκεύσετε αρχεία obj java** έργα και κάνει εύκολο το άνοιγμα του αποτελέσματος σε οποιονδήποτε 3‑D προβολέα.

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Common Issues and Solutions

| Πρόβλημα | Γιατί συμβαίνει | Διόρθωση |
|----------|----------------|----------|
| Το αρχείο OBJ εμφανίζεται κενό | Το προφίλ δεν προστέθηκε σε κόμβο | Βεβαιωθείτε ότι το `createChildNode` καλείται σε έγκυρο κόμβο |
| Η κατεύθυνση φαίνεται αμετάβλητη | `setDirection` κλήθηκε μετά την κατασκευή της εξώθησης | Ορίστε την κατεύθυνση μέσα στον αρχικοποιητή `LinearExtrusion` όπως φαίνεται |
| Πλέγμα χαμηλής ανάλυσης | Η τιμή `setSlices` είναι πολύ μικρή | Αυξήστε τον αριθμό φετών (π.χ., 100 ή περισσότερο) |

## Conclusion

Τώρα γνωρίζετε **πώς να ορίσετε την κατεύθυνση** σε μια γραμμική εξώθηση, πώς να ρυθμίσετε τις παραμέτρους περιστροφής και φετών, και πώς να **εξάγετε αρχεία 3d model obj** χρησιμοποιώντας το Aspose.3D για Java. Αυτές οι τεχνικές σας δίνουν λεπτομερή έλεγχο στη δημιουργία γεωμετρίας και καθιστούν εύκολη την ενσωμάτωση 3‑D πόρων σε μεγαλύτερα pipelines.

## FAQ's

### Q1: Μπορώ να χρησιμοποιήσω το Aspose.3D με άλλες γλώσσες προγραμματισμού;

A1: Το Aspose.3D υποστηρίζει διάφορες γλώσσες προγραμματισμού, συμπεριλαμβανομένων .NET και Java.

### Q2. Υπάρχει διαθέσιμη δωρεάν δοκιμή για το Aspose.3D;

A2: Ναι, μπορείτε να εξερευνήσετε τις δυνατότητες του Aspose.3D με μια δωρεάν δοκιμή [εδώ](https://releases.aspose.com/).

### Q3: Πού μπορώ να βρω λεπτομερή τεκμηρίωση για το Aspose.3D για Java;

A3: Η ολοκληρωμένη τεκμηρίωση είναι διαθέσιμη [εδώ](https://reference.aspose.com/3d/java/).

### Q4: Πώς μπορώ να λάβω υποστήριξη για το Aspose.3D;

A4: Επισκεφθείτε το [Aspose.3D forum](https://forum.aspose.com/c/3d/18) για οποιαδήποτε βοήθεια ή ερωτήματα.

### Q5: Υπάρχουν προσωρινές άδειες διαθέσιμες για το Aspose.3D;

A5: Ναι, μπορείτε να αποκτήσετε μια προσωρινή άδεια [εδώ](https://purchase.aspose.com/temporary-license/).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Last Updated:** 2026-02-22  
**Tested With:** Aspose.3D for Java (latest release)  
**Author:** Aspose