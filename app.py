from flask import Flask, jsonify
from flask_cors import CORS
import db_config

app = Flask(__name__)
CORS(app)

@app.route('/api/messages', methods=['GET'])
def get_messages():
    conn = db_config.get_connection()
    cursor = conn.cursor()
    cursor.execute("select id , text from messages")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify([{"id":row[0],"text":row[1]} for row in rows])

if __name__=='__main__':
    app.run(debug=True)