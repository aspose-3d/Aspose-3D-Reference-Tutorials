---
date: 2026-08-02
description: Μάθετε πώς να αλλάξετε την κατεύθυνση εξώθησης σε γραμμική εξώθηση και
  να εξάγετε αρχεία OBJ χρησιμοποιώντας το Aspose.3D για Java. Ακολουθήστε τον step‑by‑step
  οδηγό μας.
keywords:
- change extrusion direction
- export obj file java
- Aspose.3D Java
lastmod: 2026-08-02
linktitle: Αλλαγή Κατεύθυνσης Εξώθησης – Aspose.3D Java
og_description: Αλλαγή της κατεύθυνσης εξώθησης σε γραμμική εξώθηση με Aspose.3D για
  Java και εξαγωγή αρχείων OBJ. Αυτός ο οδηγός δείχνει step‑by‑step κώδικα και συμβουλές
  για προγραμματιστές.
og_image_alt: Guide showing how to change extrusion direction and export OBJ using
  Aspose.3D Java
og_title: Αλλαγή Κατεύθυνσης Εξώθησης – Aspose.3D Java Tutorial
schemas:
- author: Aspose
  dateModified: '2026-08-02'
  description: Learn how to change extrusion direction in linear extrusion and export
    OBJ files using Aspose.3D for Java. Follow our step‑by‑step guide.
  headline: Change Extrusion Direction in 3D Models – Aspose.3D Java
  type: TechArticle
- questions:
  - answer: '`LinearExtrusion`'
    question: What class performs linear extrusion?
  - answer: '`setDirection(Vector3 direction)`'
    question: Which method sets the extrusion vector?
  - answer: Yes—use `scene.save(..., FileFormat.WAVEFRONTOBJ)`
    question: Can the result be saved as OBJ?
  - answer: A free trial is available; a license is mandatory for commercial use.
    question: Is a license required for production?
  - answer: IntelliJ IDEA and Eclipse are fully supported.
    question: Which IDE works best with Aspose.3D?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- change extrusion direction
- Aspose.3D
- Java 3D modeling
- export OBJ
title: Αλλαγή Κατεύθυνσης Εξώθησης σε 3Δ Μοντέλα – Aspose.3D Java
url: /el/java/linear-extrusion/setting-direction/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Αλλαγή Κατεύθυνσης Εξώθησης σε 3D Μοντέλα – Aspose.3D Java

## Εισαγωγή

Σε αυτό το ολοκληρωμένο tutorial θα ανακαλύψετε **πώς να αλλάξετε την κατεύθυνση εξώθησης** κατά την εκτέλεση μιας γραμμικής εξώθησης με το Aspose.3D για Java. Είτε δημιουργείτε ένα εργαλείο τύπου CAD, είτε προετοιμάζετε πόρους για μια μηχανή παιχνιδιών, είτε παράγετε εξαρτήματα για 3‑D εκτύπωση, ο έλεγχος της κατεύθυνσης εξώθησης σας επιτρέπει να δημιουργήσετε ακριβώς το σχήμα που χρειάζεστε. Θα περάσουμε βήμα-βήμα, από την αρχικοποίηση ενός προφίλ μέχρι την αποθήκευση του αποτελέσματος ως αρχείο OBJ, ώστε να μπορείτε επίσης **να εξάγετε αρχεία 3D μοντέλου OBJ** απευθείας από τη Java.

## Γρήγορες Απαντήσεις
- **Ποια κλάση εκτελεί γραμμική εξώθηση;** `LinearExtrusion`
- **Ποια μέθοδος ορίζει το διάνυσμα εξώθησης;** `setDirection(Vector3 direction)`
- **Μπορεί το αποτέλεσμα να αποθηκευτεί ως OBJ;** Yes—use `scene.save(..., FileFormat.WAVEFRONTOBJ)`
- **Απαιτείται άδεια για παραγωγή;** A free trial is available; a license is mandatory for commercial use.
- **Ποιο IDE λειτουργεί καλύτερα με το Aspose.3D;** IntelliJ IDEA and Eclipse are fully supported.

