---
date: 2025-12-13
description: Μάθετε πώς να χρησιμοποιείτε το Aspose 3D Java για να μετασχηματίζετε
  κόμβους 3D. Αυτός ο οδηγός δείχνει πώς να χρησιμοποιείτε γωνίες Euler, να προσθέτετε
  περιστροφή 3D και να ορίζετε μετάφραση σε Java.
linktitle: Aspose 3D Java – Transform 3D Nodes with Euler Angles
second_title: Aspose.3D Java API
title: Aspose 3D Java – Μετασχηματισμός 3D Κόμβων με Γωνίες Euler
url: /el/java/geometry/transform-3d-nodes-with-euler-angles/
weight: 19
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Μετασχηματισμός 3Δ Κόμβων με Γωνίες Euler σε Java χρησιμοποιώντας Aspose.3D

## Εισαγωγή

Σε αυτό το εκπαιδευτικό υλικό θα ανακαλύψετε **πώς να χρησιμοποιήσετε aspose 3d java** για να μετασχηματίζετε 3Δ κόμβους εφαρμόζοντας γωνίες Euler. Στο τέλος του οδηγού θα μπορείτε να προσθέσετε περιστροφή 3δ, να ορίσετε μετάφραση java και να δημιουργήσετε δυναμικές σκηνές που αντιδρούν σε δεδομένα σε πραγματικό χρόνο.

## Γρήγορες Απαντήσεις
- **Ποια βιβλιοθήκη διαχειρίζεται 3Δ μετασχηματισμούς σε Java;** Aspose 3D for Java.  
- **Ποια μέθοδος ορίζει περιστροφή χρησιμοποιώντας γωνίες Euler;** `setEulerAngles()` στο transform του κόμβου.  
- **Πώς μετακινώ έναν κόμβο στο χώρο;** Χρησιμοποιήστε `setTranslation()` με ένα `Vector3`.  
- **Χρειάζεται άδεια για παραγωγική χρήση;** Ναι, απαιτείται εμπορική άδεια Aspose 3D.  
- **Μπορώ να εξάγω σε FBX;** Απολύτως – `scene.save(..., FileFormat.FBX7500ASCII)` λειτουργεί αμέσως.

## Προαπαιτούμενα

Πριν ξεκινήσετε το εκπαιδευτικό υλικό, βεβαιωθείτε ότι έχετε τα παρακάτω προαπαιτούμενα:

