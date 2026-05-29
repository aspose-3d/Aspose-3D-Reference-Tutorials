---
date: 2026-04-03
description: Tìm hiểu cách tạo hình dạng quạt hình trụ trong Java với Aspose.3D. Hướng
  dẫn này bao gồm mô hình 3D Java và các kỹ thuật lưu tệp OBJ trong Java.
keywords:
- create cylinder fan shape
- save obj file java
- aspose 3d export obj
linktitle: Cách tạo hình dạng quạt trụ bằng Aspose.3D cho Java
second_title: Aspose.3D Java API
title: Cách tạo hình dạng quạt trụ bằng Aspose.3D cho Java
url: /vi/java/cylinders/creating-fan-cylinders/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Cách tạo hình dạng quạt trụ bằng Aspose.3D cho Java

## Giới thiệu

Bạn đã sẵn sàng để thành thạo **cách tạo hình dạng quạt trụ** trong môi trường Java chưa? Trong hướng dẫn này, chúng tôi sẽ đi qua từng bước—từ việc thiết lập cảnh cho đến xuất tệp Wavefront OBJ—sử dụng Aspose.3D. Dù bạn đang xây dựng tài sản cho trò chơi, một nguyên mẫu CAD, hay chỉ thử nghiệm với hình học 3D, bạn sẽ thấy việc mô hình hóa 3D bằng Java trở nên dễ dàng như thế nào với thư viện mạnh mẽ này.

## Câu trả lời nhanh
- **Mục tiêu chính là gì?** Tạo một trụ dạng quạt có thể tùy chỉnh và lưu dưới dạng tệp OBJ.  
- **Thư viện nào được sử dụng?** Aspose.3D cho Java.  
- **Tôi có cần giấy phép không?** Bản dùng thử miễn phí hoạt động cho phát triển; giấy phép thương mại cần thiết cho môi trường sản xuất.  
- **Các điều kiện tiên quyết là gì?** JDK đã được cài đặt và gói Aspose.3D Java đã được thêm vào dự án của bạn.  
- **Tôi có thể xuất sang các định dạng khác không?** Có—Aspose.3D hỗ trợ nhiều định dạng; ví dụ này sử dụng Wavefront OBJ.

## Trụ quạt là gì?

Trụ quạt là một trụ bề mặt một phần, trong đó một phần của đáy tròn bị loại bỏ, tạo ra một khe mở dạng “quạt”. Hình học này hữu ích cho việc trực quan hoá các lát cắt, bảng điều khiển, hoặc các bộ phận cơ khí tùy chỉnh.

## Tại sao nên sử dụng Aspose.3D cho mô hình 3D Java?

Aspose.3D cung cấp một API sạch sẽ, hướng đối tượng, trừu tượng hoá các phép tính cấp thấp của đồ họa 3D. Bạn có thể tập trung vào thiết kế thay vì các chi tiết đặc thù của định dạng tệp, và thư viện tự động xử lý các thao tác **save obj file java**.

## Điều kiện tiên quyết

Trước khi chúng ta bắt đầu, hãy chắc chắn rằng bạn đã có:

- **Java Development Kit (JDK)** – tải xuống [tại đây](https://www.oracle.com/java/technologies/javase-downloads.html).  
- **Aspose.3D for Java** – lấy JAR mới nhất từ [liên kết tải xuống](https://releases.aspose.com/3d/java/).  

Thêm JAR Aspose.3D vào classpath của dự án.

## Nhập gói

Bắt đầu bằng việc nhập các lớp cần thiết. Điều này cho phép bạn truy cập vào cảnh 3D, các primitive hình học, và các phương thức tiện ích.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Bước 1: Tạo một Scene

Đầu tiên, chúng ta khởi tạo một `Scene` mới. Hãy nghĩ về một scene như là container chứa tất cả các đối tượng 3D, ánh sáng và camera của bạn.

```java
// ExStart:2
// Create a Scene
Scene scene = new Scene();
// ExEnd:2
```

## Bước 2: Tạo một Fan Cylinder (cách tạo cylinder)

Bây giờ chúng ta xây dựng chính trụ quạt. Các tham số của constructor xác định bán kính, chiều cao, mức chia lưới (tessellation), và liệu hình học có được tạo dưới dạng quạt hay không.

```java
// ExStart:3
// Create a cylinder with fan
Cylinder fan = new Cylinder(2, 2, 10, 20, 1, false);
fan.setGenerateFanCylinder(true);
fan.setThetaLength(MathUtils.toRadian(270.0));
// ExEnd:3
```

> **Mẹo chuyên nghiệp:** Điều chỉnh `setThetaLength` để thay đổi góc mở. 270° tạo ra một quạt ba phần tư; 180° sẽ cho một nửa trụ.

## Bước 3: Đặt vị trí Fan Cylinder

Tiếp theo, chúng ta thêm trụ quạt vào scene và di chuyển nó đến vị trí thuận tiện. Các tọa độ dịch chuyển được sắp xếp theo thứ tự (X, Y, Z).

```java
// ExStart:4
// Create ChildNode and set translation
scene.getRootNode().createChildNode(fan).getTransform().setTranslation(10, 0, 0);
// ExEnd:4
```

## Bước 4: Tạo một Non‑Fan Cylinder (so sánh mô hình 3D Java)

Để minh họa tính linh hoạt của Aspose.3D, chúng ta cũng tạo một trụ thông thường không có khe mở dạng quạt.

```java
// ExStart:5
// Create a cylinder without a fan
Cylinder nonfan = new Cylinder(2, 2, 10, 20, 1, false);
// Create ChildNode
scene.getRootNode().createChildNode(nonfan);
// ExEnd:5
```

## Bước 5: Lưu Scene (java save obj file)

Cuối cùng, chúng ta xuất toàn bộ scene ra tệp Wavefront OBJ. Định dạng này được hầu hết các trình chỉnh sửa 3D và engine trò chơi hỗ trợ rộng rãi.

```java
// ExStart:6
// Save scene
scene.save("Your Document Directory" + "CreateFanCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

> **Lưu ý:** Thay thế `"Your Document Directory"` bằng đường dẫn tuyệt đối hoặc tương đối mà bạn có quyền ghi.

## Cách lưu tệp OBJ trong Java bằng Aspose 3D

Phương thức `Scene.save` của Aspose.3D tự động xử lý quá trình **aspose 3d export obj**. Bạn chỉ cần chỉ định tên tệp đích và giá trị enum `FileFormat.WAVEFRONTOBJ`, như đã minh họa ở bước trước.

## Vấn đề thường gặp và giải pháp

| Vấn đề | Nguyên nhân | Cách khắc phục |
|-------|------------|----------------|
| Tệp OBJ rỗng | Scene không được lưu hoặc đường dẫn không đúng | Kiểm tra thư mục đầu ra tồn tại và có quyền ghi. |
| Khe mở quạt hiển thị sai | Giá trị `ThetaLength` không đúng | Sử dụng `MathUtils.toRadian(degrees)` để đặt góc chính xác bạn cần. |
| Lỗi biên dịch | Thiếu JAR Aspose.3D trong classpath | Thêm JAR vào thư mục `libs` của dự án và bao gồm nó trong đường build. |

## Câu hỏi thường gặp

**Q: Aspose.3D có tương thích với các thư viện 3D Java khác không?**  
**A:** Có, Aspose.3D có thể đồng thời tồn tại với các thư viện như Java 3D hoặc jMonkeyEngine, cho phép bạn tích hợp geometry tùy chỉnh vào các pipeline lớn hơn.

**Q: Tôi có thể tùy chỉnh thêm ngoại hình của trụ quạt không?**  
**A:** Chắc chắn. Bạn có thể áp dụng vật liệu, texture và ánh sáng bằng cách truy cập vào các collection `Material` và `Light` của node.

**Q: Tôi có thể nhận hỗ trợ bổ sung ở đâu?**  
**A:** Truy cập [diễn đàn Aspose.3D](https://forum.aspose.com/c/3d/18) để nhận trợ giúp từ cộng đồng và phản hồi chính thức.

**Q: Có bản dùng thử miễn phí không?**  
**A:** Có, bạn có thể khám phá Aspose.3D với một [bản dùng thử miễn phí](https://releases.aspose.com/) trước khi mua.

**Q: Làm thế nào để tôi có được giấy phép tạm thời để thử nghiệm?**  
**A:** Nhận một giấy phép [tại đây](https://purchase.aspose.com/temporary-license/) để mở khóa đầy đủ chức năng trong quá trình phát triển.

---

**Cập nhật lần cuối:** 2026-04-03  
**Kiểm tra với:** Aspose.3D 24.11 cho Java  
**Tác giả:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}