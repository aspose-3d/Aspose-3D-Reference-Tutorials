---
date: 2026-05-24
description: Tìm hiểu cách tạo 3d extrusion với slices bằng Aspose.3D for Java. Hướng
  dẫn từng bước này bao gồm linear extrusion, thiết lập rounding radius và xuất OBJ.
keywords:
- create 3d extrusion java
- Aspose 3D slices
- linear extrusion Java
linktitle: Tạo 3d extrusion với slices – Aspose.3D for Java
schemas:
- author: Aspose
  dateModified: '2026-05-24'
  description: Learn how to create 3d extrusion with slices using Aspose.3D for Java.
    This step‑by‑step guide covers linear extrusion, set rounding radius, and exporting
    OBJ.
  headline: Create 3D Extrusion with Slices – Aspose.3D for Java
  type: TechArticle
- description: Learn how to create 3d extrusion with slices using Aspose.3D for Java.
    This step‑by‑step guide covers linear extrusion, set rounding radius, and exporting
    OBJ.
  name: Create 3D Extrusion with Slices – Aspose.3D for Java
  steps:
  - name: Set up the scene and define the profile
    text: '`RectangleShape` is a class that defines a 2‑D rectangle profile. First
      we create a `RectangleShape` and give it a **rounding radius** so the corners
      are smooth. `Scene` is the root container for all nodes and geometry. Then we
      initialise a new `Scene` that will hold all geometry.'
  - name: Create child node objects for each extrusion
    text: '`Node` represents an element in the scene graph that can hold geometry
      and transformations. Every piece of geometry lives under a `Node`. Here we generate
      two sibling nodes – one for a low‑slice extrusion and another for a high‑slice
      extrusion – and move the left node a little to the side so the res'
  - name: Perform linear extrusion and set slices
    text: '`LinearExtrusion` is the class that creates a solid by sweeping a profile
      linearly. `LinearExtrusion` is Aspose.3D''s class that generates a solid by
      extruding a 2‑D profile along a straight line. Using an **anonymous inner class**
      we call `setSlices` to control the smoothness. The left node gets onl'
  - name: Export OBJ – save the scene
    text: Finally we write the scene to a Wavefront OBJ file, a format widely supported
      by 3‑D editors and game engines. This demonstrates the **export OBJ Java** capability
      of Aspose.3D.
  type: HowTo
