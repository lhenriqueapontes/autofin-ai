import json
from pathlib import Path


def plan(task):
    return [
        'understand the task',
        'break into small actions',
        'execute local tools',
        'save the run log',
    ]


def execute(step):
    return {'step': step, 'status': 'done'}


def run(task='organize a portfolio project'):
    steps = plan(task)
    result = {'task': task, 'results': [execute(step) for step in steps]}
    folder = Path('memory')
    folder.mkdir(exist_ok=True)
    (folder / 'log.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
    return result


if __name__ == '__main__':
    print(json.dumps(run(), indent=2))
