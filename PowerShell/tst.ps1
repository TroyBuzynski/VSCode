$myObj = [PSCustomObject] @{ 
    path = "H:\ScriptTesting"
    prop1 = 'Hello'
    prop2 = 'GoodBye!!!'


}
$myObj | Get-Member


$users = @{
    bobt = 'Bob Tiger'
    joeb = 'Joe Bob'
}

$users.GetHashCode()

Get-help -Online Clear-Content
Get-WindowsOptionalFeature -FeatureName





