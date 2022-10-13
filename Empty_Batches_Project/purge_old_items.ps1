#This script will search recursivly through the given directory and all sub-directories
#Set the path of the Folder to search through and the number of days to retain files
#These parameters can be passed into the script when calling it from the command line
# example:  .\purge_old_items.ps1 -path [Enter path] -retention [Enter number of days]
# -retention defaults to 180 days

param ( [Parameter(Mandatory=$True)] 
        $path,
        $retention = 180)


$limit = (Get-Date).AddDays(-$retention)
$timestamp = Get-Date -Format o | ForEach-Object { $_ -replace ":", "." }

if (!(Test-Path -Path $path\_Purged)) {New-Item -ItemType "directory" -Path $path\_Purged}


# Delete files older than the $limit and log the names of the purged files
Get-ChildItem -Path $path -Recurse -Force | 
    Where-Object { !$_.PSIsContainer -and $_.CreationTime -lt $limit } |
    Select-Object -ExpandProperty FullName | 
    Set-Content -Path $path\_Purged\purged_files_$timestamp.log -PassThru  |
    Remove-Item -Force

#Delete any empty directories left behind after deleting the old files.
Get-ChildItem -Path $path -Recurse -Force | 
   Where-Object { $_.PSIsContainer -and (Get-ChildItem -Path $_.FullName -Recurse -Force | Where-Object { !$_.PSIsContainer }) -eq $null } | 
   Select-Object -ExpandProperty FullName | 
   Remove-Item -Force -Recurse
