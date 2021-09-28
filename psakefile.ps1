Task default -depends Build

Task Restore {
    Exec { python -m pip install --upgrade build twine }
    Set-Location src/web
    Exec { npm ci }
    Set-Location ../..
}

Task Rebuild {
    Set-Location src/web
    Write-Output "📦 Build web"

    Exec { Write-Output "{ ""commit"": ""$(git rev-parse HEAD)"", ""shortCommit"": ""$(git rev-parse --short HEAD)"", ""date"": ""$(Get-date -AsUTC -Format 'u')"" }" > ./public/build.json }

    Exec { npm run build }

    Copy-Item -Recurse ./dist ../../dist/web

    Copy-Item -Recurse ./dist ../../src/main/paperead/server/wwwroot

    Set-Location ../..

    $readme = $(Get-Childitem "README.md")[0]

    Set-Location src/main
    Write-Output "📦 Build main"

    Copy-Item $readme ./README.md
    Exec { python -m build -o ../../dist/main }
    Remove-Item ./README.md
    
    Set-Location ../..
}

Task Build -depends Restore, Rebuild

Task Deploy -depends Build {
    Exec { python -m twine upload --skip-existing --repository pypi "dist/main/*" }
}

Task Install {

    Write-Output "🛠 Install dependencies"
    if ([System.Runtime.InteropServices.RuntimeInformation]::IsOSPlatform([System.Runtime.InteropServices.OSPlatform]::Linux)) {
        Exec { sudo apt-get update >/dev/null }
    }
    elseif ([System.Runtime.InteropServices.RuntimeInformation]::IsOSPlatform([System.Runtime.InteropServices.OSPlatform]::OSX)) {
    }
    elseif ([System.Runtime.InteropServices.RuntimeInformation]::IsOSPlatform([System.Runtime.InteropServices.OSPlatform]::Windows)) {
    }

    Write-Output "🛠 Install main"

    Set-Location ./dist/main
    Exec { python -m pip install $(Get-Childitem "paperead-*.whl")[0] }

    Set-Location ../..
}

Task Uninstall {
    Write-Output "⚒ Uninstall main"

    Set-Location ./dist/main
    Exec { python -m pip uninstall $(Get-Childitem "paperead*.whl")[0] -y }

    Set-Location ../..
}

Task Demo {
    Write-Output "⏳ 1️⃣ Version ⏳"
    Exec { paperead --version }
    Write-Output "⏳ 2️⃣ Help ⏳"
    Exec { paperead --help }
}

Task Test -depends Install, Demo, Uninstall

Task Clean {
    Remove-Item -Recurse ./src/main/paperead/server/wwwroot
    # foreach ($dist in Get-Childitem ./dist) {
    #     Write-Output "🗑 Remove $dist"
    #     Remove-Item -Recurse $dist
    # }
    Remove-Item -Recurse ./dist
    foreach ($egg in Get-Childitem -Recurse *.egg-info) {
        Write-Output "🗑 Remove $egg"
        Remove-Item -Recurse $egg
    }
}

Task Format {
    autopep8 -r --in-place .

    foreach ($file in Get-Childitem "*.py" -Recurse) {
        isort $file
    }
}