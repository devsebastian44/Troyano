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

# 2. Resetear la rama pública desde main (Para asegurar que el README y todo se actualice)
Write-Host "[*] Preparando rama 'public'..."
# Fuerza la creación/reseteo de 'public' para que sea idéntica a 'main'
git checkout -B public main

# 3. Limpieza de seguridad técnica (Archivos que NO van a GitHub)
Write-Host "[*] Aplicando filtros de seguridad..." -ForegroundColor Yellow

# Eliminar Tests y CI/CD
git rm -r --cached tests/ -f 2>$null
git rm --cached .gitlab-ci.yml -f 2>$null

# Eliminar Payload (Malware)
git rm -r --cached src/payload/ -f 2>$null

# 4. Confirmar limpieza y subir
git commit -m "docs: release update to public portfolio" --allow-empty
Write-Host "[*] Subiendo a GitHub (Público)..." -ForegroundColor Green
git push origin public:main --force


# 6. Volver al laboratorio
Write-Host "[*] Volviendo a la rama 'main' (Lab)..."
git checkout main

Write-Host "[🎉] ¡Portafolio actualizado con éxito!" -ForegroundColor Green