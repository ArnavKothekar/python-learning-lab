param(
    [Parameter(Mandatory=$true)]
    [ValidateSet('open','close')]
    [string]$Action
)

$activatePath = Join-Path $PSScriptRoot '.venv\Scripts\Activate.ps1'

switch ($Action) {
    'open' {
        if (Test-Path $activatePath) {
            Write-Host 'Activating virtual environment...'
            . $activatePath
        } else {
            Write-Error "Activation script not found at: $activatePath"
        }
        break
    }

    'close' {
        if (Get-Command deactivate -ErrorAction SilentlyContinue) {
            Write-Host 'Deactivating virtual environment...'
            deactivate
        } else {
            Write-Warning 'No active virtual environment was found in this shell.'
        }
        break
    }
}