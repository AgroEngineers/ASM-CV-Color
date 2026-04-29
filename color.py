from typing import Union

import numpy
from asm.api.base import ModuleTask, ModuleTaskInput, ModuleTaskOutput, ModuleConfiguration, ModuleInformation, \
    ContainerParameterResults, ContainerParameter, ContainerParameterType, ContainerParameterGroup, \
    ContainerParameterGroupWebSpec, ContainerParameterWebSpecAlignment
from asm.api.cv import ASMOpenCV, FrameType

color_group: ContainerParameterGroup = ContainerParameterGroup(
    "Color",
    ContainerParameterType.RANGE,
    ContainerParameterGroupWebSpec(
        html="""
            <div id="parameter-color-box" style="background-color: rgb(%cv_color_cv-color_color_r%, %cv_color_cv-color_color_g%, %cv_color_cv-color_color_b%)" class="parameter-color-box"></div>
        """,
        css="""
            .parameter-color-box {
                margin-right: 10px;
                width: 10%;
                height: 40%;
                border: 2px solid #5e5e5e;
            }
        """,
        alignment=ContainerParameterWebSpecAlignment.BEFORE
    )
)
parameters: list[ContainerParameter] = [ContainerParameter(name="R", group=color_group),
                                        ContainerParameter(name="G", group=color_group),
                                        ContainerParameter(name="B", group=color_group)]


class Color(ASMOpenCV):
    def frame_type(self) -> FrameType:
        return FrameType.OBJECT

    def module_info(self) -> ModuleInformation:
        return ModuleInformation(
            name="CV-Color",
            version="1.0.0",
            parameters=parameters
        )

    async def process(self, frame: numpy.ndarray) -> list[ContainerParameterResults]:
        b, g, r = frame.mean(axis=(0, 1))
        return [ContainerParameterResults(parameter=parameters[0], result=r),
                ContainerParameterResults(parameter=parameters[1], result=g),
                ContainerParameterResults(parameter=parameters[2], result=b)]

    def configuration(self, configuration: ModuleConfiguration):
        return None

    def task(self, task: ModuleTask, task_input: ModuleTaskInput) -> Union[ModuleTaskOutput, None]:
        return None
