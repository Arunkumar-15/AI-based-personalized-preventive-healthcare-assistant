$pptxPath = "C:\Users\arunk\Projects\health-assistant\AI_Personalized_Preventive_Healthcare_Assistant_Presentation.pptx"
$pdfPath = "C:\Users\arunk\Projects\health-assistant\AI_Personalized_Preventive_Healthcare_Assistant_Presentation.pdf"
$downloadsPdfPath = "C:\Users\arunk\Downloads\AI_Personalized_Preventive_Healthcare_Assistant_Presentation.pdf"
$pngDir = "C:\Users\arunk\Projects\health-assistant\report_assets\presentation_slides"

if (!(Test-Path $pngDir)) {
    New-Item -ItemType Directory -Path $pngDir -Force | Out-Null
}

try {
    $ppt = New-Object -ComObject PowerPoint.Application
    # Open presentation hidden / minimized
    $pres = $ppt.Presentations.Open($pptxPath, $false, $false, $false)
    
    # Export to PDF (32 = ppSaveAsPDF)
    $pres.SaveAs($pdfPath, 32)
    Write-Host "PDF exported to: $pdfPath"
    Copy-Item -Path $pdfPath -Destination $downloadsPdfPath -Force
    Write-Host "PDF copied to Downloads: $downloadsPdfPath"
    
    # Export slides to PNG (13.33 in at 1920x1080)
    $pres.Export($pngDir, "PNG", 1920, 1080)
    Write-Host "PNG slides exported to: $pngDir"
    
    $pres.Close()
    $ppt.Quit()
} catch {
    Write-Host "Error exporting presentation: $_"
}
