---
date: 2026-02-17
description: Tìm hiểu cách chuyển đổi lưới sang FBX đồng thời thiết lập màu vật liệu
  và chia sẻ dữ liệu hình học lưới trong Java 3D bằng Aspose.3D.
linktitle: Convert Mesh to FBX and Set Material Color in Java 3D
second_title: Aspose.3D Java API
title: Chuyển Đổi Mesh sang FBX và Đặt Màu Vật Liệu trong Java 3D
url: /vi/java/geometry/share-mesh-geometry-data/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Chuyển Đổi Mesh Sang FBX và Đặt Màu Vật Liệu trong Java 3D

## Giới thiệu

Nếu bạn đang xây dựng một ứng dụng 3D dựa trên Java, bạn thường cần tái sử dụng cùng một geometry cho nhiều đối tượng đồng thời cung cấp cho mỗi instance một giao diện độc đáo. Trong tutorial này, bạn sẽ học **cách chuyển đổi mesh sang FBX**, chia sẻ geometry của mesh giữa nhiều node, và **đặt màu vật liệu khác nhau cho mỗi node**. Khi hoàn thành, bạn sẽ có một scene FBX sẵn sàng xuất ra mà có thể đưa vào bất kỳ engine hay viewer nào.

## Câu trả lời nhanh
- **Mục tiêu chính là gì?** Chuyển đổi mesh sang FBX, chia sẻ geometry của mesh, và đặt màu vật liệu riêng biệt cho mỗi node.  
- **Thư viện nào được yêu cầu?** Aspose.3D for Java.  
- **Làm thế nào để xuất kết quả?** Lưu scene dưới dạng file FBX bằng cách sử dụng `FileFormat.FBX7400ASCII`.  
- **Có cần giấy phép không?** Cần một giấy phép tạm thời hoặc đầy đủ cho việc sử dụng trong môi trường sản xuất.  
- **Phiên bản Java nào hoạt động?** Bất kỳ môi trường Java 8+ nào.

## convert mesh to FBX là gì

`convert mesh to fbx` là quá trình lấy một đối tượng mesh được tạo hoặc thao tác trong bộ nhớ và ghi nó ra định dạng file FBX, được hỗ trợ rộng rãi bởi các công cụ 3D như Maya, Blender và Unity. Aspose.3D thực hiện phần lớn công việc, vì vậy bạn chỉ cần gọi `scene.save(...)` với `FileFormat` thích hợp.

## Tại sao chia sẻ dữ liệu geometry của mesh?

Chia sẻ geometry giảm tiêu thụ bộ nhớ và tăng tốc độ render vì các buffer đỉnh nền tảng chỉ được lưu một lần. Kỹ thuật này hoàn hảo cho các scene có nhiều đối tượng trùng lặp—như rừng, đám đông, hoặc kiến trúc mô-đun—nơi mỗi instance chỉ khác nhau về transform hoặc material.

## Yêu cầu trước

Trước khi bắt đầu tutorial, hãy chắc chắn bạn đã chuẩn bị các yêu cầu sau:

