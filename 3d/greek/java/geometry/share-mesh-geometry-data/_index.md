---
date: 2026-02-17
description: Μάθετε πώς να μετατρέψετε το πλέγμα σε FBX, ορίζοντας το χρώμα του υλικού
  και μοιράζοντας τα δεδομένα γεωμετρίας του πλέγματος σε Java 3D με χρήση του Aspose.3D.
linktitle: Convert Mesh to FBX and Set Material Color in Java 3D
second_title: Aspose.3D Java API
title: Μετατροπή Πλέγματος σε FBX και Ορισμός Χρώματος Υλικού σε Java 3D
url: /el/java/geometry/share-mesh-geometry-data/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Μετατροπή Mesh σε FBX και Ορισμός Χρώματος Υλικού σε Java 3D

## Εισαγωγή

Αν δημιουργείτε μια 3D εφαρμογή βασισμένη σε Java, συχνά χρειάζεται να επαναχρησιμοποιήσετε την ίδια γεωμετρία σε πολλαπλά αντικείμενα ενώ δίνετε σε κάθε αντίτυπο μια μοναδική εμφάνιση. Σε αυτό το tutorial θα μάθετε **πώς να μετατρέψετε mesh σε FBX**, να μοιραστείτε τη βασική γεωμετρία του mesh μεταξύ πολλών κόμβων και **να ορίσετε διαφορετικό χρώμα υλικού για κάθε κόμβο**. Στο τέλος θα έχετε μια σκηνή FBX έτοιμη για εξαγωγή που μπορείτε να ενσωματώσετε σε οποιονδήποτε κινητήρα ή προβολέα.

## Σύντομες Απαντήσεις
- **Ποιος είναι ο κύριος στόχος;** Μετατροπή mesh σε FBX, κοινή χρήση της γεωμετρίας του mesh και ορισμός διακριτού χρώματος υλικού για κάθε κόμβο.  
- **Ποια βιβλιοθήκη απαιτείται;** Aspose.3D for Java.  
- **Πώς εξάγω το αποτέλεσμα;** Αποθηκεύστε τη σκηνή ως αρχείο FBX χρησιμοποιώντας `FileFormat.FBX7400ASCII`.  
- **Χρειάζεται άδεια;** Απαιτείται προσωρινή ή πλήρης άδεια για παραγωγική χρήση.  
- **Ποια έκδοση Java λειτουργεί;** Οποιοδήποτε περιβάλλον Java 8+.

## Τι είναι **convert mesh to FBX**;

`convert mesh to fbx` είναι η διαδικασία λήψης ενός αντικειμένου mesh που δημιουργήθηκε ή τροποποιήθηκε στη μνήμη και εγγραφής του σε μορφή αρχείου FBX, η οποία υποστηρίζεται ευρέως από εργαλεία 3D όπως Maya, Blender και Unity. Η Aspose.3D αναλαμβάνει το βαρέως βάρους κομμάτι, οπότε χρειάζεται μόνο να καλέσετε `scene.save(...)` με το κατάλληλο `FileFormat`.

## Γιατί να μοιράζεστε δεδομένα γεωμετρίας mesh;

Η κοινή χρήση γεωμετρίας μειώνει την κατανάλωση μνήμης και επιταχύνει την απόδοση επειδή οι υποκείμενοι vertex buffers αποθηκεύονται μόνο μία φορά. Αυτή η τεχνική είναι ιδανική για σκηνές με πολλά αντίγραφα αντικειμένων—π.χ. δάση, πλήθη ή μοντέλα αρχιτεκτονικής—όπου κάθε αντίτυπο διαφέρει μόνο με μετασχηματισμό ή υλικό.

## Προαπαιτούμενα

Πριν προχωρήσουμε στο tutorial, βεβαιωθείτε ότι έχετε τα παρακάτω:

