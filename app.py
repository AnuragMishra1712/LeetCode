from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Load JSON data from file
with open('data.json', 'r') as f:
    data = json.load(f)

def time_to_seconds(hms):
    h, m, s = map(int, hms.split(':'))
    return h * 3600 + m * 60 + s

def format_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    return f"{hours:02}:{minutes:02}:{secs:02}"

@app.route('/')
def index():
    service_names = [service_info['service'] for service_info in data]
    return render_template('index.html', services=service_names)

@app.route('/data', methods=['POST'])
def get_data():
    service_name = request.form['service']
    sort_by = request.form.get('sort_by', 'pipeline')
    min_time = request.form.get('min_time', '00:00:00')
    max_time = request.form.get('max_time', '99:59:59')
    
    # If the user selects "Total Time" filter
    if service_name == 'Total Time':
        combined_data = []
        total_time_seconds = 0
        
        for service in data:
            pipelines = service['pipelines']
            if all(isinstance(p, dict) for p in pipelines.values()):
                for sub_service_name, sub_service_pipelines in pipelines.items():
                    for pipeline_name, time in sub_service_pipelines.items():
                        time_in_seconds = time_to_seconds(time)
                        if time_to_seconds(min_time) <= time_in_seconds <= time_to_seconds(max_time):
                            total_time_seconds += time_in_seconds
                            combined_data.append({
                                'pipeline': f'{sub_service_name} - {pipeline_name}',
                                'time': time,
                                'seconds': time_in_seconds
                            })
            else:
                for pipeline_name, time in pipelines.items():
                    time_in_seconds = time_to_seconds(time)
                    if time_to_seconds(min_time) <= time_in_seconds <= time_to_seconds(max_time):
                        total_time_seconds += time_in_seconds
                        combined_data.append({
                            'pipeline': pipeline_name,
                            'time': time,
                            'seconds': time_in_seconds
                        })
        
        # Sort the combined data
        if sort_by == 'time_asc':
            combined_data.sort(key=lambda x: x['seconds'])
        elif sort_by == 'time_desc':
            combined_data.sort(key=lambda x: x['seconds'], reverse=True)
        elif sort_by == 'name_asc':
            combined_data.sort(key=lambda x: x['pipeline'])
        elif sort_by == 'name_desc':
            combined_data.sort(key=lambda x: x['pipeline'], reverse=True)
        
        # Calculate total time in HH:MM:SS format
        total_time_hms = format_time(total_time_seconds)
        
        # Get top 5 pipelines by execution time
        top_5_pipelines = sorted(combined_data, key=lambda x: x['seconds'], reverse=True)[:5]
        
        return render_template('data.html', 
                               service_name="Total Time for All Services", 
                               display_data=combined_data, 
                               total_time_hms=total_time_hms, 
                               total_time_seconds=total_time_seconds,
                               top_5_pipelines=top_5_pipelines)
    
    # If the user selects a specific service
    selected_service = next(service for service in data if service['service'] == service_name)
    pipelines = selected_service['pipelines']
    
    # Prepare data for display
    display_data = []
    total_time_seconds = 0
    
    # Check if the pipelines contain nested services
    if all(isinstance(p, dict) for p in pipelines.values()):
        # Handle nested services
        for sub_service_name, sub_service_pipelines in pipelines.items():
            for pipeline_name, time in sub_service_pipelines.items():
                time_in_seconds = time_to_seconds(time)
                if time_to_seconds(min_time) <= time_in_seconds <= time_to_seconds(max_time):
                    total_time_seconds += time_in_seconds
                    display_data.append({
                        'pipeline': f'{sub_service_name} - {pipeline_name}',
                        'time': time,
                        'seconds': time_in_seconds
                    })
    else:
        # Handle flat services
        for pipeline_name, time in pipelines.items():
            time_in_seconds = time_to_seconds(time)
            if time_to_seconds(min_time) <= time_in_seconds <= time_to_seconds(max_time):
                total_time_seconds += time_in_seconds
                display_data.append({
                    'pipeline': pipeline_name,
                    'time': time,
                    'seconds': time_in_seconds
                })
    
    # Sort the data
    if sort_by == 'time_asc':
        display_data.sort(key=lambda x: x['seconds'])
    elif sort_by == 'time_desc':
        display_data.sort(key=lambda x: x['seconds'], reverse=True)
    elif sort_by == 'name_asc':
        display_data.sort(key=lambda x: x['pipeline'])
    elif sort_by == 'name_desc':
        display_data.sort(key=lambda x: x['pipeline'], reverse=True)
    
    # Calculate total time in HH:MM:SS format
    total_time_hms = format_time(total_time_seconds)
    
    # Get top 5 pipelines by execution time
    top_5_pipelines = sorted(display_data, key=lambda x: x['seconds'], reverse=True)[:5]
    
    return render_template('data.html', 
                           service_name=service_name, 
                           display_data=display_data, 
                           total_time_hms=total_time_hms, 
                           total_time_seconds=total_time_seconds,
                           top_5_pipelines=top_5_pipelines)

if __name__ == '__main__':
    app.run(debug=True)
