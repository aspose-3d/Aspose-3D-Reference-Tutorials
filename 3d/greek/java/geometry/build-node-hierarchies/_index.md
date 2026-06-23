---
date: 2026-06-23
description: Μάθετε πώς να δημιουργείτε παιδικούς κόμβους, προσθέτετε mesh σε κόμβο
  και εξάγετε FBX χρησιμοποιώντας τις δυνατότητες του java 3d scene graph του Aspose.3D
  Java API.
keywords:
- java 3d scene graph
- how to export fbx
- add mesh to node
- how to create child nodes
- save scene as fbx
- convert scene to fbx
linktitle: Δημιουργία ιεραρχιών κόμβων σε 3D σκηνές με Java και Aspose.3D
schemas:
- author: Aspose
  dateModified: '2026-06-23'
  description: Learn how to create child nodes, add mesh to node, and export FBX using
    the java 3d scene graph capabilities of Aspose.3D Java API.
  headline: 'java 3d scene graph: Create Child Nodes and Export FBX in Java with Aspose.3D'
  type: TechArticle
- description: Learn how to create child nodes, add mesh to node, and export FBX using
    the java 3d scene graph capabilities of Aspose.3D Java API.
  name: 'java 3d scene graph: Create Child Nodes and Export FBX in Java with Aspose.3D'
  steps:
  - name: '**Java Development Environment** – JDK 8+ and an IDE or build tool of your
      choice.'
    text: '**Java Development Environment** – JDK 8+ and an IDE or build tool of your
      choice.'
  - name: '**Aspose.3D for Java Library** – Download and install the library from
      the [download page](https://releases.aspose.com/3d/java/).'
    text: '**Aspose.3D for Java Library** – Download and install the library from
      the [download page](https://releases.aspose.com/3d/java/).'
  - name: '**Document Directory** – A folder on your machine where the generated FBX
      file will be saved.'
    text: '**Document Directory** – A folder on your machine where the generated FBX
      file will be saved.'
  type: HowTo
- questions:
  - answer: Absolutely! The API is designed with a clean, object‑oriented approach
      that makes it easy to learn, even if you’re new to 3D programming.
    question: Is Aspose.3D for Java suitable for beginners?
  - answer: Yes, you can. Visit the [purchase page](https://purchase.aspose.com/buy)
      for licensing details.
    question: Can I use Aspose.3D for Java for commercial projects?
  - answer: Join the [Aspose.3D forum](https://forum.aspose.com/c/3d/18) to get assistance
      from the community and Aspose support team.
    question: How can I get support for Aspose.3D for Java?
  - answer: Certainly! Explore the features with the [free trial](https://releases.aspose.com/)
      before making a commitment.
    question: Is there a free trial available?
  - answer: Refer to the [documentation](https://reference.aspose.com/3d/java/) for
      detailed information on Aspose.3D for Java.
    question: Where can I find the documentation?
  type: FAQPage
second_title: Aspose.3D Java API
title: 'java 3d scene graph: Δημιουργία παιδικών κόμβων και Εξαγωγή FBX σε Java με
  Aspose.3D'
url: /el/java/geometry/build-node-hierarchies/
weight: 16
---

{{< blocks/products/pf/main-wrap-class >}}

## Σχετικά Μαθήματα

- [Δημιουργία Mesh Aspose Java – Μετασχηματισμός 3D Κόμβων με Γωνίες Euler](/3d/java/geometry/transform-3d-nodes-with-euler-angles/)
- [Δημιουργία 3D Σκηνής Java - Εφαρμογή Υλικών PBR με Aspose.3D](/3d/java/geometry/apply-pbr-materials-to-objects/)
- [Πώς να Εξάγετε Σκηνή σε FBX και να Ανακτήσετε Πληροφορίες 3D Σκηνής σε Java](/3d/java/3d-scenes-and-models/get-scene-information/)


{{< /blocks/products/pf/tutorial-page-section >}}  
{{< blocks/products/pf/tutorial-page-section >}}  

# Πώς να Εξάγετε FBX και να Δημιουργήσετε Ιεραρχίες Κόμβων σε Java με Aspose.3D  

## Εισαγωγή  

Αν ψάχνετε για έναν σαφή, βήμα‑βήμα οδηγό σχετικά με **create child nodes**, **add mesh to node**, και **how to export FBX** από μια εφαρμογή Java, βρίσκεστε στο σωστό μέρος. Σε αυτό το μάθημα θα περάσουμε από τη δημιουργία ενός **java 3d scene graph**, την προσθήκη meshes, την εφαρμογή μετασχηματισμών, και τελικά την αποθήκευση της σκηνής ως αρχείο FBX χρησιμοποιώντας το Aspose.3D Java API. Είτε δημιουργείτε ένα απλό demo είτε σχεδιάζετε μια παραγωγική 3D μηχανή, η κατανόηση αυτών των εννοιών σας δίνει πλήρη έλεγχο πάνω στην ιεραρχία της σκηνής και τη ροή εξαγωγής.  

## Γρήγορες Απαντήσεις  
- **Ποιος είναι ο κύριος σκοπός αυτού του μαθήματος;** Δείχνει πώς να **create child nodes**, να προσαρτήσετε meshes, και να **export FBX** μετά την κατασκευή μιας ιεραρχίας κόμβων.  
- **Ποια βιβλιοθήκη χρησιμοποιείται;** Aspose.3D for Java.  
- **Χρειάζομαι άδεια;** Μια δωρεάν δοκιμή λειτουργεί για ανάπτυξη· απαιτείται εμπορική άδεια για παραγωγή.  
- **Ποια μορφή αρχείου παράγεται;** FBX (ASCII 7500).  
- **Μπορώ να προσαρμόσω τους μετασχηματισμούς των κόμβων;** Ναι – η μετάφραση, η περιστροφή και η κλιμάκωση υποστηρίζονται.  

## Τι είναι ένα java 3d scene graph;  

Ένα **java 3d scene graph** είναι μια ιεραρχική δομή δεδομένων που αντιπροσωπεύει αντικείμενα (`Node`s) και τις σχέσεις τους σε έναν 3D κόσμο. Με την οργάνωση των αντικειμένων ως ζεύγη γονέα‑παιδίου, μπορείτε να εφαρμόσετε έναν μετασχηματισμό στον γονέα και να τον μεταβιβάσετε σε όλους τους απογόνους, κάτι που απλοποιεί την κίνηση και τη διαχείριση της σκηνής.  

## Γιατί να δημιουργήσετε ιεραρχίες κόμβων πριν την εξαγωγή;  

Μια καλά δομημένη ιεραρχία μειώνει την επανάληψη κώδικα, απλοποιεί την κίνηση και αντικατοπτρίζει πραγματικές σχέσεις. Όταν αργότερα **convert scene to FBX** (ή οποιαδήποτε άλλη μορφή), η ιεραρχία διατηρείται, ώστε εργαλεία όπως Blender, Maya ή Unity να κατανοούν τις σχέσεις γονέα‑παιδίου ακριβώς όπως τις σχεδιάσατε.  

## Ποσοτικοποιημένα Οφέλη του Aspose.3D  

Το Aspose.3D υποστηρίζει **30+ μορφές εισαγωγής και εξαγωγής** – συμπεριλαμβανομένων των FBX, OBJ, STL, 3DS και Collada – και μπορεί να επεξεργαστεί **σκηνές με εκατοντάδες σελίδες** χωρίς να φορτώνει ολόκληρο το αρχείο στη μνήμη. Η βιβλιοθήκη αποδίδει meshes με **ταχύτητα έως 60 fps** σε τυπικό υλικό, επιτρέποντας προεπισκόπηση σε πραγματικό χρόνο κατά την ανάπτυξη.  

## Συνηθισμένες Χρήσεις για Ιεραρχίες Κόμβων  

| Περίπτωση χρήσης | Γιατί βοηθά η ιεραρχία | Τυπικό αποτέλεσμα |
|-------------------|------------------------|--------------------|
| **Μηχανικές συναρμολογήσεις** (π.χ., ρομποτικό βραχίονα) | Η περιστροφή ενός βασικού κόμβου μετακινεί όλα τα συνδεδεμένα τμήματα | Εύκολη κίνηση σύνθετων μηχανισμών |
| **Character rigs** | Τα οστά του σκελετού είναι παιδικοί κόμβοι ενός ριζικού | Συνεπείς μετασχηματισμοί πόζας |
| **Οργάνωση σκηνής** | Ομαδοποίηση στατικών αντικειμένων κάτω από κόμβο “props” | Καθαρότερη διαχείριση σκηνής και επιλεκτική εξαγωγή |
| **Αλλαγή επιπέδου λεπτομέρειας (LOD)** | Ο γονικός κόμβος εναλλάσσει την ορατότητα των παιδικών meshes | Βελτιστοποιημένη απόδοση για διαφορετικό υλικό |

## Προαπαιτούμενα  

1. **Java Development Environment** – JDK 8+ και ένα IDE ή εργαλείο κατασκευής της επιλογής σας.  
2. **Aspose.3D for Java Library** – Κατεβάστε και εγκαταστήστε τη βιβλιοθήκη από τη [download page](https://releases.aspose.com/3d/java/).  
3. **Document Directory** – Ένας φάκελος στον υπολογιστή σας όπου θα αποθηκευτεί το παραγόμενο αρχείο FBX.  

## Εισαγωγή Πακέτων  

Ο χώρος ονομάτων `com.aspose.threed` παρέχει όλες τις κλάσεις που χρειάζεστε για δημιουργία σκηνής, διαχείριση κόμβων και εξαγωγή αρχείων. Εισάγετε τα παρακάτω πακέτα πριν ξεκινήσετε:  

```java
import com.aspose.threed.*;
```  

## Βήμα 1: Αρχικοποίηση του Αντικειμένου Scene  

Η κλάση `Scene` είναι το ανώτερο κοντέινερ που περιέχει ολόκληρη την ιεραρχία 3D. Η δημιουργία ενός αντικειμένου `Scene` εκχωρεί τον ριζικό κόμβο και προετοιμάζει τις εσωτερικές δομές δεδομένων για meshes, φώτα και κάμερες.  

```java
// Initialize scene object
Scene scene = new Scene();
```  

## Βήμα 2: Δημιουργία Παιδικών Κόμβων και Προσθήκη Mesh σε Κόμβο  

Σε αυτό το βήμα δείχνουμε **how to create child nodes** και **add mesh to node** αντικείμενα. Η κλάση `Node` αντιπροσωπεύει ένα μοναδικό στοιχείο στην ιεραρχία, ενώ η κλάση `Mesh` αποθηκεύει γεωμετρικά δεδομένα όπως κορυφές και πρόσωπα.  

```java
// Get a child node object
Node top = scene.getRootNode().createChildNode();

// Create the first cube node
Node cube1 = top.createChildNode("cube1");
Mesh mesh = Common.createMeshUsingPolygonBuilder(); // Use your mesh creation method
cube1.setEntity(mesh);
cube1.getTransform().setTranslation(new Vector3(-10, 0, 0));

// Create the second cube node
Node cube2 = top.createChildNode("cube2");
cube2.setEntity(mesh);
cube2.getTransform().setTranslation(new Vector3(10, 0, 0));
```  

## Βήμα 3: Εφαρμογή Περιστροφής στον Κορυφαίο Κόμβο  

Η περιστροφή του γονικού κόμβου περιστρέφει αυτόματα όλα τα παιδιά του, κάτι που αποτελεί βασικό πλεονέκτημα των ιεραρχικών σκηνών. Χρησιμοποιήστε την κλάση `Quaternion` για να ορίσετε περιστροφή σε ακτίνια για ομαλή παρεμβολή.  

```java
// Rotate the top node, affecting all child nodes
top.getTransform().setRotation(Quaternion.fromEulerAngle(Math.PI, 4, 0));
```  

## Βήμα 4: Αποθήκευση της 3D Σκηνής – Πώς να Εξάγετε FBX  

Τώρα **αποθηκεύουμε τη σκηνή ως FBX**, ολοκληρώνοντας τη ροή εργασίας “how to export fbx”. Η μέθοδος `Scene.save` δέχεται μια διαδρομή αρχείου και ένα enum `FileFormat`, επιτρέποντάς σας να επιλέξετε μεταξύ FBX 2013, FBX 2014 ή της τελευταίας μορφής ASCII 7500. Το enum `FileFormat` παραθέτει τις υποστηριζόμενες μορφές εξαγωγής όπως FBX2013, FBX2014 και ASCII 7500.  

```java
// Save 3D scene in the supported file format (FBX in this case)
String MyDir = "Your Document Directory";
MyDir = MyDir + "NodeHierarchy.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
System.out.println("\nNode hierarchy added successfully to document.\nFile saved at " + MyDir);
```  

### Αναμενόμενο Αποτέλεσμα  

Η εκτέλεση του κώδικα δημιουργεί ένα αρχείο με όνομα **NodeHierarchy.fbx** στον καθορισμένο φάκελο. Ανοίξτε το σε οποιονδήποτε προβολέα συμβατό με FBX για να δείτε δύο κύβους τοποθετημένους αριστερά και δεξιά ενός κεντρικού άξονα, όλοι περιστρέφονται μαζί.  

## Συχνά Προβλήματα και Λύσεις  

| Πρόβλημα | Γιατί συμβαίνει | Διόρθωση |
|----------|----------------|----------|
| **File not found** error κατά την αποθήκευση | Η διαδρομή `MyDir` είναι λανθασμένη ή λείπει το τελικό διαχωριστικό | Βεβαιωθείτε ότι ο φάκελος υπάρχει και τελειώνει με διαχωριστικό αρχείου (`/` ή `\\`). |
| **Mesh not visible** μετά την εξαγωγή | Η οντότητα mesh δεν έχει ανατεθεί ή η μετάφραση το μετακινεί εκτός οπτικού πεδίου | Επαληθεύστε το `cube1.setEntity(mesh)` και ελέγξτε τις τιμές μετάφρασης. |
| **Rotation looks wrong** | Χρήση ακτινίων αντί για μοίρες λανθασμένα | `Quaternion.fromEulerAngle` αναμένει ακτίνια· προσαρμόστε τις τιμές αναλόγως. |

## Συμβουλές Επίλυσης Προβλημάτων  

- **Επικύρωση του φακέλου**: Χρησιμοποιήστε `new File(MyDir).mkdirs();` πριν από `scene.save` εάν ο φάκελος μπορεί να μην υπάρχει.  
- **Έλεγχος της σκηνής**: Καλέστε `scene.getRootNode().getChildren().size()` για να επιβεβαιώσετε ότι προστέθηκαν παιδικοί κόμβοι.  
- **Έλεγχος συμβατότητας έκδοσης FBX**: Ορισμένα παλαιότερα εργαλεία υποστηρίζουν μόνο FBX 2013· μπορείτε να αλλάξετε τη μορφή σε `FileFormat.FBX2013` αν χρειάζεται.  

## Συχνές Ερωτήσεις  

**Ε: Είναι το Aspose.3D for Java κατάλληλο για αρχάριους;**  
Α: Απόλυτα! Το API έχει σχεδιαστεί με καθαρή, αντικειμενοστραφή προσέγγιση που το κάνει εύκολο στην εκμάθηση, ακόμη και αν είστε νέοι στον 3D προγραμματισμό.  

**Ε: Μπορώ να χρησιμοποιήσω το Aspose.3D for Java για εμπορικά έργα;**  
Α: Ναι, μπορείτε. Επισκεφθείτε τη [purchase page](https://purchase.aspose.com/buy) για λεπτομέρειες αδειοδότησης.  

**Ε: Πώς μπορώ να λάβω υποστήριξη για το Aspose.3D for Java;**  
Α: Συμμετέχετε στο [Aspose.3D forum](https://forum.aspose.com/c/3d/18) για βοήθεια από την κοινότητα και την ομάδα υποστήριξης της Aspose.  

**Ε: Υπάρχει διαθέσιμη δωρεάν δοκιμή;**  
Α: Φυσικά! Εξερευνήστε τις δυνατότητες με τη [free trial](https://releases.aspose.com/) πριν δεσμευτείτε.  

**Ε: Πού μπορώ να βρω την τεκμηρίωση;**  
Α: Ανατρέξτε στην [documentation](https://reference.aspose.com/3d/java/) για λεπτομερείς πληροφορίες σχετικά με το Aspose.3D for Java.  

## Συμπέρασμα  

Η κατανόηση των **create child nodes**, **add mesh to node**, και **how to export FBX** είναι βασικά βήματα για την κατασκευή σύνθετων 3D εφαρμογών σε Java. Με το Aspose.3D αποκτάτε μια ισχυρή, φιλική προς την άδεια λύση που αφαιρεί τις λεπτομέρειες χαμηλού επιπέδου ενώ σας δίνει πλήρη έλεγχο πάνω στο java 3d scene graph. Πειραματιστείτε με διαφορετικά meshes, μετασχηματισμούς και μορφές εξαγωγής για να ξεκλειδώσετε ακόμη περισσότερες δυνατότητες.  

---  

**Τελευταία Ενημέρωση:** 2026-06-23  
**Δοκιμή με:** Aspose.3D for Java 24.11  
**Συγγραφέας:** Aspose  

{{< /blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/products-backtop-button >}}
{{< /blocks/products/pf/main-container >}}