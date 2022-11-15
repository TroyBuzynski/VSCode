param(
    [Parameter(Mandatory=$True)]
    $path
)
$timestamp = Get-Date -Format o | ForEach-Object { $_ -replace ":", "." }

# Search recursively, delete all .txt files, create a log of deleted files
try{
    $files = Get-ChildItem -Path $path -Recurse -Force | 
                 Where-Object { !$_.PSIsContainer -and $_.Name -like "*.txt" } |
                 Select-Object -ExpandProperty FullName
    if ($null -ne $files){
        if (!(Test-Path -Path $path\_Purged)) {New-Item -ItemType "directory" -Path $path\_Purged}
        $files |  
            Set-Content -Path $path\_Purged\purged_files_$timestamp.log -PassThru  |
            Remove-Item -Force
    }
}
catch {
    Write-Output "Error Occurred"
    Write-Output $_.ScriptStackTrace
}

#Delete any empty directories left behind after deleting the files.
Get-ChildItem -Path $path -Recurse -Force | 
   Where-Object { $_.PSIsContainer -and (Get-ChildItem -Path $_.FullName -Recurse -Force | Where-Object { !$_.PSIsContainer }) -eq $null } | 
   Select-Object -ExpandProperty FullName | 
   Remove-Item -Force -Recurse