---
date: 2026-10-03
description: Learn how to **select objects by name** using XPath‑like queries in Aspose.3D
  for Java and build a 3D scene programmatically.
images:
- /java/3d-objects-and-scenes/xpath-like-object-queries/og-image.png
keywords:
- select objects by name
- how to query scene
- Aspose.3D Java
lastmod: 2026-10-03
linktitle: Select objects by name in Java 3D scene – XPath‑like queries with Aspose.3D
og_description: Select objects by name in a Java 3D scene using Aspose.3D's XPath‑like
  queries. This guide shows you how to query the scene graph efficiently and retrieve
  cameras, lights, or any entity by name.
og_image_alt: 'Developer guide: select objects by name in Java 3D scene using Aspose.3D'
og_title: Select objects by name in Java 3D scene – Aspose.3D guide
schemas:
- author: Aspose
  dateModified: '2026-10-03'
  description: Learn how to **select objects by name** using XPath‑like queries in
    Aspose.3D for Java and build a 3D scene programmatically.
  headline: Select objects by name in Java 3D scene – XPath‑like queries with Aspose.3D
  type: TechArticle
- description: Learn how to **select objects by name** using XPath‑like queries in
    Aspose.3D for Java and build a 3D scene programmatically.
  name: Select objects by name in Java 3D scene – XPath‑like queries with Aspose.3D
  steps:
  - name: create a scene for testing
    text: We start with an empty scene that will host our hierarchy. `
  - name: build a hierarchy of nodes
    text: Next, we add a few child nodes under the root node. Some nodes contain a
      **Camera** or a **Light** entity, which we'll later query. `
  - name: query objects by traversing the scene graph
    text: Now the fun part—iterating through the scene to **select objects by name**
      or type using the `NodeVisitor` pattern. `NodeVisitor` is a built‑in Aspose.3D
      class that walks the scene graph node‑by‑node, calling your callback for each
      visited node. It lets you inspect each node’s `Entity` and `Name` wi
  type: HowTo
