$ErrorActionPreference = "SilentlyContinue"
Remove-Item -Force .git/index.lock

$files = git ls-files --others --exclude-standard
foreach ($file in $files) {
    if (Test-Path $file -PathType Leaf) {
        # Retry loop for git add
        $retry = 0
        while ($retry -lt 5) {
            git add "$file"
            if ($LASTEXITCODE -eq 0) { break }
            Start-Sleep -Milliseconds 500
            $retry++
        }

        # Retry loop for git commit
        $retry = 0
        while ($retry -lt 5) {
            git commit -m "Add $(Split-Path $file -Leaf)"
            if ($LASTEXITCODE -eq 0) { break }
            Start-Sleep -Milliseconds 500
            $retry++
        }
    }
}

git push origin master
