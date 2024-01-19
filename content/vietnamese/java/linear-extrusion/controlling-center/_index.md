---
title: Trung tâm điều khiển trong ép đùn tuyến tính với Aspose.3D cho Java
linktitle: Trung tâm điều khiển trong ép đùn tuyến tính với Aspose.3D cho Java
second_title: API Java Aspose.3D
description: Khám phá thế giới đồ họa 3D trong Java với Aspose.3D. Kiểm soát trung tâm trong quá trình đùn tuyến tính một cách dễ dàng.
type: docs
weight: 11
url: /vi/java/linear-extrusion/controlling-center/
---
## Giới thiệu

Trong thế giới đồ họa 3D và lập trình Java, việc kiểm soát trung tâm ép đùn tuyến tính đóng một vai trò quan trọng trong việc đạt được hiệu quả mong muốn trong các dự án của bạn. Aspose.3D cho Java cung cấp bộ công cụ mạnh mẽ để xử lý các tác vụ như vậy một cách liền mạch. Trong hướng dẫn này, chúng ta sẽ đi sâu vào quy trình điều khiển trung tâm trong ép đùn tuyến tính bằng Aspose.3D cho Java, chia nhỏ từng bước để đảm bảo sự hiểu biết suôn sẻ và toàn diện.

## Điều kiện tiên quyết

Trước khi chúng ta bắt đầu hành trình hướng dẫn này, hãy đảm bảo bạn có sẵn các điều kiện tiên quyết sau:

1. Môi trường phát triển Java: Đảm bảo rằng bạn đã thiết lập môi trường phát triển Java trên máy của mình.

2.  Aspose.3D cho Java: Tải xuống và cài đặt thư viện Aspose.3D. Bạn có thể tìm thấy thư viện và tài liệu của nó[đây](https://reference.aspose.com/3d/java/).

3. Thư mục Tài liệu: Tạo một thư mục để lưu trữ các tài liệu Java của bạn. Hãy gọi nó là "Thư mục tài liệu của bạn."

## Gói nhập khẩu

Trong môi trường phát triển Java của bạn, hãy nhập các gói cần thiết cho Aspose.3D. Điều này đảm bảo rằng mã của bạn có quyền truy cập vào các chức năng do thư viện cung cấp.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Bước 1: Thiết lập hồ sơ cơ sở

Khởi tạo cấu hình cơ sở sẽ được ép đùn. Trong ví dụ này, chúng ta sẽ sử dụng hình chữ nhật có bán kính làm tròn là 0,3.

```java
// Đường dẫn đến thư mục tài liệu.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Bước 2: Tạo cảnh 3D

Xây dựng nền tảng cho thế giới 3D của bạn bằng cách tạo cảnh.

```java
Scene scene = new Scene();
```

## Bước 3: Tạo nút trái và phải

Thiết lập các nút trái và phải trong cảnh của bạn. Các nút này đóng vai trò là khung vẽ cho các đối tượng 3D của bạn.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Bước 4: Đùn tuyến tính với thuộc tính trung tâm

Thực hiện đùn tuyến tính trên nút bên trái mà không cần căn giữa và đặt số lát thành 3.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

## Bước 5: Đặt mặt phẳng đất để tham khảo

Nâng cao khả năng biểu diễn trực quan bằng cách thêm mặt phẳng nền vào nút bên trái.

```java
left.createChildNode(new Box(0.01, 3, 3));
```

## Bước 6: Đùn tuyến tính với thuộc tính trung tâm (Nút bên phải)

Thực hiện đùn tuyến tính trên nút bên phải, lần này căn giữa phần đùn và đặt lại số lát thành 3.

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

## Bước 7: Đặt mặt phẳng đất để tham chiếu (Nút bên phải)

Tương tự như nút bên trái, thêm mặt phẳng nền vào nút bên phải để tham khảo.

```java
right.createChildNode(new Box(0.01, 3, 3));
```

## Bước 8: Lưu cảnh 3D

Lưu cảnh 3D của bạn ở định dạng Wavefront OBJ.

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Phần kết luận

Việc điều khiển trung tâm trong quá trình ép đùn tuyến tính bằng Aspose.3D cho Java mở ra những khả năng thú vị trong phát triển đồ họa 3D. Bằng cách làm theo hướng dẫn từng bước này, bạn đã học được cách thao tác thuộc tính trung tâm, cho phép bạn đạt được hiệu ứng hình ảnh mong muốn trong các dự án Java của mình.

## Câu hỏi thường gặp

### Câu hỏi 1: Tôi có thể sử dụng Aspose.3D cho Java trong các dự án thương mại không?

 Câu trả lời 1: Có, Aspose.3D cho Java có sẵn cho mục đích sử dụng thương mại. Để biết chi tiết cấp phép, hãy truy cập[đây](https://purchase.aspose.com/buy).

### Q2: Có bản dùng thử miễn phí không?

 Câu trả lời 2: Có, bạn có thể khám phá bản dùng thử miễn phí Aspose.3D cho Java[đây](https://releases.aspose.com/).

### Câu hỏi 3: Tôi có thể tìm hỗ trợ cho Aspose.3D cho Java ở đâu?

 Câu trả lời 3: Diễn đàn cộng đồng Aspose.3D là nơi tuyệt vời để tìm kiếm sự hỗ trợ và chia sẻ kinh nghiệm của bạn. Ghé thăm diễn đàn[đây](https://forum.aspose.com/c/3d/18).

### Q4: Tôi có cần giấy phép tạm thời để thử nghiệm không?

Câu trả lời 4: Có, nếu bạn yêu cầu giấy phép tạm thời cho mục đích thử nghiệm, bạn có thể lấy giấy phép[đây](https://purchase.aspose.com/temporary-license/).

### Câu 5: Tôi có thể tìm tài liệu ở đâu?

 Câu trả lời 5: Tài liệu về Aspose.3D dành cho Java hiện có sẵn[đây](https://reference.aspose.com/3d/java/).