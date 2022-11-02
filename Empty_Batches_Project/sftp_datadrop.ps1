<#
This script use SFTP to move files from drop-imaging@datadrop.admin.uni.edu
to E:\Autofill. It will remove all empty index files and create 
a backup directory. The the files will be made availabe for 
OnBase DIP to import. It is expected that DIP will remove the 
files after import. If DIP fails to remove the files, they will
be moved and timestamped for manual processing.
#>

# The department needs to be passed into the script when calling it from the command line
# example:  .\main.ps1 -dept [Enter the department]
param (
#an argument must be passed into the script, an argument is only valid if it belongs to the set below 
    [Parameter(Mandatory=$True)]
    [ValidateSet("Admissions", "CampusSolutions","CIEP","eBiz","Fin_Aid","Foundation",
                 "GC_Assistantships","GC_Forms","GC_Scholarships","HRS_Benefits",
                 "HRS_COMP", "HRS_PAF", "HRS_Retirement","REG_Student_Requests")]
    $dept
)

Function Move-OldItems {
<# 
This script will check if there are any files sitting in the directory where DIP runs
If there are files then the DIP schedule must have failed
The files will be moved into E:\Autofill\[department]\old to be processed manually
#>

    param ($dept)
    $localPath =  "E:\Autofill\$dept"
    $timestamp = Get-Date -Format o | ForEach-Object { $_ -replace ":", "." }

    if ((Test-Path -Path $localPath) -and $null -ne (Get-ChildItem -Path $localPath | Where-Object { !$_.PSIsContainer }) ) {  
        New-Item -ItemType "directory" -Path $localPath\old\$timestamp
        Get-ChildItem -Path $localPath |
            Where-Object {!$_.PSIsContainer} |
            Move-Item  -Destination $localPath\old\$timestamp
    }
}

Function Move-EmptyIndexFiles {
<#
This script will move all empty text files out of the target directory (not sub-directories).
Files will be placed in a log directory with a .log file
#>

   param ($dept)
   $targetDir = "E:\Autofill\$dept\sftp"
   $logDir = "E:\Logs\$dept"
   $timestamp = Get-Date -Format o | ForEach-Object { $_ -replace ":", "." }

   #Looks through the $targetDir, moves all the empty text files to the new directory labled by the timestamp, creates a log of the moved items.
    if (Test-Path -Path $targetDir) {
        $empties = Get-ChildItem -Path $targetDir  | 
                        Where-Object { ($_.PSIsContainer -eq $false) -and ($_.Length -le 1) -and ($_.Name -like "*.txt") } | 
                        Select-Object -ExpandProperty FullName 
    }
    if ($null -ne $empties){
        New-Item -ItemType "directory" -Path $logDir\$timestamp
        $empties |                
            Set-Content -Path $logDir\$timestamp\_EmptyFiles.log  -PassThru |
            Move-Item -Destination $logDir\$timestamp -Include *.txt -Force
    }

}

Function Invoke-SFTP {
#Referance: https://winscp.net/eng/docs/start
    param ($dept)
    $remotePath = "/local/home/drop_users/drop-imaging/$dept/"
    $localPath = "E:\Autofill\$dept\sftp"
    if (!(Test-Path -Path $localPath)) {New-Item -ItemType "directory" -Path $localPath}

    try {
      # Load WinSCP .NET assembly
      Add-Type -Path "C:\Program Files (x86)\WinSCP\WinSCPnet.dll"

      # Set up session options
      $sessionOptions = New-Object WinSCP.SessionOptions -Property @{
        Protocol = [WinSCP.Protocol]::Sftp
        HostName = "datadrop.admin.uni.edu"
        UserName = "drop-imaging"
        #Password = ""
        SshHostKeyFingerprint = "ssh-rsa 2048 a1:49:8e:38:59:97:94:75:21:ac:db:5f:da:45:a3:0d"
        SshPrivateKeyPath = "C:\ProgramData\ssh\drop-imaging@datadrop.ppk"
      }

      $session = New-Object WinSCP.Session

        try{
            # Connect
            $session.Open($sessionOptions)
 
            # Synchronize files to from remote directory to local directory, collect results
            $synchronizationResult = $session.SynchronizeDirectories(
                [WinSCP.SynchronizationMode]::Local, $localPath, $remotePath, $False)
 
            # Deliberately not calling $synchronizationResult.Check
            # as that would abort the script on any error.
            # We will find any error in the loop below
            # (note that $synchronizationResult.Downloads is the only operation
            # collection of SynchronizationResult that can contain any items,
            # as we are not removing nor uploading anything)
 
            # Iterate over every download
            foreach ($download in $synchronizationResult.Downloads){
                # Success or error?
                if ($Null -eq $download.Error){
                    Write-Host "Download of $($download.FileName) succeeded, removing from source"
                    # Download succeeded, remove file from source
                    $filename = [WinSCP.RemotePath]::EscapeFileMask($download.FileName)
                    $removalResult = $session.RemoveFiles($filename)
 
                    if ($removalResult.IsSuccess){
                        Write-Host "Removing of file $($download.FileName) succeeded"
                    }
                    else {
                        Write-Host "Removing of file $($download.FileName) failed"
                    }
                }
                else{
                    Write-Host (
                        "Download of $($download.FileName) failed: $($download.Error.Message)")
                }
            }
        }
        finally{
            # Disconnect, clean up
            $session.Dispose()
        }
    
    }
    catch
    {
        Write-Host "Error: $($_.Exception.Message)"
        exit 1
    }
}

Function Backup-Files {
#This function creates a backup of all the files transfered by SFTP
    param ($dept)
    $targetPath =  "E:\Autofill\$dept\sftp"
    $destinationPath = "E:\Autofill\$dept\Backup"
    $timestamp = Get-Date -Format o | ForEach-Object { $_ -replace ":", "." }

    #if there are files in the targetPath copy them to a timestamped directory 
    if ((Test-Path -Path $targetPath) -and ($null -ne (Get-ChildItem -Path $targetPath))) {
        New-Item -ItemType "directory" -Path "$destinationPath\$timestamp"
        Get-ChildItem -Path $targetPath |
            Copy-Item -Destination $destinationPath\$timestamp -Recurse
    }
}

Move-OldItems -dept $dept

Invoke-SFTP -dept $dept

Move-EmptyIndexFiles -dept $dept

Backup-Files -dept $dept

#Moves all the files to the location where DIP runs
Get-ChildItem -Path "E:\Autofill\$dept\sftp" |
    Move-Item -Destination "E:\Autofill\$dept"


