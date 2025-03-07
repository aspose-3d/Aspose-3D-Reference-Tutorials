---
title: Chuyển đổi nút bằng Quaternion
linktitle: Chuyển đổi nút bằng Quaternion
second_title: API Aspose.3D .NET
description: Tìm hiểu cách chuyển đổi các nút 3D bằng quaternion bằng Aspose.3D cho .NET. Hướng dẫn từng bước cho người mới bắt đầu.
weight: 20
url: /vi/net/geometry-and-hierarchy/transformation-node-quaternion/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Chuyển đổi nút bằng Quaternion

## Giới thiệu

Chào mừng bạn đến với hướng dẫn từng bước về cách chuyển đổi nút theo bậc bốn trong cảnh 3D bằng Aspose.3D cho .NET. Trong hướng dẫn này, chúng ta sẽ khám phá các khả năng mạnh mẽ của Aspose.3D cho .NET và hướng dẫn quy trình thêm các phép biến đổi vào nút 3D bằng cách sử dụng quaternions.

## Điều kiện tiên quyết

Trước khi chúng ta đi sâu vào hướng dẫn, hãy đảm bảo bạn có sẵn các điều kiện tiên quyết sau:

-  Aspose.3D for .NET: Đảm bảo bạn đã cài đặt thư viện Aspose.3D. Bạn có thể tải nó xuống từ[trang phát hành](https://releases.aspose.com/3d/net/).

- Môi trường phát triển: Thiết lập môi trường phát triển .NET của bạn với các công cụ và cấu hình cần thiết.

- Hiểu biết cơ bản về các khái niệm 3D: Làm quen với các khái niệm và đồ họa 3D sẽ rất hữu ích.

## Nhập không gian tên

Trong dự án .NET của bạn, hãy bao gồm các không gian tên bắt buộc cho Aspose.3D:

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

## Bước 1: Khởi tạo đối tượng cảnh

```csharp
// ExStart:AddTransformationToNodeByQuaternion
// Khởi tạo đối tượng cảnh
Scene scene = new Scene();
```

## Bước 2: Khởi tạo đối tượng lớp nút

```csharp
// Khởi tạo đối tượng lớp Node
Node cubeNode = new Node("cube");
```

## Bước 3: Tạo lưới bằng Polygon Builder

```csharp
// Gọi Lớp chung tạo lưới bằng phương pháp xây dựng đa giác để đặt phiên bản lưới
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
```

## Bước 4: Nút trỏ vào hình học lưới

```csharp
// Nút điểm vào hình học Lưới
cubeNode.Entity = mesh;
```

## Bước 5: Đặt Xoay bằng Quaternion

```csharp
// Đặt xoay
cubeNode.Transform.Rotation = Quaternion.FromRotation(new Vector3(0, 1, 0), new Vector3(0.3, 0.5, 0.1));            
```

## Bước 6: Đặt bản dịch

```csharp
// Đặt bản dịch
cubeNode.Transform.Translation = new Vector3(0, 0, 20);            
```

## Bước 7: Thêm khối vào cảnh

```csharp
// Thêm khối vào hiện trường
scene.RootNode.ChildNodes.Add(cubeNode);
```

## Bước 8: Lưu cảnh 3D

```csharp
// Đường dẫn đến thư mục tài liệu.
var output = "Your Output Directory" + "TransformationToNode.fbx";

// Lưu cảnh 3D ở các định dạng tệp được hỗ trợ
scene.Save(output, FileFormat.FBX7500ASCII);
// ExEnd:AddTransformationToNodeByQuaternion
Console.WriteLine("\nTransformation added successfully to node.\nFile saved at " + output);
```

## Phần kết luận

 Chúc mừng! Bạn đã học thành công cách chuyển đổi nút bằng quaternion trong cảnh 3D bằng cách sử dụng Aspose.3D cho .NET. Khám phá thêm các tính năng và khả năng bằng cách tham khảo[tài liệu](https://reference.aspose.com/3d/net/).

## Câu hỏi thường gặp

### Câu hỏi 1: Quaternion trong đồ họa 3D là gì?

Trả lời 1: Quaternion là các thực thể toán học được sử dụng để biểu diễn các phép quay trong không gian 3D.

### Câu hỏi 2: Làm cách nào tôi có thể tải xuống Aspose.3D cho .NET?

 A2: Bạn có thể tải xuống thư viện từ[trang phát hành](https://releases.aspose.com/3d/net/).

### Câu hỏi 3: Có bản dùng thử miễn phí dành cho Aspose.3D cho .NET không?

 Câu trả lời 3: Có, bạn có thể dùng thử miễn phí từ[đây](https://releases.aspose.com/).

### Câu hỏi 4: Tôi có thể tìm hỗ trợ cho Aspose.3D cho .NET ở đâu?

 A4: Tham quan[Diễn đàn Aspose.3D](https://forum.aspose.com/c/3d/18) để được hỗ trợ và thảo luận.

### Câu hỏi 5: Làm cách nào để có được giấy phép tạm thời cho Aspose.3D?

 A5: Nhận giấy phép tạm thời[đây](https://purchase.aspose.com/temporary-license/).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
