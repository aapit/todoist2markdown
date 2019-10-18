# @author   David Spreekmeester <@aapit>
from todoist.api import TodoistAPI
from t2m_todoist.labellist import LabelList
from t2m_todoist.tasklist import TaskList
import os
from dotenv import load_dotenv
from t2m_convert.routines import RoutineLoader


load_dotenv(override = True)
api             = TodoistAPI(os.getenv('TODOIST_TOKEN'))
api.sync()
labelList       = LabelList(api)
routines        = RoutineLoader().load()

for routine in routines:
    allTasks = TaskList(api, labelList)
    matchingList = routine.trigger.matches(allTasks)

    cCyan   = "\033[0;36m"
    cNone   = "\033[0m"
    cPurple = "\033[0;35m"

    numberOfTasks = str(len(matchingList.tasks))
    tasksNoun = 'task' if len(matchingList.tasks) == 1 else 'tasks'
    print(cCyan + "Found", cPurple + numberOfTasks,
          cCyan + tasksNoun, "labeled", cPurple + routine.trigger.tag + cNone)
    print(cCyan + ("=" * 50) + cNone)

    routine.action.run(matchingList)

    print("")
