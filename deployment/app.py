from fastai.vision.all import load_learner
import gradio as gr

cap_labels = [
    'balaclava cap',
    'baseball cap',
    'beanie cap',
    'boater hat',
    'bowler hat',
    'bucket hat',
    'cowboy hat',
    'fedora cap',
    'flat cap',
    'ivy cap',
    'kepi cap',
    'newsboy cap',
    'pork pie hat',
    'rasta cap',
    'sun hat',
    'taqiyah cap',
    'top hat',
    'trucker cap',
    'turban cap',
    'visor cap'
]

model = load_learner("models/cap_recognizer_v0.pkl")

def recognize_image(image):
  pred, idx, probs = model.predict(image)
  return dict(zip(cap_labels, map(float,probs)))


image = gr.Image()
label = gr.Label()
examples = [
    'test_images/unknown_00.jpg',
    'test_images/unknown_01.jpg',
    'test_images/unknown_02.jpg',
    'test_images/unknown_03.jpg']


demo = gr.Interface(fn=recognize_image, inputs="image", outputs="label", examples = examples)
demo.launch(inline = False, share = True)
