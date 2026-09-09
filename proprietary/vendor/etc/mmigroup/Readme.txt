CommonParam.json配置项说明
一、基本原则
    1.CommonParam.json是整个项目配置的汇总
    2.新添加的测试项, 优先在已有测试项上修改配置, 如lightTest可以测试各种灯光
    3.新测试条目命名, 尽量避免在之前测试项后面加数字, 如MainCamera2、mic2等, 根据实际情况使用WideCamera、submic、backmic、LeftSpeaker等
二、call标签
    该标签是配置支持的综测校准标志位, 目前已支持到5G
三、mmigroupConfig标签
    com.mmigroup.support.statusbar：是否支持虚拟键
    support_icon：桌面图标显示
    notch_height：设置界面离顶部距离（用于刘海屏和水滴屏）
    其他：字面意思, 主要是显示
四、systemConfig标签
    一些系统信息的显示开关
五、camera_match标签
    support_camera：支配匹配的摄像头, 支持2个或者2个以上的镜头匹配
    camera_id：每组匹配的镜头模组信息, equals匹配
六、audioConfig标签
    ColseTheAudioChannelWaittingTime：关闭通道等待时间
七、itemConfig标签
    所有的测试项集合
    1.other item
        VersionInfo：版本信息
        KeyPad：按键
        Vibrator：马达
        OTG：OTG测试, 支持正反插、读写
        RTC：RTC测试
        SdCard：SD卡测试, 支持读写测试
        MainSIMCard、SubSIMCard、DualSIMCard：使用的是同一个action, 根据配置测试不同项目
        Battery：有线充电测试, 支持电流、电压卡控, 支持正反插
        WirelessCharge：无线充电, 支持电流、电压卡控
        CALL112：拨打112测试, 现基本不使用
        PogoPinBattery：PogoPin充电测试
    2.audio item
        SMARTPA：SMARTPA测试, 使用新方案只需要配置spk_calibrate=fs16xx
        Speaker、Receiver、LeftSpeaker、RightSpeaker：音频播放测试, 指定播放设备
        HeadSet：耳机音频播放及耳机按键测试
        MainMic、SubMic：mic录音测试, 一般用于audio ATA测试
        MainMicToHeadPhone、HsMicToHeadPhone、HsMicToReceiver、MainMicToReceiver、MainMicToSpeaker、
    HsMicToSpeaker、SubMicToReceiver、SubMicToHeadPhone、HsMicToSpeakerLeft、HsMicToSpeakerRight、
    SubMicToSpeaker：各种回环测试, loop_type=manual_loop为回环, loop_type=manual_loop1为录播
    3.lcd tp item
        LCD、LCDCrossImg、RGBPDISP：图片测试
        LCD_R、LCD_G、LCD_B、LCD_W、LCD_BL：LCD单色测试, 一般用于ATA测试
        TouchPal：TP测试, 画满格子
        TouchPanel：TP测试, 划线, 不能断线
        MultiTouch：多指触控测试
        TpOpenShort：TP开短路测试
    4.light item
        Backlight：背光测试, 循环变动
        Backlight_dark、Backlight_half、Backlight_bright：背光测试, 指定亮度, 一般用于ATA
        LED：LED灯测试
        LED_R、LED_G、LED_B、LED_RGB：LED灯测试, 指定颜色, 多种颜色自动变化
        Flashlight：闪光灯测试
        LightTEST：灯光测试集合, 可测试单项和多项
        Infrared：红外（遥控器）
        KeyPadLight：按键灯, 基本不用
    5.camera item
        MainCamera、WideCamera、MacroCamera、DepthCamera、MainCamera_IR、FrontCamera：相机测试, 使用工模开发的相机
            "cameraId": 0,    ------  cameraID
            "support_takepicture": true,     ----- 是否支持拍照
            "support_camera_match": true,    ----- 是否支持camera匹配
            "takepicture_not_save_picture": true,     -----  拍照但不保存照片
            "auto_takepicture": false,   ----  自动拍照, 一般用于ATA
            "is_open_flashLight": true,  ----   是否打开闪光灯
            "support_cameraCheck": true,   ----- 是否支持camera防呆检测
            "support_cameraCheck_for_8bit": true   ----- 是否支持camera8bit防呆检测,使用这个配置, support_cameraCheck必须为true
        PlatMainCamera：使用平台相机测试, 目前不再使用, 仅保留一个模板
    6.wcn item
        Wlan、WlanAP、WlanAddress:wifi 测试相关
        Bluetooth、BluetoothAddress、BluetoothDevice：Bluetooth 测试相关
        GPS：GPS测试
        NFC：目前有com.mmigroup.action.NFC_ReadMode和com.mmigroup.action.NFC两个action, 建议使用前面的
        FM：FM测试
    7.sensor item
        Proximity：距感测试
        Proximity_st：距感测试包括灰黑卡测试, 一般用于sensor ATA
        Proximity_C：距感校准
        Optical：光感测试
        Optical_c：光感校准
        Accelerometer：加速度测试
        Accelerometer_C：加速度校准
        Gyroscope：陀螺仪测试
        Gyroscope_C：陀螺仪校准
        Sar：三星项目测试, 使用节点
        Sar_Manager：使用SensorManager获取测试数据
        Sar1：使用SensorManager获取测试数据,相同sensorID, 不同通道, 一般用于顶部sar
        Sar2：使用SensorManager获取测试数据,相同sensorID, 不同通道, 一般用于底部sar
        Magnetic：磁力传感器测试
        Hall：霍尔传感器测试
        Hall2：霍尔传感器测试（建议不使用, 重新定义测试项名称）
        Pressure：压力传感器
        Temperature：温度传感器（实现代码已全部删除, 使用需要重新开发）
        Orientation：方位角传感器（多个传感器合成数据, 一般不测试）
        Proximity_near_mode、Proximity_far_mode：距感靠近、远离单独测试
        fingerprint：指纹测试
八、各测试模式配置json
    MainMenuConfig.json：主界面配置json
    MainMenuConfigApk.json：独立APK主界面配置json
    CommonParam.json：整个项目配置
    MMIGroupNormal.json：mode 0, 88工模
    MMIGroupMmiManual.json：mode 1, MMI
    MMIGroupMmiAta.json：mode 2, MMI ATA
    MMIGroupPcbaManual.json：mode 3, PCBA
    MMIGroupPcbaAta.json：mode 4, PCBA ATA
    MMIGroupAudioManual.json：mode 5, 音频
    MMIGroupAudioAta.json：mode 6, 音频ATA
    MMIGroupCameraManual.json：mode 7, camera
    MMIGroupCameraAta.json：mode 8, camera ATA
    MMIGroupSensorManual.json：mode 9, sensor
    MMIGroupSensorAta.json：mode 10, sensor ATA
    MMIGroupMmiAtaManual.json：mode 11, ATA手动测试项
    MMIGroupASAutoTest.json：mode 12, 小米售后自动化
    MMIGroupADBCmdTest.json：mode 13, ??????
    MMIGroupIQC.json：mode 14, IQC LCD检测
    rdTest.json：mode 15, ??????
    customerAta.json：mode 16, ??????
    MMI2.json：mode 17, MMI2
    MMI2_ATA.json：mode 18, MMI2 ATA
    MMI2_ATA_Manual.json：mode 19, MMI2 ATA手动测试项
    MMIGroupNormalStreamline.json：mode 20, 86工模,精简的88工模
    MMIGroupMmiAtaManual2.json：mode 25, ATA手动测试项2
    SSAta.json：mode 26, 三星ATA测试项