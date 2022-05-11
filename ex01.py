
import torch
import numpy as np

# 创建一个没有初始化的矩阵
# x = torch.empty(5, 3)
# print(x)

# 创建一个有初始化的矩阵
x = torch.rand(5, 3)
print(x)

# 创建一个全零的矩阵并指定数据元素的类型为long
# x = torch.zeros(5,3, dtype = torch.long)
# print(x)

# 直接通过数据创建张量
# x = torch.tensor([2.5,3.5])
# print(x)


# 通过已有的张量创建相同尺寸的新张量
# x = x.new_ones(5,3,dtype=torch.double)
# print(x)
# 利用randn_like方法得到相同尺寸张量，采用随机初始化的方法为其赋值
# y = torch.randn_like(x,dtype=torch.float64)
# print(y)


# 采用.size方法得到张量的形状
# print(x.size())
# print(y.size())

# a,b = x.size()
# print('a=',a)
# print('b=',b)


# x = torch.randn(4,4)
# y= x.view(16)
# -1处直接匹配对应值
# z=x.view(-1,8)
# print(x.size(),y.size(),z.size())
# 不能整除、数值不匹配报错
# y = x.view(12)
# z = x.view(-1,5)


# x=torch.randn(1)
# print(x)    tensor类型
# print(x.item())   python类型
# .item()方法只能提取单一值 超出会报错
# x=torch.randn(1)
# print(x)
# print(x.item())

# torch tensor和numpy array共享底层的内存空间，改变其中一个值另一个也发生改变
# a = torch.ones(5)
# print(a)
# print('---------')
# b = a.numpy()
# print(b)
# # a,b 共享内存，一起加减
# a.add(1)
# print(a)
# print(b)

# import numpy as np
#
# a = np.ones(5)
# b = torch.from_numpy(a)
# print(a)
# print(b)
#
# np.add(a,1,out=a)
# print(a)
# print(b)

if torch.cuda.is_available():
    device = torch.device("cuda")
    y = torch.ones_like(x, device=device)
    x = x.to(device)
    z = x + y
    print(z)
    print(z.to("cpu",torch.double))





