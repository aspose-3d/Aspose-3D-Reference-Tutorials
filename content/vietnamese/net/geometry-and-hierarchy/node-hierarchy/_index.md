---
title: Tìm hiểu hệ thống phân cấp nút trong cảnh 3D
linktitle: Tìm hiểu hệ thống phân cấp nút trong cảnh 3D
second_title: API Aspose.3D .NET
description: Khai phá sức mạnh của Aspose.3D cho .NET! Đi sâu vào thao tác phân cấp nút với hướng dẫn từng bước này. Tạo cảnh 3D tuyệt đẹp một cách dễ dàng.
type: docs
weight: 16
url: /vi/net/geometry-and-hierarchy/node-hierarchy/
---
## Giới thiệu

Chào mừng bạn đến với thế giới của Aspose.3D cho .NET, một thư viện mạnh mẽ cho phép các nhà phát triển làm việc liền mạch với các cảnh và mô hình 3D trong ứng dụng .NET của họ. Trong hướng dẫn này, chúng ta sẽ đi sâu vào sự phức tạp của việc tìm hiểu hệ thống phân cấp nút trong cảnh 3D bằng cách sử dụng Aspose.3D. Đến cuối hướng dẫn này, bạn sẽ nắm vững cách thao tác cấu trúc của cảnh 3D thông qua các nút, cho phép bạn tạo ra trải nghiệm hình ảnh tuyệt đẹp.

## Điều kiện tiên quyết

Trước khi chúng ta bắt tay vào hành trình 3D này, hãy đảm bảo bạn có sẵn các điều kiện tiên quyết sau:

