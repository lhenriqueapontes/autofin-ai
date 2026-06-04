import json
from pathlib import Path


def build_case():
    return {
        'case_type': 'review_demo',
        'gross_value': 950000.0,
        'cost_basis': 620000.0,
        'event_date': '2026-05-10',
    }


def calculate(case):
    gain = max(case['gross_value'] - case['cost_basis'], 0)
    return {
        **case,
        'estimated_gain': gain,
        'estimated_value': round(gain * 0.15, 2),
    }


def validate(result):
    required = ['case_type', 'gross_value', 'cost_basis', 'estimated_gain']
    missing = [x for x in required if x not in result]
    return {'valid': len(missing) == 0, 'missing_fields': missing, 'payload': result}


def response(validated):
    payload = validated['payload']
    return {
        'status': 'requires_review',
        'summary': payload,
        'steps': [
            'check source files',
            'confirm dates',
            'review assumptions',
            'export report',
        ],
        'validation': {'valid': validated['valid'], 'missing_fields': validated['missing_fields']},
    }


def run():
    data = response(validate(calculate(build_case())))
    Path('memory').mkdir(exist_ok=True)
    Path('memory/log.json').write_text(json.dumps(data, indent=2), encoding='utf-8')
    return data


if __name__ == '__main__':
    print(json.dumps(run(), indent=2))
