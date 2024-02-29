import json

def fill_values(tests, values):
    for test in tests:
        test_id = test['id']
        matching_value = next((v['value'] for v in values['values'] if v['id'] == test_id), None)
        test['value'] = matching_value

        if 'values' in test:
            fill_values(test['values'], values)

def main():
    with open('tests.json', 'r') as tests_file:
        tests_data = json.load(tests_file)

    with open('values.json', 'r') as values_file:
        values_data = json.load(values_file)

    fill_values(tests_data['tests'], values_data)

    with open('report.json', 'w') as report_file:
        json.dump(tests_data, report_file, indent=2)

if __name__ == "__main__":
    main()
