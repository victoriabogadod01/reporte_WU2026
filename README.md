# Informe WU · Aquí Pago y Pago Express (1/9 – 15/11/2026)

Página estática para GitHub Pages. Abre en `informes/wu-2026.html`.

## Contenido
- `informes/wu-2026.html` — informe interactivo (datos embebidos, sin dependencias).
- `informes/wu-2026/imagenes.json` — lista de imágenes de anuncios (enlaces de Meta, vencen el 23/11/2026).
- `descargar_imagenes.py` — baja las imágenes a `informes/wu-2026/img/`.

## Pasos
1. Corré `python3 descargar_imagenes.py` (antes del 23/11/2026).
2. Subí todo al repo: `git add . && git commit -m "Informe WU 2026" && git push`.
3. En el repo: Settings → Pages → Branch `main` / carpeta raíz.

Importante: un repo o Pages público expone datos de inversión y piezas de cliente. Usá repo privado si Pages privado está disponible en tu plan.
