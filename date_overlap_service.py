from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

def check_overlap(range1, range2):
    start1 = datetime.strptime(range1['start_date'], '%Y-%m-%d')
    end1 = datetime.strptime(range1['end_date'], '%Y-%m-%d')
    start2 = datetime.strptime(range2['start_date'], '%Y-%m-%d')
    end2 = datetime.strptime(range2['end_date'], '%Y-%m-%d')
    
    return not (end1 < start2 or start1 > end2)

@app.route('/api/check_overlap', methods=['POST'])
def api_check_overlap():
    data = request.get_json()
    range1 = data['range1']
    range2 = data['range2']
    
    overlap = check_overlap(range1, range2)
    
    return jsonify({'overlap': overlap})

if __name__ == '__main__':
    app.run(debug=True)
