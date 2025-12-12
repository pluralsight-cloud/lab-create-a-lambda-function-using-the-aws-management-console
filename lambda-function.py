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
                    'error': 'Invalid units. Use \"C\" for Celsius or \"F\" for Fahrenheit"
                })
            }

        # Perform conversion
        if from_unit == to_unit:
            converted_temp = temperature
        elif from_unit == 'C' and to_unit == 'F':
            converted_temp = (temperature * 9/5) + 32
        else:
            converted_temp = (temperature - 32) * 5/9

        # Round to 2 decimal places
        converted_temp = round(converted_temp, 2)

        # Log the conversion
        print(f"Converted {temperature}°{from_unit} to {converted_temp}°{to_unit}")

        print("=== Lambda Test Completed Successfully ===")

        return {
            'statusCode': 200,
            'body': json.dumps({
                'original': {
                    'temperature': temperature,
                    'unit': from_unit
                },
                'converted': {
                    'temperature': converted_temp,
                    'unit': to_unit
                },
                'message': f'{temperature}°{from_unit} equals {converted_temp}°{to_unit}'
            })
        }

    except Exception as e:
        print("=== Lambda Test Ended with Error ===")
        print(f"Error details: {str(e)}")

        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': 'Internal server error',
                'details': str(e)
            })
        }
