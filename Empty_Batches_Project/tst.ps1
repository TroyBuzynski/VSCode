param ($dept)
$targetDir = "E:\Autofill\$dept"
$logDir = "E:\Logs\$dept"
$dateTime = Get-Date -Format FileDateTime

#Testing if the folder already exists
if (!(Test-Path -Path $logDir)) {New-Item -ItemType "directory" -Path $logDir}
New-Item -ItemType "directory" -Path $logDir\$dateTime

#Looks through the $targetDir, moves all the empty text files to the new directory labled by the dateTime, creates a log of the moved items.
Get-ChildItem -Path $targetDir  | 
    Where-Object { ($_.PSIsContainer -eq $false) -and ($_.Length -eq 0) -and ($_.Name -like "*.txt") } | 
    Select-Object -ExpandProperty FullName | Set-Content -Path $logDir\$dateTime\_EmptyFiles.log  -PassThru |
    Move-Item -Destination $logDir\$dateTime -Include *.txt -Force