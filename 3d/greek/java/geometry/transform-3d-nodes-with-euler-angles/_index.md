---
date: 2026-06-13
description: Μάθετε πώς να δημιουργήσετε mesh aspose java και να μετασχηματίσετε 3D
  nodes χρησιμοποιώντας Euler angles, να προσθέσετε rotation 3D, να ορίσετε translation
  java, και να εξάγετε scenes αποδοτικά.
keywords:
- create mesh aspose java
- set translation java
- euler angles java
- aspose 3d rotation
- export fbx java
linktitle: Δημιουργία Mesh Aspose Java – Μετασχηματισμός 3D nodes με Euler Angles
schemas:
- author: Aspose
  dateModified: '2026-06-13'
  description: Learn how to create mesh aspose java and transform 3D nodes using Euler
    angles, add rotation 3D, set translation java, and export scenes efficiently.
  headline: Create Mesh Aspose Java – Transform 3D Nodes with Euler Angles
  type: TechArticle
- questions:
  - answer: Euler angles are intuitive (pitch, yaw, roll) but can suffer from gimbal
      lock, while quaternions avoid that issue and provide smoother interpolation
      for animations.
    question: What is the difference between Euler angles and quaternion rotation?
  - answer: Yes. Call `setEulerAngles`, `setTranslation`, and `setScale` in any order;
      the library composes them into a single transform matrix.
    question: Can I chain multiple transformations on the same node?
  - answer: Absolutely. Replace `FileFormat.FBX7500ASCII` with `FileFormat.OBJ` or
      `FileFormat.STL` in the `scene.save` call.
    question: Is it possible to export to other formats like OBJ or STL?
  - answer: Create a parent node, apply the rotation to the parent, and add child
      nodes under it. All children inherit the transformation automatically.
    question: How do I apply the same rotation to several nodes at once?
  - answer: The Java garbage collector handles most resources, but you can explicitly
      call `scene.dispose()` when working with large scenes in long‑running applications.
    question: Do I need to call any cleanup methods after saving?
  type: FAQPage
second_title: Aspose.3D Java API
title: Δημιουργία Mesh Aspose Java – Μετασχηματισμός 3D nodes με Euler Angles
url: /el/java/geometry/transform-3d-nodes-with-euler-angles/
weight: 19
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Μετασχηματισμός 3Δ Κόμβων με Γωνίες Euler σε Java χρησιμοποιώντας το Aspose.3D

## Εισαγωγή

Σε αυτό το σεμινάριο θα **create mesh aspose java** αντικείμενα, θα τα συνδέσετε με κόμβους σκηνής και στη συνέχεια θα μετασχηματίσετε αυτούς τους κόμβους χρησιμοποιώντας γωνίες Euler. Στο τέλος θα είστε άνετοι με την προσθήκη 3‑Δ περιστροφής, τον ορισμό translation java, και την εξαγωγή της τελικής σκηνής σε FBX ή άλλες μορφές—όλα με το σύντομο API του Aspose 3D.

## Γρήγορες Απαντήσεις
- **Ποια βιβλιοθήκη διαχειρίζεται 3Δ μετασχηματισμούς σε Java;** Aspose 3D for Java.  
- **Ποια μέθοδος ορίζει περιστροφή χρησιμοποιώντας γωνίες Euler;** `setEulerAngles()` on a node’s transform.  
- **Πώς μετακινώ έναν κόμβο στο χώρο;** Call `setTranslation()` with a `Vector3`.  
- **Χρειάζομαι άδεια για παραγωγή;** Yes, a commercial Aspose 3D license is required.  
- **Μπορώ να εξάγω σε FBX;** Absolutely – `scene.save(..., FileFormat.FBX7500ASCII)` works out of the box.

## Τι είναι το “create mesh aspose java”;

`Mesh` είναι ο βασικός κοντέινερ γεωμετρίας του Aspose.3D που αποθηκεύει κορυφές, πρόσωπα και δεδομένα υλικού για ένα 3‑Δ αντικείμενο. Όταν **create mesh aspose java**, ορίζετε το σχήμα που θα προσαρτηθεί αργότερα σε έναν κόμβο και θα μετασχηματιστεί. Το mesh περιλαμβάνει όλες τις γεωμετρικές πληροφορίες, καθιστώντας το επαναχρησιμοποιήσιμο σε πολλούς κόμβους ή σκηνές, και μπορεί να εξαχθεί απευθείας χωρίς επιπλέον βήματα μετατροπής.

```java
import com.aspose.threed.*;
```

## Γιατί να χρησιμοποιήσετε γωνίες Euler με το Aspose 3D;

Οι γωνίες Euler σας επιτρέπουν να περιγράψετε την περιστροφή ως τρεις διαισθητικές τιμές—pitch, yaw και roll—κάνοντας εύκολο το αντιστοίχηση των ρυθμιστών UI ή των δεδομένων αισθητήρων απευθείας στον προσανατολισμό του μοντέλου. Το Aspose 3D αφαιρεί τα υποκείμενα μαθηματικά των πινάκων, ώστε να μπορείτε να εστιάσετε στα οπτικά αποτελέσματα αντί για πολύπλοκες υπολογισμούς quaternion.