- questions:
  - answer: The documentation is available **[Aspose.3D Java API reference](https://reference.aspose.com/3d/java/)**.
    question: Where can I find the Aspose.3D for Java documentation?
  - answer: You can download it **[Aspose.3D for Java download page](https://releases.aspose.com/3d/java/)**.
    question: How can I download Aspose.3D for Java?
  - answer: Yes, you can get a free trial **[Aspose free trial page](https://releases.aspose.com/)**.
    question: Is there a free trial available?
  - answer: Visit the support forum **[Aspose 3D support forum](https://forum.aspose.com/c/3d/18)**.
    question: Where can I get support for Aspose.3D for Java?
  - answer: Obtain a temporary license **[temporary license request page](https://purchase.aspose.com/temporary-license/)**.
    question: Need a temporary license?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- select objects by name
- Aspose.3D
- Java 3D scene
- XPath queries
- 3D programming
title: Select objects by name in Java 3D scene – XPath‑like queries with Aspose.3D
url: /java/3d-objects-and-scenes/xpath-like-object-queries/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Select objects by name in Java 3D scene – XPath‑like queries with Aspose.3D

## Introduction  

If you need to **create 3d scene java** applications that manipulate complex hierarchies of objects, Aspose.3D for Java gives you a clean, XPath‑style way to locate exactly what you need. In this tutorial we’ll walk through building a simple scene, adding a hierarchy of nodes, and then using XPath‑like queries to **select objects by name** (for example, cameras or lights) no matter where they live in the tree. By the end you’ll be comfortable querying, filtering, and retrieving 3‑D entities with just a single expression.

## Quick answers
- **What can I query?** Any node or entity (Camera, Light, Mesh, etc.) in a Scene.  
- **How do I select objects by type?** Use an XPath‑like expression such as `//*[(@Type='Camera')]`.  
- **Do I need a license for development?** A free trial works for testing; a license is required for production.  
- **Which Java version is supported?** Java 8 or later.  
- **Where can I download Aspose.3D?** From the official download page linked in the prerequisites.

## What is an XPath‑like query in Aspose.3D?  

An XPath‑like query in Aspose.3D is a concise expression that filters **A3DObject** instances (nodes, cameras, lights, meshes, etc.) directly against the scene graph. **A3DObject represents any object in the scene graph, such as nodes, cameras, lights, or meshes.** It works like XML XPath but targets the 3‑D object model, letting you locate “all cameras” or “objects whose name is ‘light’” without writing manual traversal code.

## Why this matters  

When you work with 3‑D content, manually walking the scene graph quickly becomes error‑prone and hard to maintain. XPath‑like queries give you a declarative, readable way to locate exactly the objects you need, which speeds up development and reduces bugs—especially in large scenes with dozens or hundreds of nodes. Aspose.3D supports **50+ input and output formats** and can process multi‑hundred‑page scenes without loading the entire file into memory, giving you both flexibility and performance.

## How to select objects by name using XPath‑like queries  

Load objects by name with a single expression that matches the `@Name` attribute. Below are three common patterns:

1. **Select all cameras** – `//*[(@Type='Camera')]`  
2. **Select nodes named “light”** – `//*[(@Name='light')]`  
3. **Combine type and name** – `//*[(@Type='Camera') or (@Name='light')]`

These expressions return the underlying entities, so you can work with them directly in Java.

## Prerequisites  

Before we start, make sure you have:

- Java Development Kit (JDK) installed on your machine.  
- Aspose.3D for Java library downloaded and set up. You can find the download link **[Aspose.3D for Java download page](https://releases.aspose.com/3d/java/)**.  
- Basic knowledge of Java programming.  

## Import packages  

First, import the Aspose.3D classes you’ll need. This step makes the library available to your project.

```java
import com.aspose.threed.*;
import com.aspose.threed.scene.*;
import java.util.ArrayList;
import java.util.List;
```

## Step‑by‑step guide  

### Step 1: create a scene for testing  

We start with an empty scene that will host our hierarchy.

````java
// ExStart:CreateScene
Scene scene = new Scene();
// ExEnd:CreateScene
````

### Step 2: build a hierarchy of nodes  

Next, we add a few child nodes under the root node. Some nodes contain a **Camera** or a **Light** entity, which we'll later query.

````java
// ExStart:CreateHierarchy
Node a = scene.getRootNode().createChildNode("a");
a.createChildNode("a1");
a.createChildNode("a2");
scene.getRootNode().createChildNode("b");
Node c = scene.getRootNode().createChildNode("c");
c.createChildNode("c1").addEntity(new Camera("cam"));
c.createChildNode("c2").addEntity(new Light("light"));
// ExEnd:CreateHierarchy
````

### Step 3: query objects by traversing the scene graph  

Now the fun part—iterating through the scene to **select objects by name** or type using the `NodeVisitor` pattern.

`NodeVisitor` is a built‑in Aspose.3D class that walks the scene graph node‑by‑node, calling your callback for each visited node. It lets you inspect each node’s `Entity` and `Name` without writing recursive loops.

```
\u0060\u0060\u0060\u0060java
// The scene from Step 1

// Create a list to store the found objects
List<Object> objects = new ArrayList<>();

// Use a NodeVisitor to traverse the scene graph
scene.getRootNode().accept(new NodeVisitor() {
    @Override
    public boolean call(Node node) {
        Entity entity = node.getEntity();
        // Check if the node has a Camera or if the node's name is 'light'
        if (entity instanceof Camera || "light".equals(node.getName())) {
            objects.add(entity);
        }
        return true;
    }
});

// Print the found objects
for (Object obj : objects) {
    System.out.println("Found: " + obj);
}
// ExEnd:XPathLikeObjectQueries
\u0060\u0060\u0060
```

**Explanation of the key expressions**

- `//*[(@Type = 'Camera') or (@Name = 'light')]` – Finds every object in the scene whose **type** attribute equals `Camera` **or** whose **name** attribute equals `light`. This is a classic example of **select objects by name** (and by type).  
- `/c/*/<Camera>` – Starts at the root, goes to node `c`, then any child (`*`), and finally selects the `<Camera>` entity.  
- `a1` – A shorthand that searches the entire tree for a node named `a1`.  
- `/` – Returns the root node itself.

### Common pitfalls & tips  

- **Case sensitivity:** Attribute names (`@Type`, `@Name`) are case‑sensitive.  
- **Entity vs. node:** Use `<Camera>` syntax only when you need the underlying entity, not just the node.  
- **Performance:** For very large scenes, narrow the search path (e.g., start from a specific subtree) to improve speed.  

## Common issues and solutions  

| Issue | Reason | Solution |
|-------|--------|----------|
| No results returned | Query string typo or wrong attribute case | Verify `@Name` spelling and case; use exact node names |
| Unexpected nodes included | Using `//*` searches the whole tree | Restrict the path, e.g., `/c/*` to limit scope |
| Slow performance on huge scenes | Query runs on the entire graph | Start the query from a known sub‑node instead of the root |

## Frequently asked questions  

**Q: Where can I find the Aspose.3D for Java documentation?**  
A: The documentation is available **[Aspose.3D Java API reference](https://reference.aspose.com/3d/java/)**.

**Q: How can I download Aspose.3D for Java?**  
A: You can download it **[Aspose.3D for Java download page](https://releases.aspose.com/3d/java/)**.

**Q: Is there a free trial available?**  
A: Yes, you can get a free trial **[Aspose free trial page](https://releases.aspose.com/)**.

**Q: Where can I get support for Aspose.3D for Java?**  
A: Visit the support forum **[Aspose 3D support forum](https://forum.aspose.com/c/3d/18)**.

**Q: Need a temporary license?**  
A: Obtain a temporary license **[temporary license request page](https://purchase.aspose.com/temporary-license/)**.

**Q: Can I query custom user‑defined properties?**  
A: Yes, you can extend the XPath expression with additional `@` attributes that you add to nodes.

**Q: Does the query engine work with animated scenes?**  
A: Absolutely – the queries operate on the static hierarchy; animations are attached to the same nodes and are therefore included in the results.

## Conclusion  

You now know how to **select objects by name** in Java 3D scenes using XPath‑like queries. This approach scales from simple demos to production‑grade 3‑D applications, giving you fine‑grained control over scene traversal without verbose code.

---

**Last Updated:** 2026-10-03  
**Tested With:** Aspose.3D for Java 24.11  
**Author:** Aspose  








```java
import com.aspose.threed.*;

import java.util.ArrayList;
import java.util.List;
```

## Related Tutorials

- [How to Use XPath to Modify Sphere Radius in Java with Aspose.3D](/3d/java/3d-objects-and-scenes/)
- [Read 3D Scenes in Java with Aspose.3D](/3d/java/load-and-save/read-existing-3d-scenes/)
- [Apply Geometric Transformations to a Node Using Aspose.3D Java API](/3d/java/geometry/expose-geometric-transformations/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}