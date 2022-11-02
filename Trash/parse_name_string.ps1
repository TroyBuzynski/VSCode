#Programmer: Troy Buzynski
#The script writes all the file names in the given directory to a .txt file.


$directory = 'H:\AIMG-362\PDF_Reports_2213_final'
$file_out = "H:\AIMG-362\myfile.txt"

$directory | Get-ChildItem | Select-Object -Property Name   | Out-File -FilePath $file_out 


