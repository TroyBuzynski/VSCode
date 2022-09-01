$parentDir = 'H:\ScriptTesting'
$dateTime = Get-Date -Format FileDateTime
$emptyFilesDir = "$parentDir\Empty_Files"
$newBatchDir = "$emptyFilesDir\$dateTime"


if (!(Test-Path -Path $emptyFilesDir)) {New-Item -ItemType "directory" -Path $emptyFilesDir}
New-Item -ItemType "directory" -Path $newBatchDir


Get-ChildItem -Path "$parentDir" -Depth 1 | 
    Where-Object { ($_.PSIsContainer -eq $false) -and ($_.Length -eq 0) -and ($_.Name -like "*.txt") } | 
    Select-Object -ExpandProperty FullName | Set-Content -Path $newBatchDir\_EmptyFiles_Log.txt -PassThru |
    Move-Item -Destination $newBatchDir -Include *.txt -Force
     
    







<#Get-ChildItem -Path $parentDir -Depth 1 -Force | 
    Where-Object { $_.PSIsContainer -eq $false -and $_.Length -eq 0 } | 
    Select-Object -ExpandProperty FullName | 

Get-ChildItem -Path "$parentDir" -Depth 2 -Force 
Get-ChildItem -Path "$parentDir"  | Push-Location -StackName "Paths1"
Set-Location -Path H:\Code
Get-Location -Stack
Pop-Location -StackName "Paths1"#>


<#$li = @()
$obj1 = Get-ChildItem -Path $parentDir  
foreach ($childDir in $obj1) {
    $tmp = $childDir.FullName 
    Get-ChildItem -Path $tmp | 
        Where-Object { $_.PSIsContainer -eq $false -and $_.Length -eq 0 } | 
        Select-Object -ExpandProperty FullName | Set-Content -Path "$tmp\EmptyFiles_Log_$dateTime.txt" 
    if (!(Test-Path -Path "$tmp\Empty_Index_Files")) {New-Item -ItemType "directory" -Path "$tmp\Empty_Index_Files"}
    if (!(Test-Path -Path "$tmp\Empty_Index_Files\Logs")) {New-Item -ItemType "directory" -Path "$tmp\Empty_Index_Files\Logs"}
}#>

#$dateTime.GetType()

#Remove-Item -Path "$parentDir\Empty_Files-Log" -Force