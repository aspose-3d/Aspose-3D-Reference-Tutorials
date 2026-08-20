---
date: 2026-05-19
description: Μάθετε πώς να μετατρέψετε το mesh σε FBX ενώ ορίζετε το Material Color
  και μοιράζεστε δεδομένα γεωμετρίας mesh σε Java 3D χρησιμοποιώντας το Aspose.3D.
keywords:
- convert mesh to fbx
- how to export fbx
- how to set material
- export mesh to fbx
- aspose 3d tutorial
linktitle: Μετατροπή Mesh σε FBX και Ορισμός Material Color σε Java 3D
schemas:
- author: Aspose
  dateModified: '2026-05-19'
  description: Learn how to convert mesh to FBX while setting material color and sharing
    mesh geometry data in Java 3D using Aspose.3D.
  headline: Convert Mesh to FBX and Set Material Color in Java 3D
  type: TechArticle
- questions:
  - answer: Yes, the shared mesh can be animated via skeletal rigs or morph targets
      while each node retains its own material.
    question: Can I reuse the same mesh for animated characters?
  - answer: Absolutely, Aspose.3D writes full UV data, so textures map correctly in
      downstream tools.
    question: Does the FBX export preserve UV coordinates?
  - answer: The library can stream meshes exceeding 2 GB without loading the entire
      file into memory, making it suitable for large scenes.
    question: What is the maximum file size Aspose.3D can handle?
  - answer: Pass a different `FileFormat` enum value, such as `FileFormat.FBX201400ASCII`,
      to `scene.save`.
    question: How do I change the FBX version?
  - answer: Yes, you can create a new `Scene`, add the desired nodes, and then save
      that scene to FBX.
    question: Is it possible to export only a subset of nodes?
  type: FAQPage
second_title: Aspose.3D Java API
title: Μετατροπή Mesh σε FBX και Ορισμός Material Color σε Java 3D
url: /el/java/geometry/share-mesh-geometry-data/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Μετατροπή Πλέγματος σε FBX και Ορισμός Χρώματος Υλικού σε Java 3D

## Εισαγωγή

Αν δημιουργείτε μια εφαρμογή 3D βασισμένη σε Java, συχνά θα χρειαστεί να επαναχρησιμοποιήσετε την ίδια γεωμετρία σε πολλαπλά αντικείμενα, δίνοντας σε κάθε παρουσία μια μοναδική εμφάνιση. Σε αυτό το tutorial θα μάθετε **πώς να μετατρέψετε πλέγμα σε FBX**, να μοιραστείτε τη βασική γεωμετρία του πλέγματος μεταξύ πολλών κόμβων και **να ορίσετε διαφορετικό χρώμα υλικού για κάθε κόμβο**. Στο τέλος θα έχετε μια έτοιμη για εξαγωγή σκηνή FBX που μπορείτε να ενσωματώσετε σε οποιαδήποτε μηχανή ή προβολέα.

## Σύντομες Απαντήσεις
- **Ποιος είναι ο κύριος στόχος;** Μετατροπή πλέγματος σε FBX, κοινή χρήση της γεωμετρίας του πλέγματος και ορισμός διακριτού χρώματος υλικού για κάθε κόμβο.  
- **Ποια βιβλιοθήκη απαιτείται;** Aspose.3D for Java.  
- **Πώς εξάγω το αποτέλεσμα;** Αποθηκεύστε τη σκηνή ως αρχείο FBX χρησιμοποιώντας `FileFormat.FBX7400ASCII`.  
- **Χρειάζομαι άδεια;** Απαιτείται προσωρινή ή πλήρης άδεια για παραγωγική χρήση.  
- **Ποια έκδοση της Java λειτουργεί;** Οποιοδήποτε περιβάλλον Java 8+.

## Τι είναι **convert mesh to FBX**?

Η μετατροπή πλέγματος σε FBX σημαίνει ότι παίρνετε ένα αντικείμενο πλέγματος που υπάρχει στη μνήμη και το γράφετε σε μορφή αρχείου FBX, ένα de‑facto πρότυπο που υποστηρίζεται από Maya, Blender, Unity και πολλά άλλα εργαλεία 3D. Η Aspose.3D εκτελεί το βαρέως έργο, έτσι χρειάζεται μόνο να καλέσετε `scene.save(...)` με το κατάλληλο `FileFormat`.

## Γιατί να μοιράζεστε δεδομένα γεωμετρίας πλέγματος;

Η κοινή χρήση γεωμετρίας μειώνει την κατανάλωση μνήμης και επιταχύνει την απόδοση επειδή οι υποκείμενοι buffer κορυφών αποθηκεύονται μόνο μία φορά. Αυτή η τεχνική είναι ιδανική για σκηνές με πολλά διπλότυπα αντικείμενα—σκεφτείτε δάση, πλήθη ή μοντέλα αρχιτεκτονικής—όπου κάθε παρουσία διαφέρει μόνο με τη μετασχηματισμό ή το υλικό.

