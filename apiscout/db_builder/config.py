DEFAULT_FOLDERS = [
    "C:\\Windows\\system32",
    "C:\\Windows\\SysWOW64",
    "C:\\Windows\\WinSxS",
    "C:\\Program Files\\Common Files"
]

# populated from a personal experience and win7's explorer.exe imports
# filename comparison in DatabaseBuilder is case-insensitive
DLL_FILTER = [
    "ActionCenter.dll",
    "actxprxy.dll",
    "advapi32.dll",
    "AltTab.dll",
    "apisetschema.dll",
    "apphelp.dll",
    "APPHELP.DLL",
    "atl.dll",
    "AudioSes.dll",
    "authui.dll",
    "avrt.dll",
    "batmeter.dll",
    "bcrypt.dll",
    "bcryptprimitives.dll",
    "cfgmgr32.dll",
    "clbcatq.dll",
    "comctl32.dll",
    "comdlg32.dll",
    "comres.dll",
    "credssp.dll",
    "credui.dll",
    "crypt32.dll",
    "cryptbase.dll",
    "cryptnet.dll",
    "cryptsp.dll",
    "cryptui.dll",
    "cscapi.dll",
    "cscdll.dll",
    "cscobj.dll",
    "cscui.dll",
    "davclnt.dll",
    "davhlpr.dll",
    "devobj.dll",
    "devrtl.dll",
    "dhcpcsvc6.dll",
    "dhcpcsvc.dll",
    "dnsapi.dll",
    "drprov.dll",
    "dsrole.dll",
    "dui70.dll",
    "duser.dll",
    "dwmapi.dll",
    "DXP.dll",
    "eappprxy.dll",
    "EhStorAPI.dll",
    "EhStorShell.dll",
    "es.dll",
    "ExplorerFrame.dll",
    "framedynos.dll",
    "FXSAPI.dll",
    "FXSST.dll",
    "gameux.dll",
    "gdi32.dll",
    "gdiplus.dll",
    "gpapi.dll",
    "hcproviders.dll",
    "hgcpl.dll",
    "hid.dll",
    "hnetcfg.dll",
    "IconCodecService.dll",
    "ieframe.dll",
    "ieproxy.dll",
    "iertutil.dll",
    "ifsutil.dll",
    "imagehlp.dll",
    "imageres.dll",
    "imapi2.dll",
    "imm32.dll",
    "iphlpapi.dll",
    "IPHLPAPI.dll",
    "kernel32.dll",
    "KernelBase.dll",
    "linkinfo.dll",
    "lpk.dll",
    "mfc42.dll",
    "mfc42u.dll",
    "midimap.dll",
    "MMDevAPI.dll",
    "mpr.dll",
    "msacm32.dll",
    "msasn1.dll",
    "msctf.dll",
    "msftedit.dll",
    "msi.dll",
    "msiltcfg.dll",
    "msimg32.dll",
    "msls31.dll",
    "mssprxy.dll",
    "msutb.dll",
    "msvcp60.dll",
    "msvcr100.dll",
    "msvcr110.dll",
    "msvcr120.dll",
    "msvcr130.dll",
    "msvcr140.dll",
    "msvcr150.dll",
    "msvcr160.dll",
    "msvcr70.dll",
    "msvcr80.dll",
    "msvcr90.dll",
    "msvcrt.dll",
    "mswsock.dll",
    "msxml6.dll",
    "ncrypt.dll",
    "nddeapi.dll",
    "ndisnpp.dll",
    "netapi32.dll",
    "netplwiz.dll",
    "netprofm.dll",
    "netshell.dll",
    "netutils.dll",
    "networkexplorer.dll",
    "nlaapi.dll",
    "npmproxy.dll",
    "npptools.dll",
    "nsi.dll",
    "ntdll.dll",
    "ntlanman.dll",
    "ntmarta.dll",
    "ntshrui.dll",
    "ole32.dll",
    "oleacc.dll",
    "oleaut32.dll",
    "opengl32.dll",
    "pnidui.dll",
    "powrprof.dll",
    "prnfldr.dll",
    "profapi.dll",
    "propsys.dll",
    "provsvc.dll",
    "psapi.dll",
    "QAGENT.dll",
    "QUTIL.dll",
    "rasadhlp.dll",
    "rasman.dll",
    "rpcrt4.dll",
    "RpcRtRemote.dll",
    "rsaenh.dll",
    "rtutils.ddll",
    "samcli.dll",
    "samlib.dll",
    "sechost.dll",
    "secur32.dll",
    "sensapi.dll",
    "SensApi.dll",
    "setupapi.dll",
    "shacct.dll",
    "shdocvw.dll",
    "shell32.dll",
    "shlwapi.dll",
    "slc.dll",
    "SndVolSSO.dll",
    "srchadmin.dll",
    "srvcli.dll",
    "sspicli.dll",
    "stobject.dll",
    "StructuredQuery.dll",
    "sxs.dll",
    "SyncCenter.dll",
    "Syncreg.dll",
    "thumbcache.dll",
    "tiptsf.dll",
    "tquery.dll",
    "UIAnimation.dll",
    "ulib.dll",
    "untfs.dll",
    "urlmon.dll",
    "user32.dll",
    "userenv.dll",
    "usp10.dll",
    "uxtheme.dll",
    "version.dll",
    "werconcpl.dll",
    "wercplsupport.dll",
    "wer.dll",
    "wevtapi.dll",
    "winbrand.dll",
    "WindowsCodecs.dll",
    "winhttp.dll",
    "wininet.dll",
    "winmm.dll",
    "winnsi.dll",
    "winspool.drv",
    "winsta.dll",
    "wintrust.dll",
    "wkscli.dll",
    "wlanapi.dll",
    "wlanutil.dll",
    "wldap32.dll",
    "Wldap32.dll",
    "ws2_32.dll",
    "ws2help.dll",
    "wscapi.dll",
    "wscinterop.dll",
    "wshext.dll",
    "wshtcpip.dll",
    "wsock32.dll",
    "wtsapi32.dll",
    "wtsapi.dll",
    "WWanAPI.dll",
    "wwapi.dll",
    "xmllite.dll",
    "zipfldr.dll"
]