- **Môi trường phát triển Java** – bất kỳ IDE hoặc thiết lập dòng lệnh nào với Java 8 trở lên.  
- **Thư viện Aspose.3D** – tải JAR mới nhất từ trang chính thức: [here](https://releases.aspose.com/3d/java/).

## Nhập các gói

Bắt đầu bằng việc nhập các gói cần thiết vào dự án Java của bạn. Bước này rất quan trọng để truy cập các chức năng do thư viện Aspose.3D cung cấp.

```java
import com.aspose.threed.*;
```

## Bước 1: Khởi tạo đối tượng Scene (initialize scene java)

Hãy bắt đầu quá trình bằng cách khởi tạo một đối tượng scene. Đối tượng này sẽ là canvas nơi phép thuật 3D của chúng ta được triển khai.

```java
// Initialize scene object
Scene scene = new Scene();
```

## Bước 2: Định nghĩa các vector màu

Trong bước này, chúng ta định nghĩa một mảng các vector màu sẽ được áp dụng cho các thành phần khác nhau của scene 3D.

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

Lặp qua các vector màu, tạo các node hình khối, và đặt các thuộc tính như material, **set material color**, và translation. Đây là phần cốt lõi để kiểm soát giao diện hình ảnh của mỗi instance mesh.

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

Xác định thư mục và tên file để lưu scene 3D ở định dạng file được hỗ trợ, trong trường hợp này là FBX7400ASCII. Bước này cũng minh họa **convert mesh to FBX**.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
MyDir = MyDir + "MeshGeometryData.fbx";

// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7400ASCII);
```

## Những lỗi thường gặp & Mẹo

- **Vấn đề đường dẫn** – Đảm bảo đường dẫn thư mục kết thúc bằng dấu phân tách file (`/` hoặc `\\`) trước khi nối tên file.  
- **Khởi tạo giấy phép** – Nếu bạn quên thiết lập giấy phép Aspose.3D trước khi gọi `scene.save`, thư viện sẽ chạy ở chế độ dùng thử và có thể chèn watermark.  
- **Ghi đè vật liệu** – Việc tái sử dụng cùng một instance `LambertMaterial` cho nhiều node sẽ khiến tất cả các node chia sẻ cùng một màu. Luôn tạo một vật liệu mới cho mỗi vòng lặp, như đã minh họa ở trên.  
- **Mesh lớn** – Đối với mesh có hàng triệu đỉnh, hãy cân nhắc sử dụng `MeshBuilder` với polygon được lập chỉ mục để giữ kích thước file FBX ở mức hợp lý.

## Câu hỏi thường gặp

**Q: Tôi có thể xuất scene sang các định dạng khác ngoài FBX không?**  
A: Có, Aspose.3D hỗ trợ OBJ, STL, 3MF, GLTF và hơn nữa. Chỉ cần thay thế enum `FileFormat` trong lời gọi `save`.

**Q: Nếu tôi cần thay đổi material sau khi scene đã được tạo thì sao?**  
A: Lấy node, sửa đổi `LambertMaterial` của nó (ví dụ, `setDiffuseColor`), và lưu lại scene.

**Q: Thư viện có xử lý mesh lớn một cách hiệu quả không?**  
A: Aspose.3D sử dụng các cấu trúc dữ liệu được tối ưu; tuy nhiên, đối với các mesh cực lớn, hãy cân nhắc streaming hoặc chia nhỏ scene.

**Q: Có cách nào để animate việc thay đổi màu không?**  
A: Có, bạn có thể animate các thuộc tính material bằng API `AnimationController`.

## Các câu hỏi thường gặp bổ sung

**Q1: Tôi có thể sử dụng Aspose.3D với các framework Java khác không?**  
A1: Có, Aspose.3D được thiết kế để hoạt động liền mạch với nhiều framework Java.

**Q2: Có các tùy chọn giấy phép nào cho Aspose.3D không?**  
A2: Có, bạn có thể khám phá các tùy chọn giấy phép [here](https://purchase.aspose.com/buy).

**Q3: Làm sao tôi có thể nhận hỗ trợ cho Aspose.3D?**  
A3: Truy cập [forum](https://forum.aspose.com/c/3d/18) của Aspose.3D để được hỗ trợ và thảo luận.

**Q4: Có bản dùng thử miễn phí không?**  
A4: Có, bạn có thể nhận bản dùng thử miễn phí [here](https://releases.aspose.com/).

**Q5: Làm sao tôi có thể lấy giấy phép tạm thời cho Aspose.3D?**  
A5: Bạn có thể lấy giấy phép tạm thời [here](https://purchase.aspose.com/temporary-license/).

## Kết luận

Chúc mừng! Bạn đã thành công **converted mesh to FBX**, chia sẻ dữ liệu geometry của mesh giữa nhiều node, và đặt màu vật liệu riêng cho từng node bằng Aspose.3D cho Java. Quy trình này cung cấp cho bạn một kiến trúc mesh nhẹ, có thể tái sử dụng và có thể xuất ra bất kỳ pipeline nào hỗ trợ FBX.

---

**Cập nhật lần cuối:** 2026-02-17  
**Đã kiểm tra với:** Aspose.3D 24.11 for Java  
**Tác giả:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}