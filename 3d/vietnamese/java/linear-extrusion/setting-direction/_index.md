---
date: 2025-12-18
description: Tìm hiểu cách tạo cảnh 3D và lưu tệp OBJ bằng Aspose.3D cho Java. Hãy
  theo dõi hướng dẫn từng bước của chúng tôi về hướng ép tuyến tính.
linktitle: Setting Direction in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Tạo Cảnh 3D – Đặt Hướng Đùn Aspose.3D Java
url: /vi/java/linear-extrusion/setting-direction/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Tạo Cảnh 3D – Đặt Hướng Đùn Aspose.3D Java

## Introduction

Trong hướng dẫn này, bạn sẽ học **cách tạo cảnh 3d** các đối tượng và kiểm soát hướng đùn với Aspose.3D cho Java. Dù bạn đang xây dựng các hình ảnh kiến trúc, mẫu sản phẩm, hay tài sản trò chơi, việc thành thạo đùn tuyến tính sẽ bạn khả năng mô hình hóa các hình dạng phức tạp một cách nhanh chóng. Chúng tôi sẽ hướng dẫn từng bước, từ việc thêm node trong Java đến **xuất tệp mô hình 3d obj**, để bạn có thể xem kết quả ngay lập tức.

## Quick Answers
- **Câu hỏi: “tạo cảnh 3d” có nghĩa là gì?** Nó có nghĩa là khởi tạo một đối tượng Aspose.3D `Scene` sẽ chứa tất cả hình học, ánh sáng và máy ảnh.  
- **Làm thế nào để đặt hướng đùn?** Sử dụng phương thức `setDirection(Vector3)` trên một thể hiện `LinearExtrusion`.  
- **Định dạng nào nên dùng để xuất?** Định dạng OBJ (`FileFormat.WAVEFRONTOBJ`) được hỗ trợ rộng rãi cho quy trình làm việc 3‑D.  
- **Tôi có cần giấy phép cho Aspose.3D không?** Bản dùng thử miễn phí đủ cho phát triển; giấy phép thương mại cần thiết cho môi trường sản xuất.  
- **Tôi có thể thêm nhiều node hơn trong Java không?** Có — sử dụng `scene.getRootNode().createChildNode()` để thêm bao nhiêu đối tượng tùy ý.

## What is a “create 3d scene” workflow?

Một quy trình **tạo cảnh 3d** bắt đầu với một đối tượng `Scene` trống, thêm hình học (như các profile đã đùn), đặt vị trí bằng các biến đổi, và cuối cùng lưu cảnh thành một định dạng tệp như OBJ. Mẫu này là nền tảng của hầu hết các ứng dụng 3‑D được xây dựng bằng Aspose.3D.

## Why set extrusion directionĐặt hướng đùn cho phép bạn nghiêng, quay hoặc lệch hình dạng trong quá trình đùn, cung cấp kiểm soát đối với hình học cuối cùng mà không cần xử lý hậu kỳ. Điều này đặc biệt hữu ích cho:

- Tạo các cột thắt dần hoặc ống có hình dạng tùy chỉnh.  
- Căn chỉnh các đùn với các trục không chuẩn trong các bộ phận cơ khí.  
- Tạo các hình dạng nghệ thuật cho hiệu ứng hình ảnh.

## Prerequisites

Trước khi bắt đầu, hãy chắc chắn rằng bạn có:

- Kiến thức cơ bản về Java.  
- Thư viện Aspose.3D đã được cài đặt – tải xuống từ [here](https://releases.aspose.com/3d/java/).  
- Một IDE như Eclipse hoặc IntelliJ IDEA.

## Import Packages

First, import the required Aspose.3D classes:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Step 1: Initialize Base Profile

Create the 2‑D profile that will be extruded. In this example we use a rounded rectangle:

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

> **Mẹo chuyên nghiệp:** Điều chỉnh bán kính bo tròn để kiểm soát độ sắc hoặc mượt của các góc hình chữ nhật trước khi đùn.

## Step 2: Create a Scene

Now we **create 3d scene** that will host our objects:

```java
Scene scene = new Scene();
```

## Step 3: Add Nodes Java – Positioning the Objects

We’ll add two child nodes (left and right) to the scene’s root node and move the left one a little to the side:

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Step 4: How to extrude – Left Node (default direction)

Extrude the profile on the left node using the default Z‑axis direction. We also set a full 360° twist and increase slice count for smoothness:

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## Step 5: How to set direction – Right Node

Here we **how to set direction** by providing a custom `Vector3`. This tilts the extrusion toward the vector (0.3, 0.2, 1):

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## Step 6: Save OBJ file – Export 3D model

Finally, we **save obj file** to see the result in any 3‑D viewer:

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

Khi bạn mở tệp OBJ đã tạo, bạn sẽ thấy hai hình chữ nhật đã đùn: một với hướng mặc định và một nghiêng theo vector mà chúng tôi đã đặt.

## Common Issues and Solutions

| Vấn đề | Nguyên nhân | Giải pháp |
|-------|------------|----------|
| Tệp OBJ xuất hiện trống | Cảnh chưa được lưu hoặc đường dẫn không đúng | Kiểm tra `MyDir` trỏ tới thư mục có quyền ghi và tên tệp kết thúc bằng `.obj`. |
| Đùn trông phẳng | `setSlices` quá thấp | Tăng `setSlices` (ví dụ, 200) để có hình học mượt hơn. |
| Hướng không thay đổi | Vector chưa được chuẩn hoá | Sử dụng `Vector3` đã chuẩn hoá hoặc điều chỉnh giá trị để phản ánh độ nghiêng mong muốn. |

## Frequently Asked Questions

### Q1: Tôi có thể sử dụng Aspose.3D với các ngôn ngữ lập trình khác không?
A1: Aspose.3D hỗ trợ nhiều ngôn ngữ, bao gồm .NET và Java.

### Q2: Có bản dùng thử phí cho Aspose.3D không?
A2: Có, bạn có thể khám phá các tính năng của Aspose.3D với bản dùng thử miễn phí [here](https://releases.aspose.com/).

### Q3: Tôi có thể tìm tài liệu chi tiết cho Aspose.3D cho Java ở đâu?
A3: Tài liệu đầy đủ có sẵn [here](https://reference.aspose.com/3d/java/).

### Q4: Làm thế nào để tôi nhận được hỗ trợ cho Aspose.3D?
A4: Truy cập [Aspose.3D forum](https://forum.aspose.com/c/3d/18) để được trợ giúp hoặc đặt câu hỏi.

### Q5: Có giấy phép tạm thời cho Aspose.3D không?
A5: Có, bạn có thể nhận giấy phép tạm thời [here](https://purchase.aspose.com/temporary-license/).

---

**Cập nhật lần cuối:** 2025-12-18  
**Được kiểm tra với:** Aspose.3D 24.11 for Java  
**Tác giả:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}