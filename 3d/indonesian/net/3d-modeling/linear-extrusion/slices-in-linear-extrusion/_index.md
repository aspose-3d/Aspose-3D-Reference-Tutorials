---
date: 2026-03-23
description: Pelajari cara ekstrusi linear dengan irisan menggunakan Aspose.3D untuk
  .NET. Buat model 3D detail dengan contoh kode langkah demi langkah.
linktitle: How to Linear Extrusion with Slices
second_title: Aspose.3D .NET API
title: Cara Ekstrusi Linear dengan Irisan Menggunakan Aspose.3D untuk .NET
url: /id/net/3d-modeling/linear-extrusion/slices-in-linear-extrusion/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Cara Linear Extrusion dengan Slices Menggunakan Aspose.3D untuk .NET

## Introduction

Selamat datang di dunia desain 3D menggunakan Aspose.3D untuk .NET! Pada tutorial ini Anda akan menemukan **cara linear extrusion** dengan slices, sebuah teknik yang memungkinkan Anda mengontrol tingkat detail pada model. Baik Anda seorang pengembang berpengalaman maupun yang baru memulai, kami akan memandu Anda melalui setiap langkah, menjelaskan alasan di balik setiap tindakan, dan memberikan tip praktis yang dapat langsung Anda terapkan.

## Quick Answers
- **Apa itu linear extrusion dengan slices?** Ini adalah metode memperluas profil 2D menjadi 3D sambil menentukan berapa banyak penampang menengah (slices) yang dihasilkan.  
- **Mengapa menggunakan slices?** Lebih banyak slices menghasilkan kelengkungan yang lebih halus; lebih sedikit slices membuat mesh lebih ringan.  
- **Prasyarat?** Aspose.3D untuk .NET, IDE yang kompatibel dengan .NET, dan pengetahuan dasar C#.  
- **Waktu runtime tipikal?** Contoh ini berjalan kurang dari satu detik pada PC modern.  
- **Format output?** Contoh menyimpan ke Wavefront OBJ, tetapi Aspose.3D mendukung banyak format.

## What is Linear Extrusion with Slices?

Linear extrusion mengambil bentuk 2‑D (sebuah profil) dan memanjang­kannya sepanjang garis lurus untuk membuat solid 3‑D. Properti **Slices** menentukan berapa banyak penampang menengah yang disisipkan antara awal dan akhir ekstrusi, memengaruhi kelancaran dan jumlah poligon.

## Why Use Slices in Linear Extrusion?

- **Control Mesh Density:** Menyetel keseimbangan antara kualitas visual dan ukuran file.  
- **Optimize Performance:** Gunakan lebih sedikit slices untuk aplikasi real‑time, lebih banyak untuk render resolusi tinggi.  
- **Creative Flexibility:** Gabungkan jumlah slice yang berbeda pada objek terpisah untuk menonjolkan maksud desain.

## Prerequisites

Sebelum memulai, pastikan Anda memiliki:

- Library Aspose.3D untuk .NET – unduh dari [here](https://releases.aspose.com/3d/net/).  
- IDE yang mendukung C# (Visual Studio, Rider, VS Code, dll.).  
- Familiaritas dasar dengan sintaks C# dan konsep berorientasi objek.  
- Rasa ingin tahu untuk bereksperimen dengan geometri 3‑D!

## Import Namespaces

Pertama, impor namespace yang memberi Anda akses ke kelas inti Aspose.3D.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Step‑by‑Step Guide

### Step 1: Initialize the Base Profile

Kami memulai dengan bentuk persegi panjang sederhana dan memberikan radius pembulatan kecil agar tepi tidak terlalu tajam.

```csharp
// ExStart:InitializeBaseProfile
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
// ExEnd:InitializeBaseProfile
```

### Step 2: Create a 3D Scene

`Scene` berfungsi sebagai wadah untuk semua node, mesh, cahaya, dan kamera.

```csharp
// ExStart:Create3DScene
Scene scene = new Scene();
// ExEnd:Create3DScene
```

### Step 3: Add Left and Right Nodes

Kami akan membuat dua node saudara di bawah root scene. Node kiri akan menerima jumlah slice rendah, node kanan jumlah slice tinggi, sehingga Anda dapat membandingkan perbedaan visualnya.

```csharp
// ExStart:CreateLeftRightNodes
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(15, 0, 0);
// ExEnd:CreateLeftRightNodes
```

### Step 4: Perform Linear Extrusion on the Left Node (Low Detail)

Di sini kami mengekstrusi persegi panjang dengan hanya **2 slices**. Ini menghasilkan mesh kasar—ideal untuk pratinjau cepat.

```csharp
// ExStart:LinearExtrusionLeftNode
left.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 2 });
// ExEnd:LinearExtrusionLeftNode
```

### Step 5: Perform Linear Extrusion on the Right Node (High Detail)

Sekarang kami menggunakan **10 slices** untuk hasil yang jauh lebih halus. Perhatikan bagaimana geometri menjadi lebih detail.

```csharp
// ExStart:LinearExtrusionRightNode
right.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 10 });
// ExEnd:LinearExtrusionRightNode
```

### Step 6: Save the 3D Scene

Akhirnya, tulis scene ke file OBJ. Ganti `"Your Output Directory"` dengan jalur yang valid di mesin Anda.

```csharp
// ExStart:Save3DScene
scene.Save("Your Output Directory" + "SlicesInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
// ExEnd:Save3DScene
```

## Common Issues and Solutions

| Issue | Why It Happens | Fix |
|-------|----------------|-----|
| **No file created** | Output path is invalid or missing write permission. | Use an absolute path and ensure the folder exists. |
| **Object looks flat** | `Slices` set to 1 or 0. | Set `Slices` to at least 2 for a visible extrusion. |
| **Unexpected geometry** | Rounding radius too large for the rectangle size. | Adjust `RoundingRadius` to a value smaller than half the rectangle’s smallest side. |

## Frequently Asked Questions

**Q: Can I change the extrusion direction?**  
A: Yes. Use the `Transform` property on the node to rotate or translate the extruded geometry before saving.

**Q: Does Aspose.3D support other extrusion types?**  
A: Absolutely. Besides `LinearExtrusion`, you can use `RevolveExtrusion`, `SweepExtrusion`, and more.

**Q: What file formats can I export to?**  
A: Aspose.3D supports OBJ, STL, FBX, 3MF, Collada, and many others. Just change the `FileFormat` enum.

**Q: Is there a way to programmatically set a material?**  
A: Yes. After creating the node, assign a `Material` to its `Entity` collection.

**Q: How does slice count affect memory usage?**  
A: More slices increase vertex and face counts, which raises memory consumption proportionally. Use profiling to find the sweet spot for your target platform.

## Original FAQ's

### Q1: Can I use Aspose.3D for .NET with other programming languages?

A1: Aspose.3D is primarily designed for .NET, but you can explore interoperability options with languages like Python using .NET bindings.

### Q2: Where can I find detailed documentation for Aspose.3D for .NET?

A2: Refer to the documentation [here](https://reference.aspose.com/3d/net/) for in‑depth information on Aspose.3D's capabilities and usage.

### Q3: Is there a free trial available for Aspose.3D for .NET?

A3: Yes, you can grab your free trial [here](https://releases.aspose.com/) to explore the library's features before making a purchase.

### Q4: How can I get technical support for Aspose.3D for .NET?

A4: Visit the Aspose.3D forum [here](https://forum.aspose.com/c/3d/18) to seek assistance and engage with the community.

### Q5: Can I use a temporary license for Aspose.3D for .NET?

A5: Yes, obtain a temporary license [here](https://purchase.aspose.com/temporary-license/) for evaluation purposes.

## Conclusion

Anda kini telah melihat **cara linear extrusion** dengan slices menggunakan Aspose.3D untuk .NET, mengeksplorasi dampak dari berbagai jumlah slice, dan belajar cara mengekspor hasil kerja Anda. Bereksperimenlah dengan profil lain, mainkan nilai `Slices`, serta integrasikan material atau cahaya untuk membuat aset 3‑D siap produksi.

---

**Last Updated:** 2026-03-23  
**Tested With:** Aspose.3D 24.11 for .NET (latest at time of writing)  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}