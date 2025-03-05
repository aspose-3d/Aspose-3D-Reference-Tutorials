---
title: Đặt hướng trong ép đùn tuyến tính với Aspose.3D cho Java
linktitle: Đặt hướng trong ép đùn tuyến tính với Aspose.3D cho Java
second_title: API Java Aspose.3D
description: Làm chủ quá trình đùn tuyến tính với Aspose.3D cho Java! Hãy làm theo hướng dẫn của chúng tôi để lập trình 3D liền mạch. Tải xuống ngay để có trải nghiệm thú vị.
type: docs
weight: 12
url: /vi/java/linear-extrusion/setting-direction/
---
## Giới thiệu

Chào mừng bạn đến với hướng dẫn từng bước của chúng tôi về cách thiết lập hướng trong ép đùn tuyến tính bằng Aspose.3D cho Java. Aspose.3D là một thư viện Java mạnh mẽ cho phép các nhà phát triển làm việc liền mạch với các tệp và cảnh 3D. Trong hướng dẫn này, chúng tôi sẽ tập trung vào nhiệm vụ cụ thể là thiết lập hướng trong ép đùn tuyến tính, nâng cao trình độ lập trình 3D của bạn.

## Điều kiện tiên quyết

Trước khi chúng ta đi sâu vào hướng dẫn, hãy đảm bảo bạn có sẵn các điều kiện tiên quyết sau:

- Kiến thức cơ bản về ngôn ngữ lập trình Java.
-  Đã cài đặt thư viện Aspose.3D. Bạn có thể tải nó xuống từ[đây](https://releases.aspose.com/3d/java/).
- Môi trường phát triển tích hợp (IDE) cho Java, chẳng hạn như Eclipse hoặc IntelliJ.

## Gói nhập khẩu

Đảm bảo rằng bạn nhập các gói cần thiết để khởi động dự án của mình:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Bước 1: Khởi tạo hồ sơ cơ sở

 Bắt đầu bằng cách khởi tạo biên dạng cơ sở sẽ được ép đùn. Trong ví dụ này, chúng tôi sử dụng một`RectangleShape` với bán kính làm tròn là 0,3:

```java
// Đường dẫn đến thư mục tài liệu.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Bước 2: Tạo cảnh

Tiếp theo, tạo cảnh 3D để chứa các đối tượng được ép đùn:

```java
Scene scene = new Scene();
```

## Bước 3: Tạo nút

Tạo các nút trái và phải trong cảnh:

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Bước 4: Thực hiện đùn tuyến tính trên nút bên trái

 Thực hiện đùn tuyến tính trên nút bên trái bằng cách sử dụng`LinearExtrusion`lớp với các tham số được chỉ định như xoắn và lát:

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## Bước 5: Thực hiện đùn tuyến tính trên nút bên phải theo hướng

 Thực hiện đùn tuyến tính trên nút bên phải, giới thiệu`setDirection` thuộc tính để xác định hướng đùn:

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## Bước 6: Lưu cảnh 3D

Lưu cảnh 3D sang định dạng tệp mong muốn. Trong ví dụ này, chúng tôi lưu nó dưới dạng tệp Wavefront OBJ:

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Phần kết luận

Chúc mừng! Bạn đã học thành công cách thiết lập hướng trong ép đùn tuyến tính bằng Aspose.3D cho Java. Hướng dẫn này nâng cao kỹ năng lập trình 3D của bạn và mở ra những khả năng mới cho các dự án sáng tạo.

## Câu hỏi thường gặp

### Câu hỏi 1: Tôi có thể sử dụng Aspose.3D với các ngôn ngữ lập trình khác không?

Trả lời 1: Aspose.3D hỗ trợ nhiều ngôn ngữ lập trình khác nhau, bao gồm .NET và Java.

### Q2. Có bản dùng thử miễn phí cho Aspose.3D không?

 Câu trả lời 2: Có, bạn có thể khám phá các tính năng của Aspose.3D bằng bản dùng thử miễn phí[đây](https://releases.aspose.com/).

### Câu hỏi 3: Tôi có thể tìm tài liệu chi tiết về Aspose.3D cho Java ở đâu?

 A3: Tài liệu toàn diện có sẵn[đây](https://reference.aspose.com/3d/java/).

### Câu hỏi 4: Làm cách nào tôi có thể nhận được hỗ trợ cho Aspose.3D?

 A4: Tham quan[Diễn đàn Aspose.3D](https://forum.aspose.com/c/3d/18) cho bất kỳ sự trợ giúp hoặc thắc mắc.

### Câu hỏi 5: Aspose.3D có giấy phép tạm thời không?

 Câu trả lời 5: Có, bạn có thể xin giấy phép tạm thời[đây](https://purchase.aspose.com/temporary-license/).