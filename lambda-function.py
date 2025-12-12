import json

def lambda_handler(event, context):
    """
    Convert temperature between Celsius and Fahrenheit.

    Expected event format:
    {
        "temperature": 32,
        "from_unit": "F",
        "to_unit": "C"
    }
    """
    try:
        print("=== Lambda Test Started ===")
        print("Incoming Event:", json.dumps(event))

        # Extract values from the event
        temperature = event.get('temperature')
        from_unit = event.get('from_unit', '').upper()
        to_unit = event.get('to_unit', '').upper()

        # Validate input
        if temperature is None:
            print("=== Lambda Test Ended: Missing temperature ===")
            return {
                'statusCode': 400,
                'body': json.dumps({
                    'error': 'Missing required field: temperature'
                })
            }

        if from_unit not in ['C', 'F'] or to_unit not in ['C', 'F']:
            print("=== Lambda Test Ended: Invalid units ===")
            return {
                'statusCode': 400,
                'body': json.dumps({
                    'error': 'Invalid units. Use \"C\" for Celsius or \"F\" for Fahrenheit'
                })
            }

        # Perform conversion
        if from_unit == to_unit:
            converted_temp = temperature
        elif from_unit == 'C' and to_unit == 'F':
