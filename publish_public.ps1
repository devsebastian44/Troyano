# publish_public.ps1
# Script para sincronizar el trabajo de 'main' (Lab) al Portafolio Público (GitHub)

Write-Host "[*] Iniciando sincronización de Portafolio..." -ForegroundColor Cyan

# 1. Asegurar que estamos en main y todo está guardado
$status = git status --porcelain
if ($status) {
    Write-Error "Error: Tienes cambios sin guardar en 'main'. Haz commit antes de publicar."
    exit
}

Write-Host "[*] Subiendo todo a GitLab (Privado)..."
git push gitlab main

# 2. Cambiar a la rama pública (o crearla si no existe)
Write-Host "[*] Preparando rama 'public'..."
if (-not (git show-ref --verify --quiet refs/heads/public)) {
    Write-Host "Creating 'public' branch..."
    git checkout -b public
}
else {
    git checkout public
}

# 3. Fusionar cambios de main
git merge main --no-edit

# 4. Limpieza de seguridad técnica (Eliminar archivos que no pertenecen a GitHub)
Write-Host "[*] Aplicando filtros de seguridad..." -ForegroundColor Yellow
# Eliminar carpeta de tests (GitHub no necesita pruebas internas de laboratorio)
if (Test-Path tests) { git rm -r --cached tests/ -f 2>$null }

# Eliminar configuración de CI/CD de GitLab
if (Test-Path .gitlab-ci.yml) { git rm --cached .gitlab-ci.yml -f 2>$null }

# Eliminar el payload real (Malware funcional) para cumplir normas de GitHub
if (Test-Path src/payload) { 
    git rm -r --cached src/payload/ -f 2>$null 
    # Opcional: Crear un README placeholder en su lugar
    New-Item -Path src/payload/README.md -Value "Contenido removido por seguridad en la versión pública." -Force | Out-Null
    git add src/payload/README.md
}

# 5. Confirmar limpieza y subir
git add .
git commit -m "docs: release update to public portfolio" --allow-empty
Write-Host "[*] Subiendo a GitHub (Público)..." -ForegroundColor Green
git push origin public:main --force

# 6. Volver al laboratorio
Write-Host "[*] Volviendo a la rama 'main' (Lab)..."
git checkout main

Write-Host "[🎉] ¡Portafolio actualizado con éxito!" -ForegroundColor Green