- **Java Development Environment** – οποιοδήποτε IDE ή ρύθμιση γραμμής εντολών με Java 8 ή νεότερη.  
- **Aspose.3D Library** – κατεβάστε το τελευταίο JAR από την επίσημη ιστοσελίδα: [here](https://releases.aspose.com/3d/java/).

## Εισαγωγή Πακέτων

Ξεκινήστε εισάγοντας τα απαραίτητα πακέτα στο έργο Java σας. Αυτό το βήμα είναι κρίσιμο για την πρόσβαση στις λειτουργίες που παρέχει η βιβλιοθήκη Aspose.3D.

```java
import com.aspose.threed.*;
```

## Βήμα 1: Αρχικοποίηση Αντικειμένου Σκηνής (initialize scene java)

Ας ξεκινήσουμε τη διαδικασία αρχικοποιώντας ένα αντικείμενο σκηνής. Αυτό θα λειτουργήσει ως καμβάς όπου θα εκτυλιχθεί η 3D μαγεία μας.

```java
// Initialize scene object
Scene scene = new Scene();
```

## Βήμα 2: Ορισμός Διανυσμάτων Χρώματος

Σε αυτό το βήμα, ορίζουμε έναν πίνακα διανυσμάτων χρώματος που θα εφαρμοστούν σε διαφορετικά στοιχεία της 3D σκηνής μας.

```java
// Define color vectors
Vector3[] colors = new Vector3[] {
    new Vector3(1, 0, 0),
    new Vector3(0, 1, 0),
    new Vector3(0, 0, 1)
};
```

## Βήμα 3: Δημιουργία 3D Mesh σε Java Χρησιμοποιώντας Polygon Builder (create 3d mesh java)

Χρησιμοποιήστε την κλάση Common για να δημιουργήσετε ένα mesh με τη μέθοδο polygon builder. Αυτό το mesh θα αποτελέσει τη βάση για τα 3D στοιχεία μας.

```java
// Call Common class create mesh using polygon builder method to set mesh instance
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

## Πώς να ορίσετε το χρώμα υλικού για κάθε κόμβο;

Επαναλάβετε μέσω των διανυσμάτων χρώματος, δημιουργήστε κόμβους κύβων και ορίστε ιδιότητες όπως υλικό, **set material color**, και μετάθεση. Αυτό αποτελεί τον πυρήνα του ελέγχου της οπτικής εμφάνισης κάθε αντίτυπου mesh.

```java
int idx = 0;
for(Vector3 color : colors) {
    // Initialize cube node object
    Node cube = new Node("cube");
    cube.setEntity(mesh);
    LambertMaterial mat = new LambertMaterial();
    // Set color
    mat.setDiffuseColor(color);
    // Set material
    cube.setMaterial(mat);
    // Set translation
    cube.getTransform().setTranslation(new Vector3(idx++ * 20, 0, 0));
    // Add cube node
    scene.getRootNode().addChildNode(cube);
}
```

## Βήμα 5: Αποθήκευση της 3D Σκηνής (save scene fbx, convert mesh to fbx)

Καθορίστε τον φάκελο και το όνομα αρχείου για την αποθήκευση της 3D σκηνής στη υποστηριζόμενη μορφή αρχείου, σε αυτήν την περίπτωση FBX7400ASCII. Αυτό το βήμα επίσης επιδεικνύει **convert mesh to FBX**.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
MyDir = MyDir + "MeshGeometryData.fbx";

// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7400ASCII);
```

## Συνηθισμένα Πιθανά Προβλήματα & Συμβουλές

- **Path Issues** – Βεβαιωθείτε ότι η διαδρομή του φακέλου λήγει με διαχωριστικό αρχείου (`/` ή `\\`) πριν προσαρτήσετε το όνομα του αρχείου.  
- **License Initialization** – Αν ξεχάσετε να ορίσετε την άδεια Aspose.3D πριν καλέσετε `scene.save`, η βιβλιοθήκη θα λειτουργήσει σε λειτουργία δοκιμής και μπορεί να ενσωματώσει υδατογράφημα.  
- **Material Overwrites** – Η επαναχρήση του ίδιου αντικειμένου `LambertMaterial` για πολλούς κόμβους θα κάνει όλους τους κόμβους να μοιράζονται το ίδιο χρώμα. Δημιουργήστε πάντα νέο υλικό σε κάθε επανάληψη, όπως φαίνεται παραπάνω.  
- **Large Meshes** – Για meshes με εκατομμύρια κορυφές, εξετάστε τη χρήση του `MeshBuilder` με ευρετηριασμένα πολύγωνα ώστε το μέγεθος του αρχείου FBX να παραμένει διαχειρίσιμο.

## Πρόσθετες Συχνές Ερωτήσεις

**Q1: Μπορώ να χρησιμοποιήσω την Aspose.3D με άλλα Java frameworks;**  
A1: Ναι, η Aspose.3D έχει σχεδιαστεί ώστε να λειτουργεί άψογα με διάφορα Java frameworks.

**Q2: Υπάρχουν διαθέσιμες επιλογές αδειοδότησης για την Aspose.3D;**  
A2: Ναι, μπορείτε να εξερευνήσετε τις επιλογές αδειοδότησης [here](https://purchase.aspose.com/buy).

**Q3: Πώς μπορώ να λάβω υποστήριξη για την Aspose.3D;**  
A3: Επισκεφθείτε το Aspose.3D [forum](https://forum.aspose.com/c/3d/18) για υποστήριξη και συζητήσεις.

**Q4: Υπάρχει δωρεάν δοκιμή διαθέσιμη;**  
A4: Ναι, μπορείτε να αποκτήσετε δωρεάν δοκιμή [here](https://releases.aspose.com/).

**Q5: Πώς μπορώ να αποκτήσω προσωρινή άδεια για την Aspose.3D;**  
A5: Μπορείτε να λάβετε προσωρινή άδεια [here](https://purchase.aspose.com/temporary-license/).

## Συμπέρασμα

Συγχαρητήρια! Έχετε μετατρέψει επιτυχώς το mesh σε FBX, μοιραστεί τα δεδομένα γεωμετρίας του mesh μεταξύ πολλαπλών κόμβων και ορίσει ατομικά χρώματα υλικού χρησιμοποιώντας την Aspose.3D for Java. Αυτή η ροή εργασίας σας παρέχει μια ελαφριά, επαναχρησιμοποιήσιμη αρχιτεκτονική mesh που μπορεί να εξαχθεί σε οποιοδήποτε pipeline συμβατό με FBX.

---

**Last Updated:** 2026-02-17  
**Tested With:** Aspose.3D 24.11 for Java  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}