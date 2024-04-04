---
title: Xi lanh đáy cắt tùy chỉnh
linktitle: Xi lanh đáy cắt tùy chỉnh
second_title: API Aspose.3D .NET
description: Tìm hiểu cách tạo các trụ đáy cắt tùy chỉnh bằng Aspose.3D cho .NET với hướng dẫn từng bước chi tiết của chúng tôi. Nâng cao kỹ năng lập mô hình 3D của bạn ngay hôm nay!
type: docs
weight: 12
url: /vi/net/3d-modeling/working-with-cylinder/
---
## Giới thiệu
Chào mừng bạn đến với hướng dẫn toàn diện của chúng tôi về cách tạo hình trụ tùy chỉnh bằng Aspose.3D cho .NET. Nếu bạn đang tìm cách nâng cao kỹ năng lập mô hình 3D và thêm các tính năng độc đáo cho dự án của mình thì bạn đã đến đúng nơi. Trong hướng dẫn này, chúng tôi sẽ hướng dẫn bạn từng bước thực hiện quy trình, sử dụng các giải thích và đoạn mã rõ ràng.
## Điều kiện tiên quyết
Trước khi chúng ta đi sâu vào hướng dẫn, hãy đảm bảo bạn có những điều sau:
- Hiểu biết cơ bản về lập trình C# và .NET.
-  Đã cài đặt thư viện Aspose.3D cho .NET. Bạn có thể tải nó xuống[đây](https://releases.aspose.com/3d/net/).
- Một môi trường phát triển được thiết lập để lập trình .NET.
## Nhập không gian tên
Trong mã C# của bạn, hãy bắt đầu bằng cách nhập các vùng tên cần thiết:
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
Bắt đầu bằng cách tạo cảnh 3D bằng Aspose.3D:
```csharp
Scene scene = new Scene();
```
## Bước 2: Tạo hình trụ 1
Tạo hình trụ đầu tiên và thiết lập các thuộc tính của nó:
```csharp
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```
## Bước 3: Tùy chỉnh đáy cắt cho xi lanh 1
Áp dụng đáy cắt tùy chỉnh cho hình trụ đầu tiên:
```csharp
//Cắt 47,5 độ trong mặt phẳng xy (trục z)
cylinder1.ShearBottom = new Vector2(0, 0.83); 

// Đặt GeneratorFanCylinder thành true
cylinder1.GenerateFanCylinder = true;
// Đặt độ dài Theta
cylinder1.ThetaLength = MathUtils.ToRadian(270);

// Đặt OffsetTop
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```
## Bước 4: Thêm Xi lanh 1 vào Cảnh
Thêm hình trụ đầu tiên vào cảnh và thiết lập bản dịch của nó:
```csharp
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```
## Bước 5: Tạo hình trụ 2
Tạo hình trụ thứ hai có đặc tính tương tự:
```csharp
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```
## Bước 6: Thêm Xi lanh 2 vào Cảnh
Thêm hình trụ thứ hai vào cảnh mà không có thông số tùy chỉnh:
```csharp
scene.RootNode.CreateChildNode(cylinder2);
```
## Bước 7: Lưu cảnh
Lưu cảnh dưới dạng tệp OBJ Wavefront trong thư mục tài liệu của bạn:
```csharp
scene.Save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WavefrontOBJ);
```
## Phần kết luận
Chúc mừng! Bạn đã tạo thành công hình trụ đáy cắt tùy chỉnh bằng Aspose.3D cho .NET. Hướng dẫn này nhằm mục đích cung cấp hướng dẫn từng bước cho người dùng có trình độ chuyên môn khác nhau về lập mô hình và lập trình 3D.
## Các câu hỏi thường gặp
### Aspose.3D cho .NET có phù hợp cho người mới bắt đầu không?
Tuyệt đối! Aspose.3D for .NET cung cấp giao diện thân thiện với người dùng, giúp cả người mới bắt đầu và nhà phát triển có kinh nghiệm đều có thể truy cập được.
### Tôi có thể áp dụng các góc cắt khác nhau cho hình trụ không?
Có, bạn có thể tùy chỉnh đáy cắt cho từng xi lanh riêng lẻ, cho phép bạn đạt được các hiệu ứng độc đáo.
### Có sẵn phiên bản dùng thử không?
 Có, bạn có thể khám phá phiên bản dùng thử miễn phí[đây](https://releases.aspose.com/).
### Tôi có thể tìm thêm hỗ trợ ở đâu?
 Tham quan[Diễn đàn Aspose.3D](https://forum.aspose.com/c/3d/18) để được cộng đồng hỗ trợ và thảo luận.
### Làm thế nào tôi có thể có được giấy phép tạm thời?
 Nhận giấy phép tạm thời của bạn[đây](https://purchase.aspose.com/temporary-license/).