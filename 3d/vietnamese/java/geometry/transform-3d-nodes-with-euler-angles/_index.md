---
date: 2025-12-13
description: Học cách sử dụng Aspose 3D Java để biến đổi các nút 3D. Hướng dẫn này
  chỉ cách sử dụng góc Euler, thêm quay 3D và thiết lập dịch chuyển trong Java.
linktitle: Aspose 3D Java – Transform 3D Nodes with Euler Angles
second_title: Aspose.3D Java API
title: Aspose 3D Java – Biến đổi các nút 3D bằng góc Euler
url: /vi/java/geometry/transform-3d-nodes-with-euler-angles/
weight: 19
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Biến đổi các nút 3D bằng góc Euler trong Java sử dụng Aspose.3D

## Giới thiệu

Trong hướng dẫn này, bạn sẽ khám phá **cách sử dụng aspose 3d java** để biến đổi các nút 3D bằng cách áp dụng góc Euler. Khi kết thúc, bạn sẽ có thể thêm quay 3d, đặt dịch chuyển java, và tạo các cảnh động phản hồi dữ liệu thời gian thực.

## Câu trả lời nhanh
- **Thư viện nào xử lý các biến đổi 3D trong Java?** Aspose 3D for Java.  
- **Phương thức nào đặt quay bằng góc Euler?** `setEulerAngles()` trên transform của node.  
- **Làm thế nào để di chuyển một node trong không gian?** Sử dụng `setTranslation()` với một `Vector3`.  
- **Tôi có cần giấy phép cho môi trường sản xuất không?** Có, cần giấy phép thương mại Aspose 3D.  
- **Tôi có thể xuất ra FBX không?** Chắc chắn – `scene.save(..., FileFormat.FBX7500ASCII)` hoạt động ngay lập tức.

## Yêu cầu trước

Trước khi bắt đầu hướng dẫn, hãy chắc chắn rằng bạn đã chuẩn bị các yêu cầu sau:

