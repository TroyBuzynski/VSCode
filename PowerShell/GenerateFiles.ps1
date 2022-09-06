$path = '\\devimgprocas2.imaging.uni.edu\e$\Autofill'

<#$fileList =  @()
$i = 0
while( $i -lt 10 ) {

    $fileList += New-Item -Path $devServerPath -Name "blank_$i.txt" -ItemType "file" -Value ""
    $i+= 1

}#>


$ADM = 'Index_ADM.txt', 'Index_docs_ADM.txt'
$CIEP = 'Index_CIEP.txt', 'Index_docs_CIEP.txt'
$HRS = 'Index_HRS.txt' , 'Index_docs_HRS.txt'

$ADM | ForEach-Object -Process {
   New-Item -Path "$path\Admissions" -Name "$_" -ItemType "file" -Value ""}
   
$CIEP | ForEach-Object -Process {
    New-Item -Path "$path\CIEP" -Name "$_" -ItemType "file" -Value ""}

$HRS | ForEach-Object -Process {
    New-Item -Path "$path\HRS_PAF" -Name "$_" -ItemType "file" -Value ""}