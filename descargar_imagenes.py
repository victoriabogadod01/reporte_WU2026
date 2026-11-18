#!/usr/bin/env python3
"""Descarga las imágenes de los anuncios de WU desde Meta y las guarda en informes/wu-2026/img/<id>.jpg
Uso:  python3 descargar_imagenes.py
Los enlaces de Meta vencen el 23/11/2026: ejecutalo lo antes posible. Solo usa la librería estándar."""
import json, os, sys, urllib.request
base = os.path.dirname(os.path.abspath(__file__))
man = json.load(open(os.path.join(base, 'informes', 'wu-2026', 'imagenes.json'), encoding='utf-8'))
out = os.path.join(base, 'informes', 'wu-2026', 'img'); os.makedirs(out, exist_ok=True)
ok = fail = 0
for cid, m in man.items():
    dest = os.path.join(out, cid + '.jpg')
    if os.path.exists(dest) and os.path.getsize(dest) > 0: ok += 1; continue
    try:
        req = urllib.request.Request(m['url'], headers={'User-Agent': 'Mozilla/5.0'})
        data = urllib.request.urlopen(req, timeout=30).read()
        open(dest, 'wb').write(data); ok += 1
        print('OK  ', cid, m['calidad'], m['anuncio'])
    except Exception as e:
        fail += 1; print('FALLO', cid, m['anuncio'], e)
print(f'\nListo: {ok} imágenes, {fail} fallos.')
if fail: print('Si fallaron por vencimiento, pedime nuevos enlaces y los regenero.')
