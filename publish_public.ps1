# publish_public.ps1
# Script para sincronizar el trabajo de 'main' (Lab) al Portafolio Público (GitHub)

$ErrorActionPreference = "Stop"

Write-Host "[*] Iniciando sincronización de Portafolio..." -ForegroundColor Cyan

# 0. Asegurar que estamos en main
if ((git branch --show-current) -ne "main") {
    Write-Error "Error: Debes ejecutar este script desde la rama 'main'."
    exit
}

# 1. Asegurar que todo está guardado
$status = git status --porcelain
if ($status) {
    Write-Error "Error: Tienes cambios sin guardar en 'main'. Haz commit antes de publicar."
    exit
}

Write-Host "[*] Subiendo todo a GitLab (Privado)..."
git push gitlab main

# 2. Resetear la rama pública para asegurar limpieza total
Write-Host "[*] Preparando rama 'public'..."

# Verificar si existe y borrarla limpiamente
if (git show-ref --verify --quiet refs/heads/public) {
    git branch -D public
}
git checkout -b public

# Verificar que estamos en la rama correcta antes de borrar nada
if ((git branch --show-current) -ne "public") {
    Write-Error "FATAL: Fallo al cambiar a la rama 'public'. Abortando para proteger 'main'."
    exit
}

# 3. Limpieza de seguridad técnica (Eliminar archivos que no pertenecen a GitHub)
Write-Host "[*] Aplicando filtros de seguridad..." -ForegroundColor Yellow

# Forzar eliminación de carpetas y archivos sensibles
# Usamos -r -f --cached para asegurar que se vayan del índice
git rm -r -f --cached tests/ 2>$null
git rm -f --cached .gitlab-ci.yml 2>$null
git rm -r -f --cached src/payload/ 2>$null

# 4. Crear placeholder para payload
$placeholder = "src/payload/README.md"
if (-not (Test-Path $placeholder)) {
    New-Item -Path $placeholder -Value "# Restricted Content`n`nThe original source code for the payload component has been removed from this public repository for security and ethical reasons.`n`nThis component is available only in the private research laboratory environment." -Force | Out-Null
}
git add -f $placeholder

# 5. Confirmar limpieza y subir
git add .
git commit -m "docs: release update to public portfolio" --allow-empty
Write-Host "[*] Subiendo a GitHub (Público)..." -ForegroundColor Green
git push origin public:main --force

# 6. Volver al laboratorio
Write-Host "[*] Volviendo a la rama 'main' (Lab)..."
git checkout main

Write-Host "[🎉] ¡Portafolio actualizado con éxito!" -ForegroundColor Green