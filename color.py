from typing import Union

import numpy
from asm.api.base import ModuleTask, ModuleTaskInput, ModuleTaskOutput, ModuleConfiguration, ModuleInformation, \
    ContainerParameterResults
from asm.api.cv import ASMOpenCV, FrameType


class Color(ASMOpenCV):
    def frame_type(self) -> FrameType:
        pass

    def process(self, frame: numpy.ndarray) -> list[ContainerParameterResults]:
        pass

    def module_info(self) -> ModuleInformation:
        pass

    def configuration(self, configuration: ModuleConfiguration):
        pass

    def task(self, task: ModuleTask, task_input: ModuleTaskInput) -> Union[ModuleTaskOutput, None]:
        pass