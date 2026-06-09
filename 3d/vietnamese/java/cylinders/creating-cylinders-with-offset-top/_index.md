---
date: 2026-04-08
description: Tìm hiểu cách tạo một hình trụ với đỉnh lệch trong Aspose.3D cho Java,
  thêm nút con Java, đặt đỉnh lệch, tạo mô hình 3D và xuất OBJ bằng giấy phép tạm
  thời của Aspose.
keywords:
- aspose temporary license
- generate 3d model
- add child node java
- java export obj
- set offset top
linktitle: Giấy phép tạm thời Aspose – Tạo hình trụ với đỉnh lệch (Java)
second_title: Aspose.3D Java API
title: Giấy phép tạm thời Aspose – Tạo hình trụ với đỉnh lệch (Java)
url: /vi/java/cylinders/creating-cylinders-with-offset-top/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose Temporary License – Tạo Trụ với Đỉnh Dịch Chuyển (Java)

## Giới thiệu

Nếu bạn muốn **tạo trụ** với một đỉnh tùy chỉnh lệch trong một cảnh 3D dựa trên Java, Aspose.3D giúp quá trình này trở nên đơn giản. Trong hướng dẫn này, chúng tôi sẽ đi qua từng bước — từ thiết lập cảnh đến xuất mô hình cuối cùng dưới dạng tệp OBJ — để bạn có thể tích hợp các trụ có đỉnh lệch vào ứng dụng của mình một cách tự tin. Khi hoàn thành, bạn sẽ hiểu cách **aspose temporary license** cho phép bạn đánh giá các tính năng này mà không cần mua bản đầy đủ.

## Câu trả lời nhanh
- **Thư viện nào được sử dụng?** Aspose.3D for Java  
- **Có thể dịch chuyển đỉnh của trụ không?** Có, sử dụng `setOffsetTop`  
- **Làm thế nào để thêm nút con trong Java?** Gọi `createChildNode` trên nút gốc  
- **Có thể xuất sang định dạng nào?** Wavefront OBJ (`java export obj`)  
- **Có cần giấy phép để thử nghiệm không?** Một **aspose temporary license** có sẵn để đánh giá  

## Aspose Temporary License là gì?

Một **aspose temporary license** là khóa đánh giá ngắn hạn, miễn phí, mở khóa toàn bộ tính năng của Aspose.3D for Java trong quá trình phát triển và thử nghiệm. Nó loại bỏ các dấu nước đánh giá và cho phép bạn tạo các tệp mô hình 3D, như OBJ, STL, hoặc FBX, chính xác như một giấy phép trả phí.

## Tại sao nên sử dụng Aspose.3D cho Java?

- **API cấp cao:** Không cần quản lý dữ liệu lưới cấp thấp.  
- **Đa nền tảng:** Hoạt động trên bất kỳ môi trường tương thích JVM nào.  
- **Bộ xuất tích hợp:** Lưu trực tiếp thành OBJ, STL, FBX và nhiều định dạng khác.  
- **Mở rộng:** Dễ dàng thêm nút con, áp dụng biến đổi và tích hợp với các thư viện Java khác.  

## Yêu cầu trước

Trước khi bắt đầu, hãy chắc chắn rằng bạn có:

- **Java Development Kit (JDK)** – một phiên bản tương thích đã được cài đặt.  
- **Thư viện Aspose.3D cho Java** – tải JAR mới nhất từ trang chính thức [here](https://releases.aspose.com/3d/java/).  
- Một IDE theo lựa chọn của bạn (Eclipse, IntelliJ IDEA, NetBeans, v.v.).  

## Nhập gói

Đầu tiên, nhập các lớp chúng ta cần. Đặt các câu lệnh này ở đầu tệp Java của bạn:

```java
import com.aspose.threed.Cylinder;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Vector3;


import java.io.IOException;
```

## Hướng dẫn từng bước

### Bước 1: Tạo một cảnh 3D Java

Một **cảnh 3D Java** đóng vai trò là container cho tất cả các đối tượng 3D.

```java
// ExStart:1
// Create a scene
Scene scene = new Scene();
// ExEnd:1
```

### Bước 2: Khởi tạo Trụ với Đỉnh Dịch Chuyển

Ở đây chúng tôi trả lời **cách tạo trụ** với một độ dịch chuyển tùy chỉnh. Constructor xác định bán kính, chiều cao, số lát cắt, số lớp, và việc trụ có đóng kín hay không. Sau đó, chúng tôi dịch chuyển đỉnh bằng cách sử dụng `setOffsetTop`.

```java
// ExStart:2
// Initialize cylinder
Cylinder cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
// Set OffsetTop
cylinder1.setOffsetTop(new Vector3(5, 3, 0));
// ExEnd:2
```

### Bước 3: Thêm nút con Java – Gắn Trụ Đầu Tiên

Chúng tôi tạo một nút con dưới nút gốc của cảnh và di chuyển trụ tới vị trí mong muốn.

```java
// ExStart:3
// Create ChildNode
scene.getRootNode().createChildNode(cylinder1).getTransform().setTranslation(10, 0, 0);
// ExEnd:3
```

### Bước 4: Khởi tạo Trụ Thứ Hai (Không Dịch Chuyển)

Để so sánh, chúng tôi thêm một trụ thông thường không có độ dịch chuyển.

```java
// ExStart:4
// Initialize second cylinder without customized OffsetTop
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// ExEnd:4
```

### Bước 5: Thêm nút con Java – Gắn Trụ Thứ Hai

```java
// ExStart:5
// Create ChildNode
scene.getRootNode().createChildNode(cylinder2);
// ExEnd:5
```

### Bước 6: Java Export OBJ – Lưu Cảnh dưới dạng OBJ

Cuối cùng, chúng tôi **java export obj** toàn cảnh (cả hai trụ) dưới dạng tệp Wavefront OBJ, được hỗ trợ rộng rãi bởi các công cụ 3D.

```java
// ExStart:6
// Save
scene.save("Your Document Directory" + "CustomizedOffsetTopCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

Khi bạn chạy chương trình, bạn sẽ thấy tệp `CustomizedOffsetTopCylinder.obj` trong thư mục đã chỉ định, sẵn sàng mở trong Blender, Maya hoặc bất kỳ trình xem OBJ nào khác.

## Cách tạo mô hình 3D và xuất OBJ trong Java

Sự kết hợp của `Scene.save(..., FileFormat.WAVEFRONTOBJ)` và **aspose temporary license** cho phép bạn **tạo mô hình 3d** nhanh chóng, mà không cần bộ chuyển đổi bên ngoài. Điều này đặc biệt hữu ích trong giai đoạn nguyên mẫu hoặc khi chia sẻ tài sản với các nhà thiết kế.

## Các trường hợp sử dụng thực tế

- **Trực quan kiến trúc:** Trụ có đỉnh lệch mô phỏng các cột thu hẹp lên phía trần.  
- **Bộ phận cơ khí:** Tạo piston hoặc vỏ bánh răng mà bề mặt trên được dịch chuyển có chủ đích.  
- **Tài sản trò chơi:** Tạo các hình dạng cột đa dạng nhanh chóng, giảm nhu cầu tạo lưới thủ công.  

## Các vấn đề thường gặp và giải pháp

| Vấn đề | Lý do | Cách khắc phục |
|-------|--------|----------------|
| **Tệp OBJ trống** | Cảnh không được lưu đúng cách hoặc đường dẫn sai. | Kiểm tra thư mục đầu ra tồn tại và bạn có quyền ghi. |
| **Dịch chuyển không được áp dụng** | Sử dụng phiên bản Aspose.3D cũ hơn. | Cập nhật lên thư viện mới nhất có hỗ trợ `setOffsetTop`. |
| **Nút con không hiển thị** | Biến đổi chưa được áp dụng. | Đảm bảo bạn gọi `getTransform().setTranslation` sau khi tạo nút con. |

## Câu hỏi thường gặp

**Q: Aspose.3D có tương thích với các IDE Java khác nhau không?**  
A: Có, nó hoạt động liền mạch với Eclipse, IntelliJ IDEA, NetBeans và các IDE khác.

**Q: Tôi có thể áp dụng texture cho các đối tượng 3D đã tạo không?**  
A: Chắc chắn! Sử dụng lớp `Material` để gán texture và các thuộc tính bề mặt.

**Q: Có các tùy chọn cấp phép cho Aspose.3D không?**  
A: Nhiều mô hình cấp phép khác nhau có sẵn; bạn có thể khám phá chúng [here](https://purchase.aspose.com/buy).

**Q: Làm sao tôi có thể nhận trợ giúp hoặc chia sẻ kinh nghiệm?**  
A: Tham gia diễn đàn cộng đồng Aspose.3D [here](https://forum.aspose.com/c/3d/18) để được hỗ trợ và thảo luận.

**Q: Có giấy phép tạm thời để thử nghiệm không?**  
A: Có, một **aspose temporary license** có thể được lấy để đánh giá [here](https://purchase.aspose.com/temporary-license/).

---

**Cập nhật lần cuối:** 2026-04-08  
**Đã kiểm tra với:** Aspose.3D for Java 24.12 (mới nhất)  
**Tác giả:** Aspose

---

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}