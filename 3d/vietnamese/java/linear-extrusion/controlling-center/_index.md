---
date: 2025-12-18
description: Tìm hiểu cách thêm mặt phẳng nền và thiết lập thuộc tính center trong
  quá trình đùn thẳng bằng Aspose.3D cho Java, kèm các ví dụ mã từng bước.
linktitle: Controlling Center in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Cách Thêm Mặt Phẳng Đất và Trung Tâm Điều Khiển trong Đùn Đường Thẳng với Aspose.3D
  cho Java
url: /vi/java/linear-extrusion/controlling-center/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Trung tâm điều khiển trong Extrusion tuyến tính với Aspose.3D cho Java

## Giới thiệu

Khi bạn xây dựng các cảnh 3D bằng Java, khả năng **thêm mặt phẳng nền** đồng thời **đặt thuộc tính center** một cách chính xác cho extrusion tuyến tính có thể tạo ra sự khác biệt giữa một nguyên mẫu phẳng và một hình ảnh hoàn thiện. Trong hướng dẫn này, chúng ta sẽ đi qua toàn bộ quy trình kiểm soát trung tâm của extrusion và thêm mặt phẳng nền bằng Aspose.3D cho Java. Bạn sẽ hiểu tại sao điều này quan trọng, cách thiết lập, và nhận được một mẫu mã sẵn sàng chạy mà bạn có thể tùy chỉnh cho dự án của mình.

## Câu trả lời nhanh
- **“Thêm mặt phẳng nền” làm gì?** Nó tạo ra một hình học tham chiếu mỏng giúp bạn nhìn thấy vị trí của extrusion so với các trục thế giới.  
- **Làm sao để đặt trung tâm cho extrusion tuyến tính?** Sử dụng phương thức `setCenter(boolean)` trên đối tượng `LinearExtrusion`.  
- **Có cần giấy phép để chạy mẫu không?** Giấy phép tạm thời hoạt động cho việc thử nghiệm; giấy phép đầy đủ cần thiết cho môi trường sản xuất.  
- **Định dạng tệp nào được dùng để lưu?** Ví dụ lưu dưới dạng Wavefront OBJ (`.obj`).  
- **Yêu cầu phiên bản Java nào?** Java 8 trở lên là đủ.

## “Thêm mặt phẳng nền” trong một cảnh 3D là gì?

Thêm mặt phẳng nền có nghĩa là chèn một hình học hình chữ nhật mỏng (thường là một hộp với độ dày tối thiểu) nằm trên mặt phẳng X‑Z. Nó hoạt động như một sàn nhìn thấy, giúp dễ dàng đánh giá chiều cao và sự căn chỉnh của các đối tượng khác, đặc biệt khi bạn đang thử nghiệm với trung tâm extrusion.

## Tại sao cần đặt thuộc tính center trên extrusion tuyến tính?

Mặc định, extrusion tuyến tính bắt đầu từ gốc của profile. Đặt thuộc tính center (`setCenter(true)`) sẽ dịch chuyển profile sao cho extrusion được căn giữa quanh gốc, hữu ích cho các thiết kế đối xứng hoặc khi bạn cần căn chỉnh nhất quán giữa nhiều đối tượng.

## Điều kiện tiên quyết

Trước khi bắt đầu hành trình hướng dẫn này, hãy chắc chắn bạn đã chuẩn bị đầy đủ các điều kiện sau:

