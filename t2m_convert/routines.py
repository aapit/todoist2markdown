import yaml
from t2m_convert.convert import ConvertRoutine, ConvertTrigger, ConvertAction
import os

class RoutineLoader:
    def load(self) -> list:
        routines = []
        scriptRootPath = os.path.realpath(os.path.dirname(__file__) + '/..')
        with open(scriptRootPath + '/routines.yaml') as f:
            allConfig = yaml.load(f, Loader=yaml.Loader)
        for singleConfig in allConfig:
            routines.append(self._composeRoutine(singleConfig))
        return routines

    def _composeRoutine(self, singleConfig: dict):
        trigger         = ConvertTrigger(tag = singleConfig['trigger']['tag'])
        action          = self._composeAction(singleConfig)
        return ConvertRoutine(trigger, action)

    def _composeAction(self, singleConfig: dict) -> ConvertAction:
        shouldAppend    = 'appendFilename' in singleConfig['action']
        appendFilename  = singleConfig['action']['appendFilename'] if shouldAppend else None
        return ConvertAction(
            dir = singleConfig['action']['dir'],
            appendFilename = appendFilename
        )
