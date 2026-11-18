# pairwise-lightmap-atlas

烘焙完的场景在墙角出现黑边、不同光照级别接缝发亮、移动端漏光：UV 展开按模型包围盒；chart 间距固定 2 像素；纹素密度按面积平均；烘焙分辨率不随光照重要度；接缝 padding 用复制边缘；光照贴图采样用双线性但没 clamp；方向光和自发光共用一张图；多场景烘焙不清理旧图；GPU 烘焙和 CPU 结果不一致；移动端压缩格式丢精度。render/lightmap_bake.py 是核心，tests/test_lightmap_bake.py 15个红。要修的是：按曲率展开；按纹素密度设间距；重要度分配分辨率；接缝 padding 扩张；边界 clamp；分层光照图；清理旧图；统一烘焙后端；压缩误差补偿；移动端 fallback。

## 运行

```bash
python -m pytest tests -q
```

初始状态：15 个用例失败。修复实现使全部用例通过，不要修改 `tests/` 下的测试。

子方向：图形渲染；任务类型：Bugfix；语言/框架：Python 3, pytest；环境可复现等级：无外部依赖。