1. **Môi trường phát triển Java** – Đảm bảo bạn đã cài đặt môi trường phát triển Java trên máy tính.  
2. **Aspose.3D cho Java** – Tải xuống và cài đặt thư viện Aspose.3D. Bạn có thể tìm thư viện và tài liệu của nó [tại đây](https://reference.aspose.com/3d/java/).  
3. **Thư mục tài liệu** – Tạo một thư mục để lưu trữ các tệp Java của bạn. Gọi nó là “Your Document Directory.”

## Nhập gói

Trong môi trường phát triển Java của bạn, nhập các gói cần thiết cho Aspose.3D. Điều này đảm bảo mã của bạn có quyền truy cập vào các chức năng do thư viện cung cấp.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Bước 1: Thiết lập Profile cơ bản

Khởi tạo profile cơ bản sẽ được extrusion. Trong ví dụ này, chúng ta sẽ sử dụng một hình chữ nhật với bán kính bo tròn là 0.3.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Bước 2: Tạo một cảnh 3D

Xây dựng nền tảng cho thế giới 3D của bạn bằng cách tạo một scene.

```java
Scene scene = new Scene();
```

## Bước 3: Tạo các nút Trái và Phải

Thiết lập các nút trái và phải trong scene. Các nút này sẽ là nền cho các đối tượng 3D của bạn.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Bước 4: Extrusion tuyến tính với thuộc tính Center (Nút Trái)

Thực hiện extrusion tuyến tính trên nút trái **không căn giữa** và đặt số lát (slices) là 3. Lưu ý lời gọi `setCenter(false)` – đây là nơi chúng ta **đặt thuộc tính center** thành *false*.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

## Bước 5: Thêm mặt phẳng nền để tham chiếu (Nút Trái)

Cải thiện hiển thị bằng cách **thêm mặt phẳng nền** vào nút trái. Hộp mỏng hoạt động như một sàn để bạn có thể nhìn rõ chiều cao của extrusion.

```java
left.createChildNode(new Box(0.01, 3, 3));
```

## Bước 6: Extrusion tuyến tính với thuộc tính Center (Nút Phải)

Bây giờ thực hiện extrusion tuyến tính trên nút phải, lần này **căn giữa extrusion**. Lời gọi `setCenter(true)` minh họa cách **đặt thuộc tính center** thành *true*.

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

## Bước 7: Thêm mặt phẳng nền để tham chiếu (Nút Phải)

Giống như phía trái, thêm một mặt phẳng nền vào nút phải để có một nền tham chiếu nhất quán.

```java
right.createChildNode(new Box(0.01, 3, 3));
```

## Bước 8: Lưu cảnh 3D

Lưu cảnh 3D của bạn ở định dạng Wavefront OBJ để có thể xem trong bất kỳ trình xem 3D tiêu chuẩn nào.

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Các vấn đề thường gặp và giải pháp

| Vấn đề | Nguyên nhân | Giải pháp |
|-------|-------------|-----------|
| Mặt phẳng nền không hiển thị | Độ dày hộp quá nhỏ so với tầm nhìn của trình xem. | Tăng độ dày (tham số đầu tiên của `Box`) hoặc thu nhỏ (zoom out) trong trình xem. |
| Extrusion bị lệch | Giá trị `setCenter` không được đặt như mong muốn. | Kiểm tra lại giá trị boolean truyền vào `setCenter`. |
| Tệp không được lưu | Đường dẫn thư mục không đúng hoặc thiếu quyền ghi. | Xác minh `MyDir` trỏ tới một thư mục tồn tại và có quyền ghi. |

## Câu hỏi thường gặp

**Q1: Tôi có thể sử dụng Aspose.3D cho Java trong các dự án thương mại không?**  
A1: Có, Aspose.3D cho Java có thể dùng cho mục đích thương mại. Để biết chi tiết về giấy phép, hãy truy cập [tại đây](https://purchase.aspose.com/buy).

**Q2: Có bản dùng thử miễn phí không?**  
A2: Có, bạn có thể khám phá bản dùng thử miễn phí của Aspose.3D cho Java [tại đây](https://releases.aspose.com/).

**Q3: Tôi có thể tìm hỗ trợ cho Aspose.3D cho Java ở đâu?**  
A3: Diễn đàn cộng đồng Aspose.3D là nơi tuyệt vời để tìm hỗ trợ và chia sẻ kinh nghiệm. Truy cập diễn đàn [tại đây](https://forum.aspose.com/c/3d/18).

**Q4: Tôi có cần giấy phép tạm thời để thử nghiệm không?**  
A4: Có, nếu bạn cần giấy phép tạm thời cho mục đích thử nghiệm, bạn có thể lấy một giấy phép [tại đây](https://purchase.aspose.com/temporary-license/).

**Q5: Tôi có thể tìm tài liệu ở đâu?**  
A5: Tài liệu cho Aspose.3D cho Java có sẵn [tại đây](https://reference.aspose.com/3d/java/).

## Kết luận

Kiểm soát trung tâm trong extrusion tuyến tính **và** học cách **thêm mặt phẳng nền** với Aspose.3D cho Java mở ra nhiều khả năng thú vị trong phát triển đồ họa 3D. Bằng cách làm theo các bước trên, bạn đã có một mẫu có thể tái sử dụng để tạo extrusion có trung tâm, mặt phẳng tham chiếu trực quan, và xuất kết quả ra OBJ. Hãy thoải mái thử nghiệm với các profile, số lát và biến đổi khác nhau để phù hợp với nhu cầu dự án của bạn.

---

**Cập nhật lần cuối:** 2025-12-18  
**Đã kiểm tra với:** Aspose.3D 24.11 cho Java (phiên bản mới nhất tại thời điểm viết)  
**Tác giả:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}