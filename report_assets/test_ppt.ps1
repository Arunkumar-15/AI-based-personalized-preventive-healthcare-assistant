try {
    $ppt = New-Object -ComObject PowerPoint.Application
    Write-Host "PowerPoint COM Success! Version: $($ppt.Version)"
    $ppt.Quit()
} catch {
    Write-Host "Error: $_"
}