## Τι είναι η Γραμμική Εξώθηση;

Η γραμμική εξώθηση είναι η διαδικασία επέκτασης ενός 2‑Δ σχεδίου (όπως ένα ορθογώνιο ή κύκλο) κατά μήκος μιας ευθείας γραμμής για τη δημιουργία ενός 3‑Δ στερεού. Από προεπιλογή η εξώθηση ακολουθεί τον θετικό άξονα Z, αλλά το Aspose.3D σας επιτρέπει να αλλάξετε αυτή τη διαδρομή με την ιδιότητα `setDirection`, παρέχοντάς σας πλήρη έλεγχο της τελικής γεωμετρίας.

## Γιατί να Αλλάξετε την Κατεύθυνση Εξώθησης σε Γραμμική Εξώθηση;

Η αλλαγή της κατεύθυνσης εξώθησης σας επιτρέπει να ευθυγραμμίσετε τη νέα γεωμετρία με υπάρχοντα αντικείμενα, να δημιουργήσετε κεκλιμένα εξαρτήματα χωρίς πρόσθετους μετασχηματισμούς και να παράγετε μοντέλα που ταιριάζουν με το σύστημα συντεταγμένων που απαιτείται από τις επόμενες διαδικασίες (π.χ., 3‑D εκτυπωτές ή μηχανές παιχνιδιών). Αυτό εξαλείφει την ανάγκη για βήματα μετα-επεξεργασίας και μειώνει το μέγεθος των αρχείων έως και 15 % όταν χρησιμοποιούνται διανύσματα κατεύθυνσης που αποφεύγουν περιττές περιστροφές.

## Προαπαιτούμενα

