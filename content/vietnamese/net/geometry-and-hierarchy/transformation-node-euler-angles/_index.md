---
title: Chuyển đổi nút bằng góc Euler trong cảnh 3D
linktitle: Chuyển đổi nút bằng góc Euler trong cảnh 3D
second_title: API Aspose.3D .NET
description: Tìm hiểu cách chuyển đổi các nút 3D một cách dễ dàng với Aspose.3D cho .NET. Hãy làm theo hướng dẫn từng bước của chúng tôi để có kết quả ấn tượng trong dự án của bạn.
type: docs
weight: 19
url: /vi/net/geometry-and-hierarchy/transformation-node-euler-angles/
---
## Giới thiệu

Chào mừng bạn đến với hướng dẫn toàn diện này về cách chuyển đổi các nút theo góc Euler trong cảnh 3D bằng Aspose.3D cho .NET. Trong hướng dẫn này, chúng ta sẽ đi sâu vào thế giới đồ họa 3D thú vị và khám phá quá trình thêm các phép biến đổi vào một nút bằng các góc Euler. Aspose.3D for .NET cung cấp các công cụ mạnh mẽ để làm việc với các cảnh và lưới 3D, khiến nó trở thành lựa chọn tuyệt vời cho các nhà phát triển đang tìm kiếm tính linh hoạt và hiệu quả trong các dự án của họ.

## Điều kiện tiên quyết

Trước khi chúng ta đi sâu vào hướng dẫn, hãy đảm bảo bạn có sẵn các điều kiện tiên quyết sau:

-  Aspose.3D for .NET Library: Đảm bảo rằng bạn đã cài đặt thư viện Aspose.3D. Bạn có thể tải nó xuống[đây](https://releases.aspose.com/3d/net/).

- Môi trường phát triển: Thiết lập môi trường phát triển .NET ưa thích của bạn, chẳng hạn như Visual Studio.

## Nhập không gian tên

Bắt đầu bằng cách nhập các không gian tên cần thiết để truy cập chức năng do Aspose.3D cung cấp cho .NET:

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

Bây giờ, hãy chia ví dụ thành nhiều bước để hiểu rõ hơn.

## Bước 1: Khởi tạo đối tượng cảnh

```csharp
// ExStart:AddTransformationToNodeByEulerAngles
// Khởi tạo đối tượng cảnh
Scene scene = new Scene();
```

 Bắt đầu bằng cách tạo cảnh 3D mới bằng cách sử dụng`Scene` lớp học.

## Bước 2: Khởi tạo đối tượng lớp nút

```csharp
// Khởi tạo đối tượng lớp Node
Node cubeNode = new Node("cube");
```

 Tạo một nút trong cảnh bằng cách sử dụng`Node`lớp học. Nút này sẽ đóng vai trò là nơi chứa đối tượng 3D của chúng ta.

## Bước 3: Tạo lưới bằng Polygon Builder

```csharp
// Gọi Lớp chung tạo lưới bằng phương pháp xây dựng đa giác để đặt phiên bản lưới
Mesh mesh = Common.CreateMeshUsingPolygonBuilder(); 
```

 Gọi một phương thức (trong trường hợp này là`CreateMeshUsingPolygonBuilder` từ một phong tục`Common` class) để tạo lưới cho đối tượng 3D.

## Bước 4: Nút trỏ vào hình học lưới

```csharp
// Nút điểm vào hình học Lưới
cubeNode.Entity = mesh;
```

Liên kết lưới đã tạo với nút.

## Bước 5: Đặt góc Euler và dịch chuyển

```csharp
// góc Euler
cubeNode.Transform.EulerAngles = new Vector3(0.3, 0.1, -0.5);            
// Đặt bản dịch
cubeNode.Transform.Translation = new Vector3(0, 0, 20);
```

Xác định các góc Euler và bản dịch cho nút để định vị nó trong không gian 3D.

## Bước 6: Thêm khối vào cảnh

```csharp
// Thêm khối vào hiện trường
scene.RootNode.ChildNodes.Add(cubeNode);
```

Kết hợp nút vào hệ thống phân cấp của cảnh.

## Bước 7: Lưu cảnh 3D

```csharp
// Đường dẫn đến thư mục tài liệu.
var output = "Your Output Directory" + "TransformationToNode.fbx";

//Lưu cảnh 3D ở các định dạng tệp được hỗ trợ
scene.Save(output, FileFormat.FBX7500ASCII);
// ExEnd:AddTransformationToNodeByEulerAngles
Console.WriteLine("\nTransformation added successfully to node.\nFile saved at " + output);
```

Chỉ định thư mục đầu ra và lưu cảnh 3D, bao gồm nút được chuyển đổi, ở định dạng tệp mong muốn (FBX7500ASCII trong trường hợp này).

## Phần kết luận

Chúc mừng! Bạn đã học thành công cách chuyển đổi nút theo góc Euler trong cảnh 3D bằng cách sử dụng Aspose.3D cho .NET. Thư viện mạnh mẽ này mở ra cánh cửa cho những khả năng vô tận trong phát triển đồ họa 3D.

## Câu hỏi thường gặp

### Câu hỏi 1: Aspose.3D có tương thích với các công cụ tạo mô hình 3D khác không?

Câu trả lời 1: Aspose.3D hỗ trợ nhiều định dạng tệp 3D khác nhau, nâng cao khả năng tương thích với các công cụ tạo mô hình phổ biến.

### Câu hỏi 2: Tôi có thể áp dụng nhiều phép biến đổi cho một nút không?

Câu trả lời 2: Có, bạn có thể kết hợp và áp dụng nhiều phép biến đổi để đạt được các hiệu ứng phức tạp.

### Câu hỏi 3: Tôi có thể tìm thêm tài liệu Aspose.3D ở đâu?

 A3: Hãy tham khảo[tài liệu](https://reference.aspose.com/3d/net/) để biết thông tin chi tiết và ví dụ.

### Câu hỏi 4: Tôi có cần giấy phép sử dụng Aspose.3D cho .NET không?

 A4: Có, bạn có thể lấy được giấy phép[đây](https://purchase.aspose.com/buy) hoặc khám phá một[dùng thử miễn phí](https://releases.aspose.com/).

### Câu 5: Cần hỗ trợ hoặc có câu hỏi cụ thể?

A5: Tham quan[Diễn đàn Aspose.3D](https://forum.aspose.com/c/3d/18) để hỗ trợ cộng đồng.