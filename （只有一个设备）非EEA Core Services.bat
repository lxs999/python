:begin
::@set/p Y=�������豸����:(adb devices)
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
echo ���˰�%bao1%
adb shell "pm list packages | grep "%bao1%""
echo=
echo ���˰�%bao2%
adb shell "pm list packages | grep "%bao2%"" 
echo=
echo ���˰�%bao3%
adb shell "pm list packages | grep "%bao3%"" 
echo=
echo ���˰�%bao4%
adb shell "pm list packages | grep "%bao4%"" 
echo=
echo ���˰�%bao5%
adb shell "pm list packages | grep "%bao5%"" 
echo=
echo ���˰�%bao6%
adb shell "pm list packages | grep "%bao6%"" 
echo=
echo ���˰�%bao7%
adb shell "pm list packages | grep "%bao7%"" 
echo=
echo ���˰�%bao8%
adb shell "pm list packages | grep "%bao8%"" 
echo=
echo ���˰�%bao9%
adb shell "pm list packages | grep "%bao9%"" 
echo=
echo ���˰�%bao10%
adb shell "pm list packages | grep "%bao10%"" 
::echo=
::echo ���˰�%bao11%
::adb shell "pm list packages | grep "%bao11%"" 
echo=
echo ���˰�%bao12%
adb shell "pm list packages | grep "%bao12%""
echo=
echo ���˰�%bao13%
adb shell "pm list packages | grep "%bao13%"" 
echo=
echo ���˰�%bao14%
adb shell "pm list packages | grep "%bao14%"" 
echo=
echo ���˰�%bao15%
adb shell "pm list packages | grep "%bao15%"" 
echo=
echo ���˰�%bao16%
adb shell "pm list packages | grep "%bao16%"" 
echo=
echo ���˰�%bao17%
adb shell "pm list packages | grep "%bao17%"" 
echo=
echo ���˰�%bao18%
adb shell "pm list packages | grep "%bao18%"" 
echo=
echo ���˰�%bao19%
adb shell "pm list packages | grep "%bao19%"" 
echo=
echo ���˰�%bao20%
adb shell "pm list packages | grep "%bao20%"" 
echo=
echo ���˰�%bao21%
adb shell "pm list packages | grep "%bao21%"" 
echo=
echo=
echo=
echo ��Additional Core Services for Android Go Devices��
echo=
echo ���˰�%bao22%
adb shell "pm list packages | grep "%bao22%"" 
echo=
echo ���˰�%bao23%
adb shell "pm list packages | grep "%bao23%"" 
echo=
echo ���˰�%bao24%
adb shell "pm list packages | grep "%bao24%"" 
echo=
echo.
:next
pause