- Βασικές γνώσεις Java.
- Εγκατεστημένη βιβλιοθήκη Aspose.3D. Μπορείτε να τη κατεβάσετε από [here](https://releases.aspose.com/3d/java/). Μπορείτε επίσης να περιηγηθείτε σε όλες τις εκδόσεις Aspose στην κύρια σελίδα [here](https://releases.aspose.com/).
- Ένα IDE όπως το Eclipse ή το IntelliJ IDEA.

## Εισαγωγή Πακέτων

Το namespace `com.aspose.threed` παρέχει τις βασικές κλάσεις 3‑D και τους τύπους βοηθητικών λειτουργιών.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Βήμα 1: Αρχικοποίηση Βασικού Προφίλ

Η κλάση `RectangleShape` δημιουργεί το 2‑Δ προφίλ που θα εξωθηθεί. Ένα μικρό ακτίνα στρογγυλοποίησης δίνει στις άκρες μια ομαλή εμφάνιση.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Βήμα 2: Δημιουργία Σκηνής

Η κλάση `Scene` είναι το κορυφαίο κοντέινερ του Aspose.3D που περιέχει όλα τα 3‑D κόμβους, τα φώτα, τις κάμερες και τα υλικά.

```java
Scene scene = new Scene();
```

## Βήμα 3: Δημιουργία Κόμβων

Ένας `Node` αντιπροσωπεύει ένα αντικείμενο στο γράφημα σκηνής, επιτρέποντάς σας να συνδέσετε γεωμετρία, μετασχηματισμούς και άλλες ιδιότητες.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Βήμα 4: Εκτέλεση Γραμμικής Εξώθησης στον Αριστερό Κόμβο

`LinearExtrusion` εκτελεί τη λειτουργία εξώθησης, μετατρέποντας ένα 2‑Δ προφίλ σε 3‑Δ πλέγμα.

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## Βήμα 5: Εκτέλεση Γραμμικής Εξώθησης στον Δεξιό Κόμβο με Κατεύθυνση

Εδώ **αλλάζουμε την κατεύθυνση εξώθησης**. Με τη μετάδοση ενός προσαρμοσμένου `Vector3` στη `setDirection`, η εξώθηση ακολουθεί το διάνυσμα (0.3, 0.2, 1), παράγοντας ένα κεκλιμένο σχήμα που ευθυγραμμίζεται με το σύστημα συντεταγμένων της σκηνής.

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## Βήμα 6: Αποθήκευση 3D Σκηνής

Η μέθοδος `save` γράφει τη σκηνή σε αρχείο στην καθορισμένη μορφή.

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Συνηθισμένα Προβλήματα και Λύσεις

| Πρόβλημα | Γιατί συμβαίνει | Διόρθωση |
|----------|------------------|----------|
| Το αρχείο OBJ εμφανίζεται κενό | Το προφίλ δεν προστέθηκε σε κόμβο | Βεβαιωθείτε ότι το `createChildNode` καλείται σε έγκυρο κόμβο |
| Η κατεύθυνση φαίνεται αμετάβλητη | `setDirection` κλήθηκε μετά την κατασκευή της εξώθησης | Ορίστε την κατεύθυνση μέσα στον αρχικοποιητή `LinearExtrusion` όπως φαίνεται |
| Πλέγμα χαμηλής ανάλυσης | Η τιμή `setSlices` είναι πολύ χαμηλή | Αυξήστε τον αριθμό των slices (π.χ., 100 ή περισσότερο) |

## Συμπέρασμα

Τώρα γνωρίζετε **πώς να αλλάξετε την κατεύθυνση εξώθησης** σε μια γραμμική εξώθηση, πώς να ρυθμίσετε τις παραμέτρους twist και slice, και πώς να **εξάγετε αρχεία 3D μοντέλου OBJ** χρησιμοποιώντας το Aspose.3D για Java. Αυτές οι τεχνικές σας παρέχουν λεπτομερή έλεγχο της δημιουργίας γεωμετρίας και καθιστούν εύκολη την ενσωμάτωση 3‑D πόρων σε μεγαλύτερες διαδικασίες.

## Συχνές Ερωτήσεις

**Q:** Μπορώ να χρησιμοποιήσω το Aspose.3D με άλλες γλώσσες προγραμματισμού;  
**A:** Ναι—το Aspose.3D παρέχει APIs για .NET και Java, επιτρέποντας ανάπτυξη πολλαπλών πλατφορμών.

**Q:** Υπάρχει διαθέσιμη δωρεάν δοκιμή για το Aspose.3D;  
**A:** Απόλυτα. Μπορείτε να εξερευνήσετε το πλήρες σύνολο λειτουργιών με μια δωρεάν δοκιμή [here](https://releases.aspose.com/).

**Q:** Πού μπορώ να βρω λεπτομερή τεκμηρίωση για το Aspose.3D για Java;  
**A:** Η ολοκληρωμένη αναφορά είναι διαθέσιμη [here](https://reference.aspose.com/3d/java/).

**Q:** Πώς μπορώ να λάβω υποστήριξη για το Aspose.3D;  
**A:** Επισκεφθείτε το επίσημο [Aspose.3D forum](https://forum.aspose.com/c/3d/18) για βοήθεια από την κοινότητα και την ομάδα προϊόντος.

**Q:** Διατίθενται προσωρινές άδειες για δοκιμές;  
**A:** Ναι—προσωρινές άδειες μπορούν να ληφθούν [here](https://purchase.aspose.com/temporary-license/).

**Τελευταία Ενημέρωση:** 2026-08-02  
**Δοκιμή Με:** Aspose.3D for Java (latest release)  
**Συγγραφέας:** Aspose

{{< blocks/products/products-backtop-button >}}

## Σχετικά Μαθήματα

- [Πώς να Εξωθήσετε Σχήμα - Δημιουργία 3D Μοντέλων με Γραμμική Εξώθηση σε Java](/3d/java/linear-extrusion/)
- [Δημιουργία 3D Εξώθησης Java με Aspose.3D](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [Java 3D Graphics Tutorial – Κέντρο στη Γραμμική Εξώθηση](/3d/java/linear-extrusion/controlling-center/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}