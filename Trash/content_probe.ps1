

# Load WinSCP .NET assembly
Add-Type -Path "C:\Program Files (x86)\WinSCP\WinSCPnet.dll"

# Set up session options
$sessionOptions = New-Object WinSCP.SessionOptions -Property @{
    Protocol = [WinSCP.Protocol]::Sftp
    HostName = "datadrop.admin.uni.edu"
    UserName = "drop-imaging"
    SshHostKeyFingerprint = "ssh-rsa 2048 mjNRceUcElSEAVoe0XFF33VjFqcZ6ACR6v01k75krvI"
    SshPrivateKeyPath = "C:\ProgramData\ssh\drop-imaging@datadrop.ppk"
}

$session = New-Object WinSCP.Session
$path = "/local/home/drop_users/drop-imaging/New folder"
try
{
    # Connect
    $session.Open($sessionOptions)

    $directory = $session.ListDirectory($path)
    
    foreach ($fileInfo in $directory.Files)
    {
        Write-Host ("$($fileInfo.Name) - Size: $($fileInfo.Length), " +
            "Last_Modification: $($fileInfo.LastWriteTime), " +
            "Owner: $($fileInfo.Owner)")
    }
}
finally
{
    $session.Dispose()
}