## Προαπαιτούμενα

- Βασική εμπειρία προγραμματισμού Java.  
- Εγκατεστημένο JDK 8 ή νεότερο.  
- Βιβλιοθήκη Aspose.3D, την οποία μπορείτε να αποκτήσετε από [Aspose.3D Java Documentation](https://reference.aspose.com/3d/java/).  
- Έγκυρη άδεια Aspose 3D για παραγωγικές εκδόσεις.

## Εισαγωγή Πακέτων

Ξεκινήστε εισάγοντας τα απαραίτητα πακέτα στο έργο Java σας. Βεβαιωθείτε ότι η βιβλιοθήκη Aspose.3D έχει προστεθεί σωστά στο classpath σας. Εάν δεν την έχετε κατεβάσει ακόμη, μπορείτε να βρείτε τον σύνδεσμο λήψης [εδώ](https://releases.aspose.com/3d/java/).

```java
// ExStart:AddTransformationToNodeByEulerAngles
// Initialize scene object
Scene scene = new Scene();

// Initialize Node class object
Node cubeNode = new Node("cube");
```

## Πώς να δημιουργήσω mesh aspose java;

`Mesh` είναι ένας κοντέινερ που περιέχει δεδομένα κορυφών και προσώπων για ένα 3‑Δ αντικείμενο. Παρέχει μεθόδους για τον προγραμματιστικό ορισμό γεωμετρίας ή τη φόρτωση από υπάρχοντα αρχεία. Για να δημιουργήσετε ένα mesh, δημιουργήστε μια παρουσία της κλάσης, προσθέστε κορυφές, ορίστε πολύγωνα και στη συνέχεια εκχωρήστε το mesh σε έναν κόμβο. Αυτό το βήμα δημιουργεί τη γεωμετρική βάση πριν εφαρμοστεί οποιοσδήποτε μετασχηματισμός, επιτρέποντάς σας να επαναχρησιμοποιήσετε το ίδιο mesh σε πολλούς κόμβους εάν χρειάζεται.

```java
// Call Common class create mesh using polygon builder method to set mesh instance
Mesh mesh = Common.createMeshUsingPolygonBuilder();

// Point node to the Mesh geometry
cubeNode.setEntity(mesh);
```

## Πώς μπορώ να ορίσω translation java σε έναν κόμβο;

`Transform` είναι το στοιχείο που συνδέεται σε κάθε `Node` και ελέγχει τη θέση, την περιστροφή και την κλίμακα. Η μέθοδος `setTranslation()` του `Transform` μετακινεί τον κόμβο καθορίζοντας μια μετατόπιση `Vector3`. Καλώντας αυτή τη μέθοδο, μετατοπίζετε ολόκληρο το mesh σε σχέση με την αρχή της σκηνής διατηρώντας τη εσωτερική του γεωμετρία. Αυτή η προσέγγιση είναι ιδανική για την τοποθέτηση αντικειμένων σε ένα παγκόσμιο σύστημα συντεταγμένων ή την ευθυγράμμιση πολλαπλών μοντέλων μαζί.

```java
// Euler angles
cubeNode.getTransform().setEulerAngles(new Vector3(0.3, 0.1, -0.5));

// Set translation
cubeNode.getTransform().setTranslation(new Vector3(0, 0, 20));
```

## Πώς να εφαρμόσω γωνίες Euler για περιστροφή ενός κόμβου;

`setEulerAngles()` είναι μια μέθοδος του `Transform` του κόμβου που δέχεται τρεις τιμές κινητής υποδιαστολής που αντιπροσωπεύουν την περιστροφή γύρω από τους άξονες X, Y και Z (σε μοίρες). Η παροχή τιμών pitch, yaw και roll σας επιτρέπει να περιστρέψετε τον κόμβο διαισθητικά, και το Aspose 3D εσωτερικά μετατρέπει αυτές τις γωνίες σε πίνακα περιστροφής. Αυτή η μέθοδος είναι ιδιαίτερα χρήσιμη για περιστροφές που ελέγχονται από UI, όπου οι χρήστες ρυθμίζουν τους ρυθμιστές που αντιστοιχούν σε κάθε άξονα.

```java
// Add cube to the scene
scene.getRootNode().getChildNodes().add(cubeNode);
```

## Πώς να προσθέσετε τον μετασχηματισμένο κόμβο στη σκηνή;

`scene.getRootNode().addChild(node)` προσθέτει έναν κόμβο στη ρίζα του γραφήματος σκηνής, καθιστώντας τον μέρος της ιεραρχίας που μπορεί να αποδοθεί. Μόλις ο κόμβος προσαρτηθεί, οποιοσδήποτε μετασχηματισμός του—όπως translation, rotation ή scaling—λαμβάνεται αυτόματα υπόψη κατά την απόδοση και τις εξαγωγές. Η προσθήκη κόμβων με αυτόν τον τρόπο ενεργοποιεί επίσης ιεραρχικές σχέσεις, επιτρέποντας στους θυγατρικούς κόμβους να κληρονομούν μετασχηματισμούς από τους γονείς τους.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
MyDir = MyDir + "TransformationToNode.fbx";

// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7500ASCII);
// ExEnd:AddTransformationToNodeByEulerAngles
System.out.println("\nTransformation added successfully to node.\nFile saved at " + MyDir);
```

## Πώς να αποθηκεύσετε τη 3Δ σκηνή σε αρχείο;

`scene.save()` writes the entire scene, including all meshes, materials, and transforms, to a specified file format. By passing the output path and a `FileFormat` enum (e.g., `FileFormat.FBX7500ASCII`), you can export to FBX, OBJ, STL, or any other supported format. This method serializes the scene graph in a single operation, ensuring that all transformations are preserved in the exported file. Replace `"Your Document Directory"` with the actual folder path on your machine.

CODE_BLOCK_PLACEHOLDER_6_END

## Συνηθισμένες Περιπτώσεις Χρήσης

- **Οπτικοποίηση δεδομένων σε πραγματικό χρόνο:** Περιστροφή μοντέλου βάσει ζωντανής εισόδου αισθητήρα.  
- **Συστήματα κάμερας τύπου παιχνιδιού:** Εφαρμόστε yaw‑pitch‑roll για προσομοίωση κάμερας πρώτου προσώπου.  
- **Διαμορφωτές προϊόντων:** Επιτρέψτε στους πελάτες να περιστρέφουν ένα 3‑Δ μοντέλο προϊόντος χρησιμοποιώντας απλούς ρυθμιστές.

## Επίλυση Προβλημάτων & Συμβουλές

- **Gimbal lock:** Εάν η περιστροφή «κλειδώνει» απροσδόκητα, μεταβείτε σε περιστροφή βασισμένη σε quaternion με `setRotationQuaternion()`.  
- **Συνεπής μονάδα:** Το Aspose 3D σέβεται τις μονάδες που παρέχετε· διατηρήστε τις τιμές translation συνεπείς με την κλίμακα του μοντέλου σας για να αποφύγετε παραμορφώσεις.  
- **Απόδοση:** Για μεγάλες σκηνές, καλέστε ρητά `scene.dispose()` μετά την αποθήκευση για να ελευθερώσετε εγγενείς πόρους και να αποτρέψετε διαρροές μνήμης.

## Συχνές Ερωτήσεις

**Q: Ποια είναι η διαφορά μεταξύ γωνιών Euler και περιστροφής quaternion;**  
A: Οι γωνίες Euler είναι διαισθητικές (pitch, yaw, roll) αλλά μπορούν να υποφέρουν από gimbal lock, ενώ τα quaternions αποφεύγουν αυτό το πρόβλημα και παρέχουν πιο ομαλή παρεμβολή για τις κινήσεις.

**Q: Μπορώ να αλυσίδω πολλαπλούς μετασχηματισμούς στον ίδιο κόμβο;**  
A: Ναι. Καλέστε `setEulerAngles`, `setTranslation` και `setScale` με οποιαδήποτε σειρά· η βιβλιοθήκη τα συνθέτει σε έναν ενιαίο πίνακα μετασχηματισμού.

**Q: Είναι δυνατόν να εξάγετε σε άλλες μορφές όπως OBJ ή STL;**  
A: Απόλυτα. Αντικαταστήστε `FileFormat.FBX7500ASCII` με `FileFormat.OBJ` ή `FileFormat.STL` στην κλήση `scene.save`.

**Q: Πώς να εφαρμόσω την ίδια περιστροφή σε πολλούς κόμβους ταυτόχρονα;**  
A: Δημιουργήστε έναν γονικό κόμβο, εφαρμόστε την περιστροφή στον γονέα και προσθέστε τους θυγατρικούς κόμβους κάτω από αυτόν. Όλοι οι θυγατρικοί κληρονομούν αυτόματα τον μετασχηματισμό.

**Q: Χρειάζεται να καλέσω κάποια μέθοδο καθαρισμού μετά την αποθήκευση;**  
A: Ο συλλέκτης απορριμμάτων της Java διαχειρίζεται τους περισσότερους πόρους, αλλά μπορείτε ρητά να καλέσετε `scene.dispose()` όταν εργάζεστε με μεγάλες σκηνές σε εφαρμογές που τρέχουν για μεγάλο χρονικό διάστημα.

---

**Τελευταία ενημέρωση:** 2026-06-13  
**Δοκιμάστηκε με:** Aspose.3D 23.12 for Java  
**Συγγραφέας:** Aspose  

{{< blocks/products/products-backtop-button >}}

## Σχετικά Σεμινάρια

- [Ορισμός Περιστροφής Quaternion σε Java χρησιμοποιώντας Aspose.3D](/3d/java/geometry/concatenate-quaternions-for-3d-rotations/)
- [Δημιουργία Node Aspose 3D σε Java – Εμφάνιση Μετασχηματισμών](/3d/java/geometry/expose-geometric-transformations/)
- [Java 3D Graphics Tutorial - Δημιουργία Σκηνής 3D Κύβου με Aspose.3D](/3d/java/geometry/create-3d-cube-scene/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}