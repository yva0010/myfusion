from typing import Optional

import gradio

import myfusion.choices
from myfusion import state_manager, wording
from myfusion.common_helper import calc_int_step

EXECUTION_QUEUE_COUNT_SLIDER : Optional[gradio.Slider] = None


def render() -> None:
	global EXECUTION_QUEUE_COUNT_SLIDER

	EXECUTION_QUEUE_COUNT_SLIDER = gradio.Slider(
		label = wording.get('uis.execution_queue_count_slider'),
		value = state_manager.get_item('execution_queue_count'),
		step = calc_int_step(myfusion.choices.execution_queue_count_range),
		minimum = myfusion.choices.execution_queue_count_range[0],
		maximum = myfusion.choices.execution_queue_count_range[-1]
	)


def listen() -> None:
	EXECUTION_QUEUE_COUNT_SLIDER.release(update_execution_queue_count, inputs = EXECUTION_QUEUE_COUNT_SLIDER)


def update_execution_queue_count(execution_queue_count : float) -> None:
	state_manager.set_item('execution_queue_count', int(execution_queue_count))
