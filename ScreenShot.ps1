[Reflection.Assembly]::LoadWithPartialName("System.Drawing")
function screenshot([Drawing.Rectangle]$bounds, $path) {
   $bmp = New-Object Drawing.Bitmap $bounds.width, $bounds.height
   $graphics = [Drawing.Graphics]::FromImage($bmp)

   $graphics.CopyFromScreen($bounds.Location, [Drawing.Point]::Empty, $bounds.size)

   $bmp.Save($path)

   $graphics.Dispose()
   $bmp.Dispose()
}

[System.Windows.Forms.SendKeys]::SendWait("%{TAB}")
$bounds = [Drawing.Rectangle]::FromLTRB(0, 0, 1000, 900)
For ($i=0; $i -le 1000; $i++) {
    sleep 1
    $bounds = [Drawing.Rectangle]::FromLTRB(0, 0, 1600, 900)
    screenshot $bounds ("D:\SS\screenshot" + ($i -as [string]) + ".png")
    [System.Windows.Forms.SendKeys]::SendWait("^{PGDN}")
    echo $i
}