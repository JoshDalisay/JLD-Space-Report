$Servers = Get-Content "\\log-s8mo-1fs\GROUPS\IT Support\Windows 10\Scripts\workstations.txt"
$Drives = "C:","D:","E:"
 
$report = @()

#Looping each server
Foreach($Server in $Servers)
{
    $Server = $Server.trim()

    #Check if server is online before proceding
    if(Test-Connection -ComputerName $Server -Quiet -Count 1 ) {

        Write-Host "Processing $Server" -ForegroundColor Green
        Try
        {
            $Disks = Get-WmiObject -Class win32_logicaldisk -ComputerName $Server -ErrorAction Stop
        }
        Catch
        {
            $_.Exception.Message
            Continue
        }    
            If(!$Disks)
            {
                Write-Warning "Something went wrong"
            }
            Else
            {
                # Adding properties to object
                $Object = New-Object PSCustomObject
                $Object | Add-Member -Type NoteProperty -Name "ServerName" -Value $Server
         
                Foreach($Letter in $Drives)
                {
                    Switch ($Letter)
                    {
                        "C:"     { $Val = "(C:)"}
                        "D:"     { $Val = "(D:)"}
                        "E:"     { $Val = "(E:)"}
                    }
 
                    $FreeSpace = ($Disks | Where-Object {$_.DeviceID -eq "$Letter"} | Select-Object @{n="FreeSpace";e={[math]::Round($_.FreeSpace/1GB,2)}}).freespace 
                    If($FreeSpace)
                    {
                        $Value = "$Freespace" + " GB"
                        $Object | Add-Member -Type NoteProperty -Name "$Val" -Value $Value   
                    }
                    Else
                    {
                        $Object | Add-Member -Type NoteProperty -Name "$Val" -Value "(not found)"
                    }
                }
                $report += $object
            }
    } 
} 


#Save results to CSV file
Write-Host "Saving Report..."
$report | Export-Csv -Path "\\log-s8mo-1fs\GROUPS\IT Support\Windows 10\Scripts\SpaceReport.csv" -NoTypeInformation -Force
#Display results
#return $report
 