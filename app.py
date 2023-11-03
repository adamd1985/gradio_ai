import gradio as gr

def predict(x):
  """ Very basic linear regression """
  return 2 * x + 1
  
iface = gr.Interface(fn=predict, inputs="number", outputs="text")

if __name__ == "__main__":
  """ MAIN """
  iface.launch()