- questions:
  - answer: You can download the library [here](https://releases.aspose.com/3d/java/).
    question: How can I download Aspose.3D for Java?
  - answer: Refer to the documentation [here](https://reference.aspose.com/3d/java/).
    question: Where can I find the documentation for Aspose.3D?
  - answer: Yes, you can explore a free trial [here](https://releases.aspose.com/).
    question: Is there a free trial available?
  - answer: Visit the support forum [here](https://forum.aspose.com/c/3d/18).
    question: How can I get support for Aspose.3D?
  - answer: Yes, a temporary license can be obtained [here](https://purchase.aspose.com/temporary-license/).
    question: Can I purchase a temporary license?
  type: FAQPage
second_title: Aspose.3D Java API
title: Tạo 3d extrusion với slices – Aspose.3D for Java
url: /vi/java/linear-extrusion/specifying-slices/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Tạo Đùn 3D với Các Lát – Aspose.3D cho Java

## Giới thiệu

Nếu bạn cần **tạo 3d extrusion** các đối tượng trông mượt mà và chính xác, việc kiểm soát số lượng lát là chìa khóa. Trong hướng dẫn này, chúng ta sẽ đi qua cách chỉ định số lát khi thực hiện một linear extrusion với Aspose.3D cho Java. Bạn sẽ thấy tại sao số lát quan trọng, cách đặt bán kính bo tròn, và cách xuất kết quả dưới dạng tệp OBJ có thể dùng trong bất kỳ pipeline 3‑D nào.

## Câu trả lời nhanh
- **“Slices” kiểm soát gì?** Số lượng các mặt cắt chéo trung gian được sử dụng để xấp xỉ bề mặt extrusion.  
- **Phương thức nào đặt số lượng lát?** `LinearExtrusion.setSlices(int)`  
- **Tôi có thể thay đổi bán kính bo tròn của profile không?** Có, thông qua `RectangleShape.setRoundingRadius(double)`  
- **Định dạng tệp nào được sử dụng trong ví dụ này?** Wavefront OBJ (`FileFormat.WAVEFRONTOBJ`)  
- **Tôi có cần giấy phép để chạy mã không?** Bản dùng thử miễn phí đủ cho việc đánh giá; giấy phép thương mại cần thiết cho môi trường sản xuất.

`LinearExtrusion.setSlices(int)` đặt số lượng lát trung gian mà extrusion sẽ tạo ra.  
`RectangleShape.setRoundingRadius(double)` xác định bán kính góc của một profile hình chữ nhật.

## Cách tạo 3d extrusion java với các lát?

Tải profile 2‑D của bạn, chọn số lượng lát, đặt bán kính bo tròn, và gọi `save` – toàn bộ quy trình chỉ cần vài dòng. Aspose.3D cho Java tự động xử lý việc tạo hình học, nội suy lát, và xuất OBJ, cho phép bạn tập trung vào chất lượng hình ảnh thay vì các tính toán lưới cấp thấp.

## Đùn tuyến tính với các lát là gì?

Một linear extrusion với các lát biến một hình dạng 2‑D phẳng thành một khối 3‑D bằng cách quét nó dọc theo một đường thẳng trong khi tạo ra một số lượng mặt cắt chéo trung gian có thể cấu hình. Số lượng lát trực tiếp ảnh hưởng đến độ mượt của các cạnh cong, chẳng hạn như các góc bo tròn.

## Tại sao sử dụng Aspose.3D cho Java để tạo 3d extrusion?

Aspose.3D cung cấp **kiểm soát lập trình đầy đủ** đối với mọi tham số extrusion, hỗ trợ **hơn 50 định dạng nhập và xuất** (bao gồm OBJ, FBX, STL và GLTF), và có thể xử lý **các mô hình hàng trăm trang** mà không cần tải toàn bộ tệp vào bộ nhớ. Nó chạy trên bất kỳ nền tảng nào hỗ trợ Java, không yêu cầu DLL gốc, và đảm bảo kết quả xác định trên Windows, Linux và macOS.

## Yêu cầu trước

1. **Java Development Kit** – JDK 8 hoặc cao hơn đã được cài đặt.  
2. **Aspose.3D cho Java** – Tải thư viện từ trang chính thức [tại đây](https://releases.aspose.com/3d/java/).  
3. Một IDE hoặc trình soạn thảo văn bản mà bạn ưa thích.

## Nhập các gói

Thêm không gian tên Aspose.3D vào dự án của bạn để có thể truy cập các lớp mô hình 3‑D.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## Hướng dẫn từng bước

### Bước 1: Thiết lập cảnh và xác định hồ sơ

`RectangleShape` là một lớp định nghĩa profile hình chữ nhật 2‑D.  
Đầu tiên chúng ta tạo một `RectangleShape` và đặt **bán kính bo tròn** để các góc trở nên mượt.  
`Scene` là container gốc cho tất cả các node và hình học.  
Sau đó chúng ta khởi tạo một `Scene` mới sẽ chứa toàn bộ hình học.

```java
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
Scene scene = new Scene();
```

### Bước 2: Tạo các đối tượng node con cho mỗi extrusion

`Node` đại diện cho một phần tử trong đồ thị cảnh có thể chứa hình học và biến đổi.  
Mọi phần hình học đều nằm dưới một `Node`. Ở đây chúng ta tạo hai node anh em – một cho extrusion ít lát và một cho extrusion nhiều lát – và di chuyển node bên trái một chút sang một bên để dễ so sánh kết quả.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### Bước 3: Thực hiện đùn tuyến tính và đặt số lát

`LinearExtrusion` là lớp tạo khối bằng cách quét một profile một cách tuyến tính.  
`LinearExtrusion` là lớp của Aspose.3D tạo khối bằng cách extrude một profile 2‑D dọc theo một đường thẳng. Sử dụng **lớp nội bộ ẩn danh** chúng ta gọi `setSlices` để kiểm soát độ mượt. Node bên trái chỉ có 2 lát (thô), trong khi node bên phải có 10 lát (mượt).

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(2);}});
right.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(10);}});
```

### Bước 4: Xuất OBJ – lưu cảnh

Cuối cùng chúng ta ghi cảnh ra tệp Wavefront OBJ, một định dạng được hỗ trợ rộng rãi bởi các trình chỉnh sửa 3‑D và engine game. Điều này thể hiện khả năng **export OBJ Java** của Aspose.3D.

```java
scene.save(MyDir + "SlicesInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Các vấn đề thường gặp và giải pháp

| Vấn đề | Nguyên nhân | Cách khắc phục |
|-------|-------------|----------------|
| **Extrusion appears flat** | Số lát được đặt thành 1 hoặc 0 | Đảm bảo `setSlices` được gọi với giá trị ≥ 2. |
| **Rounded corners look jagged** | Bán kính bo tròn quá nhỏ so với số lát | Tăng either bán kính hoặc số lát để có đường cong mượt hơn. |
| **File not found on save** | `MyDir` trỏ tới thư mục không tồn tại | Tạo thư mục trước hoặc sử dụng đường dẫn tuyệt đối. |

## Câu hỏi thường gặp

**Q: Làm sao tôi có thể tải Aspose.3D cho Java?**  
A: Bạn có thể tải thư viện [tại đây](https://releases.aspose.com/3d/java/).

**Q: Tôi có thể tìm tài liệu cho Aspose.3D ở đâu?**  
A: Tham khảo tài liệu [tại đây](https://reference.aspose.com/3d/java/).

**Q: Có bản dùng thử miễn phí không?**  
A: Có, bạn có thể khám phá bản dùng thử miễn phí [tại đây](https://releases.aspose.com/).

**Q: Làm sao tôi có thể nhận hỗ trợ cho Aspose.3D?**  
A: Truy cập diễn đàn hỗ trợ [tại đây](https://forum.aspose.com/c/3d/18).

**Q: Tôi có thể mua giấy phép tạm thời không?**  
A: Có, giấy phép tạm thời có thể được mua [tại đây](https://purchase.aspose.com/temporary-license/).

**Cập nhật lần cuối:** 2026-05-24  
**Kiểm tra với:** Aspose.3D cho Java 24.11 (phiên bản mới nhất tại thời điểm viết)  
**Tác giả:** Aspose

## Hướng dẫn liên quan

- [Tạo 3D Extrusion Java với Aspose.3D](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [Cách Đặt Hướng trong Linear Extrusion với Aspose.3D cho Java](/3d/java/linear-extrusion/setting-direction/)
- [Tạo Cảnh 3D với Twist trong Linear Extrusion – Aspose.3D cho Java](/3d/java/linear-extrusion/applying-twist/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}