- Βασικές γνώσεις προγραμματισμού Java.  
- Java Development Kit (JDK) εγκατεστημένο στον υπολογιστή σας.  
- Βιβλιοθήκη Aspose.3D, την οποία μπορείτε να αποκτήσετε από την [Τεκμηρίωση Aspose.3D Java](https://reference.aspose.com/3d/java/).

## Εισαγωγή Πακέτων

Ξεκινήστε εισάγοντας τα απαραίτητα πακέτα στο έργο Java σας. Βεβαιωθείτε ότι η βιβλιοθήκη Aspose.3D έχει προστεθεί σωστά στο classpath. Αν δεν την έχετε κατεβάσει ακόμα, μπορείτε να βρείτε τον σύνδεσμο λήψης [εδώ](https://releases.aspose.com/3d/java/).

```java
import com.aspose.threed.*;
```

## aspose 3d java – Εργασία με Γωνίες Euler

### Βήμα 1. Αρχικοποίηση Σκηνής και Κόμβου

Πρώτα, δημιουργήστε μια σκηνή και έναν κόμβο που θα κρατά τη γεωμετρία που θέλετε να μετασχηματίσετε.

```java
// ExStart:AddTransformationToNodeByEulerAngles
// Initialize scene object
Scene scene = new Scene();

// Initialize Node class object
Node cubeNode = new Node("cube");
```

### Βήμα 2. Δημιουργία Mesh και Ορισμός Γεωμετρίας

Στη συνέχεια, δημιουργήστε ένα απλό mesh (ένα κύβο σε αυτήν την περίπτωση) και συνδέστε το με τον κόμβο.

```java
// Call Common class create mesh using polygon builder method to set mesh instance
Mesh mesh = Common.createMeshUsingPolygonBuilder();

// Point node to the Mesh geometry
cubeNode.setEntity(mesh);
```

## Προσθήκη Περιστροφής 3D σε Κόμβο

### Βήμα 3. Ορισμός Γωνιών Euler και Μετάφραση

Τώρα εφαρμόζουμε την περιστροφή χρησιμοποιώντας γωνίες Euler και μετακινούμε επίσης τον κόμβο σε μια ορατή θέση.

```java
// Euler angles
cubeNode.getTransform().setEulerAngles(new Vector3(0.3, 0.1, -0.5));

// Set translation
cubeNode.getTransform().setTranslation(new Vector3(0, 0, 20));
```

## Ορισμός Μετάφρασης Java – Τοποθέτηση του Κόμβου

Το βήμα μετάφρασης παραπάνω δείχνει **set translation java** σε πράξη: ο κόμβος μετατοπίζεται 20 μονάδες κατά τον άξονα Z ώστε να είναι ορατός μετά την απόδοση.

## Βήμα 4. Προσθήκη Κόμβου στη Σκηνή

Συνδέστε τον μετασχηματισμένο κόμβο με τον ριζικό κόμβο της σκηνής.

```java
// Add cube to the scene
scene.getRootNode().getChildNodes().add(cubeNode);
```

## Βήμα 5. Αποθήκευση 3D Σκηνής

Τέλος, εξάγετε τη σκηνή σε αρχείο FBX (ή σε οποιαδήποτε άλλη υποστηριζόμενη μορφή).

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
MyDir = MyDir + "TransformationToNode.fbx";

// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7500ASCII);
// ExEnd:AddTransformationToNodeByEulerAngles
System.out.println("\nTransformation added successfully to node.\nFile saved at " + MyDir);
```

Βεβαιωθείτε ότι αντικαθιστάτε το `"Your Document Directory"` με το κατάλληλο μονοπάτι στον υπολογιστή σας.

## Συμπέρασμα

Συγχαρητήρια! Μετασχηματίσατε με επιτυχία 3Δ κόμβους χρησιμοποιώντας γωνίες Euler σε Java με **aspose 3d java**. Πειραματιστείτε με διαφορετικές γωνίες και μεταφράσεις για να δημιουργήσετε δυναμικές και ελκυστικές 3Δ σκηνές.

## Συχνές Ερωτήσεις

### Q1: Μπορώ να χρησιμοποιήσω το Aspose.3D για Java σε εμπορικά έργα;

A1: Ναι, μπορείτε. Επισκεφθείτε τη [σελίδα αγοράς](https://purchase.aspose.com/buy) για λεπτομέρειες άδειας.

### Q2: Πού μπορώ να βρω υποστήριξη για το Aspose.3D;

A2: Το [φόρουμ Aspose.3D](https://forum.aspose.com/c/3d/18) είναι το σημείο για βοήθεια και σύνδεση με την κοινότητα.

### Q3: Υπάρχει δωρεάν δοκιμή διαθέσιμη;

A3: Ναι, μπορείτε να εξερευνήσετε τη [δωρεάν δοκιμή](https://releases.aspose.com/) για να δοκιμάσετε τις δυνατότητες του Aspose.3D.

### Q4: Πώς μπορώ να αποκτήσω προσωρινή άδεια;

A4: Μπορείτε να αποκτήσετε προσωρινή άδεια [εδώ](https://purchase.aspose.com/temporary-license/).

### Q5: Πού μπορώ να βρω την τεκμηρίωση;

A5: Η [τεκμηρίωση](https://reference.aspose.com/3d/java/) παρέχει ολοκληρωμένες οδηγίες για τη χρήση του Aspose.3D για Java.

## Συχνές Ερωτήσεις

**Ε: Ποια είναι η διαφορά μεταξύ γωνιών Euler και περιστροφής quaternion;**  
Α: Οι γωνίες Euler είναι διαισθητικές (pitch, yaw, roll) αλλά μπορεί να υποφέρουν από gimbal lock, ενώ τα quaternions αποφεύγουν αυτό το πρόβλημα και είναι καλύτερα για ομαλές παρεμβολές.

**Ε: Μπορώ να αλυσίδω πολλαπλούς μετασχηματισμούς στον ίδιο κόμβο;**  
Α: Ναι. Καλέστε `setEulerAngles`, `setTranslation` και `setScale` σε οποιαδήποτε σειρά· η βιβλιοθήκη τα συνθέτει σε έναν ενιαίο πίνακα μετασχηματισμού.

**Ε: Είναι δυνατόν να εξάγω σε άλλες μορφές όπως OBJ ή STL;**  
Α: Απόλυτα. Αντικαταστήστε το `FileFormat.FBX7500ASCII` με `FileFormat.OBJ` ή `FileFormat.STL` στην κλήση `scene.save`.

**Ε: Πώς εφαρμόζω την ίδια περιστροφή σε πολλούς κόμβους ταυτόχρονα;**  
Α: Δημιουργήστε έναν γονικό κόμβο, εφαρμόστε την περιστροφή στον γονέα και προσθέστε τα παιδιά κάτω από αυτόν. Όλα τα παιδιά κληρονομούν τον μετασχηματισμό.

**Ε: Πρέπει να καλέσω κάποια μέθοδο καθαρισμού μετά την αποθήκευση;**  
Α: Ο συλλέκτης απορριμμάτων της Java διαχειρίζεται τις περισσότερες πόρους, αλλά μπορείτε ρητά να καλέσετε `scene.dispose()` εάν εργάζεστε με μεγάλες σκηνές σε εφαρμογή που τρέχει συνεχώς.

---

**Τελευταία Ενημέρωση:** 2025-12-13  
**Δοκιμασμένο Με:** Aspose.3D 23.12 for Java  
**Συγγραφέας:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}