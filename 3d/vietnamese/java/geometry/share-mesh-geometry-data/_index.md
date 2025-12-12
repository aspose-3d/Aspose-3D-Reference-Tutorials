---
date: 2025-12-12
description: Tìm hiểu cách thiết lập màu vật liệu khi chia sẻ dữ liệu hình học lưới
  và lưu cảnh dưới dạng FBX trong Java 3D bằng Aspose.3D.
linktitle: Set Material Color and Share Mesh Geometry Data in Java 3D with Aspose.3D
second_title: Aspose.3D Java API
title: Đặt màu vật liệu và chia sẻ dữ liệu hình học lưới trong Java 3D với Aspose.3D
url: /vi/java/geometry/share-mesh-geometry-data/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Đặt Màu Vật Liệu và Chia Sẻ Dữ Liệu Hình Học Lưới trong Java 3D với Aspose.3D

## Giới thiệu

Bắt đầu hành trình khám phá Java 3D cùng Aspose.3D mở ra một thế giới đầy tiềm năng để tạo ra những hình ảnh trực quan tuyệt đẹp và trải nghiệm nhập vai. Trong hướng dẫn này, chúng tôi sẽ chỉ cho bạn **cách chia sẻ dữ liệu hình học lưới** trong Java 3D bằng Aspose.3D, và sẽ cho bạn thấy **cách đặt màu vật liệu** cho mỗi thể hiện lưới. Hãy làm theo từng bước một cách cẩn thận, và vào cuối bạn sẽ có thể trao đổi dữ liệu lưới giữa nhiều node một cách liền mạch, đồng thời kiểm soát màu sắc và xuất ra định dạng FBX.

## Câu trả lời nhanh
- **Mục tiêu chính là gì?** Đặt màu vật liệu cho mỗi node và chia sẻ dữ liệu hình học lưới.  
- **Thư viện nào cần thiết?** Aspose.3D cho Java.  
- **Làm sao để xuất kết quả?** L cảnh dưới dạng tệp FBX (FBX740ASCII).  
- **Có cần giấy phép không?** Cần giấy phép tạm thời hoặc đầy đủ cho môi trường sản xuất.  
- **Phiên bản Java nào hỗ trợ?** Bất kỳ môi trường Java 8+ nào.

## Yêu cầu trước

Trước khi bắt đầu hướng dẫn, hãy chắc chắn rằng bạn đã chuẩn bị các yêu cầu sau:

- Môi trường phát triển Java: Đảm bảo bạn đã cài đặt môi trường phát triển Java trên hệ thống.  
- Thư viện Aspose.3D: Tải và cài đặt thư viện Aspose.3D. Bạn có thể tìm thư viện [tại đây](https://releases.aspose.com/3d/java/).

## Nhập các Gói

Bắt đầu bằng việc nhập các gói cần thiết vào dự án Java của bạn. Bước này rất quan trọng để truy cập các chức năng do thư viện Aspose.3D cung cấp.

```java
import com.aspose.threed.*;
```

## Bước 1: Khởi tạo Đối tượng Scene (initialize scene java)

Hãy khởi tạo một đối tượng scene. Đây sẽ là canvas nơi phép màu 3D của chúng ta sẽ diễn ra.

```java
// Initialize scene object
Scene scene = new Scene();
```

## Bước 2: Định nghĩa Vector Màu

Trong bước này, chúng ta định nghĩa một mảng các vector màu sẽ được áp dụng cho các thành phần khác nhau của cảnh 3D.

```java
// Define color vectors
Vector3[] colors = new Vector3[] {
    new Vector3(1, 0, 0),
    new Vector3(0, 1, 0),
    new Vector3(0, 0, 1)
};
```

## Bước 3: Tạo Mesh 3D Java bằng Polygon Builder (create 3d mesh java)

Sử dụng lớp Common để tạo một mesh bằng phương pháp polygon builder. Mesh này sẽ là nền tảng cho các phần tử 3D của chúng ta.

```java
// Call Common class create mesh using polygon builder method to set mesh instance
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

## Cách đặt màu vật liệu cho mỗi node?

Lặp qua các vector màu, tạo các node hình khối lập phương, và đặt các thuộc tính như vật liệu, **đặt màu vật liệu**, và dịch chuyển. Đây là phần cốt lõi để kiểm soát giao diện hình ảnh của mỗi thể hiện mesh.

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

## Bước 5: Lưu Scene 3D (save scene fbx, convert mesh to fbx)

Xác định thư mục và tên tệp để lưu cảnh 3D ở định dạng hỗ trợ, trong trường hợp này là FBX7400ASCII. Bước này cũng minh họa **chuyển đổi mesh sang FBX**.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
MyDir = MyDir + "MeshGeometryData.fbx";

// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7400ASCII);
```

## Kết luận

Chúc mừng! Bạn đã thành công **đặt màu vật liệu**, chia sẻ dữ liệu hình học lưới giữa nhiều node, và xuất kết quả dưới dạng tệp FBX bằng Aspose.3D cho Java. Điều này mở ra vô vàn khả năng để tạo ra các ứng dụng 3D tương tác và bắt mắt.

## Câu hỏi thường gặp

### Q1: Tôi có thể dùng Aspose.3D với các framework Java khác không?

A1: Có, Aspose.3D được thiết kế để hoạt động liền mạch với nhiều framework Java.

### Q2: Có những tùy chọn cấp phép nào cho Aspose.3D?

A2: Có, bạn có thể khám phá các tùy chọn cấp phép [tại đây](https://purchase.aspose.com/buy).

### Q3: Làm sao tôi có thể nhận hỗ trợ cho Aspose.3D?

A3: Truy cập [diễn đàn Aspose.3D](https://forum.aspose.com/c/3d/18) để được hỗ trợ và thảo luận.

### Q4: Có bản dùng thử miễn phí không?

A4: Có, bạn có thể nhận bản dùng thử miễn phí [tại đây](https://releases.aspose.com/).

### Q5: Làm sao tôi có thể lấy giấy phép tạm thời cho Aspose.3D?

A5: Bạn có thể nhận giấy phép tạm thời [tại đây](https://purchase.aspose.com/temporary-license/).

## Các Câu hỏi Thường gặp Bổ sung

**Q: Tôi có thể xuất cảnh sang các định dạng khác ngoài FBX không?**  
A: Có, Aspose.3D hỗ trợ OBJ, STL, 3MF và nhiều định dạng khác. Chỉ cần thay đổi enum `FileFormat` trong lời gọi `save`.

**Q: Nếu tôi cần thay đổi vật liệu sau khi đã tạo cảnh thì sao?**  
A: Lấy node tương ứng, sửa đổi `LambertMaterial` của nó (ví dụ, `setDiffuseColor`), và lưu lại cảnh.

**Q: Thư viện có xử lý các mesh lớn một cách hiệu quả không?**  
A: Aspose.3D sử dụng các cấu trúc dữ liệu được tối ưu; tuy nhiên, với các mesh cực lớn, bạn nên cân nhắc streaming hoặc chia nhỏ cảnh.

**Q: Có cách nào để tạo hoạt ảnh thay đổi màu không?**  
A: Có, bạn có thể tạo hoạt ảnh cho các thuộc tính vật liệu bằng API `AnimationController`.

---

**Cập nhật lần cuối:** 2025-12-12  
**Đã kiểm tra với:** Aspose.3D 24.11 cho Java  
**Tác giả:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}