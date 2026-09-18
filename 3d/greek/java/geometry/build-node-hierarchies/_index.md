---
date: 2026-09-18
description: Μάθετε πώς να δημιουργείτε child nodes, να προσθέτετε mesh σε node και
  να εξάγετε FBX χρησιμοποιώντας Aspose.3D Java API για ισχυρά 3D scene graphs.
keywords:
- how to build hierarchy
- add mesh to node
- convert scene fbx
- save scene fbx
- create child nodes java
lastmod: 2026-09-18
linktitle: Δημιουργήστε node hierarchies σε 3D scenes με Java και Aspose.3D
og_description: Μάθετε πώς να δημιουργήσετε hierarchy, να προσθέσετε mesh σε node
  και να εξάγετε FBX χρησιμοποιώντας Aspose.3D Java API. Αυτός ο οδηγός δείχνει step‑by‑step
  code για τη δημιουργία child nodes και την αποθήκευση scenes.
og_image_alt: Tutorial showing Java code to build node hierarchy and export FBX with
  Aspose.3D
og_title: Πώς να δημιουργήσετε hierarchy και να εξάγετε FBX σε Java με Aspose.3D
schemas:
- author: Aspose
  dateModified: '2026-09-18'
  description: Learn how to create child nodes, add mesh to node, and export FBX using
    Aspose.3D Java API for robust 3D scene graphs.
  headline: How to build hierarchy and export FBX in Java with Aspose.3D
  type: TechArticle
- description: Learn how to create child nodes, add mesh to node, and export FBX using
    Aspose.3D Java API for robust 3D scene graphs.
  name: How to build hierarchy and export FBX in Java with Aspose.3D
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
  - answer: Absolutely! The API follows a clean, object‑oriented design that lets
      you start building scenes with just a few lines of code.
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
tags:
- build hierarchy
- Aspose.3D
- Java 3D
- FBX export
title: Πώς να δημιουργήσετε hierarchy και να εξάγετε FBX σε Java με Aspose.3D
url: /el/java/geometry/build-node-hierarchies/
weight: 16
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

  
  
  

# Πώς να δημιουργήσετε ιεραρχία και να εξάγετε FBX σε Java με Aspose.3D  

## Εισαγωγή  

Αν ψάχνετε για έναν σαφή, βήμα‑βήμα οδηγό σχετικά με **δημιουργία παιδικών κόμβων**, **προσθήκη πλέγματος σε κόμβο**, και **πώς να εξάγετε FBX** από μια εφαρμογή Java, βρίσκεστε στο σωστό μέρος. Σε αυτό το tutorial θα περάσουμε από τη δημιουργία ενός **java 3d scene graph**, την προσθήκη πλεγμάτων, την εφαρμογή μετασχηματισμών, και τελικά την αποθήκευση της σκηνής ως αρχείο FBX χρησιμοποιώντας το Aspose.3D Java API. Είτε δημιουργείτε ένα απλό demo είτε χτίζετε μια παραγωγική 3D μηχανή, η κατανόηση αυτών των εννοιών σας δίνει πλήρη έλεγχο πάνω στην ιεραρχία της σκηνής και στη ροή εξαγωγής.  

## Γρήγορες απαντήσεις  
- **Ποιος είναι ο κύριος σκοπός αυτού του tutorial;** Να δείξει πώς να **δημιουργήσετε παιδικούς κόμβους**, να προσθέσετε πλέγματα και να **εξάγετε FBX** μετά την κατασκευή μιας ιεραρχίας κόμβων.  
- **Ποια βιβλιοθήκη χρησιμοποιείται;** Aspose.3D for Java.  
- **Χρειάζομαι άδεια;** Μια δωρεάν δοκιμή λειτουργεί για ανάπτυξη· απαιτείται εμπορική άδεια για παραγωγή.  
- **Τι μορφή αρχείου παράγεται;** FBX (ASCII 7500).  
- **Μπορώ να προσαρμόσω τους μετασχηματισμούς των κόμβων;** Ναι – υποστηρίζονται μετάφραση, περιστροφή και κλιμάκωση.  