- Kiến thức cơ bản về lập trình Java.  
- Java Development Kit (JDK) đã được cài đặt trên máy của bạn.  
- Thư viện Aspose.3D, bạn có thể tải từ [Aspose.3D Java Documentation](https://reference.aspose.com/3d/java/).

## Nhập khẩu các gói

Bắt đầu bằng việc nhập các gói cần thiết vào dự án Java của bạn. Đảm bảo rằng thư viện Aspose.3D đã được thêm đúng vào classpath. Nếu bạn chưa tải xuống, bạn có thể tìm liên kết tải về [here](https://releases.aspose.com/3d/java/).

```java
import com.aspose.threed.*;
```

## aspose 3d java – Làm việc với góc Euler

### Bước 1. Khởi tạo Scene và Node

Đầu tiên, tạo một scene và một node sẽ chứa hình học bạn muốn biến đổi.

```java
// ExStart:AddTransformationToNodeByEulerAngles
// Initialize scene object
Scene scene = new Scene();

// Initialize Node class object
Node cubeNode = new Node("cube");
```

### Bước 2. Tạo Mesh và Đặt Geometry

Tiếp theo, tạo một mesh đơn giản (một khối lập phương trong trường hợp này) và gắn nó vào node.

```java
// Call Common class create mesh using polygon builder method to set mesh instance
Mesh mesh = Common.createMeshUsingPolygonBuilder();

// Point node to the Mesh geometry
cubeNode.setEntity(mesh);
```

## Thêm quay 3D vào một Node

### Bước 3. Đặt góc Euler và Dịch chuyển

Bây giờ chúng ta áp dụng quay bằng góc Euler và cũng di chuyển node đến vị trí có thể nhìn thấy.

```java
// Euler angles
cubeNode.getTransform().setEulerAngles(new Vector3(0.3, 0.1, -0.5));

// Set translation
cubeNode.getTransform().setTranslation(new Vector3(0, 0, 20));
```

## Đặt Dịch chuyển Java – Định vị Node

Bước dịch chuyển ở trên minh họa **set translation java** trong thực tế: node được dịch chuyển 20 đơn vị dọc theo trục Z để bạn có thể thấy nó sau khi render.

## Bước 4. Thêm Node vào Scene

Gắn node đã biến đổi vào node gốc của scene.

```java
// Add cube to the scene
scene.getRootNode().getChildNodes().add(cubeNode);
```

## Bước 5. Lưu Scene 3D

Cuối cùng, xuất scene ra file FBX (hoặc bất kỳ định dạng hỗ trợ nào khác).

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
MyDir = MyDir + "TransformationToNode.fbx";

// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7500ASCII);
// ExEnd:AddTransformationToNodeByEulerAngles
System.out.println("\nTransformation added successfully to node.\nFile saved at " + MyDir);
```

Hãy chắc chắn thay thế `"Your Document Directory"` bằng đường dẫn thích hợp trên máy của bạn.

## Kết luận

Chúc mừng! Bạn đã thành công biến đổi các nút 3D bằng góc Euler trong Java với **aspose 3d java**. Hãy thử nghiệm với các góc và dịch chuyển khác nhau để tạo ra các cảnh 3D động và hấp dẫn.

## Câu hỏi thường gặp

### Q1: Tôi có thể sử dụng Aspose.3D cho Java trong các dự án thương mại không?

A1: Có, bạn có thể. Tham khảo [purchase page](https://purchase.aspose.com/buy) để biết chi tiết giấy phép.

### Q2: Tôi có thể tìm hỗ trợ cho Aspose.3D ở đâu?

A2: [Aspose.3D forum](https://forum.aspose.com/c/3d/18) là nơi bạn có thể tìm trợ giúp và kết nối với cộng đồng.

### Q3: Có bản dùng thử miễn phí không?

A3: Có, bạn có thể khám phá [free trial](https://releases.aspose.com/) để trải nghiệm các tính năng của Aspose.3D.

### Q4: Làm sao để tôi có được giấy phép tạm thời?

A4: Bạn có thể nhận giấy phép tạm thời [here](https://purchase.aspose.com/temporary-license/).

### Q5: Tôi có thể tìm tài liệu ở đâu?

A5: [documentation](https://reference.aspose.com/3d/java/) cung cấp hướng dẫn chi tiết về việc sử dụng Aspose.3D cho Java.

## Câu hỏi thường gặp

**Q: Sự khác biệt giữa góc Euler và quay quaternion là gì?**  
A: Góc Euler trực quan (pitch, yaw, roll) nhưng có thể gặp hiện tượng gimbal lock, trong khi quaternion tránh được vấn đề này và phù hợp hơn cho các nội suy mượt mà.

**Q: Tôi có thể xâu chuỗi nhiều biến đổi trên cùng một node không?**  
A: Có. Gọi `setEulerAngles`, `setTranslation` và `setScale` theo bất kỳ thứ tự nào; thư viện sẽ hợp nhất chúng thành một ma trận biến đổi duy nhất.

**Q: Có thể xuất ra các định dạng khác như OBJ hoặc STL không?**  
A: Chắc chắn. Thay `FileFormat.FBX7500ASCII` bằng `FileFormat.OBJ` hoặc `FileFormat.STL` trong lời gọi `scene.save`.

**Q: Làm sao áp dụng cùng một quay cho nhiều node cùng lúc?**  
A: Tạo một node cha, áp dụng quay cho node cha, sau đó thêm các node con vào dưới nó. Tất cả các node con sẽ kế thừa biến đổi.

**Q: Tôi có cần gọi bất kỳ phương thức dọn dẹp nào sau khi lưu không?**  
A: Trình thu gom rác Java sẽ xử lý hầu hết tài nguyên, nhưng bạn có thể gọi rõ ràng `scene.dispose()` nếu làm việc với các scene lớn trong ứng dụng chạy lâu.

**Last Updated:** 2025-12-13  
**Tested With:** Aspose.3D 23.12 for Java  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}