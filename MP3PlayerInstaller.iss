; ---------------------------------------------
; Nikhil MP3 Player Installer Script
; ---------------------------------------------

[Setup]
AppName=Nikhil MP3 Player
AppVersion=1.0
DefaultDirName={pf}\Nikhil MP3 Player
DefaultGroupName=Nikhil MP3 Player
OutputBaseFilename=mysetup
Compression=lzma
SolidCompression=yes
AllowNoIcons=yes
DisableProgramGroupPage=no
UninstallDisplayIcon={app}\mp3.exe
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Files]
; Main executable
Source: "C:\Users\Nikhil tiwari\Desktop\All stydy folder\MP3Player\dist\mp3.exe"; DestDir: "{app}"; Flags: ignoreversion

; Music folder
Source: "C:\Users\Nikhil tiwari\Desktop\All stydy folder\MP3Player\music_file\*"; DestDir: "{app}\music_file"; Flags: ignoreversion recursesubdirs

; App icon
Source: "C:\Users\Nikhil tiwari\Desktop\All stydy folder\MP3Player\icon.ico"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
; Desktop shortcut
Name: "{userdesktop}\Nikhil MP3 Player"; Filename: "{app}\mp3.exe"; IconFilename: "{app}\icon.ico"
; Start Menu shortcut
Name: "{group}\Nikhil MP3 Player"; Filename: "{app}\mp3.exe"; IconFilename: "{app}\icon.ico"

[Run]
; Launch after install
Filename: "{app}\mp3.exe"; Description: "Launch Nikhil MP3 Player"; Flags: nowait postinstall skipifsilent