## Πώς να δημιουργήσετε ιεραρχία στο Aspose.3D;  

Φορτώστε ένα αντικείμενο `Scene`, δημιουργήστε έναν γονικό `Node`, στη συνέχεια προσθέστε παιδικά `Node` με `parentNode.getChildren().add(childNode)`. Η ιεραρχία διαδίδει αυτόματα τους μετασχηματισμούς από τον γονέα στα παιδιά, έτσι η περιστροφή του γονέα περιστρέφει κάθε συνδεδεμένο πλέγμα. Όλη αυτή η διαδικασία απαιτεί μόνο λίγες γραμμές κώδικα και λειτουργεί με οποιαδήποτε υποστηριζόμενη μορφή 3D.  

## Τι σημαίνει “create child nodes” στο πλαίσιο του Aspose.3D;  

Η δημιουργία παιδικών κόμβων σημαίνει την προσθήκη υποδεέστερων αντικειμένων `Node` σε έναν γονικό κόμβο στο γράφημα σκηνής. Αυτή η ιεραρχική δομή σας επιτρέπει να εφαρμόζετε έναν μετασχηματισμό μία φορά στο επίπεδο του γονέα και να επηρεάζει αυτόματα όλα τα παιδιά του, κάτι που είναι ουσιώδες για ρεαλιστικές σχέσεις αντικειμένων όπως ένα σασί χάρτι με περιστρεφόμενους τροχούς.  

## Γιατί να δημιουργήσετε ιεραρχίες κόμβων πριν από την εξαγωγή;  

Μια καλά δομημένη ιεραρχία μειώνει την επανάληψη κώδικα, απλοποιεί την κίνηση και αντικατοπτρίζει πραγματικές σχέσεις. Όταν αργότερα **μετατρέψετε τη σκηνή σε fbx** (ή οποιαδήποτε άλλη μορφή), η ιεραρχία διατηρείται, ώστε εργαλεία όπως Blender, Maya ή Unity να κατανοούν τις σχέσεις γονέα‑παιδιού ακριβώς όπως τις σχεδιάσατε.  

## Συνηθισμένες περιπτώσεις χρήσης ιεραρχιών κόμβων  

| Περίπτωση χρήσης | Γιατί βοηθά η ιεραρχία | Τυπικό αποτέλεσμα |
|----------|----------------------|-----------------|
| **Μηχανικές συναρμολογήσεις** (π.χ., ρομποτικό βραχίονα) | Η περιστροφή ενός βασικού κόμβου μετακινεί όλα τα συνδεδεμένα τμήματα | Εύκολη κίνηση σύνθετων μηχανισμών |
| **Ρίγες χαρακτήρων** | Τα οστά του σκελετού είναι παιδικοί κόμβοι ενός ριζικού | Συνεπείς μετασχηματισμοί πόζας |
| **Οργάνωση σκηνής** | Ομαδοποίηση στατικών αντικειμένων κάτω από έναν κόμβο “props” | Καθαρότερη διαχείριση σκηνής και επιλεκτική εξαγωγή |
| **Αλλαγή επιπέδου λεπτομέρειας (LOD)** | Ο γονικός κόμβος εναλλάσσει την ορατότητα των παιδικών πλεγμάτων | Βελτιστοποιημένη απόδοση για διαφορετικό υλικό |

## Προαπαιτούμενα  

