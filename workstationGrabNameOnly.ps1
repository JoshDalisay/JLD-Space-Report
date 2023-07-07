#list of Desktops starting with "DC-WMO"

Get-ADComputer -Filter 'name -like "DC-WMO*"' |
foreach Name |
Out-File -FilePath "\\log-s8mo-1fs\GROUPS\IT Support\Windows 10\Scripts\workstations.txt"

