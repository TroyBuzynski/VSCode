# Set the path of the Folder to search through
$path = 'H:\ScriptTesting - Copy'
# Set the Folder to save purge logs in
$logPath = 'H:\'
# Set the length of time in days to keep files
$retention = 1300 



$limit = (Get-Date).AddDays(-$retention)
$dateTime = Get-Date -Format FileDateTime
$path = 'H:\ScriptTesting - Copy'
$logPath = 'H:\'

# Delete files older than the $limit.
Get-ChildItem -Path $path -Recurse -Force | 
    Where-Object { !$_.PSIsContainer -and $_.CreationTime -lt $limit } |
    Select-Object -ExpandProperty FullName | 
    Set-Content -Path $logPath\_purgedFiles_Log_$dateTime.txt -PassThru  |
    Remove-Item -Force

# Delete any empty directories left behind after deleting the old files.
Get-ChildItem -Path $path -Recurse -Force | 
    Where-Object { $_.PSIsContainer -and (Get-ChildItem -Path $_.FullName -Recurse -Force | Where-Object { !$_.PSIsContainer }) -eq $null } | 
    Select-Object -ExpandProperty FullName | 
    Set-Content -Path $logPath\_purgedFolders_Log_$dateTime.txt -PassThru |
    Remove-Item -Force -Recurse
