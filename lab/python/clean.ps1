# Remove not unused files and folders
Remove-Item -Path "$(Get-Location)\zap*"
if(Test-Path -Path "$(Get-Location)\zapv2" ){
   Remove-Item .\zapv2 -Recurse 
}
if(Test-Path -Path "$(Get-Location)\requests" ){
   Remove-Item .\requests -Recurse 
}