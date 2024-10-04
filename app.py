import streamlit as st
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {'message': 'Hello from Flask!'}
    return jsonify(data)

def streamlit_app():
    st.title("Streamlit App")
    response = requests.get('http://localhost:5000/api/data')
    data = response.json()
    st.write(data)

if __name__ == '__main__':
    if st._is_running_with_streamlit:
        streamlit_app()
    else:
        app.run(debug=True)
