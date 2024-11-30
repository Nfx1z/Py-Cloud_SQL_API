from src.MySQL.handler import fetch_data_from_db, add_data_to_db

def fetch_data(request):
    query = request.GET.get('query')
    table = request.GET.get('table')
    
    if not query or not table:
        return 'Missing required parameters: query and table'
    
    try:
        result = fetch_data_from_db(query, table)
        return result
    except Exception as e:
        return f'Error fetching data: {str(e)}'