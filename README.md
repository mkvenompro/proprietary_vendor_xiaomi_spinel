# Proprietary Vendor لـ Redmi Note 15 4G (spinel)

> **Proprietary blobs** لـ Redmi Note 15 4G (spinel) مستمدة من نسخة الـ stock الرسمية لـ Android 15 (HyperOS 2.2) OS2.0.212.0.VPGMIXM.

## محتويات الـ repository

```
proprietary_vendor_xiaomi_spinel/
├── .github/
│   └── workflows/
│       └── build-vendor.yml          # workflow بناء الـ vendor tree
├── proprietary/
│   ├── BoardConfigVendor.mk          # AB_OTA_PARTITIONS لأقساط الـ bootloader
│   ├── tanzanite-vendor.mk          # PRODUCT_COPY_FILES و soong namespaces
│   ├── Android.mk                   # (إن وجدت)
│   ├── Android.bp                   # (إن وجدت)
│   ├── .gitattributes               # إعدادات Git LFS لأقساط الـ bootloader
│   ├── proprietary/                 # ملفات الـ blob الأخرى (من dump)
│   └── radio/
│       ├── Android.mk               # $(call add-radio-file-sha1-checked,...)
│       ├── dpm.img
│       ├── gz.img
│       ├── lk.img
│       ├── mcupm.img
│       ├── md1img.img
│       ├── pi_img.img
│       ├── preloader_raw.img
│       ├── scp.img
│       ├── spmfw.img
│       ├── sspm.img
│       └── tee.img
└── README.md
```

## كيف تعمل؟

1. **تنزيل ROM الـ stock Fastboot** (OS2.0.212.0.VPGMIXM) من:
   ```
   https://bigota.d.miui.com/OS2.0.212.0.VPGMIXM/spinel_global_images_OS2.0.212.0.VPGMIXM_20260311.0000.00_15.0_global_1e7d24d317.tgz
   ```

2. **استخراج أقساط الـ bootloader** من ROM الـ stock:
   - `lk.img` (lk_fenrir.img)
   - `preloader_raw.img` (preloader_spinel.bin)
   - `scp.img`
   - `spmfw.img`
   - `sspm.img`
   - `mcupm.img`
   - `pi_img.img`
   - `dpm.img`
   - `gz.img`

3. **دمج الـ blobs الأخرى** من GitLab dump:
   - `https://gitlab.com/mkpromvp/dumber-2-mk`
   - الـ dump SHA: `51a7d8118db68c9caca33756452bde31f61b9552`

4. **إنشاء الـ makefile** تلقائياً:
   - `BoardConfigVendor.mk`
   - `tanzanite-vendor.mk`
   - `Android.mk` (للـ radio)
   - `.gitattributes` (لأقساط الـ LFS)

## تشغيل الـ workflow

يمكنك تشغيل الـ workflow يدوياً:

1. انتقل إلى: https://github.com/mkvenompro/proprietary_vendor_xiaomi_spinel/actions
2. اختر workflow: "بناء شجرة الـ vendor من ROM الـ stock لـ VPGMIXM"
3. أدخل القيم المطلوبة (أو استخدم الافتراضية)
4. انقر على "Run workflow"

## دمجه مع LineageOS

في ملف `device.mk` للـ device tree (`android_device_xiaomi_spinel`):

```makefile
$(call inherit-product, vendor/xiaomi/spinel/tanzanite-vendor.mk)
```

ثم أضف إلى `BoardConfig.mk`:

```makefile
-include vendor/xiaomi/spinel/BoardConfigVendor.mk
```

## المراجع

- **tanzanite**: https://github.com/nathanzerogarage/proprietary_vendor_xiaomi_tanzanite
  - البنية المستخدمة كمرجع
- **Android 15 stock**: OS2.0.212.0.VPGMIXM (Redmi Note 15 4G Global)

## التواصل

- **المطور**: mkvenompro
- **الرخصة**: Apache 2.0
- **الدعم**: افتح issue إذا واجهت أي مشاكل
