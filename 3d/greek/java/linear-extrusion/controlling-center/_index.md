---
title: Κέντρο Ελέγχου στη Γραμμική Εξώθηση με Aspose.3D για Java
linktitle: Κέντρο Ελέγχου στη Γραμμική Εξώθηση με Aspose.3D για Java
second_title: Aspose.3D Java API
description: Εξερευνήστε τον κόσμο των τρισδιάστατων γραφικών σε Java με το Aspose.3D. Ελέγξτε το κέντρο στη γραμμική εξώθηση χωρίς κόπο.
weight: 11
url: /el/java/linear-extrusion/controlling-center/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Κέντρο Ελέγχου στη Γραμμική Εξώθηση με Aspose.3D για Java

## Εισαγωγή

Στον κόσμο των τρισδιάστατων γραφικών και του προγραμματισμού Java, ο έλεγχος του κέντρου στη γραμμική εξώθηση παίζει καθοριστικό ρόλο στην επίτευξη των επιθυμητών αποτελεσμάτων στα έργα σας. Το Aspose.3D για Java παρέχει μια ισχυρή εργαλειοθήκη για απρόσκοπτη διαχείριση τέτοιων εργασιών. Σε αυτό το σεμινάριο, θα βουτήξουμε στη διαδικασία ελέγχου του κέντρου σε γραμμική εξώθηση χρησιμοποιώντας το Aspose.3D για Java, αναλύοντας κάθε βήμα για να εξασφαλίσουμε μια ομαλή και ολοκληρωμένη κατανόηση.

## Προαπαιτούμενα

Πριν ξεκινήσουμε αυτό το ταξίδι εκμάθησης, βεβαιωθείτε ότι έχετε τις ακόλουθες προϋποθέσεις:

1. Περιβάλλον ανάπτυξης Java: Βεβαιωθείτε ότι έχετε ρυθμίσει ένα περιβάλλον ανάπτυξης Java στον υπολογιστή σας.

2.  Aspose.3D για Java: Κάντε λήψη και εγκατάσταση της βιβλιοθήκης Aspose.3D. Μπορείτε να βρείτε τη βιβλιοθήκη και την τεκμηρίωσή της[εδώ](https://reference.aspose.com/3d/java/).

3. Κατάλογος εγγράφων: Δημιουργήστε έναν κατάλογο για να αποθηκεύσετε τα έγγραφά σας Java. Ας το ονομάσουμε "Ο Κατάλογος Εγγράφων σας".

## Εισαγωγή πακέτων

Στο περιβάλλον ανάπτυξης Java, εισαγάγετε τα απαραίτητα πακέτα για το Aspose.3D. Αυτό διασφαλίζει ότι ο κώδικάς σας έχει πρόσβαση στις λειτουργίες που παρέχονται από τη βιβλιοθήκη.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Βήμα 1: Ρυθμίστε το Βασικό Προφίλ

Αρχικοποιήστε το προφίλ βάσης που πρόκειται να εξωθηθεί. Σε αυτό το παράδειγμα, θα χρησιμοποιήσουμε ένα ορθογώνιο σχήμα με ακτίνα στρογγυλοποίησης 0,3.

```java
// Η διαδρομή προς τον κατάλογο εγγράφων.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Βήμα 2: Δημιουργήστε μια τρισδιάστατη σκηνή

Χτίστε τα θεμέλια του τρισδιάστατου κόσμου σας δημιουργώντας μια σκηνή.

```java
Scene scene = new Scene();
```

## Βήμα 3: Δημιουργήστε αριστερούς και δεξιούς κόμβους

Δημιουργήστε αριστερό και δεξιό κόμβο στη σκηνή σας. Αυτοί οι κόμβοι χρησιμεύουν ως καμβάς για τα τρισδιάστατα αντικείμενα σας.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Βήμα 4: Γραμμική εξώθηση με κεντρική ιδιότητα

Εκτελέστε γραμμική εξώθηση στον αριστερό κόμβο χωρίς κεντράρισμα και ορίστε τον αριθμό των τομών σε 3.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

## Βήμα 5: Ορίστε το επίπεδο εδάφους για αναφορά

Βελτιώστε την οπτική αναπαράσταση προσθέτοντας ένα επίπεδο γείωσης στον αριστερό κόμβο.

```java
left.createChildNode(new Box(0.01, 3, 3));
```

## Βήμα 6: Γραμμική εξώθηση με κεντρική ιδιότητα (δεξιός κόμβος)

Εκτελέστε γραμμική εξώθηση στον δεξιό κόμβο, αυτή τη φορά κεντράροντας την εξώθηση και ορίστε ξανά τον αριθμό των τμημάτων σε 3.

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

## Βήμα 7: Ορισμός επιπέδου γείωσης για αναφορά (δεξιός κόμβος)

Παρόμοια με τον αριστερό κόμβο, προσθέστε ένα επίπεδο γείωσης στον δεξιό κόμβο για αναφορά.

```java
right.createChildNode(new Box(0.01, 3, 3));
```

## Βήμα 8: Αποθηκεύστε την τρισδιάστατη σκηνή

Αποθηκεύστε την τρισδιάστατη σκηνή σας σε μορφή Wavefront OBJ.

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## συμπέρασμα

Ο έλεγχος του κέντρου σε γραμμική εξώθηση με το Aspose.3D για Java ανοίγει συναρπαστικές δυνατότητες στην ανάπτυξη τρισδιάστατων γραφικών. Ακολουθώντας αυτόν τον οδηγό βήμα προς βήμα, έχετε μάθει πώς να χειρίζεστε την ιδιότητα κέντρου, επιτρέποντάς σας να επιτύχετε τα επιθυμητά οπτικά εφέ στα έργα σας Java.

## Συχνές ερωτήσεις

### Ε1: Μπορώ να χρησιμοποιήσω το Aspose.3D για Java σε εμπορικά έργα;

 A1: Ναι, το Aspose.3D για Java είναι διαθέσιμο για εμπορική χρήση. Για λεπτομέρειες αδειοδότησης, επισκεφθείτε[εδώ](https://purchase.aspose.com/buy).

### Ε2: Υπάρχει διαθέσιμη δωρεάν δοκιμή;

 A2: Ναι, μπορείτε να εξερευνήσετε μια δωρεάν δοκιμή του Aspose.3D για Java[εδώ](https://releases.aspose.com/).

### Ε3: Πού μπορώ να βρω υποστήριξη για το Aspose.3D για Java;

 A3: Το φόρουμ κοινότητας Aspose.3D είναι ένα εξαιρετικό μέρος για να αναζητήσετε υποστήριξη και να μοιραστείτε τις εμπειρίες σας. Επισκεφθείτε το φόρουμ[εδώ](https://forum.aspose.com/c/3d/18).

### Ε4: Χρειάζομαι μια προσωρινή άδεια για δοκιμή;

A4: Ναι, εάν χρειάζεστε μια προσωρινή άδεια για σκοπούς δοκιμής, μπορείτε να αποκτήσετε μια[εδώ](https://purchase.aspose.com/temporary-license/).

### Ε5: Πού μπορώ να βρω την τεκμηρίωση;

 A5: Η τεκμηρίωση για το Aspose.3D για Java είναι διαθέσιμη[εδώ](https://reference.aspose.com/3d/java/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