## Προαπαιτούμενα

Πριν ξεκινήσουμε το tutorial, βεβαιωθείτε ότι έχετε τα παρακάτω προαπαιτούμενα:

- **Java Development Environment** – οποιοδήποτε IDE ή ρύθμιση γραμμής εντολών με Java 8 ή νεότερη.  
- **Aspose.3D Library** – κατεβάστε το πιο πρόσφατο JAR από την επίσημη ιστοσελίδα: [here](https://releases.aspose.com/3d/java/).

## Εισαγωγή Πακέτων

Ο χώρος ονομάτων `com.aspose.threed` περιέχει όλες τις κλάσεις που θα χρειαστείτε για τη δημιουργία σκηνών, πλεγμάτων και υλικών. Εισάγετε αυτά τα πακέτα στην αρχή του αρχείου Java ώστε ο μεταγλωττιστής να μπορεί να αναγνωρίσει τους τύπους.

```java
import com.aspose.threed.*;
```

## Βήμα 1: Αρχικοποίηση Αντικειμένου Σκηνής (initialize scene java)

Η κλάση `Scene` είναι το κορυφαίο κοντέινερ της Aspose.3D που αντιπροσωπεύει ολόκληρο τον 3D κόσμο. Η αρχικοποίηση ενός `Scene` σας παρέχει έναν καθαρό καμβά όπου μπορούν να προστεθούν πλέγματα, φωτισμοί και κάμερες.

```java
// Initialize scene object
Scene scene = new Scene();
```

## Βήμα 2: Ορισμός Διανυσμάτων Χρώματος

`Vector3` αντιπροσωπεύει ένα διάνυσμα τριών συνιστωσών (X, Y, Z) που χρησιμοποιείται για θέσεις, κατευθύνσεις ή χρώματα.  
Δημιουργήστε έναν πίνακα αντικειμένων `Vector3` που περιέχουν τιμές RGB. Κάθε διάνυσμα θα ανατεθεί αργότερα σε ξεχωριστό κόμβο, δίνοντας σε κάθε παρουσία τη δική της απόχρωση υλικού.

```java
// Define color vectors
Vector3[] colors = new Vector3[] {
    new Vector3(1, 0, 0),
    new Vector3(0, 1, 0),
    new Vector3(0, 0, 1)
};
```

## Βήμα 3: Δημιουργία 3D Πλέγματος Java Χρησιμοποιώντας Polygon Builder (create 3d mesh java)

Η κλάση `PolygonBuilder` σας επιτρέπει να δημιουργήσετε ένα πλέγμα ορίζοντας κορυφές και πρόσωπα χειροκίνητα. Αυτό το πλέγμα θα επαναχρησιμοποιηθεί σε όλους τους κόμβους, δείχνοντας πώς λειτουργεί η κοινή χρήση γεωμετρίας στην πράξη.

```java
// Call Common class create mesh using polygon builder method to set mesh instance
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

## Πώς να ορίσετε χρώμα υλικού για κάθε κόμβο;

`LambertMaterial` είναι ένας απλός τύπος υλικού που ορίζει το διαχυτικό χρώμα για ένα πλέγμα.  
Διατρέξτε τα διανύσματα χρώματος, δημιουργήστε έναν κόμβο κύβου για κάθε στοιχείο, εκχωρήστε ένα νέο `LambertMaterial` με το τρέχον χρώμα και τοποθετήστε τον κόμβο χρησιμοποιώντας έναν πίνακα μετάφρασης. Αυτό το μοτίβο εξασφαλίζει ότι κάθε κόμβος εμφανίζει μοναδικό χρώμα ενώ εξακολουθεί να αναφέρεται στο ίδιο υποκείμενο πλέγμα.

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

Καθορίστε τον φάκελο και το όνομα αρχείου για την αποθήκευση της 3D σκηνής στη υποστηριζόμενη μορφή αρχείου, σε αυτήν την περίπτωση, FBX7400ASCII. Αυτό το βήμα επίσης δείχνει **convert mesh to FBX** με την αποθήκευση της σκηνής με κοινή γεωμετρία στο δίσκο.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
MyDir = MyDir + "MeshGeometryData.fbx";

// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7400ASCII);
```

## Συνηθισμένα Προβλήματα & Συμβουλές

- **Προβλήματα Διαδρομής** – Βεβαιωθείτε ότι η διαδρομή του φακέλου τελειώνει με διαχωριστικό αρχείου (`/` ή `\\`) πριν προσαρτήσετε το όνομα αρχείου.  
- **Αρχικοποίηση Άδειας** – Εάν ξεχάσετε να ορίσετε την άδεια Aspose.3D πριν καλέσετε `scene.save`, η βιβλιοθήκη θα λειτουργήσει σε δοκιμαστική λειτουργία και μπορεί να ενσωματώσει υδατογράφημα.  
- **Αντικατάσταση Υλικού** – Η επαναχρησιμοποίηση της ίδιας παρουσίας `LambertMaterial` για πολλούς κόμβους θα προκαλέσει όλοι οι κόμβοι να μοιράζονται το ίδιο χρώμα. Δημιουργήστε πάντα νέο υλικό ανά επανάληψη, όπως φαίνεται παραπάνω.  
- **Μεγάλα Πλέγματα** – Για πλέγματα με εκατομμύρια κορυφές, εξετάστε τη χρήση του `MeshBuilder` με ευρετήριο πολυγώνων για να διατηρήσετε το μέγεθος του αρχείου FBX διαχειρίσιμο.

## Πρόσθετες Συχνές Ερωτήσεις

**Q1: Μπορώ να χρησιμοποιήσω την Aspose.3D με άλλα Java frameworks;**  
A1: Ναι, η Aspose.3D έχει σχεδιαστεί ώστε να λειτουργεί απρόσκοπτα με διάφορα Java frameworks.

**Q2: Υπάρχουν διαθέσιμες επιλογές αδειοδότησης για την Aspose.3D;**  
A2: Ναι, μπορείτε να εξερευνήσετε τις επιλογές αδειοδότησης [here](https://purchase.aspose.com/buy).

**Q3: Πώς μπορώ να λάβω υποστήριξη για την Aspose.3D;**  
A3: Επισκεφθείτε το Aspose.3D [forum](https://forum.aspose.com/c/3d/18) για υποστήριξη και συζητήσεις.

**Q4: Υπάρχει διαθέσιμη δωρεάν δοκιμή;**  
A4: Ναι, μπορείτε να αποκτήσετε δωρεάν δοκιμή [here](https://releases.aspose.com/).

**Q5: Πώς μπορώ να αποκτήσω προσωρινή άδεια για την Aspose.3D;**  
A5: Μπορείτε να αποκτήσετε προσωρινή άδεια [here](https://purchase.aspose.com/temporary-license/).

## Συχνές Ερωτήσεις

**Q: Μπορώ να επαναχρησιμοποιήσω το ίδιο πλέγμα για animated characters;**  
A: Ναι, το κοινό πλέγμα μπορεί να αναπαραχθεί μέσω σκελετικών rigs ή morph targets ενώ κάθε κόμβος διατηρεί το δικό του υλικό.

**Q: Διατηρεί η εξαγωγή FBX τις συντεταγμένες UV;**  
A: Απόλυτα, η Aspose.3D γράφει πλήρη δεδομένα UV, ώστε οι υφές να απεικονίζονται σωστά στα επόμενα εργαλεία.

**Q: Ποιο είναι το μέγιστο μέγεθος αρχείου που μπορεί να διαχειριστεί η Aspose.3D;**  
A: Η βιβλιοθήκη μπορεί να μεταφέρει πλέγματα που υπερβαίνουν τα 2 GB χωρίς να φορτώνει ολόκληρο το αρχείο στη μνήμη, καθιστώντας το κατάλληλο για μεγάλες σκηνές.

**Q: Πώς αλλάζω την έκδοση του FBX;**  
A: Περνάτε μια διαφορετική τιμή του enum `FileFormat`, όπως `FileFormat.FBX201400ASCII`, στη `scene.save`.

**Q: Είναι δυνατόν να εξάγω μόνο ένα υποσύνολο κόμβων;**  
A: Ναι, μπορείτε να δημιουργήσετε ένα νέο `Scene`, να προσθέσετε τους επιθυμητούς κόμβους και στη συνέχεια να αποθηκεύσετε αυτή τη σκηνή σε FBX.

## Συμπέρασμα

Συγχαρητήρια! Έχετε επιτυχώς **converted mesh to FBX**, μοιραστείτε δεδομένα γεωμετρίας πλέγματος μεταξύ πολλαπλών κόμβων και ορίσατε μεμονωμένα χρώματα υλικού χρησιμοποιώντας την Aspose.3D για Java. Αυτή η ροή εργασίας σας παρέχει μια ελαφριά, επαναχρησιμοποιήσιμη αρχιτεκτονική πλέγματος που μπορεί να εξαχθεί σε οποιοδήποτε pipeline συμβατό με FBX.

---

**Τελευταία Ενημέρωση:** 2026-05-19  
**Δοκιμή Με:** Aspose.3D 24.11 for Java  
**Συγγραφέας:** Aspose  

{{< blocks/products/products-backtop-button >}}

## Σχετικά Μαθήματα

- [Πώς να Διαχωρίσετε το Πλέγμα κατά Υλικό σε Java Χρησιμοποιώντας Aspose.3D](/3d/java/3d-mesh-data/split-meshes-by-material/)
- [Ενσωμάτωση Υφής FBX σε Java – Εφαρμογή Υλικών σε 3D Αντικείμενα με Aspose.3D](/3d/java/geometry/apply-materials-to-3d-objects/)
- [Πώς να Εξάγετε Σκηνή σε FBX και να Ανακτήσετε Πληροφορίες 3D Σκηνής σε Java](/3d/java/3d-scenes-and-models/get-scene-information/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}