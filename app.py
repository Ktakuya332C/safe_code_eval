import evaluate
from evaluate.utils import launch_gradio_widget


module = evaluate.load("ktakuya/safe_code_eval")
launch_gradio_widget(module)