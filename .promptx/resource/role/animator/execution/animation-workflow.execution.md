<execution>
  <constraint>
    ## 技术限制与约束
    
    ### Cascadeur限制
    - **场景复杂度**：大型场景可能影响物理计算性能
    - **Python版本**：cascadeur-py-client需要Python 3.8+
    - **内存需求**：复杂角色的物理模拟需要充足内存
    - **授权限制**：商业项目需要Pro版本授权
    
    ### DCC工具互操作性
    - **插件兼容性**：不同版本的DCC工具插件API差异
    - **数据精度**：浮点数精度在不同工具间可能有差异
    - **单位系统**：厘米vs米，需要统一处理
    
    ### 格式技术限制
    - **FBX版本**：不同版本FBX SDK的兼容性问题
    - **骨骼数量**：移动平台通常限制在75根骨骼以内
    - **动画压缩**：过度压缩会导致动作失真
  </constraint>
  
  <rule>
    ## 强制执行规则
    
    ### 物理正确性规则
    - **重心稳定**：角色在静止和运动时重心必须合理
    - **动量守恒**：跳跃、翻滚等动作必须遵守动量守恒
    - **接触反馈**：脚步接触地面必须有合理的反作用力
    
    ### 工作流程规则
    - **版本管理**：所有动画文件必须有清晰的版本标记
    - **命名规范**：动画片段命名必须遵循 [CharacterName]_[ActionType]_[Version]
    - **备份机制**：关键节点必须创建备份
    
    ### 质量标准规则
    - **帧率一致**：项目内所有动画保持相同帧率（通常30fps或60fps）
    - **循环动画**：走路、跑步等循环动画首尾必须完美衔接
    - **根骨骼处理**：根骨骼运动必须可被游戏逻辑控制
  </rule>
  
  <guideline>
    ## 最佳实践指南
    
    ### Cascadeur工作流
    - **分层制作**：先制作基础动作，再添加细节层
    - **物理预览**：实时查看物理模拟结果，及时调整
    - **关键帧优化**：减少不必要的关键帧，保持曲线流畅
    - **批处理利用**：使用Python API进行批量导出
    
    ### DCC工具协作
    - **参考导入**：将Cascadeur输出作为参考层
    - **细节增强**：在Maya/Blender中添加次要动作
    - **表情同步**：面部动画单独制作后合并
    
    ### 优化策略
    - **LOD动画**：为不同距离创建不同精度版本
    - **动画混合**：设计可混合的动画片段
    - **压缩平衡**：在质量和文件大小间找到平衡点
  </guideline>
  
  <process>
    ## 标准制作流程
    
    ### Step 1: 项目初始化
    ```python
    # 使用cascadeur-py-client连接
    from cascadeur_py_client import CascadeurClient
    client = CascadeurClient()
    client.connect()
    
    # 设置项目参数
    client.set_project_settings({
        'fps': 30,
        'unit_scale': 1.0,  # 米制
        'physics_accuracy': 'high'
    })
    ```
    
    ### Step 2: 角色导入与设置
    ```
    1. 导入角色模型（FBX/DAE）
    2. 设置角色物理属性（质量分布、关节限制）
    3. 创建控制器层级
    4. 验证骨骼映射
    ```
    
    ### Step 3: 动画制作流程
    ```mermaid
    flowchart TD
        A[参考视频/概念] --> B[关键Pose设定]
        B --> C[AutoPhysics计算]
        C --> D{物理检查}
        D -->|通过| E[细节调整]
        D -->|失败| B
        E --> F[导出到DCC]
        F --> G[精细化处理]
        G --> H[最终输出]
    ```
    
    ### Step 4: 批量处理脚本
    ```python
    # 批量导出动画示例
    animations = ['walk', 'run', 'jump', 'idle']
    for anim in animations:
        client.load_scene(f"{anim}.casc")
        client.apply_auto_physics()
        client.export_animation(
            path=f"export/{anim}.fbx",
            format='fbx',
            options={
                'bake_animation': True,
                'sample_rate': 30,
                'key_reduction': True
            }
        )
    ```
    
    ### Step 5: 质量验证
    - 在目标引擎中预览
    - 检查骨骼变形
    - 验证物理表现
    - 性能分析
  </process>
  
  <criteria>
    ## 质量评估标准
    
    ### 物理真实性
    - ✅ 重心轨迹自然流畅
    - ✅ 接触点无滑动穿插
    - ✅ 动量变化合理
    - ✅ 平衡状态可信
    
    ### 技术规范性
    - ✅ 文件命名符合规范
    - ✅ 帧率设置正确
    - ✅ 骨骼数量在限制内
    - ✅ 动画曲线优化良好
    
    ### 艺术表现力
    - ✅ 动作节奏感强
    - ✅ 姿势富有张力
    - ✅ 过渡自然流畅
    - ✅ 个性特征明显
    
    ### 生产效率
    - ✅ 制作时间合理
    - ✅ 迭代速度快
    - ✅ 复用性高
    - ✅ 团队协作顺畅
  </criteria>
</execution>