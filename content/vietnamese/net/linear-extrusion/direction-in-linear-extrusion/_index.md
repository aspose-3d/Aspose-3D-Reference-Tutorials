---
title: Hướng trong đùn tuyến tính
linktitle: Hướng trong đùn tuyến tính
second_title: API Aspose.3D .NET
description: Mở khóa thế giới mô hình 3D với Aspose.3D cho .NET. Tìm hiểu hướng ép đùn tuyến tính, tăng khả năng sáng tạo và tạo ra các ứng dụng sống động một cách dễ dàng.
type: docs
weight: 11
url: /vi/net/linear-extrusion/direction-in-linear-extrusion/
---
## Giới thiệu

Trong thế giới phát triển phần mềm năng động, việc tạo ra các mô hình 3D sống động là một kỹ năng không thể thiếu. Aspose.3D for .NET cung cấp cho các nhà phát triển một bộ công cụ mạnh mẽ để khai thác tiềm năng của mô hình 3D trong các ứng dụng của họ. Trong hướng dẫn này, chúng ta sẽ đi sâu vào thế giới hấp dẫn của ép đùn tuyến tính và khám phá các sắc thái của tính năng "Hướng trong ép đùn tuyến tính".

## Điều kiện tiên quyết

Trước khi chúng ta bắt đầu cuộc hành trình thú vị này, hãy đảm bảo bạn có sẵn các điều kiện tiên quyết sau:

-  Aspose.3D for .NET: Tải xuống và cài đặt thư viện từ[Tài liệu Aspose.3D .NET](https://reference.aspose.com/3d/net/).

- Môi trường phát triển: Đảm bảo bạn đã thiết lập môi trường phát triển .NET đang hoạt động.

## Nhập không gian tên

Trong dự án .NET của bạn, hãy nhập các vùng tên cần thiết để truy cập chức năng của Aspose.3D. Thêm các dòng sau vào đầu mã của bạn:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Bước 1: Khởi tạo hồ sơ cơ sở

Bắt đầu bằng cách khởi tạo biên dạng cơ sở sẽ được ép đùn. Trong ví dụ này, chúng ta tạo một hình chữ nhật có bán kính làm tròn là 0,3.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## Bước 2: Tạo cảnh 3D

Xây dựng nền tảng cho kiệt tác 3D của bạn bằng cách tạo cảnh.

```csharp
Scene scene = new Scene();
```

## Bước 3: Tạo nút

Tạo các nút trong cảnh để thể hiện các thành phần khác nhau trong môi trường 3D của bạn.

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(8, 0, 0);
```

## Bước 4: Đùn tuyến tính không có hướng

 Thực hiện đùn tuyến tính trên nút bên trái bằng cách sử dụng`Twist` Và`Slices` của cải.

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100 });
```

## Bước 5: Đùn tuyến tính có hướng

 Mở rộng khả năng ép đùn bằng cách kết hợp`Direction` thuộc tính ở nút bên phải.

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100, Direction = new Vector3(0.3, 0.2, 1) });
```

## Bước 6: Lưu cảnh 3D

 Bảo tồn tác phẩm của bạn bằng cách lưu cảnh 3D. Thay thế`"Your Output Directory"` với thư mục mong muốn.

```csharp
scene.Save("Your Output Directory" + "DirectionInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

Chúc mừng! Bạn đã triển khai thành công tính năng ép đùn tuyến tính với Aspose.3D cho .NET, khám phá cả cách tiếp cận truyền thống và định hướng.

## Phần kết luận

Trong hướng dẫn này, chúng ta đã tìm hiểu lĩnh vực mô hình 3D hấp dẫn bằng cách sử dụng Aspose.3D cho .NET. Ép đùn tuyến tính, có và không có hướng, mở ra khả năng vô tận cho các nhà phát triển đang tìm cách tạo ra các ứng dụng có hình ảnh đẹp mắt. Với Aspose.3D, sức mạnh của mô hình 3D nằm trong tầm tay bạn.

## Câu hỏi thường gặp

### Câu hỏi 1: Làm cách nào tôi có thể nhận được giấy phép tạm thời cho Aspose.3D cho .NET?

 A1: Tham quan[Cung cấp giấy phép tạm thời](https://purchase.aspose.com/temporary-license/) để có được giấy phép tạm thời.

### Câu hỏi 2: Tôi có thể tìm hỗ trợ cho Aspose.3D ở đâu?

 A2: Tham gia[Diễn đàn Aspose.3D](https://forum.aspose.com/c/3d/18) để tìm kiếm sự hỗ trợ và kết nối với cộng đồng.

### Câu 3: Có bản dùng thử miễn phí không?

 Câu trả lời 3: Có, hãy khám phá các tính năng bằng bản dùng thử miễn phí tại[Bản phát hành Aspose.3D](https://releases.aspose.com/).

### Câu hỏi 4: Làm cách nào để mua Aspose.3D cho .NET?

 A4: Điều hướng đến[Trang mua hàng giả định](https://purchase.aspose.com/buy) để biết các tùy chọn cấp phép và chi tiết mua hàng.

### Câu hỏi 5: Tôi có thể tìm tài liệu chi tiết về Aspose.3D cho .NET ở đâu?

 A5: Tham khảo toàn diện[Tài liệu Aspose.3D .NET](https://reference.aspose.com/3d/net/) để biết thông tin chuyên sâu.