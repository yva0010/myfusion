import gradio

from myfusion import state_manager
from myfusion.uis.components import about, job_list, job_list_options


def pre_check() -> bool:
	return True


def render() -> gradio.Blocks:
	with gradio.Blocks() as layout:
		with gradio.Row():
			with gradio.Column(scale = 4):
				with gradio.Blocks():
					about.render()
				with gradio.Blocks():
					job_list_options.render()
			with gradio.Column(scale = 11):
				with gradio.Blocks():
					job_list.render()
	return layout


def listen() -> None:
	job_list_options.listen()
	job_list.listen()


def run(ui : gradio.Blocks) -> None:
	ui.launch(favicon_path = 'myfusion.ico', inbrowser = state_manager.get_item('open_browser'), share=True)
