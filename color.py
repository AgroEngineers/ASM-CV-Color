from typing import Union

import numpy
from asm.api.base import ModuleTask, ModuleTaskInput, ModuleTaskOutput, ModuleConfiguration, ModuleInformation, \
    ContainerParameterResults, ContainerParameter, ContainerParameterType
from asm.api.cv import ASMOpenCV, FrameType


class Color(ASMOpenCV):
    def frame_type(self) -> FrameType:
        return FrameType.OBJECT

    def module_info(self) -> ModuleInformation:
        return ModuleInformation(name="CV-Color", version="1.0.0",
                                 parameters=[ContainerParameter(name="R", parameter_type=ContainerParameterType.RANGE),
                                             ContainerParameter(name="G", parameter_type=ContainerParameterType.RANGE),
                                             ContainerParameter(name="B", parameter_type=ContainerParameterType.RANGE)])

    def process(self, frame: numpy.ndarray) -> list[ContainerParameterResults]:
        b, g, r = frame.mean(axis=0)
        return [ContainerParameterResults(name="R", result=r),
                ContainerParameterResults(name="G", result=g),
                ContainerParameterResults(name="B", result=b)]

    def configuration(self, configuration: ModuleConfiguration):
        return None

    def task(self, task: ModuleTask, task_input: ModuleTaskInput) -> Union[ModuleTaskOutput, None]:
        return None
