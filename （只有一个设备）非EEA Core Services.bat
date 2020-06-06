:begin
::@set/p Y=请输入设备名称:(adb devices)
@set bao1=com.google.android.gms.policy_sidecar_aps
@set bao2=com.google.android.configupdater
@set bao3=com.google.android.gms
@set bao4=com.google.android.backuptransport
@set bao5=com.google.android.feedback
@set bao6=com.google.android.onetimeinitializer
@set bao7=com.google.android.partnersetup
@set bao8=com.google.android.apps.restore
@set bao9=com.google.android.gsf
@set bao10=com.google.android.setupwizard
::@set bao11=com.google.android.gms.policy_sidecar_aps
@set bao12=com.google.android.calendar
@set bao13=com.google.android.syncadapters.contacts
@set bao14=com.google.android.webview
@set bao15=com.google.android.tts
@set bao16=com.google.android.packageinstaller
@set bao17=com.google.android.ext.services
@set bao18=com.google.android.ext.shared
@set bao19=com.google.android.printservice.recommendation
@set bao20=com.google.android.maps.jar
@set bao21=com.google.android.media.effects.jar
::Additional Core Services for Android Go Devices
@set bao22=com.google.android.apps.speechservices
@set bao23=com.google.android.inputmethod.latin
@set bao24=com.google.android.apps.navlite
@echo off
echo=
echo 检查此包%bao1%
adb shell "pm list packages | grep "%bao1%""
echo=
echo 检查此包%bao2%
adb shell "pm list packages | grep "%bao2%"" 
echo=
echo 检查此包%bao3%
adb shell "pm list packages | grep "%bao3%"" 
echo=
echo 检查此包%bao4%
adb shell "pm list packages | grep "%bao4%"" 
echo=
echo 检查此包%bao5%
adb shell "pm list packages | grep "%bao5%"" 
echo=
echo 检查此包%bao6%
adb shell "pm list packages | grep "%bao6%"" 
echo=
echo 检查此包%bao7%
adb shell "pm list packages | grep "%bao7%"" 
echo=
echo 检查此包%bao8%
adb shell "pm list packages | grep "%bao8%"" 
echo=
echo 检查此包%bao9%
adb shell "pm list packages | grep "%bao9%"" 
echo=
echo 检查此包%bao10%
adb shell "pm list packages | grep "%bao10%"" 
::echo=
::echo 检查此包%bao11%
::adb shell "pm list packages | grep "%bao11%"" 
echo=
echo 检查此包%bao12%
adb shell "pm list packages | grep "%bao12%""
echo=
echo 检查此包%bao13%
adb shell "pm list packages | grep "%bao13%"" 
echo=
echo 检查此包%bao14%
adb shell "pm list packages | grep "%bao14%"" 
echo=
echo 检查此包%bao15%
adb shell "pm list packages | grep "%bao15%"" 
echo=
echo 检查此包%bao16%
adb shell "pm list packages | grep "%bao16%"" 
echo=
echo 检查此包%bao17%
adb shell "pm list packages | grep "%bao17%"" 
echo=
echo 检查此包%bao18%
adb shell "pm list packages | grep "%bao18%"" 
echo=
echo 检查此包%bao19%
adb shell "pm list packages | grep "%bao19%"" 
echo=
echo 检查此包%bao20%
adb shell "pm list packages | grep "%bao20%"" 
echo=
echo 检查此包%bao21%
adb shell "pm list packages | grep "%bao21%"" 
echo=
echo=
echo=
echo 【Additional Core Services for Android Go Devices】
echo=
echo 检查此包%bao22%
adb shell "pm list packages | grep "%bao22%"" 
echo=
echo 检查此包%bao23%
adb shell "pm list packages | grep "%bao23%"" 
echo=
echo 检查此包%bao24%
adb shell "pm list packages | grep "%bao24%"" 
echo=
echo.
:next
pause