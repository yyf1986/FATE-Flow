#
#  Copyright 2019 The FATE Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

from fate_flow.components.param.param_extract import ParamExtract
from fate_flow.components.framework.scheduler.setting_conf_plugins import Components


def get_support_role(module, roles=None):
    return Components.get(module).get_supported_roles(roles)


def get_module(module, role):
    return Components.get(module).get_run_obj(role)


def get_module_name(module, role):
    return Components.get(module).get_run_obj_name(role)


def get_module_param(module, alias):
    return Components.get(module).get_param_obj(alias)


# this interface only support for dsl v1
def get_not_builtin_types_for_dsl_v1(param):
    return ParamExtract().get_not_builtin_types(param)