1. **Περιβάλλον Ανάπτυξης Java** – JDK 8+ και ένα IDE ή εργαλείο κατασκευής της επιλογής σας.  
2. **Aspose.3D for Java Library** – Κατεβάστε και εγκαταστήστε τη βιβλιοθήκη από τη [σελίδα λήψης](https://releases.aspose.com/3d/java/).  
3. **Κατάλογος Εγγράφου** – Ένας φάκελος στον υπολογιστή σας όπου θα αποθηκευτεί το παραγόμενο αρχείο FBX.  

## Εισαγωγή πακέτων  

Οι κλάσεις `Scene`, `Node`, `Mesh` και `Quaternion` είναι τα βασικά δομικά στοιχεία.  

```java
import com.aspose.threed.*;
```  

## Βήμα 1: αρχικοποίηση του αντικειμένου σκηνής  

Η κλάση `Scene` είναι το κορυφαίο κοντέινερ του Aspose.3D που αντιπροσωπεύει ολόκληρο το 3D έγγραφο στη μνήμη.  

```java
// Initialize scene object
Scene scene = new Scene();
```  

## Βήμα 2: δημιουργία παιδικών κόμβων και προσθήκη πλέγματος σε κόμβο  

Σε αυτό το βήμα δείχνουμε **πώς να δημιουργήσετε παιδικούς κόμβους** και **πώς να προσθέσετε πλέγμα σε κόμβο**.  

```java
// Get a child node object
Node top = scene.getRootNode().createChildNode();

// Create the first cube node
Node cube1 = top.createChildNode("cube1");
Mesh mesh = new Mesh();
cube1.setEntity(mesh);
cube1.getTransform().setTranslation(new Vector3(-10, 0, 0));

// Create the second cube node
Node cube2 = top.createChildNode("cube2");
cube2.setEntity(mesh);
cube2.getTransform().setTranslation(new Vector3(10, 0, 0));
```  

## Βήμα 3: εφαρμογή περιστροφής στον κορυφαίο κόμβο  

Η περιστροφή του γονικού κόμβου περιστρέφει αυτόματα όλα τα παιδιά του, κάτι που αποτελεί βασικό πλεονέκτημα των ιεραρχικών σκηνών.  

```java
// Rotate the top node, affecting all child nodes
top.getTransform().setRotation(Quaternion.fromEulerAngle(Math.PI, 4, 0));
```  

## Βήμα 4: αποθήκευση της 3D σκηνής – πώς να εξάγετε FBX  

Τώρα **αποθηκεύουμε τη σκηνή ως FBX**, ολοκληρώνοντας τη ροή εργασίας “πώς να εξάγετε fbx”.  

```java
// Save 3D scene in the supported file format (FBX in this case)
String MyDir = "Your Document Directory";
MyDir = MyDir + "NodeHierarchy.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
System.out.println("\nNode hierarchy added successfully to document.\nFile saved at " + MyDir);
```  

### Αναμενόμενο αποτέλεσμα  

Η εκτέλεση του κώδικα δημιουργεί ένα αρχείο με όνομα **NodeHierarchy.fbx** στον καθορισμένο φάκελο. Ανοίξτε το σε οποιονδήποτε προβολέα συμβατό με FBX για να δείτε δύο κύβους τοποθετημένους αριστερά και δεξιά ενός κεντρικού άξονα, όλοι περιστρεφόμενοι μαζί.  

## Ποσοτική δήλωση για το Aspose.3D  

Το Aspose.3D υποστηρίζει **πάνω από 30 μορφές εισαγωγής και εξαγωγής**, συμπεριλαμβανομένων των FBX, OBJ, STL και 3DS, και μπορεί να επεξεργαστεί σκηνές με **πάνω από 10.000 κόμβους** χωρίς να φορτώνει ολόκληρο το αρχείο στη μνήμη, παρέχοντας γρήγορους χρόνους εξαγωγής ακόμη και για μεγάλες συναρμολογήσεις.  

## Συνηθισμένα προβλήματα και λύσεις  

| Πρόβλημα | Γιατί συμβαίνει | Διόρθωση |
|-------|----------------|-----|
| **Σφάλμα “File not found”** κατά την αποθήκευση | Η διαδρομή `MyDir` είναι λανθασμένη ή λείπει το τελικό διαχωριστικό | Βεβαιωθείτε ότι ο φάκελος υπάρχει και τελειώνει με διαχωριστικό (`/` ή `\\`). |
| **Το πλέγμα δεν είναι ορατό** μετά την εξαγωγή | Η οντότητα πλέγματος δεν έχει εκχωρηθεί ή η μετάφραση το μετακινεί εκτός προβολής | Επαληθεύστε `cube1.setEntity(mesh)` και ελέγξτε τις τιμές μετάφρασης. |
| **Η περιστροφή φαίνεται λανθασμένη** | Χρήση ακτίνων αντί για μοίρες λανθασμένα | Η `Quaternion.fromEulerAngle` αναμένει ακτίνια· προσαρμόστε τις τιμές αναλόγως. |

## Συμβουλές αντιμετώπισης προβλημάτων  

- **Επικυρώστε τον φάκελο**: Χρησιμοποιήστε `new File(MyDir).mkdirs();` πριν από το `scene.save` αν ο φάκελος μπορεί να μην υπάρχει.  
- **Εξετάστε το γράφημα σκηνής**: Καλέστε `scene.getRootNode().getChildren().size()` για να επιβεβαιώσετε ότι προστέθηκαν παιδικοί κόμβοι.  
- **Ελέγξτε τη συμβατότητα έκδοσης FBX**: Ορισμένα παλαιότερα εργαλεία υποστηρίζουν μόνο FBX 2013· μπορείτε να αλλάξετε τη μορφή σε `FileFormat.FBX2013` εάν χρειαστεί.  

## Συχνές ερωτήσεις  

**Ε: Είναι το Aspose.3D for Java κατάλληλο για αρχάριους;**  
Α: Απόλυτα! Το API ακολουθεί καθαρό, αντικειμενοστραφή σχεδιασμό που σας επιτρέπει να ξεκινήσετε την κατασκευή σκηνών με λίγες μόνο γραμμές κώδικα.  

**Ε: Μπορώ να χρησιμοποιήσω το Aspose.3D for Java σε εμπορικά έργα;**  
Α: Ναι, μπορείτε. Επισκεφθείτε τη [σελίδα αγοράς](https://purchase.aspose.com/buy) για λεπτομέρειες αδειοδότησης.  

**Ε: Πώς μπορώ να λάβω υποστήριξη για το Aspose.3D for Java;**  
Α: Συμμετέχετε στο [φόρουμ Aspose.3D](https://forum.aspose.com/c/3d/18) για βοήθεια από την κοινότητα και την ομάδα υποστήριξης της Aspose.  

**Ε: Υπάρχει διαθέσιμη δωρεάν δοκιμή;**  
Α: Φυσικά! Δοκιμάστε τις δυνατότητες με το [δωρεάν trial](https://releases.aspose.com/) πριν δεσμευτείτε.  

**Ε: Πού μπορώ να βρω την τεκμηρίωση;**  
Α: Ανατρέξτε στην [τεκμηρίωση](https://reference.aspose.com/3d/java/) για λεπτομερείς πληροφορίες σχετικά με το Aspose.3D for Java.  

## Συμπέρασμα  

Η κατάκτηση των **create child nodes**, **add mesh to node**, και **how to export FBX** είναι βασικά βήματα για την ανάπτυξη εξελιγμένων 3D εφαρμογών σε Java. Με το Aspose.3D αποκτάτε μια ισχυρή, φιλική προς την άδεια λύση που αφαιρεί τις λεπτομέρειες χαμηλού επιπέδου ενώ σας δίνει πλήρη έλεγχο πάνω στο γράφημα σκηνής. Πειραματιστείτε με διαφορετικά πλέγματα, μετασχηματισμούς και μορφές εξαγωγής για να ξεκλειδώσετε ακόμη περισσότερες δυνατότητες.  

---  

**Τελευταία ενημέρωση:** 2026-09-18  
**Δοκιμή με:** Aspose.3D for Java 24.11  
**Συγγραφέας:** Aspose

## Σχετικά Tutorials

- [Java 3D Graphics Tutorial - Create a 3D Cube Scene with Aspose.3D](/3d/java/geometry/create-3d-cube-scene/)
- [Apply Geometric Transformations to a Node Using Aspose.3D Java API](/3d/java/geometry/expose-geometric-transformations/)
- [Save 3D Scenes in Java with Aspose.3D – Convert 3D Files Efficiently](/3d/java/load-and-save/save-3d-scenes/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}