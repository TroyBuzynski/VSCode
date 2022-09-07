$path = 'E:\Autofill'

$ADM = 'imaging_index.txt', 'supporting_docs_index.txt'
$CIEP = 'ciep_index.txt', 'ciep_docs_index.txt'
$HRS = 'imaging_index.txt'

$ADM | ForEach-Object -Process {
   New-Item -Path "$path\Admissions" -Name "$_" -ItemType "file" -Value ""}
   
$CIEP | ForEach-Object -Process {
    New-Item -Path "$path\CIEP" -Name "$_" -ItemType "file" -Value ""}

$HRS | ForEach-Object -Process {
    New-Item -Path "$path\HRS_PAF" -Name "$_" -ItemType "file" -Value ""}