-  Aspose.3D for .NET Library: Đảm bảo rằng bạn đã tích hợp thư viện Aspose.3D vào dự án .NET của mình. Nếu bạn chưa làm điều này, hãy đến[tài liệu](https://reference.aspose.com/3d/net/) để được hướng dẫn.

-  Tải xuống Thư viện: Nếu bạn chưa tải xuống thư viện Aspose.3D, hãy lấy phiên bản mới nhất từ[Liên kết tải xuống](https://releases.aspose.com/3d/net/)và làm theo hướng dẫn cài đặt được cung cấp trong tài liệu.

- Nhận giấy phép: Để mở khóa toàn bộ tiềm năng của Aspose.3D, bạn cần có giấy phép hợp lệ. Nếu bạn không có, bạn có thể lấy nó[đây](https://purchase.aspose.com/buy) hoặc chọn một[dùng thử miễn phí](https://releases.aspose.com/) để khám phá khả năng của nó.

-  Hỗ trợ và Cộng đồng: Tham gia cộng đồng Aspose.3D trên[diễn đàn hỗ trợ](https://forum.aspose.com/c/3d/18)để kết nối với các nhà phát triển khác, tìm kiếm trợ giúp và cập nhật những phát triển mới nhất.

-  Giấy phép tạm thời (Tùy chọn): Nếu bạn đang khám phá Aspose.3D trước khi mua hàng, hãy cân nhắc việc lấy giấy phép[giấy phép tạm thời](https://purchase.aspose.com/temporary-license/) để truy cập mở rộng.

Bây giờ chúng ta đã chuẩn bị sẵn các công cụ, hãy cùng đi sâu vào thế giới thú vị của thao tác phân cấp nút 3D bằng Aspose.3D.

## Nhập không gian tên

Trong dự án .NET của bạn, hãy đảm bảo bạn nhập các vùng tên cần thiết để tận dụng chức năng do Aspose.3D cung cấp. Thêm các dòng sau vào mã của bạn:

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

Những không gian tên này sẽ cung cấp cho bạn quyền truy cập vào các lớp và phương thức cần thiết để làm việc với cảnh 3D.

## Bước 1: Khởi tạo đối tượng cảnh

```csharp
Scene scene = new Scene();
```

 Bắt đầu bằng cách tạo cảnh 3D mới bằng cách sử dụng`Scene` lớp học.

## Bước 2: Tạo nút con

```csharp
Node top = scene.RootNode.CreateChildNode();
Node cube1 = top.CreateChildNode("cube1");
Node cube2 = top.CreateChildNode("cube2");
```

 Thiết lập cấu trúc phân cấp bằng cách tạo mối quan hệ cha-con giữa các nút. Trong ví dụ này,`cube1` Và`cube2` là các nút con của`top` nút.

## Bước 3: Tạo và gán lưới

```csharp
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
cube1.Entity = mesh;
cube2.Entity = mesh;
```

 Tạo lưới bằng phương pháp phù hợp (ở đây,`CreateMeshUsingPolygonBuilder`) và gán nó cho các nút con.

## Bước 4: Đặt bản dịch

```csharp
cube1.Transform.Translation = new Vector3(-10, 0, 0);
cube2.Transform.Translation = new Vector3(10, 0, 0);
```

Xác định các bản dịch cho từng nút khối, định vị chúng trong không gian 3D.

## Bước 5: Áp dụng Xoay cho nút gốc

```csharp
top.Transform.Rotation = Quaternion.FromEulerAngle(Math.PI, 4, 0);
```

Xoay nút cha (`top`) và quan sát sự chuyển đổi này ảnh hưởng như thế nào đến tất cả các nút con của nó.

## Bước 6: Lưu cảnh 3D

```csharp
string output = "Your Output Directory" + "NodeHierarchy.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

Chỉ định thư mục đầu ra và lưu cảnh 3D ở định dạng tệp mong muốn (ở đây là FBX7500ASCII).

## Bước 7: Hiển thị thông báo thành công

```csharp
Console.WriteLine("\nNode hierarchy added successfully to document.\nFile saved at " + output);
```

Thông báo cho người dùng về việc bổ sung thành công hệ thống phân cấp nút và vị trí tệp đã lưu.

## Phần kết luận

Chúc mừng! Bạn đã điều hướng thành công thế giới phức tạp của hệ thống phân cấp nút 3D trong Aspose.3D cho .NET. Hướng dẫn này đã trang bị cho bạn kiến thức để tạo, thao tác và lưu cảnh 3D một cách dễ dàng. Khi bạn tiếp tục hành trình của mình, hãy khám phá nhiều tính năng hơn và phát huy toàn bộ tiềm năng của Aspose.3D trong các dự án .NET của bạn.

## Câu hỏi thường gặp

### Câu hỏi 1: Tôi có thể sử dụng Aspose.3D cho .NET mà không cần giấy phép không?

Câu trả lời 1: Mặc dù giấy phép mở khóa tất cả các tính năng nhưng bạn có thể khám phá Aspose.3D với các khả năng hạn chế bằng bản dùng thử miễn phí.

### Câu hỏi 2: Có định dạng tệp nào khác được hỗ trợ để lưu cảnh 3D không?

Câu trả lời 2: Có, Aspose.3D hỗ trợ nhiều định dạng khác nhau; tham khảo tài liệu để có danh sách đầy đủ.

### Câu 3: Làm cách nào tôi có thể đóng góp cho cộng đồng Aspose.3D?

Câu trả lời 3: Tham gia diễn đàn hỗ trợ, chia sẻ trải nghiệm của bạn và đóng góp bằng cách giúp đỡ người khác giải đáp các thắc mắc của họ.

### Câu hỏi 4: Aspose.3D có phù hợp để phát triển trò chơi không?

A4: Chắc chắn rồi! Aspose.3D rất linh hoạt và có thể được tích hợp vào các dự án phát triển trò chơi.

### Câu hỏi 5: Sự khác biệt giữa giấy phép tạm thời và giấy phép đầy đủ là gì?

Câu trả lời 5: Giấy phép tạm thời cung cấp quyền truy cập ngắn hạn cho mục đích đánh giá, trong khi giấy phép đầy đủ cung cấp quyền sử dụng không hạn chế.