git init
git config user.email "lakipop@example.com"
git config user.name "Lakindu"

$files = Get-ChildItem -File -Recurse | Where-Object { $_.FullName -notmatch '\\\.git\\' }

foreach ($file in $files) {
    git add "$($file.FullName)"
    git commit -m "Add $($file.Name)"
}
