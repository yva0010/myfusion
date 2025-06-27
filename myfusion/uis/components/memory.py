from typing import Optional

import gradio

import myfusion.choices
from myfusion import state_manager, wording
from myfusion.common_helper import calc_int_step
from myfusion.typing import VideoMemoryStrategy

VIDEO_MEMORY_STRATEGY_DROPDOWN : Optional[gradio.Dropdown] = None
SYSTEM_MEMORY_LIMIT_SLIDER : Optional[gradio.Slider] = None


def render() -> None:
	global VIDEO_MEMORY_STRATEGY_DROPDOWN
	global SYSTEM_MEMORY_LIMIT_SLIDER

	VIDEO_MEMORY_STRATEGY_DROPDOWN = gradio.Dropdown(
		label = wording.get('uis.video_memory_strategy_dropdown'),
		choices = myfusion.choices.video_memory_strategies,
		value = state_manager.get_item('video_memory_strategy')
	)
	SYSTEM_MEMORY_LIMIT_SLIDER = gradio.Slider(
		label = wording.get('uis.system_memory_limit_slider'),
		step = calc_int_step(myfusion.choices.system_memory_limit_range),
		minimum = myfusion.choices.system_memory_limit_range[0],
		maximum = myfusion.choices.system_memory_limit_range[-1],
		value = state_manager.get_item('system_memory_limit')
	)


def listen() -> None:
	VIDEO_MEMORY_STRATEGY_DROPDOWN.change(update_video_memory_strategy, inputs = VIDEO_MEMORY_STRATEGY_DROPDOWN)
	SYSTEM_MEMORY_LIMIT_SLIDER.release(update_system_memory_limit, inputs = SYSTEM_MEMORY_LIMIT_SLIDER)


def update_video_memory_strategy(video_memory_strategy : VideoMemoryStrategy) -> None:
	state_manager.set_item('video_memory_strategy', video_memory_strategy)


def update_system_memory_limit(system_memory_limit : float) -> None:
	state_manager.set_item('system_memory_limit', int(system_memory_limit))
