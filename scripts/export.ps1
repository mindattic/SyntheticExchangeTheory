#Requires -Version 5.1
<#
.SYNOPSIS
    Exports the dissertation through the shared MindAttic.Export library.

.DESCRIPTION
    Reads export.json (title page, sources, output folder, formats) and writes a versioned bundle
    "SET V<N>.{txt,md,docx,pdf}" plus description.txt and keywords.txt into
    D:\Projects\MindAttic\ePub\MindAttic\SET\. The previous bundle is archived into
    Archives\v<N>\ first (archive, never delete).

.EXAMPLE
    powershell -File scripts\export.ps1
    powershell -File scripts\export.ps1 -Formats pdf,docx
#>
param([string]$Formats = '')

$ErrorActionPreference = 'Stop'
$repo = Split-Path $PSScriptRoot -Parent
$cli = Join-Path $repo '..\MindAttic.Export\MindAttic.Export.Cli'
if (-not (Test-Path $cli)) { throw "MindAttic.Export not found beside this repo: $cli" }

$cliArgs = @('--config', (Join-Path $repo 'export.json'))
if ($Formats) { $cliArgs += @('--formats', $Formats) }
dotnet run --project $cli -c Release -v q -- @cliArgs
exit $LASTEXITCODE
