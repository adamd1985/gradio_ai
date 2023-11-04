---
title: Gradio Ai
emoji: 🏢
colorFrom: red
colorTo: gray
sdk: gradio
sdk_version: 4.0.2
app_file: app.py
pinned: false
license: mit
---

# Gradio.AI Sample

Sample Gradio.AI to display an easy linear model. See the Spaces UI web [here](https://huggingface.co/spaces/radmada/gradio_ai).

## Build & Run

1. Python 3.11+
2. `pip install -f requirements.txt`
3. `python app.py`
4. Go to the URL provided.

## Deploy with GH Actions and GH Pages

1. In Github go to Setting->pages
2. Select the source as `/root`.
3. Make sure there is an `index.py` that can start the Gradio UI.
4. Add `.nojekyll` so that GH Actions don't ignore python files.
5. Create a hugging face Spaces
6. Connect the GH repo to Spaces, see this [documentation](https://huggingface.co/docs/hub/spaces-github-actions).
7. 

# Boilerplate Code Generated By Anisotropic (AKA Claude)

AI Prompt:

```
Using Gradio.ai

Write a simple webapp boilerplate. 
Write a linear function to predict input.
Diplay function output
Provide git workflow yaml to deploy github page
```

Unfortunately it doesn't know anything about GH Actions or  GH Pages!

# Contributors

[Adam Darmanin](https://github.com/adamd1985)

# References

- https://github.com/actions/setup-python
- https://claude.ai/
- https://www.gradio.app/guides/quickstart
- https://huggingface.co/docs/hub/spaces-github-actions
- https://huggingface.co/docs/hub/spaces-config-reference
