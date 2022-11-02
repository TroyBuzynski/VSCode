#Set the $parentDir to the directory to be searched through
$parentDir = "[SomePath]"

#Folder to store empty files and logs
$emptyFilesDir = "[SomePath]"
$dateTime = Get-Date -Format FileDateTime
$newBatchDir = "$emptyFilesDir\$dateTime"
#Testing if the folder already exists
if (!(Test-Path -Path $emptyFilesDir)) {New-Item -ItemType "directory" -Path $emptyFilesDir}
New-Item -ItemType "directory" -Path $newBatchDir

#Looks through the $parentDir, moves all the empty text files to the newBatchDir, creates a log of the moved items.
Get-ChildItem -Path "$parentDir" -Depth 1 | 
    Where-Object { ($_.PSIsContainer -eq $false) -and ($_.Length -le 1) -and ($_.Name -like "*.txt") } | 
    Select-Object -ExpandProperty FullName | Set-Content -Path $newBatchDir\_EmptyFiles.log  -PassThru |
    Move-Item -Destination $newBatchDir -Include *.txt -Force