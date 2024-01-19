---
title: Tạo xi lanh quạt
linktitle: Tạo xi lanh quạt
second_title: API Aspose.3D .NET
description: Mở khóa thế giới thiết kế 3D với Aspose.3D cho .NET! Dễ dàng tạo ra các xi lanh có quạt và không có quạt tuyệt đẹp. Tải xuống bản dùng thử của bạn ngay bây giờ.
type: docs
weight: 10
url: /vi/net/working-with-cylinder/create-fan-cylinder/
---
## Giới thiệu
Chào mừng bạn đến với thế giới mô hình hóa và trực quan hóa 3D với Aspose.3D cho .NET! Trong hướng dẫn từng bước này, chúng ta sẽ khám phá cách tạo một hình trụ quạt quyến rũ bằng Aspose.3D cho .NET. Aspose.3D là một thư viện mạnh mẽ cung cấp các khả năng mở rộng để làm việc với nội dung 3D trong các ứng dụng .NET.
## Điều kiện tiên quyết
Trước khi chúng ta đi sâu vào thế giới thú vị của mô hình 3D, hãy đảm bảo rằng bạn có các điều kiện tiên quyết sau:
- Hiểu biết cơ bản về lập trình .NET.
- Visual Studio được cài đặt trên máy của bạn.
-  Thư viện Aspose.3D cho .NET mà bạn có thể tải xuống[đây](https://releases.aspose.com/3d/net/).
- Sự quan tâm thực sự đến việc giải phóng khả năng sáng tạo của bạn thông qua thiết kế 3D.
## Nhập không gian tên
Hãy bắt đầu mọi thứ bằng cách nhập các không gian tên cần thiết để cung cấp chức năng Aspose.3D trong dự án .NET của bạn.
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
// Nhập không gian tên Aspose.3D
```
Bây giờ chúng ta đã thiết lập xong, hãy chia nhỏ quá trình tạo hình trụ quạt thành các bước có thể quản lý được.
## Bước 1: Tạo cảnh
```csharp
// Tạo cảnh
Scene scene = new Scene();
```
Bắt đầu bằng cách khởi tạo cảnh 3D mới. Điều này đóng vai trò như bức vẽ nơi hình trụ quạt của chúng ta sẽ trở nên sống động.
## Bước 2: Tạo xi lanh quạt
```csharp
// Tạo một hình trụ
var fan = new Cylinder(2, 2, 10, 20, 1, false);
```
Xác định các đặc điểm của xi lanh quạt, chỉ định các thông số như bán kính, chiều cao và độ phân giải.
## Bước 3: Tùy chỉnh thuộc tính xi lanh quạt
```csharp
// Đặt GeneratorFanCylinder thành true
fan.GenerateFanCylinder = true;
// Đặt độ dài Theta
fan.ThetaLength = MathUtils.ToRadian(270);
```
Điều chỉnh xi lanh quạt của bạn bằng cách cho phép tạo bộ phận quạt và điều chỉnh độ quét góc bằng ThetaLength.
## Bước 4: Định vị xi lanh quạt trong cảnh
```csharp
// Tạo nút con
scene.RootNode.CreateChildNode(fan).Transform.Translation = new Vector3(10, 0, 0);
```
Thêm hình trụ quạt làm nút con vào nút gốc của cảnh và định vị nó trong không gian 3D.
## Bước 5: Tạo một hình trụ không có quạt
```csharp
// Tạo hình trụ không cần quạt
var nonfan = new Cylinder(2, 2, 10, 20, 1, false);
```
Khám phá tính linh hoạt của Aspose.3D bằng cách tạo một hình trụ không có bộ phận quạt.
## Bước 6: Tùy chỉnh thuộc tính xi lanh không có quạt
```csharp
// Đặt GeneratorFanCylinder thành false
nonfan.GenerateFanCylinder = false;
// Đặt độ dài Theta
nonfan.ThetaLength = MathUtils.ToRadian(270);
```
Phân biệt xi lanh không quạt bằng cách vô hiệu hóa việc tạo ra bộ phận quạt.
## Bước 7: Định vị xi lanh không có quạt trong cảnh
```csharp
// Tạo nút con
scene.RootNode.CreateChildNode(nonfan);
```
Tương tự, thêm hình trụ không có quạt làm nút con vào nút gốc của cảnh.
## Bước 8: Lưu cảnh
```csharp
// Lưu cảnh
scene.Save("Your Document Directory" + "CreateFanCylinder.obj", FileFormat.WavefrontOBJ);
```
Lưu kiệt tác của bạn ở định dạng và vị trí mong muốn. Bây giờ, bạn đã tạo thành công một hình trụ có quạt và không có quạt bằng Aspose.3D cho .NET!
## Phần kết luận
Chúc mừng bạn đã hoàn thành hướng dẫn thực hành này về lập mô hình 3D với Aspose.3D cho .NET! Bạn đã thỏa sức sáng tạo trong lĩnh vực kỹ thuật số, chế tạo các trụ có quạt và không có quạt một cách dễ dàng.
## Các câu hỏi thường gặp
### Tôi có thể sử dụng Aspose.3D cho .NET với các khung .NET khác không?
Có, Aspose.3D tương thích với nhiều khung .NET khác nhau, mang lại tính linh hoạt trong các dự án phát triển của bạn.
### Có bản dùng thử miễn phí dành cho Aspose.3D cho .NET không?
 Có, bạn có thể khám phá bản dùng thử miễn phí[đây](https://releases.aspose.com/).
### Tôi có thể tìm tài liệu chi tiết về Aspose.3D cho .NET ở đâu?
 Tài liệu có sẵn[đây](https://reference.aspose.com/3d/net/).
### Làm cách nào tôi có thể nhận được hỗ trợ cho Aspose.3D cho .NET?
 Truy cập diễn đàn hỗ trợ[đây](https://forum.aspose.com/c/3d/18)để nhận được sự hỗ trợ từ cộng đồng và các chuyên gia Aspose.
### Giấy phép tạm thời có sẵn cho Aspose.3D cho .NET không?
 Có, có thể lấy được giấy phép tạm thời[đây](https://purchase.aspose.com/temporary-license/).