# 🧪 Test de Entornos de Desarrollo (DAW 1.º)

Aplicación web hecha con [Streamlit](https://streamlit.io) para practicar con preguntas de tipo test
(3 alternativas por pregunta) basadas en el material de clase **ENTORNOS.pptx**.

## Temas

1. Conceptos básicos
2. Ciclo de vida del software
3. Modelos de desarrollo
4. Lenguajes de programación

## Archivos

| Archivo | Para qué sirve |
|---|---|
| `app.py` | La aplicación (interfaz, corrección y nota) |
| `preguntas.py` | El banco de preguntas (100) |
| `requirements.txt` | Dependencias |
| `README.md` | Este archivo |

## Ejecutar en tu ordenador

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Publicarla gratis (GitHub + Streamlit Community Cloud)

1. Crea un repositorio en GitHub y sube estos 4 archivos a la raíz.
2. Entra en <https://share.streamlit.io> con tu cuenta de GitHub.
3. Pulsa **Create app**, elige el repositorio, la rama `main` y el archivo principal `app.py`.
4. Pulsa **Deploy**. Te dará un enlace que puedes compartir con tus compañeros.

## Añadir preguntas

En `preguntas.py`, añade una línea con este formato (la correcta va siempre primero; la app mezcla las alternativas):

```python
q(T3, "Pregunta", "Respuesta correcta", "Incorrecta 1", "Incorrecta 2", "Explicación breve"),
```
