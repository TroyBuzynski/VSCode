
#Set the $parentDir to the directory to be searched through
$parentDir = '\\devimgprocas2.imaging.uni.edu\e$\Autofill'

#Folder to store empty files and logs
$emptyFilesDir = "\\devimgprocas2.imaging.uni.edu\e$\Empty_Files"
$dateTime = Get-Date -Format FileDateTime
$newBatchDir = "$emptyFilesDir\$dateTime"
#Testing if the folder already exists
if (!(Test-Path -Path $emptyFilesDir)) {New-Item -ItemType "directory" -Path $emptyFilesDir}
New-Item -ItemType "directory" -Path $newBatchDir

#Looks through the $parentDir, moves all the empty text files to the newBatchDir, creates a log of the moved items.
Get-ChildItem -Path "$parentDir" -Depth 1 | 
    Where-Object { ($_.PSIsContainer -eq $false) -and ($_.Length -eq 0) -and ($_.Name -like "*.txt") } | 
    Select-Object -ExpandProperty FullName | Set-Content -Path $newBatchDir\_EmptyFiles_Log.txt -PassThru |
    Move-Item -Destination $newBatchDir -Include *.txt -Force