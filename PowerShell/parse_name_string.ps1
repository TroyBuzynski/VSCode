$path = 'H:\AIMG-362\PDF_Reports_2213_final'

$path | Get-ChildItem | Select-Object -Property Name   | Out-File -FilePath "H:\AIMG-362\myfile.txt" 

