---
title: Xi lanh hàng đầu bù đắp tùy chỉnh
linktitle: Xi lanh hàng đầu bù đắp tùy chỉnh
second_title: API Aspose.3D .NET
description: Khám phá những điều kỳ diệu của đồ họa 3D với Aspose.3D cho .NET. Tìm hiểu cách tạo các hình trụ trên cùng có độ lệch tùy chỉnh một cách dễ dàng. Nâng cao trải nghiệm mã hóa của bạn ngay bây giờ!
type: docs
weight: 11
url: /vi/net/working-with-cylinder/customized-offset-top-cylinder/
---
## Giới thiệu
Chào mừng bạn đến với thế giới thao tác đồ họa 3D với Aspose.3D cho .NET! Trong hướng dẫn này, chúng tôi sẽ hướng dẫn bạn quy trình tạo hình trụ trên cùng bù tùy chỉnh bằng Aspose.3D, một thư viện mạnh mẽ để làm việc với cảnh, đối tượng và định dạng 3D trong các ứng dụng .NET.
## Điều kiện tiên quyết
Trước khi chúng ta đi sâu vào hướng dẫn, hãy đảm bảo bạn có các điều kiện tiên quyết sau:
- Kiến thức cơ bản về ngôn ngữ lập trình C#.
- Visual Studio được cài đặt trên máy của bạn.
- Thư viện Aspose.3D cho .NET được tải xuống và tham chiếu trong dự án của bạn.
Bây giờ, hãy bắt đầu với hướng dẫn từng bước!
## Nhập không gian tên
Trước tiên, hãy đảm bảo nhập các không gian tên cần thiết trong mã C# của bạn:
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```
## Bước 1: Tạo cảnh
```csharp
// Tạo cảnh
Scene scene = new Scene();
```
Thao tác này sẽ khởi tạo cảnh 3D mới bằng Aspose.3D.
## Bước 2: Khởi tạo Xi lanh
```csharp
// Khởi tạo hình trụ
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```
Ở đây, chúng ta tạo một hình trụ với các thông số cụ thể như bán kính, chiều cao và lát cắt.
## Bước 3: Đặt OffsetTop cho Xi lanh đầu tiên
```csharp
// Đặt OffsetTop
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```
Điều này đặt một đỉnh bù tùy chỉnh cho hình trụ đầu tiên.
## Bước 4: Tạo ChildNode cho trụ đầu tiên
```csharp
// Tạo nút con
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```
Chúng tôi thêm hình trụ đầu tiên làm nút con vào cảnh, điều chỉnh vị trí của nó.
## Bước 5: Khởi tạo trụ thứ hai
```csharp
//Khởi tạo trụ thứ hai mà không tùy chỉnh OffsetTop
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```
Trụ thứ hai được khởi tạo mà không có đỉnh bù tùy chỉnh.
## Bước 6: Tạo ChildNode cho trụ thứ hai
```csharp
// Tạo nút con
scene.RootNode.CreateChildNode(cylinder2);
```
Chúng tôi thêm hình trụ thứ hai làm nút con vào cảnh.
## Bước 7: Lưu cảnh
```csharp
// Cứu
scene.Save("Your Document Directory" + "CustomizedOffsetTopCylinder.obj", FileFormat.WavefrontOBJ);
```
Thao tác này sẽ lưu cảnh 3D, bao gồm cả hình trụ trên cùng được bù tùy chỉnh, ở định dạng Wavefront OBJ.
Bây giờ bạn đã tạo thành công hình trụ trên cùng có độ lệch tùy chỉnh bằng Aspose.3D cho .NET!
## Phần kết luận
Trong hướng dẫn này, chúng ta đã khám phá những kiến thức cơ bản khi làm việc với Aspose.3D cho .NET để tạo hình trụ trên cùng bù tùy chỉnh. Thư viện này mở ra khả năng vô tận cho thao tác đồ họa 3D trong các ứng dụng .NET của bạn.
## Câu hỏi thường gặp
### Câu hỏi: Tôi có thể tìm tài liệu về Aspose.3D cho .NET ở đâu?
 A: Tài liệu có sẵn[đây](https://reference.aspose.com/3d/net/).
### Hỏi: Làm cách nào tôi có thể tải xuống Aspose.3D cho .NET?
 Trả lời: Bạn có thể tải xuống[đây](https://releases.aspose.com/3d/net/).
### Câu hỏi: Có bản dùng thử miễn phí dành cho Aspose.3D cho .NET không?
 Đ: Có, bạn có thể dùng thử miễn phí[đây](https://releases.aspose.com/).
### Câu hỏi: Tôi có thể nhận hỗ trợ cho Aspose.3D cho .NET ở đâu?
 Đáp: Hãy ghé thăm[Diễn đàn Aspose.3D](https://forum.aspose.com/c/3d/18) để hỗ trợ.
### Câu hỏi: Tôi có thể xin giấy phép tạm thời cho Aspose.3D cho .NET không?
 A: Có, bạn có thể nhận được giấy phép tạm thời[đây](https://purchase.aspose.com/temporary-license/).